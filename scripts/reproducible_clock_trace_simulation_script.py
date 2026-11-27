#!/usr/bin/env python3
"""
NCG-007: Discrete-Grid Numerical Verification of the Lorentzian Clock Trace Z(l)
across Matter-Field Thresholds (arXiv:2611.34924v1, Section 5.3).

Aligned with NCG-005 and NCG-007 conventions (Planck units l_P = 1):
- Uniform horizon-area grid s_k = s_0 + k * ds (default s_0 = 1.0, ds = 1.0).
- Physical clock-area cutoff s_*(l) = pi * l^2 / (1 - eps)^2 (default eps = 0.05),
  so u_bar_{*,k} / l = sqrt(s_k / s_*(l)).
- One-loop area-density weight w_k(alpha) = (c_0 / sqrt(4*pi)) * s_k^(alpha - 1/2) * ds,
  matching the continuum normalization of NCG-005 for any grid spacing ds.

Features:
1. Hybrid direct (`math.fsum`) + 5-term Euler-Maclaurin evaluator for finite sums
   and infinite tails, eliminating both IEEE-754 cancellation in steep UV tails
   (e.g. pure N=8 SUGRA, alpha = -5) and O(s_*) loop limits at ultra-asymptotic l.
2. Startup self-test comparing Euler-Maclaurin evaluation against brute-force
   summation (< 1e-13 relative error).
3. Moderate-l (l in [10^2.5, 10^4]) and ultra-asymptotic (l in [10^25, 10^30])
   log-log / semi-log slope fits for Z(l) (or Delta Z(l) = Z_inf - Z(l)),
   the clock ratio <u_bar_*>_l / l, and the area ratio <s>_l / s_*, explicitly
   demonstrating the n_V = 20 pre-asymptotic steepening vs. true -1/15 decay.
4. Discrete Gaussian-windowed conditioning check using the exact Section 5.3
   window f_b(s) = exp(-(s - s_b)^2 / (4 * s_b)) (variance sigma_s^2 = 2 * s_b),
   recovering both <s_k>_{C_b} / s_b -> 1 + (2*alpha - 1)/s_b and the slope alpha
   via log Tr_disc(C_b^dagger C_b) vs. log s_b across all phases.

Dependencies: Python 3.9+ standard library only (argparse, dataclasses, json, math).
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional, Tuple


def sen_alpha(
    n_v: float,
    n_s: float = 0.0,
    n_f: float = 0.0,
    n_32: float = 0.0,
) -> float:
    """Return 4D Schwarzschild mixed-ensemble log-area coefficient alpha = C_local / 2."""
    c_local = (2.0 * n_s - 26.0 * n_v + 7.0 * n_f - 116.5 * n_32 + 424.0) / 90.0
    return 0.5 * c_local


def s_star_from_l(l: float, eps: float = 0.05) -> float:
    """Upper dimensionless area s_*(l) = pi * l^2 / (1 - eps)^2 in Planck units."""
    if not (0.0 <= eps < 1.0):
        raise ValueError(f"Cap parameter eps must lie in [0, 1), got {eps}")
    denom = 1.0 - eps
    return math.pi * (l * l) / (denom * denom)


def _falling_power_deriv(x: float, power: float, order: int) -> float:
    """Return d^order/dx^order (x^power) = power*(power-1)*...*(power-order+1) * x^(power-order)."""
    coeff = 1.0
    for j in range(order):
        coeff *= power - j
    if coeff == 0.0:
        return 0.0
    return coeff * (x ** (power - order))


def sum_shifted_powers(
    s0: float,
    ds: float,
    k_start: int,
    k_end: int,
    power: float,
    n_direct: int = 10000,
) -> float:
    """
    Evaluate sum_{k=k_start}^{k_end} (s0 + k * ds)^power to ~float64 precision
    using exact rounded direct summation near the UV cutoff and 5-term
    Euler-Maclaurin summation above x0 + n_direct.
    """
    if k_end < k_start:
        return 0.0
    if s0 <= 0.0 or ds <= 0.0:
        raise ValueError("Grid parameters s0 and ds must be strictly positive.")

    x0 = s0 / ds
    scale = ds ** power
    count = k_end - k_start + 1

    if count <= 2 * n_direct:
        return scale * math.fsum((x0 + k) ** power for k in range(k_start, k_end + 1))

    if x0 + k_start >= n_direct:
        direct = 0.0
        k_mid = k_start
    else:
        k_mid = k_start + n_direct
        direct = math.fsum((x0 + k) ** power for k in range(k_start, k_mid))

    a = x0 + k_mid
    b = x0 + k_end
    q = power + 1.0

    if abs(q) < 1e-12:
        integral = math.log(b / a)
    else:
        log_ratio = math.log(b / a)
        if abs(q * log_ratio) < 1e-4:
            integral = (a ** q) * math.expm1(q * log_ratio) / q
        else:
            integral = (b ** q - a ** q) / q

    em = (
        integral
        + 0.5 * (a ** power + b ** power)
        + (1.0 / 12.0) * (_falling_power_deriv(b, power, 1) - _falling_power_deriv(a, power, 1))
        - (1.0 / 720.0) * (_falling_power_deriv(b, power, 3) - _falling_power_deriv(a, power, 3))
        + (1.0 / 30240.0) * (_falling_power_deriv(b, power, 5) - _falling_power_deriv(a, power, 5))
    )
    return scale * (direct + em)


def tail_shifted_powers(
    s0: float,
    ds: float,
    k_start: int,
    power: float,
    n_direct: int = 10000,
) -> float:
    """
    Evaluate the convergent infinite tail sum_{k=k_start}^{inf} (s0 + k * ds)^power
    for power < -1 directly (avoiding catastrophic cancellation when subtracting Z_inf - Z(l)).
    """
    if power >= -1.0:
        raise ValueError(f"Convergent infinite tail requires power < -1, got {power}")
    if s0 <= 0.0 or ds <= 0.0:
        raise ValueError("Grid parameters s0 and ds must be strictly positive.")

    x0 = s0 / ds
    scale = ds ** power

    if x0 + k_start >= n_direct:
        direct = 0.0
        k_mid = k_start
    else:
        k_mid = k_start + n_direct
        direct = math.fsum((x0 + k) ** power for k in range(k_start, k_mid))

    a = x0 + k_mid
    integral = -(a ** (power + 1.0)) / (power + 1.0)
    em = (
        integral
        + 0.5 * (a ** power)
        - (1.0 / 12.0) * _falling_power_deriv(a, power, 1)
        + (1.0 / 720.0) * _falling_power_deriv(a, power, 3)
        - (1.0 / 30240.0) * _falling_power_deriv(a, power, 5)
    )
    return scale * (direct + em)


def verify_em_accuracy() -> None:
    """Self-test Euler-Maclaurin accuracy against brute-force summation (< 1e-13 rel error)."""
    s0, ds = 1.0, 1.0
    k_end = 5000
    for p in (1.8555555555555556, -1.0, -1.0333333333333334, -5.5):
        brute = math.fsum((s0 + k * ds) ** p for k in range(0, k_end + 1))
        hybrid = sum_shifted_powers(s0, ds, 0, k_end, p, n_direct=1000)
        rel_err = abs(hybrid - brute) / abs(brute)
        if rel_err > 1e-13:
            raise AssertionError(
                f"Euler-Maclaurin self-test failed for p={p}: rel_err={rel_err:.3e}"
            )


def ols_slope(xs: List[float], ys: List[float]) -> Tuple[float, float]:
    """Ordinary least squares linear fit y = slope * x + intercept."""
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("Need at least two paired points for linear fit.")
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    den = sum((a - mx) ** 2 for a in xs)
    slope = num / den
    intercept = my - slope * mx
    return slope, intercept


def log_log_slope(xs: List[float], ys: List[float]) -> Tuple[float, float]:
    """Ordinary least squares fit log(y) = slope * log(x) + intercept."""
    return ols_slope([math.log(x) for x in xs], [math.log(y) for y in ys])


@dataclass(frozen=True)
class BenchmarkModel:
    name: str
    n_s: float
    n_v: float
    n_f: float
    n_32: float
    regime: str
    description: str

    @property
    def alpha(self) -> float:
        return sen_alpha(self.n_v, n_s=self.n_s, n_f=self.n_f, n_32=self.n_32)

    @property
    def theory_q_limit(self) -> float:
        a = self.alpha
        return (2.0 * a + 1.0) / (2.0 * a + 2.0) if a > -0.5 else 0.0

    @property
    def theory_x2_limit(self) -> float:
        a = self.alpha
        return (2.0 * a + 1.0) / (2.0 * a + 3.0) if a > -0.5 else 0.0

    @property
    def theory_q_decay_slope(self) -> Optional[float]:
        """Asymptotic power-law exponent of <u_bar_*>_l / l vs. l (None at log boundaries)."""
        a = self.alpha
        if a > -0.5:
            return 0.0
        if math.isclose(a, -0.5, abs_tol=1e-12) or math.isclose(a, -1.0, abs_tol=1e-12):
            return None
        if a > -1.0:
            return 2.0 * a + 1.0
        return -1.0

    @property
    def theory_x2_decay_slope(self) -> Optional[float]:
        """Asymptotic power-law exponent of <s>_l / s_* vs. l (None at log boundaries)."""
        a = self.alpha
        if a > -0.5:
            return 0.0
        if math.isclose(a, -0.5, abs_tol=1e-12) or math.isclose(a, -1.5, abs_tol=1e-12):
            return None
        if a > -1.5:
            return 2.0 * a + 1.0
        return -2.0


BENCHMARKS: Tuple[BenchmarkModel, ...] = (
    BenchmarkModel("Pure 4D gravity (n_V=0)", 0, 0, 0, 0, "supercritical", "alpha = +106/45"),
    BenchmarkModel("Einstein-Maxwell (n_V=1)", 0, 1, 0, 0, "supercritical", "alpha = +199/90"),
    BenchmarkModel("Unbroken SM (45 Weyl)", 4, 12, 22.5, 0, "supercritical", "alpha = +37/24"),
    BenchmarkModel("Threshold 19 photons", 0, 19, 0, 0, "supercritical", "alpha = -7/18"),
    BenchmarkModel("Critical (3S, 20V)", 3, 20, 0, 0, "critical", "alpha = -1/2"),
    BenchmarkModel("Breakdown 20 photons", 0, 20, 0, 0, "weak_uv", "alpha = -8/15"),
    BenchmarkModel("Pure N=4 SUGRA", 2, 6, 2, 4, "boundary_minus_one", "alpha = -1"),
    BenchmarkModel("25 photons", 0, 25, 0, 0, "strong_uv_mid", "alpha = -113/90"),
    BenchmarkModel("Pure N=8 SUGRA", 70, 28, 28, 8, "strong_uv_deep", "alpha = -5"),
)


@dataclass
class TracePoint:
    l: float
    s_star: float
    k_max: int
    z_l: float
    tail_delta_z: Optional[float]
    clock_ratio: float
    area_ratio: float
    macro_band_share: float
    uv_first10_share: float


def evaluate_trace_point(
    alpha: float,
    l: float,
    s0: float = 1.0,
    ds: float = 1.0,
    eps: float = 0.05,
    c0: float = 1.0,
) -> TracePoint:
    """Evaluate exact/hybrid discrete trace observables at a single clock cutoff l."""
    s_star = s_star_from_l(l, eps=eps)
    k_max = int(math.floor((s_star - s0) / ds))
    pref = (c0 / math.sqrt(4.0 * math.pi)) * ds
    p_z = alpha - 0.5

    if k_max < 0:
        z_inf = pref * tail_shifted_powers(s0, ds, 0, p_z) if alpha < -0.5 else None
        return TracePoint(
            l=l,
            s_star=s_star,
            k_max=k_max,
            z_l=0.0,
            tail_delta_z=z_inf,
            clock_ratio=float("nan"),
            area_ratio=float("nan"),
            macro_band_share=float("nan"),
            uv_first10_share=float("nan"),
        )

    z_l = pref * sum_shifted_powers(s0, ds, 0, k_max, p_z)
    sum_s_half = pref * sum_shifted_powers(s0, ds, 0, k_max, alpha)
    sum_s_one = pref * sum_shifted_powers(s0, ds, 0, k_max, alpha + 0.5)

    clock_ratio = (sum_s_half / z_l) / math.sqrt(s_star)
    area_ratio = (sum_s_one / z_l) / s_star

    # Strict macroscopic band: s_*/4 < s_k < s_*/2
    k_band_lo = max(0, int(math.floor((0.25 * s_star - s0) / ds)) + 1)
    k_band_hi = min(k_max, int(math.ceil((0.50 * s_star - s0) / ds)) - 1)
    macro_w = pref * sum_shifted_powers(s0, ds, k_band_lo, k_band_hi, p_z)
    uv10_w = pref * sum_shifted_powers(s0, ds, 0, min(9, k_max), p_z)

    tail_dz = pref * tail_shifted_powers(s0, ds, k_max + 1, p_z) if alpha < -0.5 else None

    return TracePoint(
        l=l,
        s_star=s_star,
        k_max=k_max,
        z_l=z_l,
        tail_delta_z=tail_dz,
        clock_ratio=clock_ratio,
        area_ratio=area_ratio,
        macro_band_share=macro_w / z_l,
        uv_first10_share=uv10_w / z_l,
    )


def fit_window(
    model: BenchmarkModel,
    log10_l_grid: List[float],
    s0: float = 1.0,
    ds: float = 1.0,
    eps: float = 0.05,
    c0: float = 1.0,
) -> Dict[str, object]:
    """Fit trace scaling, clock-ratio scaling, and area-ratio scaling over a log-spaced l window."""
    l_vals = [10.0 ** p for p in log10_l_grid]
    pts = [evaluate_trace_point(model.alpha, lv, s0=s0, ds=ds, eps=eps, c0=c0) for lv in l_vals]

    if model.alpha > -0.5:
        trace_slope, _ = log_log_slope([p.l for p in pts], [p.z_l for p in pts])
        trace_theory = 2.0 * model.alpha + 1.0
        trace_obs = "log Z(l) vs log l"
    elif math.isclose(model.alpha, -0.5, abs_tol=1e-12):
        trace_slope, _ = ols_slope([math.log(p.l) for p in pts], [p.z_l for p in pts])
        # Continuum dZ/d(ln l) = 2 * c_0 / sqrt(4*pi) = c_0 / sqrt(pi) for any grid spacing ds
        trace_theory = c0 / math.sqrt(math.pi)
        trace_obs = "Z(l) vs log l"
    else:
        trace_slope, _ = log_log_slope(
            [p.l for p in pts],
            [p.tail_delta_z for p in pts if p.tail_delta_z is not None],
        )
        trace_theory = 2.0 * model.alpha + 1.0
        trace_obs = "log(Z_inf - Z(l)) vs log l"

    q_slope, _ = log_log_slope([p.l for p in pts], [p.clock_ratio for p in pts])
    x2_slope, _ = log_log_slope([p.l for p in pts], [p.area_ratio for p in pts])
    last = pts[-1]

    return {
        "l_range": [l_vals[0], l_vals[-1]],
        "trace_observable": trace_obs,
        "trace_slope_fit": trace_slope,
        "trace_slope_theory": trace_theory,
        "trace_slope_abs_err": abs(trace_slope - trace_theory),
        "q_slope_fit": q_slope,
        "q_slope_theory": model.theory_q_decay_slope,
        "x2_slope_fit": x2_slope,
        "x2_slope_theory": model.theory_x2_decay_slope,
        "clock_ratio_end": last.clock_ratio,
        "clock_ratio_limit": model.theory_q_limit,
        "area_ratio_end": last.area_ratio,
        "area_ratio_limit": model.theory_x2_limit,
        "macro_band_share_end": last.macro_band_share,
        "uv_first10_share_end": last.uv_first10_share,
    }


def gaussian_conditioned_check(
    alpha: float,
    s_b_grid: Tuple[float, ...] = (2000.0, 5000.0, 10000.0, 20000.0, 50000.0),
    s0: float = 1.0,
    ds: float = 1.0,
    c0: float = 1.0,
) -> Dict[str, float]:
    """
    Evaluate the externally conditioned discrete trace Tr_disc(C_b^dagger C_b)
    with the Section 5.3 Gaussian window f_b(s) = exp(-(s - s_b)^2 / (4 * s_b))
    (variance sigma_s^2 = 2 * s_b). Verifies both:
      1. Log-log slope of Tr_disc(C_b^dagger C_b) vs. s_b recovers alpha;
      2. Conditioned expectation <s_k>_{C_b} / s_b matches 1 + (2*alpha - 1)/s_b.
    """
    log_pref = math.log((c0 / math.sqrt(4.0 * math.pi)) * ds)
    log_traces: List[float] = []
    area_ratio_at_5000 = float("nan")

    for s_b in s_b_grid:
        sigma = math.sqrt(2.0 * s_b)
        k_lo = max(0, int(math.floor((s_b - 10.0 * sigma - s0) / ds)))
        k_hi = int(math.ceil((s_b + 10.0 * sigma - s0) / ds))

        log_w: List[float] = []
        s_vals: List[float] = []
        for k in range(k_lo, k_hi + 1):
            s_k = s0 + k * ds
            lw = log_pref + (alpha - 0.5) * math.log(s_k) - ((s_k - s_b) ** 2) / (4.0 * s_b)
            log_w.append(lw)
            s_vals.append(s_k)

        max_lw = max(log_w)
        scaled_w = [math.exp(lw - max_lw) for lw in log_w]
        sum_w = math.fsum(scaled_w)
        log_traces.append(max_lw + math.log(sum_w))

        if math.isclose(s_b, 5000.0, rel_tol=1e-12):
            mean_s = math.fsum(s * w for s, w in zip(s_vals, scaled_w)) / sum_w
            area_ratio_at_5000 = mean_s / s_b

    fitted_alpha, _ = ols_slope([math.log(sb) for sb in s_b_grid], log_traces)
    return {
        "alpha_true": alpha,
        "alpha_conditioned_fit": fitted_alpha,
        "alpha_abs_err": abs(fitted_alpha - alpha),
        "area_ratio_at_sb5000": area_ratio_at_5000,
        "area_ratio_saddle_pred": 1.0 + (2.0 * alpha - 1.0) / 5000.0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="NCG-007 discrete-grid numerical verification of Lorentzian clock trace Z(l)."
    )
    parser.add_argument("--s0", type=float, default=1.0, help="Planck-scale lower area cutoff s_0.")
    parser.add_argument("--ds", type=float, default=1.0, help="Uniform horizon-area grid spacing ds.")
    parser.add_argument("--eps", type=float, default=0.05, help="Cap parameter epsilon in [0, 1).")
    parser.add_argument("--json-out", type=str, default="", help="Optional JSON output file path.")
    parser.add_argument("--skip-selftest", action="store_true", help="Skip Euler-Maclaurin self-test.")
    args = parser.parse_args()

    if not args.skip_selftest:
        verify_em_accuracy()

    moderate_grid = [2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0]
    ultra_grid = [25.0, 26.0, 27.0, 28.0, 29.0, 30.0]

    print(
        f"=== NCG-007 Moderate Window: l in [10^2.5, 10^4] "
        f"(s0={args.s0}, ds={args.ds}, eps={args.eps}) ==="
    )
    header = (
        f"{'Model':24s} | {'alpha':>7s} | {'Z-Fit':>9s} | {'Z-Th':>9s} | "
        f"{'q-Slope':>8s} | {'<u*>/l':>7s} | {'<s>/s*':>7s} | {'Band':>6s} | {'UV10':>6s}"
    )
    print(header)
    print("-" * len(header))

    report: Dict[str, object] = {
        "parameters": {"s0": args.s0, "ds": args.ds, "eps": args.eps},
        "moderate_window": [],
        "ultra_asymptotic_window": [],
        "gaussian_conditioned_checks": [],
    }

    for model in BENCHMARKS:
        fit = fit_window(model, moderate_grid, s0=args.s0, ds=args.ds, eps=args.eps)
        print(
            f"{model.name:24s} | {model.alpha:+7.4f} | {fit['trace_slope_fit']:+9.5f} | "
            f"{fit['trace_slope_theory']:+9.5f} | {fit['q_slope_fit']:+8.4f} | "
            f"{fit['clock_ratio_end']:7.4f} | {fit['area_ratio_end']:7.4f} | "
            f"{fit['macro_band_share_end']:6.4f} | {fit['uv_first10_share_end']:6.4f}"
        )
        report["moderate_window"].append({"model": asdict(model), "fit": fit})

    print("\n=== NCG-007 Ultra-Asymptotic Window: l in [10^25, 10^30] (Pre-Asymptotic Check) ===")
    u_header = (
        f"{'Model':24s} | {'Z-Fit':>9s} | {'Z-Th':>9s} | "
        f"{'q-Slope':>8s} | {'q-Th':>8s} | {'x2-Slope':>8s} | {'x2-Th':>8s} | {'<u*>/l':>8s}"
    )
    print(u_header)
    print("-" * len(u_header))

    for model in BENCHMARKS:
        ufit = fit_window(model, ultra_grid, s0=args.s0, ds=args.ds, eps=args.eps)
        q_th_str = f"{ufit['q_slope_theory']:+8.4f}" if ufit["q_slope_theory"] is not None else "     log"
        x2_th_str = f"{ufit['x2_slope_theory']:+8.4f}" if ufit["x2_slope_theory"] is not None else "     log"
        print(
            f"{model.name:24s} | {ufit['trace_slope_fit']:+9.5f} | {ufit['trace_slope_theory']:+9.5f} | "
            f"{ufit['q_slope_fit']:+8.4f} | {q_th_str} | {ufit['x2_slope_fit']:+8.4f} | {x2_th_str} | "
            f"{ufit['clock_ratio_end']:8.4e}"
        )
        report["ultra_asymptotic_window"].append({"model": asdict(model), "fit": ufit})

    print("\n=== Externally Conditioned Gaussian Window Check: f_b(s) = exp(-(s - s_b)^2 / (4*s_b)) ===")
    for model in (BENCHMARKS[0], BENCHMARKS[5], BENCHMARKS[7], BENCHMARKS[8]):
        chk = gaussian_conditioned_check(model.alpha, s0=args.s0, ds=args.ds)
        print(
            f"  {model.name:24s} | alpha_true={chk['alpha_true']:+7.4f} | "
            f"alpha_fit={chk['alpha_conditioned_fit']:+7.4f} | "
            f"<s_k>/s_b(5000)={chk['area_ratio_at_sb5000']:.6f} "
            f"(pred {chk['area_ratio_saddle_pred']:.6f})"
        )
        report["gaussian_conditioned_checks"].append({"model": model.name, "check": chk})

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2)
        print(f"\nSaved full JSON results to {args.json_out}")


if __name__ == "__main__":
    main()

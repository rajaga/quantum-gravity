---
id: NCG-007
target_paper: arXiv:2611.34924v1 (Chandrasekaran, Nov 2026)
sections_covered: [5.3, Appendix D.3]
status: numerically-verified
last_updated: 2026-11-28
companion_script: scripts/simulate_clock_trace.py
---

# NCG-007: Discrete-Grid Numerical Simulation of the Lorentzian Clock Trace Across $\alpha = -1/2$

## 1. Purpose and Phase Structure

In `NCG-005`, we proved unconditionally that positivity and monotonicity of the unconditioned Lorentzian clock trace $Z(l) = \sum_{\bar{u}_{*,i} \le l} e^{-s_i}$ enforce a strict floor $\alpha > -1/2$ on the fixed-mass mixed-ensemble logarithmic entropy coefficient $\alpha = \frac{q}{2(1-q)} - \frac{1}{2}$ in any macroscopic black hole regime ($0 < q < 1$) [1, 2]. Evaluating the area-window trace integral across all values of $\alpha$ separates four-dimensional matter-coupled gravity into distinct asymptotic phases:

1. **Macroscopic / IR-dominated phase ($\alpha > -1/2$, e.g., $n_V \le 19$ photons or the unbroken Standard Model):** $Z(l)$ grows as $s_*^{\alpha + 1/2} \propto l^{2\alpha + 1}$, the clock ratio $\langle \hat{\bar{u}}_* \rangle_l / l \to q = \frac{2\alpha + 1}{2\alpha + 2} \in (0, 1)$, the area ratio $\langle \hat{s} \rangle_l / s_*(l) \to x^2 = \frac{2\alpha + 1}{2\alpha + 3}$, and the macroscopic band probability $P(s_*/4 < s < s_*/2) \to 2^{-(\alpha + 1/2)} - 4^{-(\alpha + 1/2)} > 0$.
2. **Critical marginal point ($\alpha = -1/2$, e.g., $n_S = 3, n_V = 20$):** $Z(l) \sim \frac{c_0}{\sqrt{4\pi}}\ln(s_*/s_0) = \frac{c_0}{\sqrt{\pi}}\ln(l/l_0)$, while $\langle \hat{\bar{u}}_* \rangle_l / l \sim (\ln(l/l_0))^{-1} \to 0$, $\langle \hat{s} \rangle_l / s_*(l) \sim (2\ln(l/l_0))^{-1} \to 0$, and $P(s_*/4 < s < s_*/2) \to 0$.
3. **Weak UV-dominated phase ($-1 < \alpha < -1/2$, e.g., $n_V = 20$ photons where $\alpha = -8/15$):** $Z(l)$ converges to a finite UV constant $Z_\infty$, and the trace tail $\Delta Z(l) = Z_\infty - Z(l)$, the clock ratio $\langle \hat{\bar{u}}_* \rangle_l / l$, and the area ratio $\langle \hat{s} \rangle_l / s_*(l)$ all decay asymptotically as $l^{2\alpha + 1}$ (for $n_V = 20$, $2\alpha + 1 = -1/15 \approx -0.066667$).
4. **Strong UV-dominated phase ($\alpha \le -1$, e.g., $n_V \ge 24$ photons or pure $\mathcal{N} = 4, 6, 8$ supergravities):** $\Delta Z(l) \propto l^{2\alpha + 1}$, while the clock numerator localizes in the UV, giving $\langle \hat{\bar{u}}_* \rangle_l / l \propto l^{-1}\ln l$ at $\alpha = -1$ and $\propto l^{-1}$ for $\alpha < -1$. Meanwhile, the area ratio $\langle \hat{s} \rangle_l / s_*(l)$ undergoes a secondary UV transition at $\alpha = -3/2$: its numerator remains IR-dominated for $-3/2 < \alpha < -1$ (so $\langle \hat{s} \rangle_l / s_* \propto l^{2\alpha + 1}$, e.g., $l^{-68/45}$ for $n_V = 25$), decays as $l^{-2}\ln l$ at $\alpha = -3/2$, and collapses as $l^{-2}$ for $\alpha < -3/2$ (e.g., pure $\mathcal{N} = 8$ supergravity).

This note documents the reproducible, zero-dependency Python simulation `scripts/simulate_clock_trace.py` and reports the verified numerical results confirming all four scaling phases, quantifying pre-asymptotic finite-size steepening near $n_V = 19$ and $n_V = 20$, and demonstrating that externally conditioning on a Gaussian area window $C_b$ recovers $\alpha$ even after the unconditioned ensemble $\rho_{\mathscr{D}}$ collapses into the ultraviolet.

---

## 2. Discrete Area-Grid Model and Hybrid Euler--Maclaurin Method

Following `NCG-005` Section 5 and Section 5.3 of `arXiv:2611.34924v1` [1], we work in Planck units ($\ell_P = \sqrt{G_N\hbar} = 1$) and discretize the dimensionless horizon area $\hat{s} = \hat{\mathscr{A}}/(4G_N\hbar)$ on a uniform grid of step $\Delta s$ (default $\Delta s = 1.0$) starting at a Planck-scale cutoff $s_0 \ge 1$ (default $s_0 = 1.0$):

$$
s_k = s_0 + k\,\Delta s, \qquad k = 0, 1, 2, \dots, K_{\max}(l).
$$

For a causal diamond truncated at cap parameter $\epsilon \in [0, 1)$ (default $\epsilon = 0.05$) and upper clock cutoff $l \equiv \ell(\mathscr{D})$, the shear-free clock eigenvalue $\bar{u}_{*,k} = (1-\epsilon)\sqrt{s_k/\pi}$ satisfies $\bar{u}_{*,k} \le l$ if and only if $s_k \le s_*(l)$, where

$$
s_*(l) = \frac{\pi l^2}{(1-\epsilon)^2}, \qquad K_{\max}(l) = \left\lfloor \frac{s_*(l) - s_0}{\Delta s} \right\rfloor.
$$

Each grid level carries the semiclassical area-density-times-Boltzmann Riemann weight from `NCG-005`:

$$
w_k(\alpha) = \frac{c_0}{\sqrt{4\pi}}\, s_k^{\alpha - 1/2}\,\Delta s \qquad (\text{default } c_0 = 1.0),
$$

so that the discrete Riemann sum matches the continuum normalization of `NCG-005` for any grid spacing $\Delta s$. Over $0 \le k \le K_{\max}(l)$, we evaluate:

$$
Z_{\mathrm{disc}}(l) = \sum_{k=0}^{K_{\max}(l)} w_k(\alpha), \qquad
\frac{\langle \hat{\bar{u}}_* \rangle_l}{l} = \frac{1}{Z_{\mathrm{disc}}(l)} \sum_{k=0}^{K_{\max}(l)} w_k(\alpha) \sqrt{\frac{s_k}{s_*(l)}}, \qquad
\frac{\langle \hat{s} \rangle_l}{s_*(l)} = \frac{1}{Z_{\mathrm{disc}}(l)} \sum_{k=0}^{K_{\max}(l)} w_k(\alpha) \frac{s_k}{s_*(l)},
$$

along with the macroscopic band share $P_{\mathrm{band}}(l) = Z_{\mathrm{disc}}(l)^{-1}\sum_{s_*/4 < s_k < s_*/2} w_k(\alpha)$ and the lowest-10-level UV share $P_{\mathrm{UV10}}(l) = Z_{\mathrm{disc}}(l)^{-1}\sum_{k=0}^{\min(9, K_{\max})} w_k(\alpha)$.

### Eliminating Cancellation and Pre-Asymptotic Bottlenecks

Naive $O(s_*)$ floating-point summation fails on two fronts:

1. **Catastrophic cancellation in steep UV tails:** When $\alpha \ll -1/2$ (such as pure $\mathcal{N}=8$ supergravity, $\alpha = -5$), $\Delta Z(l) = Z_\infty - Z_{\mathrm{disc}}(l) \propto l^{-9}$ falls far below $10^{-16} Z_\infty$, so subtracting $Z_\infty - Z_{\mathrm{disc}}(l)$ loses all significant digits in IEEE-754 float64.
2. **Ultra-slow pre-asymptotic steepening at $n_V = 20$:** With $\delta \equiv |\alpha + 1/2| = 1/30$, the unconditioned trace approaches saturation as $Z(l) \propto 1 - (s_*/s_0)^{-1/30}$. Even at $l = 10^4$ ($s_* \approx 3.48 \times 10^8$), $(s_*/s_0)^{-1/30} \approx 0.519$, so $Z(l)$ has reached less than half of $Z_\infty$ and the effective log-log slope of $\langle \hat{\bar{u}}_* \rangle_l / l$ over $l \in [10^{2.5}, 10^4]$ steepens to
   $$
   \frac{d \ln(\langle \hat{\bar{u}}_* \rangle_l / l)}{d \ln l} \approx -\frac{2\delta}{1 - (s_*/s_0)^{-\delta}} \approx -0.156
   $$
   rather than its true asymptotic value $-2\delta = -1/15 \approx -0.0667$. Reaching within $1\%$ of $-1/15$ requires $(s_*/s_0)^{-1/30} \lesssim 0.01$, i.e., $s_* \gtrsim 10^{60}$ ($l \gtrsim 10^{30}$), which is intractable by brute-force iteration.

To resolve both issues cleanly, `scripts/simulate_clock_trace.py` uses a **hybrid direct + 5-term Euler--Maclaurin evaluator**:
* The first $N_{\mathrm{direct}} = 10^4$ terms near $s_0$ are summed directly with exact rounded summation (`math.fsum`), preserving every discrete Planck-scale effect.
* Terms above $x_0 + N_{\mathrm{direct}}$ and infinite subcritical tails $k \ge K_{\max} + 1$ are evaluated directly via the 5-term Euler--Maclaurin formula (through $B_6/6!$), achieving relative accuracy $< 10^{-14}$ in $O(1)$ time for any $l$ up to $l = 10^{30}$ without cancellation. A built-in startup self-test verifies agreement ($< 10^{-13}$ relative error) against brute-force summation over $5{,}000$ terms.

---

## 3. Benchmark Suite and Analytical Expectations

The script evaluates nine four-dimensional matter benchmarks from `NCG-005` using Sen's mixed-ensemble formula $\alpha = \frac{106}{45} + \frac{1}{90}n_S - \frac{13}{90}n_V + \frac{7}{180}n_F - \frac{233}{360}n_{3/2}$ [2]:

| Benchmark Model | $(n_S, n_V, n_F, n_{3/2})$ | $\alpha$ | $Z$ / $\Delta Z$ Slope ($2\alpha+1$) | Asymptotic $q(l) = \langle\hat{\bar{u}}_*\rangle_l / l$ | Asymptotic $x^2(l) = \langle\hat{s}\rangle_l / s_*$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pure 4D gravity** | $(0, 0, 0, 0)$ | $+106/45 \approx +2.3556$ | $+257/45 \approx +5.7111$ | $257/302 \approx 0.8510$ | $257/347 \approx 0.7406$ |
| **Einstein--Maxwell** | $(0, 1, 0, 0)$ | $+199/90 \approx +2.2111$ | $+244/45 \approx +5.4222$ | $244/289 \approx 0.8443$ | $122/167 \approx 0.7305$ |
| **Unbroken SM** | $(4, 12, 45/2, 0)$ | $+37/24 \approx +1.5417$ | $+49/12 \approx +4.0833$ | $49/61 \approx 0.8033$ | $49/73 \approx 0.6712$ |
| **Threshold 19 photons** | $(0, 19, 0, 0)$ | $-7/18 \approx -0.3889$ | $+2/9 \approx +0.2222$ | $2/11 \approx 0.1818$ | $1/10 = 0.1000$ |
| **Critical point** | $(3, 20, 0, 0)$ | $-1/2 = -0.5000$ | $\frac{dZ}{d\ln l} = \frac{c_0}{\sqrt{\pi}} \approx 0.5642$ | $\sim (\ln l)^{-1} \to 0$ | $\sim (2\ln l)^{-1} \to 0$ |
| **20 photons (UV onset)** | $(0, 20, 0, 0)$ | $-8/15 \approx -0.5333$ | $-1/15 \approx -0.0667$ | $\sim l^{-1/15} \to 0$ | $\sim l^{-1/15} \to 0$ |
| **Pure $\mathcal{N}=4$ SUGRA** | $(2, 6, 2, 4)$ | $-1.0000$ | $-1.0000$ | $\sim l^{-1}\ln l \to 0$ | $\sim l^{-1} \to 0$ |
| **25 photons** | $(0, 25, 0, 0)$ | $-113/90 \approx -1.2556$ | $-68/45 \approx -1.5111$ | $\sim l^{-1} \to 0$ | $\sim l^{-68/45} \to 0$ |
| **Pure $\mathcal{N}=8$ SUGRA** | $(70, 28, 28, 8)$ | $-5.0000$ | $-9.0000$ | $\sim l^{-1} \to 0$ | $\sim l^{-2} \to 0$ |

---

## 4. Verified Numerical Results

All numerical results below are from the verified run of `scripts/simulate_clock_trace.py` with default parameters ($s_0 = 1.0$, $\Delta s = 1.0$, $\epsilon = 0.05$, $c_0 = 1.0$).

### 4.1 Moderate Clock-Cutoff Window ($l \in [10^{2.5}, 10^4]$)

Ordinary least-squares log-log fits (semi-log $Z(l)$ vs. $\ln l$ at $\alpha = -1/2$, and $\log(Z_\infty - Z(l))$ vs. $\log l$ for $\alpha < -1/2$) over seven log-spaced cutoffs $l \in [10^{2.5}, 10^4]$, with ensemble ratios and shares evaluated at $l = 10^4$:

| Model | $\alpha$ | Trace Fit | Theory | $q$-Slope | $\langle\hat{\bar{u}}_*\rangle_l / l$ | $\langle\hat{s}\rangle_l / s_*$ | Band | UV10 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Pure 4D gravity ($n_V=0$) | $+2.3556$ | $+5.711112$ | $+5.711111$ | $+0.0000$ | $0.8510$ | $0.7406$ | $0.1191$ | $3.3 \times 10^{-22}$ |
| Einstein--Maxwell ($n_V=1$) | $+2.2111$ | $+5.422223$ | $+5.422222$ | $+0.0000$ | $0.8443$ | $0.7305$ | $0.1294$ | $4.1 \times 10^{-21}$ |
| Unbroken SM (45 Weyl) | $+1.5417$ | $+4.083334$ | $+4.083333$ | $+0.0000$ | $0.8033$ | $0.6712$ | $0.1839$ | $4.4 \times 10^{-16}$ |
| Threshold 19 photons | $-0.3889$ | $+0.264146$ | $+0.222222$ | $-0.0419$ | $0.2032$ | $0.1118$ | $0.0767$ | $0.0455$ |
| Critical $(3S, 20V)$ | $-0.5000$ | $+0.564190$ | $+0.564190$ | $-0.1201$ | $0.0988$ | $0.0494$ | $0.0342$ | $0.1447$ |
| **Breakdown 20 photons** | **$-0.5333$** | **$-0.066667$** | **$-0.066667$** | **$-0.1564$** | **$0.0741$** | **$0.0358$** | **$0.0248$** | **$0.1894$** |
| Pure $\mathcal{N}=4$ SUGRA | $-1.0000$ | $-1.000000$ | $-1.000000$ | $-0.8799$ | $0.0004$ | $4.1 \times 10^{-5}$ | $2.4 \times 10^{-5}$ | $0.7638$ |
| 25 photons ($-113/90$) | $-1.2556$ | $-1.511111$ | $-1.511111$ | $-0.9921$ | $0.0001$ | $7.3 \times 10^{-7}$ | $2.8 \times 10^{-7}$ | $0.8854$ |
| Pure $\mathcal{N}=8$ SUGRA | $-5.0000$ | $-9.000001$ | $-9.000000$ | $-1.0000$ | $5.4 \times 10^{-5}$ | $3.0 \times 10^{-9}$ | $3.9 \times 10^{-37}$ | $1.0000$ |

### 4.2 Ultra-Asymptotic Window ($l \in [10^{25}, 10^{30}]$)

Evaluating the same benchmarks over $l \in [10^{25}, 10^{30}]$ confirms that every pre-asymptotic deviation in Section 4.1 relaxes cleanly onto its analytical exponent once $(s_*/s_0)^{-|\alpha + 1/2|} \ll 1$:

| Model | Trace Fit | Abs. Err | $q$-Slope | $q$-Th | $x^2$-Slope | $x^2$-Th | $\langle\hat{\bar{u}}_*\rangle_l / l$ ($l = 10^{30}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Pure 4D gravity ($n_V=0$) | $+5.711111$ | $6.2 \times 10^{-15}$ | $+0.0000$ | $0.0000$ | $+0.0000$ | $0.0000$ | $0.850993$ |
| Einstein--Maxwell ($n_V=1$) | $+5.422222$ | $4.4 \times 10^{-15}$ | $-0.0000$ | $0.0000$ | $-0.0000$ | $0.0000$ | $0.844291$ |
| Unbroken SM (45 Weyl) | $+4.083333$ | $1.8 \times 10^{-15}$ | $+0.0000$ | $0.0000$ | $+0.0000$ | $0.0000$ | $0.803279$ |
| Threshold 19 photons | $+0.222222$ | $1.7 \times 10^{-7}$ | $-0.0000$ | $0.0000$ | $-0.0000$ | $0.0000$ | $0.181818$ |
| Critical $(3S, 20V)$ | $+0.564190$ | $5.6 \times 10^{-16}$ | $-0.0156$ | log | $-0.0156$ | log | $0.014288$ |
| **Breakdown 20 photons** | **$-0.066667$** | **$2.1 \times 10^{-16}$** | **$-0.0676$** | **$-0.0667$** | **$-0.0676$** | **$-0.0667$** | **$6.79 \times 10^{-4}$** |
| Pure $\mathcal{N}=4$ SUGRA | $-1.000000$ | $2.2 \times 10^{-16}$ | $-0.9844$ | log | $-1.0000$ | $-1.0000$ | $2.87 \times 10^{-29}$ |
| 25 photons ($-113/90$) | $-1.511111$ | $2.2 \times 10^{-16}$ | $-1.0000$ | $-1.0000$ | $-1.5111$ | $-1.5111$ | $1.24 \times 10^{-30}$ |
| Pure $\mathcal{N}=8$ SUGRA | $-9.000000$ | $5.3 \times 10^{-15}$ | $-1.0000$ | $-1.0000$ | $-2.0000$ | $-2.0000$ | $5.42 \times 10^{-31}$ |

### 4.3 Key Numerical Findings

1. **Machine-precision recovery across all phases:** Supercritical models reproduce $q = 257/302 \approx 0.850993$, $q = 244/289 \approx 0.844291$, $q = 49/61 \approx 0.803279$, and $q = 2/11 \approx 0.181818$ to six decimal places; the critical slope $dZ/d\ln l$ matches $1/\sqrt{\pi} \approx 0.564190$ to $5.6 \times 10^{-16}$; and the $n_V = 20$ tail exponent matches $-1/15 = -0.066667$ to $2.1 \times 10^{-16}$.
2. **Pre-asymptotic steepening at $n_V = 20$:** In the moderate window ($l \le 10^4$), the clock and area ratios for $n_V = 20$ decay with effective slope $-0.1564$---more than twice as steep as $-1/15$---because $Z(l)$ has not yet saturated $Z_\infty$. At $l \in [10^{25}, 10^{30}]$, the fitted slope settles to $-0.0676$, within $1.4\%$ of $-0.0667$.
3. **Secondary $\alpha = -3/2$ transition for the area ratio:** Comparing $n_V = 25$ ($\alpha = -113/90$) against pure $\mathcal{N} = 8$ supergravity ($\alpha = -5$) confirms that $\langle \hat{s} \rangle_l / s_*$ decays as $l^{2\alpha + 1} = l^{-1.5111}$ between $-3/2$ and $-1$, switching to $l^{-2}$ only for $\alpha < -3/2$ while $P_{\mathrm{UV10}}$ reaches $0.999995$.

---

## 5. External Gaussian Conditioning Check ($C_b$)

In Section 5.3 of `arXiv:2611.34924v1` [1] (and `NCG-004`), the trace is decomposed into Gaussian area windows $f_b(s) = \exp[-(s - s_b)^2/(4 s_b)]$ with variance $\sigma_s^2 = 2 s_b$. On the discrete grid, the externally conditioned trace is

$$
\mathrm{Tr}_{\mathrm{disc}}(C_b^\dagger C_b) = \sum_{k} w_k(\alpha)\exp\!\left(-\frac{(s_k - s_b)^2}{4 s_b}\right) \sim c_0\, s_b^\alpha,
$$

with first-order saddle shift $\langle s_k \rangle_{C_b} / s_b = 1 + (2\alpha - 1)/s_b + O(s_b^{-2})$. Fitting $\log \mathrm{Tr}_{\mathrm{disc}}(C_b^\dagger C_b)$ against $\log s_b$ over $s_b \in [2 \times 10^3, 5 \times 10^4]$ yields:

| Model | $\alpha_{\mathrm{true}}$ | $\alpha_{\mathrm{fit}}$ | Abs. Err | $\langle s_k \rangle_{C_b} / s_b$ ($s_b = 5000$) | Saddle Pred. |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Pure 4D gravity ($n_V=0$) | $+2.3556$ | $+2.3553$ | $2.26 \times 10^{-4}$ | $1.000742$ | $1.000742$ |
| Breakdown 20 photons | $-0.5333$ | $-0.5336$ | $3.01 \times 10^{-4}$ | $0.999586$ | $0.999587$ |
| 25 photons ($-113/90$) | $-1.2556$ | $-1.2562$ | $6.93 \times 10^{-4}$ | $0.999297$ | $0.999298$ |
| Pure $\mathcal{N}=8$ SUGRA | $-5.0000$ | $-5.0051$ | $5.14 \times 10^{-3}$ | $0.997794$ | $0.997800$ |

External Gaussian conditioning localizes $\langle s_k \rangle_{C_b} / s_b$ to within $0.03\%$--$0.22\%$ of $1$ and recovers $\alpha$ across all phases---including $n_V = 20$ and pure $\mathcal{N}=8$ supergravity---confirming that $C_b$ masks rather than cures the unconditioned clock-trace UV collapse.

---

## 6. How to Run Locally

From the repository root (requires Python 3.9+, standard library only):

```bash
python scripts/simulate_clock_trace.py --json-out ncg_007_results.json
```

Optional flags: `--s0` (lower area cutoff, default `1.0`), `--ds` (grid spacing, default `1.0`), `--eps` (cap truncation $\epsilon$, default `0.05`), and `--skip-selftest`.

---

## 7. Assumptions and Limitations

* **Continuum one-loop input:** The weights $w_k(\alpha)$ take Sen's one-loop exponent $\alpha$ [2] as input; this study verifies the *statistical mechanics of the trace sum* in Section 5.3 rather than performing an independent Lorentzian heat-kernel calculation.
* **Uniform area spacing:** Real quantum gravity spectra need not have uniform $\Delta s$ at $s_k \sim O(1)$, which changes $O(1)$ UV constants (such as $Z_\infty$ and $P_{\mathrm{UV10}}$) without altering large-$l$ exponents or the $\alpha = -1/2$ phase boundary.
* **Neglected quantum focusing delay:** Setting $\bar{u}_{*,k} = (1-\epsilon)\sqrt{s_k/\pi}$ isolates the $\alpha$-driven phase transition under the Section 5.3 assumption that average quantum focusing delays are $o(r_h)$.

---

## 8. References

1. V. Chandrasekaran, *An algebraic quantization of gravity from the null cone*, `arXiv:2611.34924v1 [hep-th]` (2026).
2. A. Sen, *Logarithmic corrections to Schwarzschild and other non-extremal black hole entropy in different dimensions*, JHEP **04** (2013) 156 [`arXiv:1205.0971`].
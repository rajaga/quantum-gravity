---
id: NCG-004
target_paper: arXiv:2611.34924v1 (Chandrasekaran, Nov 2026)
sections_covered: [5.3, Appendix D.3]
status: conditional
last_updated: 2026-11-27
companion_pdf: lorentzian_entropy_section_5_3_wrapup.pdf
---

# Lorentzian Black Hole Entropy and Matter Extension

**Wrap-Up Technical Note on Section 5.3 of `arXiv:2611.34924v1`**

## Abstract

This note wraps up our examination of the Lorentzian black hole entropy calculation in Section 5.3 of *An algebraic quantization of gravity from the null cone* (`arXiv:2611.34924v1`, Chandrasekaran, 2026) [1]. We trace every step by which the Bekenstein--Hawking area law and its one-loop logarithmic correction for large Schwarzschild black holes are obtained from a Lorentzian trace on the future inward null cone of a marginally trapped surface, separate thermodynamic/analytic-continuation evaluation from microscopic state counting, audit the structural dependencies on causal-diamond finiteness, replica bulk cancellation, and ensemble choice, and formulate two concrete matter-field tests: (i) coupling a minimally coupled massless scalar field, which shifts the fixed-mass mixed-ensemble logarithmic coefficient by $+1/90$, and (ii) coupling minimally coupled massless $U(1)$ vector fields, which exposes a sharp structural breakdown of the clock-projected ensemble when $n_V \ge 20$.

---

## 1. Overview and Main Conclusions

In Section 5.3 of `arXiv:2611.34924v1` [1], Chandrasekaran evaluates a Lorentzian trace over interior states of a causal diamond $\mathscr{D}$ bounded by a marginally trapped surface $S$ and truncated on its future inward null cone at a spacelike cap $\Sigma_1$ with maximum clock reading $\ell(\mathscr{D})$. From this trace, the paper obtains:

1. The von Neumann entropy identity

$$
S(\rho_{\mathscr{D}}) = -\mathrm{Tr}(\rho_{\mathscr{D}}\log\rho_{\mathscr{D}}) = \frac{\langle \hat{\mathscr{A}} \rangle}{4G_N\hbar} + \log Z_{\mathscr{D},1},
$$

where $\rho_{\mathscr{D}} = e^{-\hat{\mathscr{A}}/(4G_N\hbar)} / Z_{\mathscr{D},1}$ and $Z_{\mathscr{D},1} = \mathrm{Tr}_{\mathcal{H}_{\mathscr{D}}} e^{-\hat{\mathscr{A}}/(4G_N\hbar)}$, recovering the Bekenstein--Hawking area term [2, 3]; and

2. For a large Schwarzschild black hole ($r_h / \ell_P \to \infty$, with $\ell_P = \sqrt{G_N\hbar}$), a logarithmic correction $\frac{q}{2(1-q)} \log\!\left(\frac{\langle \hat{\mathscr{A}} \rangle}{4G_N\hbar}\right)$, where $q = \lim_{r_h/\ell_P \to \infty} \langle \hat{\bar{u}}_* \rangle / \ell(\mathscr{D}) = 257/302$ at one loop in pure vacuum gravity. Changing variables from horizon area to Schwarzschild mass $M$ at fixed mass (with angular momenta summed) shifts the coefficient by $-1/2$, giving $\frac{q}{2(1-q)} - \frac{1}{2} = \frac{106}{45}$ in agreement with Sen's Euclidean mixed-ensemble result [7].

Our audit concludes that **the real-time Lorentzian reformulation of the cone-boost trace and the reproduction of Sen's vacuum mixed-ensemble coefficient $106/45$ are the strongest constructive results in Section 5.3**, provided they are interpreted as a Lorentzian counterpart to Gibbons--Hawking [4] and real-time replica [10] calculations rather than a microscopic enumeration of black hole microstates.

---

## 2. Anatomy of the Section 5.3 Calculation

### 2.1 Marginally Trapped Surfaces and Clock Normalization

A genuine conceptual merit of Section 5.3 [1] is that it characterizes the horizon *locally* on the interior side before gluing on an exterior spacetime, avoiding the teleological dependence of an event horizon on future matter infall [5]. On a spherically symmetric cut $S$ of a Schwarzschild horizon of radius $r_h$, the outward and inward future-directed null normals ($l \cdot n = -1$) satisfy the marginally trapped surface conditions

$$
\Theta_{(l)}|_S = 0, \qquad \Theta_{(n)}|_S < 0,
$$

so that $\nabla_a \rho \nabla^a \rho|_S = -\frac{\rho_S^2}{2}\Theta_{(l)}\Theta_{(n)}|_S = 0$ on the background. Truncating the future inward null cone at a spacelike cap $\Sigma_1$ placed at $\rho = \epsilon \rho_S(y)$ (for fixed $0 < \epsilon \ll 1$) and normalizing the affine parameter by $u = 0$ and $\partial_u \rho = 1$ at $\Sigma_1$ defines a gravitational dressing clock [13] whose classical shear-free reading is

$$
\bar{u}_*^{\mathrm{class}} = \rho_S \int_\epsilon^1 dv = (1-\epsilon)\sqrt{\frac{\mathscr{A}}{4\pi}} = (1-\epsilon)r_h.
$$

### 2.2 Corner Boost Continuation and the Area Term

In the edge-mode phase space of a gravitational subregion [9, 6], the corner area operator generates relative boosts of the normal frame at $S$ via $\hat{\mathscr{K}} = \hat{\mathscr{A}}/(8\pi G_N)$. To assign weights to interior states admitted by the clock projector $P_{\mathscr{D}} = \mathbf{1}_{[0,\ell(\mathscr{D})]}(\hat{\bar{u}}_*)$, Chandrasekaran glues the future half of the causal diamond to its time reflection along $\Sigma_1$. Summing over a complete basis on $\Sigma_1$ cancels unitary evolution ($U^\dagger U = \hat{1}$), leaving only the corner boost at $S$. Analytically continuing the boost rapidity $\eta \to i\pi$ on each copy produces a full $2\pi$ rotation around $S$ and yields the unnormalized density operator

$$
C_{\mathscr{D}}^\dagger C_{\mathscr{D}} = P_{\mathscr{D}} e^{-\hat{\mathscr{A}}/(4G_N\hbar)} P_{\mathscr{D}} = P_{\mathscr{D}} e^{-\hat{s}} P_{\mathscr{D}}, \qquad \hat{s} \equiv \frac{\hat{\mathscr{A}}}{4G_N\hbar}.
$$

Assuming $\dim \mathcal{H}_{\mathscr{D}} < \infty$ (so $Z_{\mathscr{D},1} = \mathrm{Tr}_{\mathcal{H}_{\mathscr{D}}} e^{-\hat{s}} < \infty$), normalizing $\rho_{\mathscr{D}} = e^{-\hat{s}} / Z_{\mathscr{D},1}$ immediately produces the Bekenstein--Hawking term $\langle \hat{s} \rangle = \langle \hat{\mathscr{A}} \rangle / (4G_N\hbar)$ [2, 3, 12] together with the subleading correction $\log Z_{\mathscr{D},1}$.

### 2.3 Clock Ratio $q$, Replica Gluing, and the $106/45$ Coefficient

To evaluate $\log Z_{\mathscr{D},1}$, vary the upper cutoff $l$ in the clock projector $\mathbf{1}_{[0,l]}(\hat{\bar{u}}_*)$ and define $Z(l) = \sum_{\bar{u}_{*,i} \le l} e^{-s_i}$ (valid since $[\hat{s}, \hat{\bar{u}}_*] = 0$). Integrating $Z(l')$ from $0$ to $l$ weights each eigenstate by $(l - \bar{u}_{*,i})$:

$$
\int_0^l Z(l')\,dl' = \sum_{\bar{u}_{*,i} \le l} (l - \bar{u}_{*,i}) e^{-s_i} = Z(l)\left(l - \langle \hat{\bar{u}}_* \rangle_l\right).
$$

Differentiating $\log\!\left[\frac{1}{l}\int_0^l Z(l')\,dl'\right]$ with respect to $\log l$ gives the exact identity

$$
l \frac{d}{dl} \log\!\left[\frac{1}{l}\int_0^l Z(l')\,dl'\right] = \frac{\langle \hat{\bar{u}}_* \rangle_l}{l - \langle \hat{\bar{u}}_* \rangle_l}.
$$

Define $r_h$ dynamically in the clock-projected ensemble by $4\pi r_h^2 = \langle \hat{\mathscr{A}} \rangle_l$ and assume the average quantum focusing delay is subleading: $\langle \hat{\bar{u}}_* - (1-\epsilon)(\hat{\mathscr{A}}/4\pi)^{1/2} \rangle = o(r_h)$. Defining $x = (1-\epsilon)r_h / \ell(\mathscr{D}) < 1$ and the limiting ratio $q = \lim_{r_h/\ell_P \to \infty} \langle \hat{\bar{u}}_* \rangle / \ell(\mathscr{D})$, concavity of the square root and the Raychaudhuri lower bound $\hat{\bar{u}}_* \ge (1-\epsilon)(\hat{\mathscr{A}}/4\pi)^{1/2}$ bracket $q$ in $x^2 \le q \le x < 1$ (and in fact fix $q = 2x^2/(1+x^2)$ self-consistently via the second-moment identity in Footnote 23 of [1]). Integrating the logarithmic derivative from a fixed reference scale $l_0$ to $\ell(\mathscr{D})$ and substituting $\log(\ell(\mathscr{D})/l_0) = \frac{1}{2}\log\langle \hat{s} \rangle + O(1)$ yields

$$
\log Z_{\mathscr{D},1} = \left[\frac{q}{1-q} + o(1)\right]\log\frac{\ell(\mathscr{D})}{l_0} + O(1) = \left[\frac{q}{2(1-q)} + o(1)\right]\log\langle \hat{s} \rangle + O(1).
$$

To determine $q$ at one loop, Chandrasekaran resolves the trace into Gaussian area windows $f_b(s) = \exp[-(s-s_b)^2/(4s_b)]$ (using $\sigma_s^2 = 2s_b$, so $\int_0^\infty f_b(s)\,(4\pi s_b)^{-1/2}\,ds_b = 1$):

$$
Z(l) = \int_0^\infty \frac{ds_b}{(4\pi s_b)^{1/2}} \, \mathrm{Tr}(C_b^\dagger C_b), \qquad C_b = C_{\mathscr{D}} f_b(\hat{s})^{1/2}.
$$

In the one-loop graviton-plus-ghost determinant [11] on the Ricci-flat Schwarzschild background ($R_{ab} = 0$), the logarithmic term is controlled by the four-dimensional Gauss--Bonnet density $E_4 = R_{abcd}R^{abcd}$. Comparing $n$ copies glued cyclically against $n$ copies closed separately in the Lorentzian replica trace [10] cancels smooth bulk and cap terms, leaving the opening-angle variation at $S$ [8]:

$$
\log \mathrm{Tr}(C_b^\dagger C_b) = \frac{53}{45(4\pi)^2} \left(8\pi \int_S R[q]\,dA\right)\log(s_b^{1/2}) + O(1) = \frac{106}{45}\log s_b + O(1),
$$

where $\int_S R[q]\,dA = 8\pi$ by the two-dimensional Gauss--Bonnet theorem on $S \simeq S^2$. In the Gaussian area-window decomposition, the measure $ds_b / s_b^{1/2}$ contributes an additional power $+1/2$ to the scaling of $Z(l)$ with the upper area bound $s_* = \pi l^2 / [G_N\hbar(1-\epsilon)^2] \propto l^2$. Matching $\log Z_{\mathscr{D},1}$ therefore yields

$$
\frac{q}{2(1-q)} = \frac{106}{45} + \frac{1}{2} = \frac{257}{90} \quad\Longrightarrow\quad \frac{q}{1-q} = \frac{257}{45} \quad\Longrightarrow\quad q = \frac{257}{302} \approx 0.8510,
$$

with self-consistent radius-to-cutoff ratio $x = \sqrt{257/347} \approx 0.8606$. Finally, transforming from horizon area $s_b = 4\pi G_N M^2/\hbar$ to Schwarzschild mass $M$ via $ds_b / s_b^{1/2} \propto dM$ removes the $+1/2$ measure shift. Summing over angular momenta (whose rotational fluctuations shift $s_b$ only by $O(1)$ at fixed $M$) yields the fixed-mass mixed-ensemble logarithmic coefficient

$$
\frac{q}{2(1-q)} - \frac{1}{2} = \frac{106}{45},
$$

matching Sen's Euclidean result [7] in $D = 4$, where $S_{\mathrm{mixed}}(M) = S_{\mathrm{BH}}(M, \vec{J}=0) + C_{\mathrm{local}}\log(r_h/\ell_P)$ with $C_{\mathrm{local}}^{\mathrm{grav}} = 424/90 = 212/45$ and $\log(r_h/\ell_P) = \frac{1}{2}\log s_b$.

---

## 3. Critical Audit of Assumptions and Limitations

The table below summarizes the key structural assumptions underlying Section 5.3 of [1] and identifies where the argument relies on unproved steps or subtle ensemble/geometric identifications.

| Aspect | Role in Section 5.3 | Critical Assessment |
| :--- | :--- | :--- |
| **Analytic continuation $\eta \to i\pi$** | Produces the thermal weight $e^{-s_i}$ and the leading $\langle \hat{\mathscr{A}} \rangle / (4G_N\hbar)$ entropy term. | Geometric/thermodynamic continuation analogous to Gibbons--Hawking [4] and Euclidean path-integral traces [14]; does *not* count explicit microstates in a Hilbert space basis. |
| **Finite dimension $\dim \mathcal{H}_{\mathscr{D}} < \infty$** | Guarantees $Z_{\mathscr{D},1} < \infty$ and ensures $\rho_{\mathscr{D}}$ is a trace-class density operator. | Inherits both defects of Section 5.2: infinite angular degeneracy of $P_{\mathscr{D}}$ (requiring the joint transverse-focusing projection $\mathcal{H}_{\mathscr{D}}^{\mathrm{reg}}$) and the circular trace-convergence argument. |
| **Subleading focusing delay and ratio $q$** | Locks $x = (1-\epsilon)r_h/\ell(\mathscr{D})$ to $q$ via $q = 2x^2/(1+x^2)$ and fixes $\log Z_{\mathscr{D},1}$. | Unlike an arbitrary external parameter, $x$ is dynamically set by $Z(l)$, but this relies critically on the unproved non-perturbative assumption $\langle \hat{\bar{u}}_* - (1-\epsilon)(\hat{\mathscr{A}}/4\pi)^{1/2} \rangle = o(r_h)$ and on $Z(l)$ being dominated by macroscopic areas $s_b \sim s_*$. |
| **Bulk/cap cancellation in replica trace** | Isolates the $106/45$ coefficient from the opening-angle variation at $S$ via [8]. | For the static Schwarzschild saddle at $n=1$, the conical variation matches the smooth bulk Euler integral ($\chi=2$). For a general dynamical marginally trapped surface inside a collapsing star with a cap $\Sigma_1$, verifying that cap boundary terms do not pollute the $n=1$ trace $\mathrm{Tr}(C_b^\dagger C_b)$ requires a dedicated boundary heat-kernel analysis. |
| **Ensemble and zero modes** | Matches Sen's coefficient $\frac{106}{45}$ at fixed mass with angular momenta summed. | Corresponds strictly to Sen's *mixed ensemble* $S_{\mathrm{mixed}}(M)$ [7]. In the fixed-$(M, J_3)$ microcanonical ensemble in $D=4$, rotational zero modes subtract $N_C \log(r_h/\ell_P) = \frac{1}{2}\log s_b$, giving $\frac{167}{90}$. How zero modes behave on a finite capped diamond versus asymptotically flat Schwarzschild needs explicit verification. |
| **Vacuum-only scope** | All 4D constructions in Sections 3--5 assume vacuum gravity ($\Lambda$ only). | Coupling matter modifies both the Raychaudhuri clock and the one-loop determinant, providing sharp falsifiable tests (Section 4) and linking to null-hypersurface quantization programs [15]. |

---

## 4. Matter-Field Extensions and Falsifiable Tests

In four-dimensional general relativity coupled to $n_S$ minimally coupled massless real scalars, $n_V$ massless $U(1)$ vector fields, $n_F$ massless Dirac fermions, and $n_{3/2}$ massless spin-$3/2$ fields, Sen's Euclidean calculation [7] (Eqs. (1.2) and (1.4)) gives the mixed-ensemble logarithmic entropy correction for an uncharged Schwarzschild black hole as

$$
S_{\mathrm{mixed}}(M) = S_{\mathrm{BH}}(M, \vec{J}=0) + \frac{1}{2} C_{\mathrm{local}} \log s_b, \qquad C_{\mathrm{local}} = \frac{1}{90}\left(2 n_S - 26 n_V + 7 n_F - \frac{233}{2} n_{3/2} + 424\right),
$$

where we used $\log(r_h/\ell_P) = \frac{1}{2}\log s_b$. Comparing this formula against the Lorentzian clock-trace mechanism of Section 5.3 yields two concrete tests—one quantitative consistency check for scalars, and one structural breakdown for vector fields.

### 4.1 Test 1: Minimally Coupled Massless Scalar Field ($n_S = 1$)

Add a single minimally coupled massless real scalar field $\varphi$ with action $I_{\mathrm{mat}}[\varphi, g] = -\frac{1}{2}\int_{\mathscr{D}} \sqrt{-g}\, g^{ab}\partial_a\varphi\partial_b\varphi\, d^4x$.

> **Proposition 4.1 (Scalar Focusing and Modified Null Clock).**
> Along a future-directed affinely parametrized null generator with tangent $l^a$, the scalar stress-energy tensor $T_{ab}^{(\varphi)} = \partial_a\varphi\partial_b\varphi - \frac{1}{2}g_{ab}(\partial\varphi)^2$ obeys $T_{ab}^{(\varphi)} l^a l^b = (\partial_u \varphi)^2 \ge 0$. Through the null Einstein constraint $R_{ab}l^a l^b = 8\pi G_N (\partial_u\varphi)^2$, the Raychaudhuri equation becomes
>
> $$
> \frac{d^2\rho}{du^2} + \rho\left[\frac{1}{8}(\partial_u\bar{q})^{AB}\partial_u\bar{q}_{AB} + 4\pi G_N (\partial_u\varphi)^2\right] = 0.
> $$
>
> Changing to the normalized area coordinate $v = \rho / \rho_S(y)$ (on expanding generators where $\partial_u\rho > 0$), the dimensionless focusing integral in Eq. (3.26c) of [1] acquires an additive, non-negative scalar flux term:
>
> $$
> \Xi_y^{(\varphi)}(v) = \int_\epsilon^v s\left[\frac{1}{8}(\partial_s\bar{q})^{AB}\partial_s\bar{q}_{AB} + 4\pi G_N (\partial_s\varphi)^2\right] ds, \qquad u_*(y) = \rho_S(y)\int_\epsilon^1 e^{\Xi_y^{(\varphi)}(v)}\,dv.
> $$

*Quantitative prediction and caveats:*

1. **Joint restriction and persistent angular degeneracy:** Because $4\pi G_N (\partial_s\varphi)^2 \ge 0$, scalar excitations delay the clock $u_*(y)$ just like graviton shear, so $\hat{\bar{u}}_* \le \ell(\mathscr{D})$ restricts both radial graviton and radial scalar modes. However, $\Xi_y^{(\varphi)}(v)$ still lacks angular derivatives $\nabla_A \varphi$, so the scalar sector inherits the same infinite angular-momentum degeneracy as the graviton sector unless a transverse focusing projection $\hat{Q}$ (including the scalar momentum flux $T_{ab}^{(\varphi)} q_c{}^a l^b$ in $\mathfrak{C}_{la}$) is imposed simultaneously.
2. **Exact shift in the logarithmic coefficient and clock ratio:** From Sen's formula with $n_S = 1$, a minimally coupled massless real scalar adds $+\frac{2}{90} = +\frac{1}{45}$ to $C_{\mathrm{local}}$, shifting the coefficient of $\log s_b$ in $S_{\mathrm{mixed}}(M)$ by $+\frac{1}{90}$ (from $\frac{106}{45}$ to $\frac{213}{90} = \frac{71}{30}$). Plugging $\alpha_\varphi = \frac{71}{30}$ into the Section 5.3 relation $\frac{q_\varphi}{2(1-q_\varphi)} = \alpha_\varphi + \frac{1}{2} = \frac{43}{15}$ predicts a slightly larger limiting clock ratio:

$$
q_\varphi = \frac{86}{101} \approx 0.8515 \qquad \left(\Delta q = q_\varphi - q = \frac{86}{101} - \frac{257}{302} = +\frac{15}{30502} > 0\right).
$$

Notably, $\Delta q > 0$ has the sign expected from additional positive scalar focusing raising $\langle \hat{\bar{u}}_* \rangle / \ell(\mathscr{D})$. Verifying directly from the Lorentzian null-cone trace that adding $\varphi$ shifts $\log \mathrm{Tr}(C_b^\dagger C_b)$ by $+\frac{1}{90}\log s_b$ without introducing uncancelled cap terms at $\Sigma_1$ is a clean, falsifiable one-loop calculation.

### 4.2 Test 2: Vector Fields ($n_V > 0$) and Breakdown of the Clock-Projected Ensemble

A far sharper stress test arises when coupling minimally coupled massless $U(1)$ vector fields (such as Einstein--Maxwell theory or multi-photon extensions).

> **Observation 4.2 (Positivity Bound on the Lorentzian Clock Trace vs. Vector Fields).**
> Because $Z(l) = \sum_{\bar{u}_{*,i} \le l} e^{-s_i}$ is a sum of strictly positive Boltzmann weights, $Z(l)$ is monotonically non-decreasing in $l$. Consequently, in any regime where $\rho_{\mathscr{D}}$ remains dominated by macroscopic horizon areas ($0 < q < 1$), the clock-ratio formula enforces a strict lower bound on the fixed-mass mixed-ensemble logarithmic coefficient:
>
> $$
> \frac{q}{2(1-q)} > 0 \quad\Longrightarrow\quad \alpha \equiv \frac{q}{2(1-q)} - \frac{1}{2} > -\frac{1}{2}.
> $$
>
> By contrast, Sen's Euclidean formula [7] gives $\alpha(n_V) = \frac{106}{45} - \frac{13}{90} n_V = \frac{212 - 13 n_V}{90}$ for pure gravity coupled to $n_V$ minimally coupled massless $U(1)$ vector fields. Although classical Maxwell radiation obeys the null energy condition ($T_{ab}^{(A)} l^a l^b \ge 0$) and focuses null generators positively, quantum gauge/ghost contributions enter $C_{\mathrm{local}}$ with a *negative* sign:
> - For $1 \le n_V \le 19$, $\alpha(n_V) + \frac{1}{2} = \frac{257 - 13 n_V}{90} > 0$, predicting that adding Maxwell fields *decreases* $q$ (e.g., $q_{V=1} = \frac{244}{289} \approx 0.8443 < \frac{257}{302}$) despite positive classical focusing.
> - For $n_V \ge 20$, $\alpha(n_V) \le -\frac{8}{15} < -\frac{1}{2}$ (violating the positivity floor), so $\alpha(n_V) + \frac{1}{2} \le -\frac{1}{30} < 0$.

> **Remark (Physical Interpretation of the $n_V \ge 20$ Failure Mode).**
> For $n_V \ge 20$, the integral $Z(l) = \int_{s_0}^{s_*} (4\pi s_b)^{-1/2}\mathrm{Tr}(C_b^\dagger C_b)\,ds_b \sim \int_{s_0}^{s_*} s_b^{\alpha - 1/2}\,ds_b$ converges at its upper limit $s_*$ and becomes *ultraviolet-dominated* by Planck-scale areas $s_b \sim s_0 = O(1)$ rather than macroscopic black holes ($s_*/4 < s < s_*/2$). Thus $q \to 0$, the macroscopic probability assumption behind Eq. (5.63) of [1] fails, and the unconditioned clock-projected ensemble $\rho_{\mathscr{D}}$ ceases to describe a macroscopic Schwarzschild black hole. Extracting Sen's negative logarithmic coefficient in this regime requires conditioning externally on a macroscopic area or mass band (via $C_b$) rather than relying on the clock-ratio formula $\frac{q}{2(1-q)} - \frac{1}{2}$. (See `NCG-005` for the full phase analysis and $\mathcal{N} \ge 4$ supergravity benchmarks.)

---

## 5. Bibliography and References

1. V. Chandrasekaran, *An algebraic quantization of gravity from the null cone*, `arXiv:2611.34924v1 [hep-th]` (2026).
2. J. D. Bekenstein, *Black holes and entropy*, Phys. Rev. D **7** (1973) 2333--2346.
3. S. W. Hawking, *Particle creation by black holes*, Commun. Math. Phys. **43** (1975) 199--220.
4. G. W. Gibbons and S. W. Hawking, *Action integrals and partition functions in quantum gravity*, Phys. Rev. D **15** (1977) 2752--2756.
5. S. A. Hayward, *General laws of black-hole dynamics*, Phys. Rev. D **49** (1994) 6467--6474 [`gr-qc/9303006`].
6. S. Carlip and C. Teitelboim, *The off-shell black hole*, Class. Quant. Grav. **12** (1995) 1699--1704 [`gr-qc/9312002`].
7. A. Sen, *Logarithmic corrections to Schwarzschild and other non-extremal black hole entropy in different dimensions*, JHEP **04** (2013) 156 [`arXiv:1205.0971`].
8. D. V. Fursaev, A. Patrushev, and S. N. Solodukhin, *Distributional geometry of squashed cones*, Phys. Rev. D **88** (2013) 044054 [`arXiv:1306.4000`].
9. W. Donnelly and L. Freidel, *Local subsystems in gauge theory and gravity*, JHEP **09** (2016) 102 [`arXiv:1601.04744`].
10. S. Colin-Ellerin, X. Dong, D. Marolf, M. Rangamani, and Z. Wang, *Real-time gravitational replicas: Formalism and a variational principle*, JHEP **05** (2021) 117 [`arXiv:2012.00828`].
11. F. Bastianelli, R. Bonezzi, and M. Melis, *Gauge-invariant coefficients in perturbative quantum gravity*, Eur. Phys. J. C **82** (2022) 1139 [`arXiv:2206.13287`].
12. V. Chandrasekaran, G. Penington, and E. Witten, *Large $N$ algebras and generalized entropy*, JHEP **04** (2023) 009 [`arXiv:2209.10454`].
13. L. Ciambelli, L. Freidel, and R. G. Leigh, *Null Raychaudhuri: canonical structure and the dressing time*, JHEP **01** (2024) 166 [`arXiv:2309.03932`].
14. E. Colafranceschi, X. Dong, D. Marolf, and Z. Wang, *Algebras and Hilbert spaces from gravitational path integrals: Understanding Ryu--Takayanagi/HRT as entropy without AdS/CFT*, JHEP **10** (2024) 063 [`arXiv:2310.02189`].
15. L. Ciambelli and M. S. Klinger, *Quantization of gravity on null hypersurfaces*, `arXiv:2607.07785 [hep-th]` (2026).
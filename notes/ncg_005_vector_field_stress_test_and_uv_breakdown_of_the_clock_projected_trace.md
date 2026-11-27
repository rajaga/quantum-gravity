---
id: NCG-005
target_paper: arXiv:2611.34924v1 (Chandrasekaran, Nov 2026)
sections_covered: [5.3, Appendix D.3]
status: conditional
last_updated: 2026-11-27
---

# NCG-005: Massless Vector-Field Stress Test and the $n_V \ge 20$ Breakdown of the Clock-Projected Trace

## 1. Claim Being Examined

In Section 5.3 of `arXiv:2611.34924v1`, the thermodynamic entropy of a large four-dimensional Schwarzschild black hole is extracted from a Lorentzian trace over interior states of a causal diamond $\mathscr{D}$ bounded by a marginally trapped surface $S$ and truncated on its future inward null cone at maximum clock reading $\ell(\mathscr{D})$:

$$
S(\rho_{\mathscr{D}}) = \frac{\langle \hat{\mathscr{A}} \rangle}{4G_N\hbar} + \log Z_{\mathscr{D},1}, \qquad Z_{\mathscr{D},1} = \mathrm{Tr}_{\mathcal{H}_{\mathscr{D}}} e^{-\hat{s}}, \qquad \hat{s} \equiv \frac{\hat{\mathscr{A}}}{4G_N\hbar}.
$$

Varying the upper clock cutoff $l$ in $Z(l) = \sum_{\bar{u}_{*,i} \le l} e^{-s_i}$ and defining the macroscopic limiting clock ratio $q = \lim_{r_h/\ell_P \to \infty} \langle \hat{\bar{u}}_* \rangle_l / l$ (with $\ell_P = \sqrt{G_N\hbar}$), Section 5.3 obtains the fixed-mass mixed-ensemble logarithmic correction:

$$
\Delta S_{\log}(M) = \alpha \log s_b + O(1), \qquad \alpha = \frac{q}{2(1-q)} - \frac{1}{2}, \qquad s_b = \frac{4\pi G_N M^2}{\hbar}.
$$

In pure vacuum gravity, one-loop evaluation yields $q = 257/302$, giving $\alpha = 106/45$ in agreement with Sen's Euclidean mixed-ensemble result (`JHEP 04 (2013) 156`). We test whether this unconditioned clock-trace mechanism remains viable when minimally coupled massless matter fields—in particular $n_V$ massless $U(1)$ vector fields or $\mathcal{N} \ge 4$ supergravity multiplets—are coupled to four-dimensional general relativity.

## 2. Verdict / Summary

**Unconditional result (Positivity Floor and UV Takeover):** Assuming the causal-diamond Hilbert space $\mathcal{H}_{\mathscr{D}}^{\mathrm{reg}}$ is finite-dimensional, the positivity and monotonicity of $Z(l) = \sum_{\bar{u}_{*,i} \le l} e^{-s_i}$ enforce a strict lower bound $\alpha > -1/2$ in any regime where $\rho_{\mathscr{D}}$ remains dominated by macroscopic horizon areas ($0 < q < 1$). Whenever the one-loop area-window trace scales as $\mathrm{Tr}(C_b^\dagger C_b) \sim c_0 s_b^\alpha$ with $\alpha \le -1/2$, the unconditioned trace $Z(l)$ fails to concentrate on macroscopic black holes ($s_*/4 < s < s_*/2$), becomes ultraviolet-dominated by Planck-scale areas $s_b \sim s_0 = O(1)$ (or spreads logarithmically across scales at $\alpha = -1/2$), and drives $q \to 0$.

**Conditional application to 4D matter-coupled gravity:** Provided the Lorentzian one-loop trace $\mathrm{Tr}(C_b^\dagger C_b)$ reproduces Sen's 4D mixed-ensemble coefficient $\alpha(n_S, n_V, n_F, n_{3/2})$ without uncancelled cap or edge-mode shifts:

1. **Vector-field threshold ($n_V \ge 20$):** Minimally coupled massless $U(1)$ vector fields shift $\alpha$ downward by $-13/90$ per field—despite satisfying the classical null energy condition and focusing null generators positively. In Einstein--Maxwell theory with $n_V \ge 20$ massless photons (and no other matter), $\alpha$ drops to $-8/15 < -1/2$ and the unconditioned clock-projected ensemble $\rho_{\mathscr{D}}$ breaks down.
2. **Standard $\mathcal{N} \ge 4$ supergravities also trigger the breakdown:** The obstruction is not confined to contrived large-$n_V$ models. Pure four-dimensional $\mathcal{N}=4$, $\mathcal{N}=6$, and $\mathcal{N}=8$ supergravities on an uncharged Schwarzschild background give $\alpha = -1, -3, -5$ respectively—all strictly below $-1/2$.
3. **No $D=4$ charge-ensemble loophole:** In four dimensions, $\partial^2 S_{\mathrm{BH}}/\partial Q_\alpha^2\vert_{Q=0} = -4\pi$ is independent of $r_h$, so summing over electric charges ($\mu_\alpha = 0$) versus fixing $Q_\alpha = 0$ changes $\log Z$ only by $O(1)$ and cannot shift $\alpha$.

## 3. Derivation / Audit Steps

### Step 3.1: Monotonicity of $Z(l)$ and the $\alpha > -1/2$ Positivity Floor

Assume $\dim \mathcal{H}_{\mathscr{D}}^{\mathrm{reg}} < \infty$ (with the joint clock and transverse-focusing regularization of `NCG-001` so that $Z(l)$ is well-defined and finite). Because $[\hat{s}, \hat{\bar{u}}_*] = 0$, expand in a joint orthonormal eigenbasis $\lvert i \rangle$ with eigenvalues $(s_i, \bar{u}_{*,i})$:

$$
Z(l) = \sum_{\bar{u}_{*,i} \le l} e^{-s_i}.
$$

Integrating $Z(l')$ over $l' \in [0, l]$ weights each eigenstate by $(l - \bar{u}_{*,i})$:

$$
\int_0^l Z(l')\,dl' = \sum_{\bar{u}_{*,i} \le l} (l - \bar{u}_{*,i}) e^{-s_i} = Z(l)\left(l - \langle \hat{\bar{u}}_* \rangle_l\right).
$$

Dividing by $l$ and differentiating with respect to $\log l$ (almost everywhere on the discrete spectrum, or equivalently in integrated form from a fixed UV scale $l_0$ to $\ell(\mathscr{D})$) yields the exact identity:

$$
\log\!\left[\frac{1}{\ell(\mathscr{D})}\int_0^{\ell(\mathscr{D})} Z(l')\,dl'\right] - \log\!\left[\frac{1}{l_0}\int_0^{l_0} Z(l')\,dl'\right] = \int_{l_0}^{\ell(\mathscr{D})} \frac{\langle \hat{\bar{u}}_* \rangle_{l'}}{l' - \langle \hat{\bar{u}}_* \rangle_{l'}} \frac{dl'}{l'}.
$$

Since $\frac{1}{l}\int_0^l Z(l')\,dl' = Z(l)(1 - \langle \hat{\bar{u}}_* \rangle_l / l)$, whenever $\langle \hat{\bar{u}}_* \rangle_l / l \to q \in [0, 1)$ as $l/\ell_P \to \infty$, the factor $\log(1 - \langle \hat{\bar{u}}_* \rangle_l / l) = \log(1-q) + o(1)$ is $O(1)$, giving:

$$
\log Z_{\mathscr{D},1} = \left[\frac{q}{1-q} + o(1)\right]\log\frac{\ell(\mathscr{D})}{l_0} + O(1).
$$

In a macroscopic regime where $0 < q < 1$ and the average quantum focusing delay is subleading ($\langle \hat{\bar{u}}_* - (1-\epsilon)\ell_P\sqrt{\hat{s}/\pi} \rangle = o(l)$), the area expectation value $\langle \hat{s} \rangle_l \equiv \pi r_h^2/\ell_P^2$ scales proportionally to $s_*(l) \equiv \pi l^2 / [\ell_P^2(1-\epsilon)^2]$, with limiting ratio $x^2 \equiv \lim_{l/\ell_P \to \infty} \langle \hat{s} \rangle_l / s_*(l) = q/(2-q) \in (0, 1)$ (Footnote 23 of `arXiv:2611.34924v1`). Hence $\log(\ell(\mathscr{D})/l_0) = \frac{1}{2}\log\langle \hat{s} \rangle + O(1)$, and

$$
\log Z_{\mathscr{D},1} = \left[\frac{q}{2(1-q)} + o(1)\right]\log\langle \hat{s} \rangle + O(1).
$$

Transforming from the area-window measure $ds_b / s_b^{1/2}$ to fixed Schwarzschild mass $M$ via $s_b = 4\pi G_N M^2/\hbar$ ($ds_b / s_b^{1/2} \propto dM$) subtracts $1/2$ from the logarithmic coefficient, yielding the fixed-mass mixed-ensemble exponent:

$$
\alpha = \frac{q}{2(1-q)} - \frac{1}{2} \quad \Longleftrightarrow \quad q = \frac{2\alpha + 1}{2\alpha + 2}, \qquad x^2 = \frac{2\alpha + 1}{2\alpha + 3}.
$$

Because $0 < q < 1 \iff \frac{q}{2(1-q)} > 0$, any macroscopic clock-projected black hole regime strictly satisfies the positivity floor

$$
\alpha > -\frac{1}{2}.
$$

### Step 3.2: Exact Matter Thresholds from Sen's 4D Formula

For an uncharged 4D Schwarzschild black hole coupled to $n_S$ minimally coupled massless real scalars, $n_V$ massless $U(1)$ vector fields, $n_F$ massless **Dirac** fermions, and $n_{3/2}$ massless **Majorana** (equivalently Weyl) spin-$3/2$ fields, Sen (`JHEP 04 (2013) 156`, Eqs. 1.2 and 1.4) obtains the mixed-ensemble logarithmic entropy correction:

$$
S_{\mathrm{mixed}}(M, \vec{Q}=0) = S_{\mathrm{BH}}(M, \vec{J}=0, \vec{Q}=0) + C_{\mathrm{local}}\log\!\left(\frac{r_h}{\ell_P}\right), \qquad C_{\mathrm{local}} = \frac{1}{90}\left(2n_S - 26n_V + 7n_F - \frac{233}{2}n_{3/2} + 424\right).
$$

(In $D$ dimensions, the mass and charge Legendre-transform corrections carry factors of $-\frac{1}{2}(D-4)$, which vanish identically in $D=4$.) Using $\log(r_h/\ell_P) = \frac{1}{2}\log s_b$, the coefficient $\alpha = \frac{1}{2}C_{\mathrm{local}}$ multiplying $\log s_b$ is:

$$
\alpha(n_S, n_V, n_F, n_{3/2}) = \frac{106}{45} + \frac{1}{90}n_S - \frac{13}{90}n_V + \frac{7}{180}n_F - \frac{233}{360}n_{3/2}.
$$

The positivity floor $\alpha > -1/2$ is violated ($\alpha \le -1/2$) whenever

$$
13n_V + \frac{233}{4}n_{3/2} - n_S - \frac{7}{2}n_F \ge 257.
$$

Evaluating representative four-dimensional matter spectra gives:

| Theory / Field Content $(n_S, n_V, n_F, n_{3/2})$ | Fixed-Mass Coeff $\alpha$ | Trace Exponent $\alpha + \frac{1}{2}$ | Clock Ratio $q = \frac{2\alpha+1}{2\alpha+2}$ | Area Ratio $x^2 = \frac{2\alpha+1}{2\alpha+3}$ | Ensemble Regime |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Pure gravity $(0, 0, 0, 0)$ | $+106/45 \approx +2.356$ | $+257/90 \approx +2.856$ | $257/302 \approx 0.8510$ | $257/347 \approx 0.7406$ | Macroscopic (IR) |
| Einstein--Maxwell / IR SM $(0, 1, 0, 0)$ | $+199/90 \approx +2.211$ | $+244/90 \approx +2.711$ | $244/289 \approx 0.8443$ | $244/334 \approx 0.7305$ | Macroscopic (IR) |
| Unbroken SM $(4, 12, 45/2, 0)$ | $+37/24 \approx +1.542$ | $+49/24 \approx +2.042$ | $49/61 \approx 0.8033$ | $49/73 \approx 0.6712$ | Macroscopic (IR) |
| $10$ photons $(0, 10, 0, 0)$ | $+41/45 \approx +0.911$ | $+127/90 \approx +1.411$ | $127/172 \approx 0.7384$ | $127/217 \approx 0.5853$ | Macroscopic (IR) |
| $19$ photons $(0, 19, 0, 0)$ | $-7/18 \approx -0.389$ | $+1/9 \approx +0.111$ | $2/11 \approx 0.1818$ | $1/10 = 0.1000$ | Marginal IR |
| Exact threshold $(3, 20, 0, 0)$ | $-1/2 = -0.500$ | $0$ | $q \to 0$ (log) | $x^2 \to 0$ (log) | **Critical ($\log s_*$)** |
| $20$ photons $(0, 20, 0, 0)$ | $-8/15 \approx -0.533$ | $-1/30 \approx -0.033$ | $q \to 0$ ($l^{-1/15}$) | $x^2 \to 0$ ($l^{-1/15}$) | **UV-dominated** |
| Pure $\mathcal{N}=4$ SUGRA $(2, 6, 2, 4)$ | $-1$ | $-1/2$ | $q \to 0$ ($l^{-1}\log l$) | $x^2 \to 0$ ($l^{-1}$) | **UV-dominated** |
| $\mathcal{N}=8$ SUGRA $(70, 28, 28, 8)$ | $-5$ | $-9/2$ | $q \to 0$ ($l^{-1}$) | $x^2 \to 0$ ($l^{-2}$) | **UV-dominated** |

Two physical notes on this table:

* **Standard Model regimes:** For a macroscopic astrophysical Schwarzschild black hole ($r_h \gg m_e^{-1}$), only truly massless fields ($m \ll r_h^{-1}$, i.e., the graviton and $n_V = 1$ photon, plus any ultralight neutrinos) contribute to the logarithmic term, giving $\alpha = 199/90$ (or $\alpha = 817/360$ if all three neutrinos were massless Weyl fermions, $n_F = 3/2$). In the formal massless limit of the unbroken Standard Model (3 generations without right-handed neutrinos: $n_V = 12$, $n_S = 4$, and $45$ Weyl $\equiv n_F = 45/2 = 22.5$ Dirac fermions), $13(12) - 4 - \frac{7}{2}(22.5) = 73.25 < 257$, giving $\alpha_{\mathrm{SM}} = 37/24$ and $q_{\mathrm{SM}} = 49/61 \approx 0.8033$; adding $15$ extra dark $U(1)$ photons ($n_V = 27$ total) pushes the sum to $268.25 \ge 257$ and triggers the breakdown.
* **Supergravity universality:** On an uncharged Schwarzschild background ($F_{\mu\nu} = 0$ and constant moduli), non-minimal Pauli and scalar-vector couplings in $\mathcal{N} \ge 4$ supergravity are at least cubic in fluctuations and drop out of the one-loop quadratic operator. Moreover, each $\mathcal{N}=4$ vector multiplet $(n_S=6, n_V=1, n_F=2, n_{3/2}=0)$ satisfies $2(6) - 26(1) + 7(2) = 0$, so $\mathcal{N}=4$ supergravity coupled to *any* number of vector multiplets retains $\alpha = -1 < -1/2$.

### Step 3.3: Asymptotic Scaling of $Z(l)$ and $\langle \hat{\bar{u}}_* \rangle_l / l$ Across $\alpha = -1/2$

In the Gaussian area-window decomposition (Eq. 5.66 of `arXiv:2611.34924v1`, with $f_b(s) = \exp[-(s-s_b)^2/(4s_b)]$ and $\int_{-\infty}^\infty f_b(s)\,ds = \sqrt{4\pi s_b}$):

$$
Z(l) = \int_{s_0}^{s_*} \frac{ds_b}{\sqrt{4\pi s_b}} \, \mathrm{Tr}(C_b^\dagger C_b), \qquad \mathrm{Tr}(C_b^\dagger C_b) \sim c_0 \, s_b^{\alpha},
$$

where $s_0 = O(1)$ is a fixed Planck-scale lower cutoff and $s_* = \pi l^2 / [\ell_P^2(1-\epsilon)^2]$. Writing the effective area-density weight as $\rho_s(s) e^{-s} \sim \frac{c_0}{\sqrt{4\pi}} s^{\alpha - 1/2}$ and approximating $\bar{u}_*(s)/l \approx \sqrt{s/s_*}$ (valid when quantum focusing delays are subleading), the trace and clock expectation value obey:

$$
Z(l) \sim \frac{c_0}{\sqrt{4\pi}} \int_{s_0}^{s_*} s^{\alpha - 1/2}\,ds, \qquad
\frac{\langle \hat{\bar{u}}_* \rangle_l}{l} \sim \frac{s_*^{-1/2} \int_{s_0}^{s_*} s^{\alpha}\,ds}{\int_{s_0}^{s_*} s^{\alpha - 1/2}\,ds}.
$$

Evaluating these integrals as $s_* / s_0 = (l/l_0)^2 \to \infty$ separates the parameter space into distinct asymptotic phases:

1. **Macroscopic / IR-dominated phase ($\alpha > -1/2$, e.g., $n_V \le 19$):**
   Both integrals are dominated by the upper limit $s_*$:
   $$
   Z(l) \sim \frac{c_0}{\sqrt{4\pi}\,(\alpha + \frac{1}{2})} s_*^{\alpha + 1/2}, \qquad
   \frac{\langle \hat{\bar{u}}_* \rangle_l}{l} \to q = \frac{2\alpha + 1}{2\alpha + 2} \in (0, 1).
   $$
   The probability of lying in the macroscopic band $s_*/4 < s < s_*/2$ approaches the positive constant $2^{-(\alpha + 1/2)} - 4^{-(\alpha + 1/2)} > 0$ (matching Eq. 5.63 of `arXiv:2611.34924v1`).

2. **Critical marginal point ($\alpha = -1/2$, e.g., $n_V = 20, n_S = 3$):**
   The trace diverges only logarithmically, probability spreads logarithmically over all area scales $[s_0, s_*]$, and $q \to 0$:
   $$
   Z(l) \sim \frac{c_0}{\sqrt{4\pi}} \log\!\left(\frac{s_*}{s_0}\right), \qquad
   \frac{\langle \hat{\bar{u}}_* \rangle_l}{l} \sim \frac{2}{\log(s_*/s_0)} = \frac{1}{\log(l/l_0)} \to 0, \qquad
   P(s_*/4 < s < s_*/2) \sim \frac{\log 2}{\log(s_*/s_0)} \to 0.
   $$

3. **Weak UV-dominated phase ($-1 < \alpha < -1/2$, e.g., $n_V = 20$ where $\alpha = -8/15$):**
   $Z(l)$ converges at $s_* \to \infty$ to an $l$-independent UV constant $Z(\infty) \sim \frac{c_0}{\sqrt{4\pi}\,\lvert\alpha + 1/2\rvert} s_0^{\alpha + 1/2}$, while the numerator of $\langle \hat{\bar{u}}_* \rangle_l$ remains IR-dominated. Thus $\langle \hat{\bar{u}}_* \rangle_l / l$ decays to zero via a slow power law:
   $$
   \frac{\langle \hat{\bar{u}}_* \rangle_l}{l} \sim \frac{\lvert \alpha + \frac{1}{2} \rvert}{\alpha + 1} \left(\frac{s_*}{s_0}\right)^{\alpha + 1/2} \propto \left(\frac{l}{l_0}\right)^{2\alpha + 1} \to 0.
   $$
   At $n_V = 20$, $2\alpha + 1 = -1/15$, so convergence to $q = 0$ is extremely slow ($\propto (l/l_0)^{-1/15}$)—an important finite-size effect for numerical checks.

4. **Strong UV-dominated phase ($\alpha \le -1$, e.g., $n_V \ge 24$, or pure $\mathcal{N}=4, 6, 8$ SUGRA):**
   For $\alpha = -1$ (such as pure $\mathcal{N}=4$ SUGRA), $\langle \hat{\bar{u}}_* \rangle_l / l \sim \frac{1}{2}\sqrt{s_0/s_*}\log(s_*/s_0) \propto (l/l_0)^{-1}\log(l/l_0)$. For $\alpha < -1$ (such as $n_V \ge 24$ or $\mathcal{N}=8$ SUGRA), both numerator and denominator localize at $s_0$, so $\langle \hat{\bar{u}}_* \rangle_l \to O(\ell_P)$ and:
   $$
   \frac{\langle \hat{\bar{u}}_* \rangle_l}{l} \sim \frac{\lvert \alpha + \frac{1}{2} \rvert}{\lvert \alpha + 1 \rvert} \sqrt{\frac{s_0}{s_*}} \propto \left(\frac{l}{l_0}\right)^{-1} \to 0.
   $$

In all cases with $\alpha \le -1/2$, the macroscopic probability weight $P(s_*/4 < s < s_*/2) \to 0$, and the unconditioned clock-projected state $\rho_{\mathscr{D}}$ no longer describes a macroscopic black hole.

## 4. Assumptions & Failure Modes

* **Classical Focusing vs. Quantum Ghost Sign:** Classically, a Maxwell field satisfies $T_{ab}^{(A)} l^a l^b = F_{ac}F_b{}^c l^a l^b \ge 0$, adding a non-negative focusing term to the Raychaudhuri equation and increasing $\bar{u}_*$ on every individual configuration. At one loop, however, the heat-kernel $a_4$ coefficient on Ricci-flat 4D backgrounds combines the Weyl-squared and Euler anomaly coefficients as $(c - a) = (36 - 62)/360 = -26/360 < 0$ per vector field (reflecting Faddeev--Popov ghost and longitudinal gauge contributions). For $n_V \ge 20$, this negative quantum prefactor suppresses the large-area density of states $\rho_s(s) e^{-s} \propto s^{\alpha - 1/2}$ strongly enough that $Z(l)$ saturates in the ultraviolet.
* **Ensemble Check for Electric Charges ($D = 4$):** For a 4D Reissner--Nordström black hole, expanding $S_{\mathrm{BH}}(M, Q)$ around $Q = 0$ gives $S_{\mathrm{BH}} = 4\pi G_N M^2/\hbar - 2\pi Q^2/\hbar + O(Q^4/M^2)$, so $\partial^2 S_{\mathrm{BH}}/\partial Q_\alpha^2\vert_{Q=0} = -4\pi/\hbar$ is strictly independent of $M$ and $r_h$. Consequently, summing over electric charges $Q_\alpha$ (fixed chemical potential $\mu_\alpha = 0$) versus fixing $Q_\alpha = 0$ modifies $\log Z$ only by an $r_h$-independent $O(1)$ constant, confirming that the $n_V \ge 20$ breakdown is not an artifact of charge-ensemble mismatch.
* **Unconditioned Clock Ensemble vs. Area-Conditioned Ensemble:** The breakdown occurs specifically because $\rho_{\mathscr{D}} = P_{\mathscr{D}} e^{-\hat{s}} P_{\mathscr{D}} / Z_{\mathscr{D},1}$ sums over *all* areas $0 \le s \le s_*$ weighted solely by $e^{-s}$ and the upper clock cutoff. If one instead conditions externally on a narrow macroscopic area window via $C_b = C_{\mathscr{D}} f_b(\hat{s})^{1/2}$ (fixing $s_b = 4\pi G_N M^2/\hbar \gg 1$ by hand), $\log \mathrm{Tr}(C_b^\dagger C_b) \sim \alpha \log s_b$ still reproduces Sen's negative coefficient—but the dynamical clock-ratio identity $\alpha = \frac{q}{2(1-q)} - \frac{1}{2}$ of Section 5.3 is abandoned.
* **Unverified Gauge Edge-Mode / Cap Matching:** Applying Sen's exact coefficient $-13/90$ per vector field to `arXiv:2611.34924v1` assumes that gauge-fixing and boundary conditions on the truncated cap $\Sigma_1$ and corner $S$ yield the same conical Gauss--Bonnet coefficient as Sen's smooth Euclidean Schwarzschild calculation. Because $U(1)$ gauge fields carry their own electric/magnetic corner edge modes at $S$ (Donnelly--Freidel, `JHEP 09 (2016) 102`), verifying whether these edge modes shift the one-loop trace $\mathrm{Tr}(C_b^\dagger C_b)$ remains an open check.

## 5. Follow-Up / Next Action

* **Candidate note `NCG-006` (Numerical Check of the $\alpha = -1/2$ Transition):** Construct a discrete spectral toy model on an area grid $s_k \in [s_0, s_*(l)]$ ($\Delta s = 1$) with one-loop density of states per unit dimensionless area $\rho_s(s) \sim \frac{c_0}{\sqrt{4\pi}} s^{\alpha - 1/2} e^s$ (corresponding to $\rho_M(M)\,dM \propto s^\alpha e^s dM$) and clock eigenvalues $\bar{u}_{*,k} = (1-\epsilon)\ell_P\sqrt{s_k/\pi}$. Verify numerically how $\langle \hat{\bar{u}}_* \rangle_l / l$ and $\langle \hat{s} \rangle_l / s_*(l)$ transition from $q = \frac{2\alpha + 1}{2\alpha + 2}$ and $x^2 = \frac{2\alpha + 1}{2\alpha + 3}$ (for $\alpha > -1/2$) through logarithmic decay at $\alpha = -1/2$ to power-law UV collapse ($l^{2\alpha+1}$ for $-1 < \alpha < -1/2$ and $l^{-1}$ for $\alpha < -1$, comparing e.g. $n_V = 0, 19, 20, 25$ and $\mathcal{N}=8$ SUGRA).
* **Candidate note `NCG-007` (Vector Edge Modes at $S$):** Compute the $U(1)$ edge-mode contribution on the capped inward null cone and check whether gauge boundary terms at $\Sigma_1$ and $S$ alter the one-loop conical determinant in $\mathrm{Tr}(C_b^\dagger C_b)$ relative to Sen's asymptotically flat Euclidean calculation.

## 6. References

* V. Chandrasekaran, *An algebraic quantization of gravity from the null cone*, `arXiv:2611.34924v1 [hep-th]` (2026).
* A. Sen, *Logarithmic corrections to Schwarzschild and other non-extremal black hole entropy in different dimensions*, JHEP **04** (2013) 156 [`arXiv:1205.0971`].
* S. M. Christensen and M. J. Duff, *Axial and conformal anomalies for arbitrary spin in gravity and supergravity*, Phys. Lett. B **76** (1978) 571--574; *New gravitational index theorems and supertheorems*, Nucl. Phys. B **154** (1979) 301--342.
* W. Donnelly and L. Freidel, *Local subsystems in gauge theory and gravity*, JHEP **09** (2016) 102 [`arXiv:1601.04744`].
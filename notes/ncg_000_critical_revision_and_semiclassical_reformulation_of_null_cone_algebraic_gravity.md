---
id: NCG-000
target_paper: arXiv:2611.34924v1 (Chandrasekaran, Nov 2026)
sections_covered: [3, 4.4, 5.2, 5.3, 5.4, 6, Appendices A--E]
status: verified-audit
last_updated: 2026-11-27
companion_pdf: salvaged_null_cone_gravity_revision.pdf
---

# A Critical Revision and Semiclassical Reformulation of Null-Cone Algebraic Gravity

**Technical Audit, Mathematical Repairs, and Scope Reduction of `arXiv:2611.34924v1`**

## Abstract

We present a systematic technical audit and formal reformulation of the background-independent null-cone quantization of four-dimensional vacuum general relativity proposed in `arXiv:2611.34924v1` (Chandrasekaran, 2026) [1]. While the classical symplectic reduction on intersecting null cones, the one-loop focusing bounds, and the Lorentzian derivation of black hole entropy corrections rest on solid ground, the headline claims of an unconditional, non-perturbative theory of four-dimensional quantum gravity fail at several load-bearing steps. Specifically, we identify:

1. An infinite angular-momentum degeneracy in the causal-diamond clock projector $P_{\mathscr{D}}$ that persists even at the full nonlinear level;
2. A functional-analytic circularity in the proof of finite-dimensionality ($\dim \mathcal{H}_{\mathscr{D}} < \infty$), which misapplies an open-amplitude convergence bound to a closed-loop trace;
3. Unaddressed multiple-choice, factor-ordering, and branch-suppression obstructions inherent to reduced phase space quantization; and
4. An unconstructed nonlinear Hamiltonian $\hat{H} = \mathcal{Q}(H_c)$ together with an unrenormalized coincidence limit in the semiclassical limit.

We provide rigorous repairs wherever possible—replacing the circular proof with a single-operator joint focusing projection and a clean conditional theorem, demonstrating the quantum reference frame resolution in a toy model, and salvaging the semiclassical backreaction as a covariant one-loop effective field theory (EFT)—while isolating the genuine non-perturbative open problems that remain.

---

## 1. Motivation and Scope of the Revision

Constructing a non-perturbative, ultraviolet-complete quantum theory of four-dimensional Einstein gravity remains one of the central unsolved problems in theoretical physics. In perturbative quantum gravity around Minkowski spacetime, pure general relativity is non-renormalizable at two loops in four-graviton scattering [5]. Any proposal claiming to bypass this obstruction through a background-independent quantization must therefore be subjected to stringent structural tests: it must establish that its Hilbert space and Hamiltonian are rigorously defined, that its finiteness proofs do not smuggle in trace-class assumptions, and that diffeomorphism invariance survives quantization without anomalies.

The proposal in `arXiv:2611.34924v1` [1] approaches this problem by reducing first-order general relativity on intersecting null cones of a causal diamond $\mathscr{D}$, quantizing the resulting radiative and corner edge-mode data algebraically, and assembling global amplitudes by gluing subregions. Notably, the original manuscript acknowledges extensive development in collaboration with an automated reasoning system (GPT-6 Astra). In pure mathematics, formal proof assistants can verify deductive validity line by line; in theoretical physics, however, no equivalent compiler checks whether formal manipulations of infinite-dimensional field operators correspond to well-defined, renormalized physical objects.

Subsequent critical scrutiny has highlighted that several of the paper's most ambitious non-perturbative claims rest on hidden assumptions or formal leaps. The purpose of this document is neither to dismiss the work wholesale nor to leave its overclaims uncorrected, but to perform a *constructive triage*:

1. Separate the mathematically sound classical, perturbative, and conditional results from the unjustified non-perturbative claims.
2. Provide explicit, non-circular mathematical repairs for the causal-diamond finiteness argument (Section 5.2) and the semiclassical backreaction derivation (Section 6).
3. Clarify the exact structural gap between reduced phase space quantization and Dirac quantization via solvable toy models.
4. State clearly the remaining constructive quantum field theory problems required to complete the program.

---

## 2. Section-by-Section Comparison: Original vs. Salvaged Framework

When stripped of unproved non-perturbative assertions, `arXiv:2611.34924v1` [1] retains substantial value as a study of classical null-cone phase spaces, semiclassical subregion algebras, one-loop focusing bounds, and Lorentzian black hole thermodynamics. The table below summarizes the exact boundary between what survives scrutiny and what must be dropped or downgraded.

| Section / Topic | Original Claim | Salvaged Result | Must Be Dropped |
| :--- | :--- | :--- | :--- |
| **Classical Null-Cone Phase Space** (Sec. 3, App. A--B) | Exact reduced phase space and boundary Hamiltonian on intersecting null cones. | Sound classical GR: null constraint reduction, edge-mode symplectic form, and gluing of overlapping causal diamonds. | Treating classical reduction as automatically equivalent to Dirac quantization (suppresses caustic fluctuations; clock-dependent). |
| **Finiteness of Amplitudes** (Sec. 4.4) | All intermediate-state sums converge; UV divergences are artifacts of expanding in $G_N$ first. | A neat toy calculation on one null cone illustrating non-commuting limits ($N \to \infty$ vs. $G_N \to 0$). | Any claim that this resolves the 2-loop 4-graviton UV divergence in flat-space scattering [5]. |
| **Causal Diamond Finiteness & Area Spectrum** (Sec. 5.2, App. D.3) | Unconditional proof that $\dim \mathcal{H}_{\mathscr{D}} < \infty$ and $\hat{\mathscr{A}}$ has a discrete spectrum. | (1) Joint-operator space $\mathcal{H}_{\mathscr{D}}^{\mathrm{reg}}$; (2) Conditional Finiteness Theorem; (3) One-loop mode count $\log d(s) \le_\epsilon 1 + (sQ_*)^{3/4}$. | Unconditional proof by contradiction (circularly assumes unconditional trace convergence) and single-clock projection (infinite $j$-degeneracy). |
| **Black Hole Entropy** (Sec. 5.3) | Bekenstein--Hawking entropy and one-loop log correction from the Lorentzian trace. | Clean real-time derivation of the area term via corner-boost continuation and reproduction of Sen's mixed-ensemble $106/45$ vacuum coefficient [12]. | Any implication of microscopic state counting; unconditioned clock-trace universality (breaks down for $n_V \ge 20$ massless $U(1)$ vector fields). |
| **ER = EPR & Factorization** (Sec. 5.4) | Connected spatial topologies are physically identical to entangled disconnected states. | Perturbative demonstration that entangled graviton modes on disconnected horizons reproduce connected horizon correlators. | Non-perturbative proof that spatial topology is never a superselection sector in full 4D gravity. |
| **Semiclassical Limit** (Sec. 6, App. D.1) | Einstein's equations and one-loop backreaction emerge from the non-perturbative theory. | Rigorous one-loop EFT derivation of dressed graviton backreaction on a fixed background via Schwinger--Keldysh and Hadamard subtraction. | Derivation from an unconstructed non-perturbative Hamiltonian $\hat{H} = \mathcal{Q}(H_c)$ and ad-hoc fixed-smearing coincidence limits. |
| **Diffeomorphism Invariance** (App. E) | Background-independent, anomaly-free Lorentzian quantum gravity. | An axiomatic framework specifying conditions under which Lorentzian amplitudes match Euclidean path-integral axioms [16]. | The claim that 4D first-order gravity has been proved to satisfy these axioms non-perturbatively. |

---

## 3. Repairing Section 5.2: Angular Degeneracy and Conditional Finiteness

Section 5.2 of the original paper [1] attempts to prove unconditionally that a macroscopic causal diamond with bounded gravitational clock reading $\hat{\bar{u}}_* \le \ell(\mathscr{D})$ has a finite-dimensional Hilbert space $\mathcal{H}_{\mathscr{D}}$, and hence a discrete corner area spectrum. This argument suffers from two distinct mathematical defects that must be repaired.

### 3.1 Defect 1: Infinite Angular Degeneracy in $P_{\mathscr{D}}$

In Eq. (4.22) of [1], the shear focusing operator entering the gravitational clock $\hat{\bar{u}}_*$ is defined along each null generator $y \in S$ by

$$
\hat{\Xi}_y(v) = \frac{1}{4}\int_{\epsilon}^{v} s \left[ (\partial_s \hat{z}^1)^\dagger \partial_s \hat{z}^1 + (\partial_s \hat{z}^2)^\dagger e^{2\hat{z}^1} \partial_s \hat{z}^2 \right] ds.
$$

Crucially, $\hat{\Xi}_y(v)$ contains *no angular derivatives* ($\nabla_A \hat{z}^\alpha$), and the radiative symplectic form (Eq. (3.42b) of [1]) is likewise independent of angular momentum $j$. Consequently, at the linearized level, a single graviton excitation in the lowest radial mode ($k=1$) with arbitrary tensor-harmonic angular momentum $j \in \{2, 3, 4, \dots\}$ produces the exact same angular-averaged focusing shift.

Moreover, this obstruction is not cured by the nonlinear exponential $e^{\Xi_y(v)}$. Taking a sequence of smoothed, mutually orthonormal Walsh-type sign profiles $w_n(y)$ in equal-area coordinates on $S^2$ satisfying $|w_n(y)| \le (4\pi)^{-1/2}$ uniformly everywhere on $S^2$ (with arbitrarily high angular momentum as $n \to \infty$), the shear profile $h_{AB}(v,y) = f(v) w_n(y) e_{AB}$ yields a *pointwise* focusing integral $\Xi_y(v)$—and hence a full nonlinear clock reading $\bar{u}_*$—bounded above by the exact same finite constant for all $n \ge 1$. The single-projector space $P_{\mathscr{D}}\mathcal{H}_\omega$ with $P_{\mathscr{D}} = \mathbf{1}_{[0,\ell(\mathscr{D})]}(\hat{\bar{u}}_*)$ therefore exhibits an infinite angular degeneracy and cannot be finite dimensional.

**Repair (Single-Operator Joint Focusing Projection).** To suppress both radial and angular excitations, one must incorporate the dimensionless inward transverse focusing functional $Q[h]$ from Appendix D.3 (Eq. (D.40) of [1]), which couples to the normal connection $\varpi_I$ via the linearized angular constraint $\partial_v(v^2 \varpi_I) = -\frac{t_j}{2} v^2 \partial_v h_I$ with $t_j^2 = (j-1)(j+2)/2$:

$$
Q[h] = \sum_I \int_\epsilon^1 dv \left( |\varpi_I|^2 + \frac{v^2}{8} |\partial_v h_I|^2 \right).
$$

Because $|\varpi_I|^2$ scales as $j(j+1)|h_I|^2$, high angular momentum is penalized (and blows up on the Walsh-type family $w_n(y)$ as $n \to \infty$).

Note, however, that because the radiative commutator $[\hat{h}_I(v), \hat{h}_I(v')] \propto i\hbar\,\mathrm{sgn}(v-v')/(vv')$ is nonlocal along each null generator (Eq. (A.36) of [1]), the operators $\hat{\bar{u}}_*$ and $\hat{Q}$ do *not* commute in general, so a naive product of spectral projections $P_{\mathscr{D}}\mathbf{1}_{[0,Q_*]}(\hat{Q})$ is not a self-adjoint orthogonal projection. Furthermore, $\hat{\bar{u}}_*$ has dimensions of length whereas $\hat{Q}$ is dimensionless. Fixing a positive macroscopic length scale $\lambda > 0$, we therefore form the single positive self-adjoint joint focusing operator

$$
\hat{F}_\lambda \equiv \hat{\bar{u}}_* + \lambda \hat{Q},
$$

and define the regularized causal diamond projection and Hilbert space by its orthogonal spectral projection:

$$
P_{\mathscr{D}}^{\mathrm{reg}} \equiv \mathbf{1}_{[0, \ell_{\mathrm{eff}}(\mathscr{D})]}(\hat{F}_\lambda), \qquad \mathcal{H}_{\mathscr{D}}^{\mathrm{reg}} \equiv P_{\mathscr{D}}^{\mathrm{reg}} \mathcal{H}_\omega.
$$

Because $\hat{Q} \ge 0$ is constructed from area-preserving radiative and normal-connection data commuting with the total corner area $\hat{\mathscr{A}}$ on each fixed-area sector $\mathcal{K}_{\mathscr{A}}$ (so $[\hat{F}_\lambda, \hat{\mathscr{A}}] = 0$), the operator inequality $\hat{F}_\lambda \ge \hat{\bar{u}}_* \ge (1-\epsilon)(\hat{\mathscr{A}}/4\pi)^{1/2}$ preserves the compact upper bound on the dimensionless area operator $\hat{s} = \hat{\mathscr{A}}/(4G_N\hbar)$:

$$
0 \le P_{\mathscr{D}}^{\mathrm{reg}} \hat{s} P_{\mathscr{D}}^{\mathrm{reg}} \le s_* P_{\mathscr{D}}^{\mathrm{reg}}, \qquad s_* \equiv \frac{\pi \ell_{\mathrm{eff}}(\mathscr{D})^2}{G_N\hbar(1-\epsilon)^2}.
$$

### 3.2 Defect 2: Circularity in the Proof by Contradiction

With the corner boost operator $\hat{\mathscr{K}} = \hat{\mathscr{A}}/(8\pi G_N)$ analytically continued to $\eta = i\pi$ and weighted by the positive Gaussian $f_b(s)$ (with minimum $m_{b,\mathscr{D}} = \min_{0 \le s \le s_*} f_b(s) > 0$), the reflected preparation operator $C_b = C_{\mathscr{D}} f_b(\hat{s})^{1/2}$ satisfies

$$
0 < e^{-s_*} m_{b,\mathscr{D}} \hat{1} \le C_b^\dagger C_b = f_b(\hat{s}) e^{-\hat{s}} \le \hat{1}.
$$

Note that if $\mathrm{Tr}(C_b^\dagger C_b) < \infty$ were assumed upfront, the operator bounds above would yield $\dim \mathcal{H}_{\mathscr{D}}^{\mathrm{reg}} \le e^{s_*} m_{b,\mathscr{D}}^{-1}\mathrm{Tr}(C_b^\dagger C_b) < \infty$ in two lines without graviton correlators or boosts. To avoid this, the original paper assumes $\dim \mathcal{H}_{\mathscr{D}} = \infty$, groups an adapted basis into length-$r$ cycles $V$, and proves that for the shifted boost-response operator $X = \Delta_\eta \hat{\mathcal{O}} - \frac{\delta_\eta}{2}\hat{1}$, every finite union of cycles $P$ obeys $Z_P[X] \le 0 < Z[X]$. It then invokes Eq. (4.29) to claim that $Z_P[X]$ must converge to $Z[X]$, yielding a contradiction.

This final step is circular for three functional-analytic reasons:

1. **Inner product vs. trace:** Eqs. (4.29)--(4.30) prove absolute convergence via Cauchy--Schwarz only for *open* transition amplitudes $\langle \phi | U_2 U_1 | \psi \rangle$ between normalizable $L^2$ states. Closing the cut at $S$ computes a *trace*, to which Cauchy--Schwarz does not apply.
2. **Non-trace-class rearrangement:** If $\dim \mathcal{H}_{\mathscr{D}}^{\mathrm{reg}} = \infty$, then the lower bound on $C_b^\dagger C_b$ forces $\mathrm{Tr}(C_b^\dagger C_b) = +\infty$. For a non-absolutely-convergent trace, partial sums depend on basis grouping. Demanding that the cycle-grouped net converge to $Z[X]$ implicitly assumes unconditional trace convergence.
3. **Unproved existence of $Z[X]$:** The one-loop calculation in Eq. (5.28a) computes only the *ratio* $Z(j_L, j_R)/Z(0,0)$ where the one-loop determinant cancels; the unnormalized loop amplitude $Z[X]$ is never shown to be finite.

**Repair (Conditional Finiteness Theorem and Promoted One-Loop Bound).** Removing the circularity requires stating the gluing-convergence assumption explicitly as a hypothesis, and promoting the one-loop focusing mode count of Appendix D.3 to the main text as the primary non-circular evidence.

> **Theorem 3.1 (Conditional Finiteness of $\mathcal{H}_{\mathscr{D}}^{\mathrm{reg}}$).**
> Let $X = \Delta_\eta \hat{\mathcal{O}} - \frac{\delta_\eta}{2}\hat{1}$ be the shifted two-sided shear boost-response observable across $S$, with $\delta_\eta = \langle 0 | \Delta_\eta \hat{\mathcal{O}} | 0 \rangle > 0$. Assume that:
> - **(H1)** The uncut closed-loop amplitude $Z[X]$ is well-defined and strictly positive ($Z[X] > 0$); and
> - **(H2)** Gluing across $S$ holds unconditionally on $\mathcal{H}_{\mathscr{D}}^{\mathrm{reg}}$, meaning $\lim_{P \uparrow \hat{1}} Z_P[X] = Z[X]$ along every increasing net of finite-rank projections converging to $\hat{1}$ in the strong operator topology, independent of the choice of orthonormal basis and grouping.
>
> Then $\dim \mathcal{H}_{\mathscr{D}}^{\mathrm{reg}} < \infty$, and the corner area operator $\hat{\mathscr{A}}$ has a purely discrete spectrum on $\mathcal{H}_{\mathscr{D}}^{\mathrm{reg}}$.

*Proof.* Suppose $\dim \mathcal{H}_{\mathscr{D}}^{\mathrm{reg}} = \infty$. Partition $[0, s_*]$ into finitely many intervals of width at most $\Delta s$; at least one interval $I$ satisfies $\dim(\mathbf{1}_I(\hat{s})\mathcal{H}_{\mathscr{D}}^{\mathrm{reg}}) = \dim \mathcal{H}_{\mathscr{D}}^{\mathrm{reg}}$. Grouping an adapted orthonormal basis into disjoint $r$-cycles $V$ each containing at most one vector outside $I$, every finite union of complete cycles $P$ satisfies the variance bound (Eq. (D.25) of [1])

$$
\mathrm{Tr}\!\left[\rho_P (\hat{s} - s_0)^2\right] \le (\Delta s)^2 + \frac{s_*^2}{r \, e^{-s_*} m_{b,\mathscr{D}}}, \qquad s_0 \in I.
$$

By the boost-sensitivity bound $|\langle \Delta_\eta \hat{\mathcal{O}} \rangle_P| \le (|\eta|/\pi)\|\hat{\mathcal{O}}\| (\mathrm{Tr}[\rho_P(\hat{s}-s_0)^2])^{1/2}$ (Eq. (D.23) of [1]), choosing $\Delta s$ small and $r$ large ensures $|\langle \Delta_\eta \hat{\mathcal{O}} \rangle_P| \le \delta_\eta/2$ uniformly for all such $P$. Hence

$$
Z_P[X] = \mathrm{Tr}(P C_b^\dagger C_b)\left(\langle \Delta_\eta \hat{\mathcal{O}} \rangle_P - \frac{\delta_\eta}{2}\right) \le 0.
$$

As $P$ runs over finite unions of cycles ordered by inclusion, $P \uparrow \hat{1}$ strongly. By hypothesis (H2), $Z[X] = \lim_{P \uparrow \hat{1}} Z_P[X] \le 0$, contradicting (H1). Thus $\dim \mathcal{H}_{\mathscr{D}}^{\mathrm{reg}} < \infty$. $\blacksquare$

> **Proposition 3.2 (One-Loop Finiteness of Graviton States via Focusing).**
> Expanding the reduced phase space to quadratic order around a spherically symmetric causal diamond of dimensionless area $s \in (0, s_*]$ with fixed boundary data on $\partial\Sigma_i$ and $S$, impose the joint focusing bound $Q[h] \le Q_*$. Then the number of radiative modes whose single-graviton focusing shift satisfies $\nu_i \le \nu$ is bounded by $C_\epsilon (s\nu)^3$, and the number $d(s)$ of orthogonal graviton states obeying $\sum_i n_i \nu_i \le Q_*$ is finite:
>
> $$
> \log d(s) \le_\epsilon 1 + (s Q_*)^{3/4}.
> $$

---

## 4. Reduced Phase Space vs. Dirac Quantization

A core structural critique of `arXiv:2611.34924v1` [1] is its reliance on *Reduced Phase Space Quantization* (RPSQ): solving the gravitational constraints classically on expanding null cones ($\partial_u \rho > 0$) before quantizing. In constrained systems, RPSQ and *Dirac Quantization* [2] (quantizing first, then imposing constraints as operator equations) are generally inequivalent.

### 4.1 Toy Model Comparison

Consider a gravitational clock $(u, p_u)$ ($u > 0$) coupled to a matter or graviton mode $(q, p)$:

- **Linear constraint** $C = u p_u + H_{\mathrm{mat}}(q, p) = 0$: RPSQ fixes $T = \ln u$ (so $p_T = u p_u$) and quantizes $(q,p)$ on $L^2(\mathbb{R}, dq)$. Dirac quantization on $L^2(\mathbb{R}_+, du) \otimes L^2(\mathbb{R}, dq)$ agrees with RPSQ *provided* one chooses Weyl ordering $\mathcal{Q}(u p_u) = -i\hbar(u\partial_u + \frac{1}{2})$ and defines the physical inner product by group averaging $\langle \Psi_1 | \delta(\hat{C}) | \Psi_2 \rangle$.
- **Quadratic constraint** $C = p_u^2 - u^{-2} H_{\mathrm{mat}}(q, p) = 0$: Here RPSQ and Dirac quantization diverge sharply. Solving classically forces a choice of sign $p_u = \pm u^{-1}\sqrt{H_{\mathrm{mat}}}$, permanently discarding one branch (expanding vs. contracting). Moreover, choosing $u$ as the clock versus choosing $q$ as the clock yields unitarily inequivalent reduced quantum theories—the classic *multiple-choice problem* [7, 8].

### 4.2 The Quantum Reference Frame Resolution and the 4D Bottleneck

In the quadratic toy model with a free-clock matter sector $H_{\mathrm{mat}} = p_q^2$, multiplying $C$ classically by $u^2$ and setting $T = \ln u$ yields $\tilde{C} = p_T^2 - p_q^2 = 0$. (Even here, rescaling the constraint before quantization exposes a concrete factor-ordering ambiguity: for the Weyl-ordered momentum $\hat{p}_T = -i\hbar(u\partial_u + \frac{1}{2})$ on $L^2(\mathbb{R}_+, du)$, direct expansion gives $\hat{p}_T^2 = \hat{u}\hat{p}_u^2\hat{u} - \frac{\hbar^2}{4}$, shifting the constraint spectrum by $-\hbar^2/4$ relative to $\hat{u}\hat{p}_u^2\hat{u}$.) Once a self-adjoint quantization $\hat{\tilde{C}} = \hat{p}_T^2 - \hat{p}_q^2$ is fixed, both the branch-suppression and multiple-choice defects are rigorously resolved via Refined Algebraic Quantization [9] and Quantum Reference Frames (QRF) [15]:

1. **Restoring suppressed fluctuations:** Group averaging with $\delta(\hat{\tilde{C}})$ preserves both frequency branches, decomposing $\mathcal{H}_{\mathrm{phys}} = \mathcal{H}_+ \oplus \mathcal{H}_-$ and allowing coherent superpositions (and, when a potential $V(T,q)$ is present, quantum tunneling across turning points).
2. **Resolving the multiple-choice problem:** Conditioning $\mathcal{H}_{\mathrm{phys}}$ on Clock $T$ via a Page--Wootters reduction map $\mathcal{R}_T(\tau): \mathcal{H}_{\mathrm{phys}} \to L^2(\mathbb{R}, dq) \otimes \mathbb{C}^2$ and on Clock $q$ via $\mathcal{R}_q(q_0): \mathcal{H}_{\mathrm{phys}} \to L^2(\mathbb{R}, dT) \otimes \mathbb{C}^2$ yields an explicit unitary clock-switch operator $\hat{S}_{T \to q} = \mathcal{R}_q(q_0) \circ \mathcal{R}_T(\tau)^{-1}$.

Translating this blueprint to four-dimensional null-cone gravity would require starting from the unreduced symplectic potential in Appendix A.3 (Eq. (A.30a) of [1])—keeping $(\rho^2, \mu)$ and $(z^\alpha, \pi_\alpha)$ as independent quantum variables—and imposing the Raychaudhuri constraint $\hat{\mathfrak{C}}_v |\Psi\rangle = 0$ quantum mechanically. Doing so, however, immediately confronts the ultraviolet renormalization of the nonlinear coincident-point shear-squared term $\frac{\rho^2}{2} g_{\alpha\beta} (\partial_v z^\alpha)(\partial_v z^\beta)$ and requires proving that the quantum constraint algebra closes without anomalies (an active frontier in null-hypersurface quantization [17]). Because `arXiv:2611.34924v1` [1] solves $\mathfrak{C}_l = 0$ classically to bypass this wall, its quantization remains foliation- and state-dependent (as noted in Footnote 20 of [1]) and excludes off-shell caustic fluctuations.

---

## 5. Salvaging Section 6 as Perturbative Effective Field Theory

Section 6 of the original paper [1] aims to derive the classical Einstein equations and their one-loop quantum backreaction directly from the non-perturbative theory. This derivation fails as a non-perturbative proof for two reasons:

1. **Unconstructed interacting Hamiltonian:** Section 6.1 relies on the Moyal commutator expansion $\frac{i}{\hbar}[\mathcal{Q}(H_c), \mathcal{Q}(\mathcal{O})] = \mathcal{Q}(\{\mathcal{O}, H_c\}) + O(\hbar^2)$ for the nonlinear boundary Hamiltonian $H_c$ (Eq. (3.54) of [1]). In four-dimensional field theory, $\mathcal{Q}(H_c)$ is never constructed as a self-adjoint operator on $\mathcal{H}_\omega$, and the $O(\hbar^2)$ remainder contains uncontrolled ultraviolet contractions.
2. **Unrenormalized coincidence limit:** In Eq. (6.14) of [1], the quadratic backreaction source $\langle E_{ab}^{(2)}[h,h] \rangle_{\mathcal{G}}$ is evaluated by taking $p' \to p$ in $[\nabla_e \nabla_{f'} \mathcal{G}_{abc'd'}(p,p')]_{p'=p}$ while holding an ad-hoc smearing function fixed, rather than performing covariant renormalization of the quartically divergent coincidence limit of this twice-differentiated two-point function (since $\mathcal{G} \sim \sigma^{-1}$ diverges quadratically and $\nabla_e\nabla_{f'}\mathcal{G} \sim \sigma^{-2}$ diverges quartically as $p' \to p$).

**Repair (Perturbative One-Loop EFT Reformulation).** Section 6 can be made mathematically rigorous by abandoning the unconstructed non-perturbative $\mathcal{Q}(H_c)$ and reformulating the derivation directly as a one-loop effective field theory on a fixed classical background $g_0$ solving $E_{ab}[g_0] = G_{ab}[g_0] + \Lambda g_{0\,ab} = 0$:

1. Expand the first-order action directly to quadratic order in perturbations $h_{ab}$ around $g_0$ on the Schwinger--Keldysh contour $\mathcal{C}$ [6] (as in Appendix D.1, Eq. (D.4) of [1]), yielding the well-defined linearized equation $E_{ab}^{(1)}[h] = 0$.
2. Quantize the *linearized* graviton modes rigorously on the null-cone Fock space using the background symplectic form $\Omega$, choosing a physical Hadamard state $\rho_G$. To handle the gauge dependence of $E_{ab}^{(2)}[h,h]$ under linearized diffeomorphisms, work consistently with the boundary-dressed metric $X^*g$ (Eq. (6.8) of [1], following [13, 14]) or in a fixed covariant gauge on $\mathcal{C}$.
3. Replace the fixed-smearing coincidence limit in Eq. (6.14) with covariant *Hadamard point-splitting* [10, 11]: subtract the local geometric Hadamard parametrix $\mathcal{G}^{\mathrm{Had}}_{abc'd'}(p,p')$ before taking $p' \to p$, yielding a finite, covariantly conserved renormalized source $\langle E_{ab}^{(2)}[h,h] \rangle_{\mathrm{ren}}$. On a Ricci-flat vacuum background ($\Lambda = 0$, $R_{ab} = 0$), pure four-dimensional gravity is one-loop on-shell finite [4]; for $\Lambda \ne 0$ or with matter, the finite renormalization ambiguities take the standard curvature-squared form ($\alpha_1 R^2 + \alpha_2 R_{ab}R^{ab}$), which renormalize $\Lambda$ and $G_N$ on Einstein backgrounds.
4. Solve the resulting one-loop backreaction equation with the retarded Green's function $\mathcal{G}_R$:

$$
E_{ab}[\bar{g}] + \langle E_{ab}^{(2)}[h,h] \rangle_{\mathrm{ren}} = O(\hbar^2), \qquad \Delta g = \Delta g_0 - \mathcal{G}_R \langle E^{(2)}[h,h] \rangle_{\mathrm{ren}} + O(\hbar^2).
$$

> **Remark.** This reformulation makes Section 6 completely rigorous, but changes its physical status: it no longer demonstrates that a non-perturbative theory of quantum gravity recovers general relativity at low energies, instead reproducing the standard one-loop effective field theory of gravitons on curved spacetime [3, 6].

---

## 6. Remaining Open Problems

The repairs above yield a coherent, mathematically honest framework for semiclassical null-cone algebras, one-loop focusing bounds, and Lorentzian black hole thermodynamics. Upgrading this framework to a genuine non-perturbative theory of four-dimensional quantum gravity requires resolving four foundational open problems:

> **Conjecture 6.1 (Compact Resolvent of the Nonlinear Joint Focusing Operator).**
> At finite $G_N$ and $\hbar$ and fixed scale $\lambda > 0$, the renormalized nonlinear joint focusing operator $\hat{F}_\lambda = \hat{\bar{u}}_* + \lambda \hat{Q}$ admits a self-adjoint realization on $\mathcal{H}_\omega$ commuting with $\hat{\mathscr{A}}$ and possessing a compact resolvent on each area-bounded sector $\mathbf{1}_{[0,s_*]}(\hat{s})\mathcal{H}_\omega$. Proving this would establish $\dim \mathcal{H}_{\mathscr{D}}^{\mathrm{reg}} < \infty$ unconditionally and discharge hypotheses (H1)--(H2) of Theorem 3.1.

1. **Constructive Interacting Hamiltonian:** Rigorously constructing and renormalizing $\hat{H}_c$ as a self-adjoint operator on $\mathcal{H}_\omega$, free of ordering and ultraviolet pathologies, so that unitary time evolution and the classical limit $\hbar \to 0$ can be proved non-perturbatively.
2. **Two-Loop Four-Graviton Scattering:** Computing the flat-space $2 \to 2$ graviton scattering amplitude at two loops from glued causal diamonds to determine whether the Goroff--Sagnotti $R^3$ ultraviolet divergence [5] is genuinely cured or merely postponed.
3. **Anomaly-Free Diffeomorphism Invariance:** Upgrading Axiom 1 of Appendix E (and its equivalence with the Euclidean path-integral axioms [16]) from an assumption to a theorem by proving that amplitudes are independent of causal-diamond covers, cap truncations, and choices of pure state $\omega$ at finite $G_N$, and clarifying the relation to double-null crossed-product constructions [17].
4. **Microscopic Black Hole State Counting and Matter Tests:** Explicitly diagonalizing $(\hat{\mathscr{A}}, \hat{F}_\lambda)$ on marginally trapped surfaces to count microstates directly—replacing the corner-boost analytic continuation ($\eta \to i\pi$) with a genuine microscopic derivation of $S_{\mathrm{BH}} = \mathscr{A}/(4G_N\hbar)$—and resolving how the clock-projected ensemble responds to matter couplings (such as the $+1/90$ mixed-ensemble logarithmic shift for a massless scalar and the UV-dominated breakdown for $n_V \ge 20$ massless $U(1)$ vector fields compared against Sen's Euclidean results [12]).

---

## References

1. V. Chandrasekaran, *An algebraic quantization of gravity from the null cone*, `arXiv:2611.34924v1 [hep-th]` (2026).
2. P. A. M. Dirac, *Lectures on Quantum Mechanics*, Belfer Graduate School of Science, Yeshiva University, New York (1964).
3. B. S. DeWitt, *Quantum theory of gravity. II. The manifestly covariant theory*, Phys. Rev. **162** (1967) 1195--1239.
4. G. 't Hooft and M. Veltman, *One-loop divergencies in the theory of gravitation*, Ann. Inst. H. Poincaré Phys. Théor. A **20** (1974) 69--94.
5. M. H. Goroff and A. Sagnotti, *The ultraviolet behavior of Einstein gravity*, Nucl. Phys. B **266** (1986) 709--736.
6. E. Calzetta and B. L. Hu, *Closed-time-path functional formalism in curved spacetime: Application to cosmological back-reaction problems*, Phys. Rev. D **35** (1987) 495--509.
7. K. V. Kuchař, *Time and interpretations of quantum gravity*, in *Proceedings of the 4th Canadian Conference on General Relativity and Relativistic Astrophysics*, World Scientific (1992) 211--314; reprinted in Int. J. Mod. Phys. D **20** (2011) 3--86.
8. C. J. Isham, *Canonical quantum gravity and the problem of time*, in *Integrable Systems, Quantum Groups, and Quantum Field Theories*, NATO ASI Series C **409**, Kluwer (1993) 157--287 [`gr-qc/9210011`].
9. D. Giulini and D. Marolf, *On the generality of refined algebraic quantization*, Class. Quant. Grav. **16** (1999) 2479--2488 [`gr-qc/9812024`].
10. S. Hollands and R. M. Wald, *Local Wick polynomials and time ordered products of quantum fields in curved spacetime*, Commun. Math. Phys. **223** (2001) 289--326 [`gr-qc/0103074`].
11. S. Hollands and R. M. Wald, *Conservation of the stress tensor in perturbative interacting quantum field theory in curved spacetimes*, Rev. Math. Phys. **17** (2005) 227--311 [`gr-qc/0404074`].
12. A. Sen, *Logarithmic corrections to Schwarzschild and other non-extremal black hole entropy in different dimensions*, JHEP **04** (2013) 156 [`arXiv:1205.0971`].
13. W. Donnelly and L. Freidel, *Local subsystems in gauge theory and gravity*, JHEP **09** (2016) 102 [`arXiv:1601.04744`].
14. A. J. Speranza, *Local phase space and edge modes for diffeomorphism-invariant theories*, JHEP **02** (2018) 021 [`arXiv:1706.05061`].
15. P. A. Höhn, A. R. H. Smith, and M. P. E. Lock, *Trinity of relational quantum dynamics*, Phys. Rev. D **104** (2021) 066001 [`arXiv:1912.00033`].
16. E. Colafranceschi, X. Dong, D. Marolf, and Z. Wang, *Algebras and Hilbert spaces from gravitational path integrals: Understanding Ryu--Takayanagi/HRT as entropy without AdS/CFT*, JHEP **10** (2024) 063 [`arXiv:2310.02189`].
17. L. Ciambelli and M. S. Klinger, *Quantization of gravity on null hypersurfaces*, `arXiv:2607.07785 [hep-th]` (2026).
# Technical Audit Notes: Null-Cone Algebraic Quantum Gravity (arXiv:2611.34924)

A proposal on quantum gravity by Venkatesa Chandrasekaran has been published on arXiv: *"An algebraic quantization of gravity from the null cone"* (arXiv:2611.34924).

This repository is an independent, AI-assisted technical audit of that proposal. It makes **no claim** to solve non-perturbative 4D quantum gravity. The goal is narrower and falsifiable: separate rigorous classical/one-loop results from unproved non-perturbative leaps, check specific claims against established semiclassical benchmarks, and document where the framework breaks down.

Critiques of the approach have also started appearing—most notably Jonathan Oppenheim's *"Has AI come for quantum gravity?"*. The revision document (`NCG-000`) engages directly with those objections: rather than defending the paper's headline non-perturbative claims, it concedes where the original arguments fail (such as the unconstructed Hamiltonian $\mathcal{Q}(H_c)$ and the circular finiteness proof) and tests what can be cleanly salvaged as conditional algebra and one-loop effective field theory (EFT).

Corrections, counterexamples, and critical issues are very welcome.

## Index of Notes & Reports

| ID | Topic | Key Takeaway | Status | Files |
| :--- | :--- | :--- | :--- | :--- |
| **NCG-000** | Critical Revision & Semiclassical Reformulation | Section-by-section triage; repairs Sec. 5.2 via $\hat{F}_\lambda = \hat{\bar{u}}_* + \lambda\hat{Q}$ and a Conditional Finiteness Theorem; salvages Sec. 6 as one-loop Schwinger–Keldysh EFT with Hadamard point-splitting. | Conditional / Audit | [Markdown](notes/ncg_000_critical_revision_and_semiclassical_reformulation_of_null_cone_algebraic_gravity.md) · [PDF](pdfs/ncg_000_critical_revision_and_semiclassical_reformulation_of_null_cone_algebraic_gravity.pdf) |
| **NCG-004** | Sec. 5.3 Lorentzian Black Hole Entropy & Matter | Audits the corner-boost Lorentzian trace, clarifies mixed ($106/45$) vs. microcanonical ($167/90$) ensembles, and checks a minimally coupled massless scalar ($+1/90 \to 71/30$). | Conditional | [Markdown](notes/ncg_004_lorentzian_black_hole_entropy_and_matter_extension_section_5_3_wrap_up.md) · [PDF](pdfs/ncg_004_lorentzian_black_hole_entropy_and_matter_extension_section_5_3_wrap_up.pdf) |
| **NCG-005** | Massless Vector-Field Clock-Trace Breakdown | Proves an unconditional $\alpha > -1/2$ positivity floor for $Z(l)$ and shows UV-dominated breakdown for $n_V \ge 20$ photons and pure $\mathcal{N} \ge 4$ 4D supergravities against Sen (2013). | Proved floor / Conditional match | [Markdown](notes/ncg_005_vector_field_stress_test_and_uv_breakdown_of_the_clock_projected_trace.md) · [PDF](pdfs/ncg_005_vector_field_stress_test_and_uv_breakdown_of_the_clock_projected_trace.pdf) |
| **NCG-006** | RPSQ vs. Dirac & QRF Clock-Switching (Sec. 4) | Exposes the $-\hbar^2/4$ constraint-rescaling shift and four-ray multiple-choice obstruction, constructs the unitary Page–Wootters clock switch, and isolates 4D null-cone renormalization obstructions. | Proved toy model / Conditional 4D | [Markdown](notes/ncg_006_rpsq_dirac_qrf_clock_switching.md) · [PDF](pdfs/ncg_006_rpsq_dirac_qrf_clock_switching.pdf) |

## Methodology & Epistemic Hygiene
* **AI-assisted workflow:** Derivations, literature cross-checks (e.g., Sen 2013, Hollands–Wald, Page–Wootters/QRF literature), and audits were developed iteratively with LLM assistance and structured into self-contained notes.
* **Explicit separation of claims:** Every note separates **proved/checked algebra**, **conditional statements** (explicitly naming the unproved hypotheses), and **open bottlenecks**.
* **Canonical sources:** Markdown files in `notes/` serve as the editable source of truth; PDFs in `pdfs/` are compiled snapshots with formal equation numbering and bibliographies.
```[cite: 5]








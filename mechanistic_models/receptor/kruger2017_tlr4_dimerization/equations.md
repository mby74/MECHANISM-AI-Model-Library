# Equations

We model receptor dimerization as:

M + M ⇌ D

Let:
- M = fraction of monomers
- D = fraction of dimers

Constraint:
M + 2D = 1

Dynamics:
dD/dt = k_on * M^2 - k_off * D

At steady state:
k_on * M^2 = k_off * D

Ligand effects are modeled by modifying k_on and/or k_off.

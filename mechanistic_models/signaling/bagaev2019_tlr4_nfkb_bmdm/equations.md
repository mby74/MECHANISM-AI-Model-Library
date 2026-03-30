# Equations

## Model Type
Reduced ODE-based model inspired by Bagaev et al. (2019)

## Purpose
Capture the key phenomenon:

> Increased basal nuclear NF-κB accelerates NF-κB nuclear translocation under LPS stimulation.

---

## Variables

- N(t): nuclear NF-κB level
- B: basal nuclear NF-κB fraction (initial condition)

---

## Model Equation

dN/dt = k_act * (1 - N) * S - k_deg * N

Where:
- k_act: activation rate constant
- k_deg: degradation/export rate
- S: stimulation strength (LPS input)

---

## Initial Condition

N(0) = B

---

## Observable

Time-to-peak NF-κB nuclear level:
t_peak = argmax N(t)

---

## Biological Interpretation

- Higher basal NF-κB (B) reduces the time required to reach peak activation
- This reproduces the key effect described in Bagaev et al. (2019)

---

## Limitations

- Does not include full pathway (IKK, IκB, feedback loops)
- Not an SBML-equivalent implementation
- Intended as a minimal reproducible model

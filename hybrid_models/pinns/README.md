# PINNs (Physics-Informed Neural Networks)

This module contains Physics-Informed Neural Network (PINN) implementations used within the MECHANISM-AI framework.

## Purpose

PINNs are used to:

- Learn system dynamics constrained by differential equations
- Integrate mechanistic knowledge with data-driven models
- Approximate signaling pathway behavior (e.g., NF-κB dynamics)
- Enable fast surrogate modeling of biological systems

## Role in MECHANISM-AI

PINNs act as hybrid models that bridge:

- Mechanistic models (ODE/PDE systems)
- AI-based approximations
- Uncertainty-aware prediction

They support the iterative loop:
Design → Model → UQ → Experiment → Update

## Files

- `pinn_model.py` – neural network architecture
- `loss_functions.py` – physics-informed loss terms
- `training.py` – training routine

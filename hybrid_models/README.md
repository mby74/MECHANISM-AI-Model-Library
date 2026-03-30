# Hybrid Models

This directory contains hybrid AI–mechanistic models used within the MECHANISM-AI framework.

## Contents

- `pinns/`  
  Physics-Informed Neural Networks (PINNs) for learning constrained biological dynamics while incorporating mechanistic structure and differential equation information.

- `surrogate_models/`  
  Data-driven approximation models used to emulate computationally expensive mechanistic simulations for faster evaluation, screening, and iterative refinement.

## Purpose

Hybrid models complement mechanistic models by:

- improving scalability
- accelerating evaluation
- enabling learning under partial mechanistic knowledge
- supporting uncertainty-aware model refinement

These models are intended to work together with mechanistic models, cross-scale mappings, and the closed-loop workflow.

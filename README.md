# MECHANISM-AI-Model-Library

## 1. Project Goal

The goal of this project is to develop a multi-scale, AI–mechanistic modeling framework for understanding and controlling nonlinear biological systems.

Specifically, the framework aims to:

- Link molecular interactions (e.g., peptide binding) to system-level functional responses (e.g., NF-κB signaling)
- Enable uncertainty-aware prediction and decision-making
- Support iterative, closed-loop discovery through integration of AI, mechanistic models, and experimental data

The TLR4–MD-2 signaling pathway is used as a testbed system, with the broader goal of developing a generalizable platform for biological discovery and design.


## Model Library Architecture

The MECHANISM-AI model library is organized as a modular, multi-scale framework that integrates mechanistic models, hybrid AI approaches, and uncertainty-aware decision-making within a unified system.

Mechanistic models across biological scales (molecular → receptor → signaling → cellular → tissue) are defined in a hierarchical but interconnected framework, where outputs from one level inform and interact with adjacent scales through explicit mappings and iterative feedback.

- molecular models: peptide–protein interactions and binding features
- receptor models: receptor activation, dimerization, and kinetics
- signaling models: intracellular signaling pathways (e.g., NF-κB)
- cellular models: cytokine production and gene expression
- tissue models: multicellular systems and microphysiological models

Hybrid models augment scale-specific models (molecular through tissue) by combining data-driven learning with mechanistic structure to bridge scales, infer missing dynamics, and accelerate model evaluation.

The model purpose categories define the functional role of each model (e.g., forward, inverse, surrogate, hypothesis). This enables systematic organization, comparison, and selection within the workflow.

Interfaces define standardized input and output schemas for all models, ensuring interoperability and seamless integration across different scales and modeling approaches.

Mappings specify how outputs from one scale are transformed into inputs for another, enabling consistent information flow and coupling across molecular, receptor, signaling, cellular, and tissue levels.

Uncertainty quantification (UQ) provides a framework for assessing model confidence, comparing alternative models, and guiding decision-making and experimental prioritization.



```text
mechanism-ai-models/
│
├── mechanistic models/
│   ├── molecular (tructure-based, Energy-based and Feature extraction models) 
│   ├── receptor (kinetic, dimerization/clustering, and rule-based models)
│   ├── signaling (ODE-based, stochastic, and reduced-order models)
│   ├── cellular (cytokine production, gene expression, and phenotype models)
│   └── tissue (microphysiological systems, cell–cell interaction, and spatial/agent-based models)
│
├── hybrid_models/
│   ├── pinns (physics-informed neural network models for learning constrained dynamics)
│   └── surrogate_models (data-driven approximation models for fast evaluation)
│
├── model_purpose: classification of models by functional role in the workflow
│   ├── forward (predictive models mapping inputs to system-level outputs)
│   ├── inverse (models identifying inputs that achieve desired outcomes)
│   ├── surrogate (fast approximations of complex or computationally expensive models)
│   └── hypothesis (alternative mechanistic or conceptual models for testing assumptions)
│
├── interfaces: standardized input/output definitions for all models
│   ├── input_schema.py (defines required inputs such as molecular features, receptor states, and experimental conditions)
│   └── output_schema.py (defines outputs such as signaling responses, functional outcomes, and uncertainty estimates)
│
├── mappings: cross-scale transformation functions linking model outputs to inputs across scales
│   ├── molecular_to_receptor.py (maps binding and structural features to receptor activation states)
│   ├── receptor_to_signaling.py (translates receptor activation into signaling pathway dynamics)
│   └── signaling_to_cellular.py (maps signaling outputs to cellular responses such as cytokine production)
│
├── uq: uncertainty quantification and model evaluation framework
│   ├── uncertainty_methods (methods for estimating prediction confidence and uncertainty across models)
│   └── model_selection  (tools for comparing models and selecting the most reliable predictions)
│
├── mediator: integration layer coordinating model interaction and data flow
│   └── integration_engine.py (orchestrates model execution, applies mappings, and manages iterative updates)
│
└── workflows: end-to-end pipelines implementing the modeling and discovery process
    └── closed_loop_pipeline (iterative workflow integrating design, modeling, uncertainty evaluation, and experimental feedback)
```

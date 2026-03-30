# MECHANISM-AI-Model-Library

## 1. Project Goal

The goal of this project is to develop a multi-scale, AI–mechanistic modeling framework for understanding and controlling nonlinear biological systems.

This project aims to:

- Link molecular interactions (e.g., peptide binding) to system-level functional responses (e.g., NF-κB signaling)
- Enable uncertainty-aware prediction and decision-making
- Support iterative, closed-loop discovery through integration of AI, mechanistic models, and experimental data

The TLR4–MD-2 signaling pathway is used as a testbed system, with the broader goal of developing a generalizable platform for biological discovery and design. This is significant bacuase excessive Toll-like receptor 4 (TLR4) activation drives harmful inflammation in pediatric conditions including septic shock and severe Gram-negative infections. Current approaches broadly suppress inflammation and risk impairing host defense. There is currently no approved therapy that selectively attenuates lipopolysaccharide (LPS)-driven signaling while preserving protective immune response. There is an urgent need to develop precision approaches to block pathogenic inflammation while preserving immunity. Conventional one-shot design pipelines optimize structural affinity but do not incorporate functional signaling feedback. As shown in Figure 1, we propose an iterative AI framework that integrates experimental signaling data to refine design hypotheses and improve immune modulation. 

<p align="center">
![Picture2](https://github.com/user-attachments/assets/f273d0ef-ec1c-4899-89c6-b01a24903ebb)
</p>

## 2. Model Library Architecture

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
    └── closed_loop_pipeline (iterative workflow of design, modeling, uncertainty evaluation & experimental feedback)
```
## 3. Model Compatibility and Integration

Compatibility across models is ensured by design through a unified architecture that enables interoperability across biological scales (molecular → receptor → signaling → cellular → tissue) and modeling paradigms (mechanistic and hybrid AI models). This framework is implemented across the repository structure (`models/`, `hybrid_models/`, `interfaces/`, `mappings/`, `mediator/`, and `uq/`) and is governed by the following principles.



### 3.1. Design for Interoperability from the Start (Shared Interfaces)

All models in the `models/` and `hybrid_models/` directories follow standardized input and output interfaces defined in `interfaces/input_schema.py` and `interfaces/output_schema.py`. Each model may use different internal formulations such as ordinary differential equations, stochastic models, or physics-informed neural networks, but must accept and return a consistent set of variables including molecular features, receptor activation states, signaling outputs, and uncertainty estimates. This ensures seamless integration across scales within a unified workflow.



### 3.2. Cross-Scale Mapping Functions

Compatibility across scales is enforced through mapping functions defined in the `mappings/` directory. These functions formalize how outputs from one scale become inputs to another, ensuring consistent propagation of biological information. For example, molecular-scale outputs such as binding affinity and interface geometry are mapped to receptor-scale variables such as probability of dimerization and activation likelihood in `molecular_to_receptor.py`. Receptor activation states are translated into signaling pathway rate constants in `receptor_to_signaling.py`, and signaling outputs such as NF-κB dynamics are mapped to cellular responses including cytokine production in `signaling_to_cellular.py`. These mappings preserve biological meaning while ensuring computational consistency.



### 3.3. Time-Scale Alignment Across Models

Models at different biological scales operate on different time resolutions, ranging from molecular dynamics at nanoseconds to microseconds, to signaling processes at minutes to hours, and cellular responses at hours to days. Compatibility is achieved through time-scale alignment strategies implemented within model wrappers and hybrid models. These include coarse-graining of fast molecular processes, surrogate modeling for efficient approximation, and time rescaling to match signaling and cellular dynamics. These approaches enable consistent information exchange without temporal mismatch.



### 3.4. Model Wrappers for Modular Integration

Each model is encapsulated within a standardized wrapper that enables plug-and-play integration via `mediator/integration_engine.py`. These wrappers define how models receive inputs, produce outputs, and expose metadata such as scale and purpose. This abstraction allows models from both `models/` and `hybrid_models/` to be easily compared, replaced, or combined without modifying the overall workflow, thereby supporting modularity and extensibility.



### 3.5. Model Metadata for Consistency and Selection

All models include structured metadata aligned with the `model_purpose/` classification. This metadata defines the role and compatibility of each model within the system and includes elements such as the model name (for example, `nfkb_model_v1`), the biological scale, the modeling purpose, the defined inputs and outputs consistent with interface specifications, the underlying assumptions, and the type of uncertainty representation. This structured description enables systematic model comparison, selection, and integration across the workflow.



### 3.6. Mediator Layer for System Integration

A central integration layer implemented in `mediator/integration_engine.py` coordinates all model interactions. Instead of directly connecting models across scales, the framework uses this mediator to manage execution, apply cross-scale mappings, enforce interface compatibility, and control iterative updates. The integration follows a structured pattern in which design outputs are passed to the mediator, evaluated by models, and then returned to the mediator for progression to the next stage. This ensures that all interactions are controlled, consistent, and traceable.



### 3.7. Uncertainty Quantification as the Organizing Principle

Uncertainty quantification, implemented in the `uq/` directory, serves as the primary mechanism for coordinating model interaction and decision-making. It is used to reconcile conflicting predictions across models, determine which models are most reliable under specific conditions, and combine outputs when appropriate. It also guides model selection through `uq/model_selection/` and informs experimental prioritization. By incorporating uncertainty throughout the workflow, the system becomes adaptive and data-driven.



## 4. Integration with Workflow

These principles are operationalized in `workflows/closed_loop_pipeline/`, where AI-guided design generates candidate perturbations, models from `models/` and `hybrid_models/` evaluate system responses, mappings and interfaces ensure cross-scale consistency, the mediator coordinates execution and data flow, and uncertainty quantification guides decision-making and refinement. In summary, this architecture ensures that the model library functions as a coherent, interoperable system rather than a collection of independent models.

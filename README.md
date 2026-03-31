# Model Library for Project MECHANISM-AI

**MECHANISM-AI**: 'M'ulti-scale, 'E'xplainable 'C'ontrol and 'H'ypothesis-driven 'A'nalysis of 'N'onlinear 'I'mmune 'S'ystems via 'M'echanistic 'AI'
# **M**<sub>ulti-scale,</sub> **E**<sub>xplainable</sub> **C**<sub>ontrol</sub>

## 1. Overview
**MECHANISM-AI** is an iterative, mechanism-guided AI framework for discovering governing rules and control strategies in nonlinear, multi-scale biological systems.

The framework integrates:

- Structure-based molecular design (e.g., peptide–protein interactions)  
- Mechanistic modeling (receptor dynamics, signaling pathways)  
- AI/ML (including Physics-Informed Neural Networks and LLM-assisted reasoning)  
- Uncertainty Quantification (UQ)  
- Experimental feedback loops  

The **TLR4-mediated immune signaling pathway** is used as a testbed system, while the overall goal is to develop a generalizable AI-enabled scientific discovery platform.



## 2. Motivation 

Current AI-driven approaches in biology often optimize binding affinity but fail to predict functional outcomes (e.g., signaling response). Biological systems are nonlinear, multi-scale, and highly context-dependent.   

**MECHANISM-AI addresses this gap by linking** predicted molecular structures to multi-scale dynamics across molecular, receptor, signaling, cellular, and tissue levels, bridging structural interactions (e.g., binding and conformational changes) with emergent functional outcomes such as pathway activation and nonlinear system behavior..

**Structure → Dynamics → Function**

This enables:
- Predictive modeling of system-level responses  
- Discovery of interpretable governing rules  
- AI-guided identification of control mechanisms  

This aligns with the DOE GENESIS Mission goal of achieving AI advantage in scientific discovery.

## 3. From Structure-Based to Function-Guided Peptide Design

Conventional peptide design pipelines, such as BindCraft, generate candidates based on structural information and binding affinity. While effective for identifying peptides that bind to target proteins (e.g., the TLR4–MD-2 complex), these approaches do not account for downstream biological responses such as NF-κB activation or cytokine production.

In the MECHANISM-AI framework, functional outcomes obtained from mechanistic modeling, hybrid models (e.g., PINNs), and experimental data are used to refine peptide design hypotheses. These system-level insights are not directly used as inputs to BindCraft; instead, they are translated into updated structure-based design constraints, such as redefining target binding regions, modifying geometric constraints, and prioritizing peptides predicted to alter signaling dynamics.

This enables an iterative design loop in which functional outcomes inform updated structural constraints, guiding subsequent BindCraft design cycles toward peptides that achieve desired system-level effects.

### From Binding-Based Design to Function-Guided Peptide Design: Integration of Mechanistic AI with BindCraft
| Category | Conventional Design Hypothesis | Updated System-Level Hypothesis | How Knowledge Is Embedded into BindCraft Inputs | Improvement in Peptide Design |
|----------|--------------------------------|--------------------------------|------------------------------------------------|--------------------------------|
| Binding vs Function | High peptide binding affinity to MD-2 or TLR4 will inhibit LPS-induced signaling | Binding does not necessarily reduce NF-κB activation; functional outcome depends on receptor activation and signaling dynamics | Prioritize peptides predicted to reduce NF-κB activation and filter out high-affinity but non-functional binders | Select peptides based on functional impact, not just binding affinity |
| Target Site | Peptides should block the LPS binding pocket on MD-2 | Binding at dimerization interfaces or allosteric regions may more effectively alter TLR4 activation | Redefine target regions in BindCraft to include dimerization interfaces and allosteric sites | Target functionally relevant regions |
| Receptor Activation | Blocking LPS binding will prevent TLR4 activation | Activation depends on receptor dimerization and spatial organization | Introduce geometric constraints to disrupt receptor dimerization | Design peptides that disrupt receptor organization |
| Signaling Response | Reducing receptor activation reduces NF-κB signaling | NF-κB signaling exhibits nonlinear threshold behavior | Enforce design constraints that achieve sufficient disruption to cross activation thresholds | Design peptides that reduce NF-κB activation effectively |
| Modeling Level | Structure-based docking is sufficient | Functional outcomes emerge from multi-scale interactions | Use mechanistic models to pre-screen and rank candidates | Predict system-level responses before experiments |
| Hybrid Models (PINNs) | Not used | PINNs learn signaling dynamics from equations and data | Use PINNs as fast surrogate models to evaluate peptide impact on signaling | Efficient exploration of design space |
| LLM-Assisted Reasoning | Not used | LLMs generate and refine mechanistic hypotheses | Use LLMs to suggest new binding regions and constraints for BindCraft | Improve design strategy exploration |
| Context Dependence | Peptide effect is fixed | Response depends on cellular context and receptor state | Evaluate and refine constraints across biological conditions | Design context-aware peptides |
| Optimization Objective | Maximize binding affinity | Optimize reduction of NF-κB activation and cytokine response | Combine binding metrics with predicted functional outcomes | Shift to functional optimization |
| Interpretation of Failure | Failed peptides are discarded | Failure reveals missing mechanistic understanding | Update constraints by excluding ineffective regions and patterns | Improve design iteratively |
| Role of Peptides | Peptides block LPS binding | Peptides can modulate signaling dynamics | Design peptides to alter NF-κB activation patterns | Enable modulation instead of simple inhibition |
| Search Strategy | Screen based on binding scores | Use AI and uncertainty quantification | Use UQ to select informative candidates and refine constraints | Reduce experimental burden |

This framework transforms peptide design from a structure-based screening process into a mechanism-guided, function-aware system capable of iteratively improving design strategies based on biological response.

## 4. Overarching Goal

The goal of this project is to develop a multi-scale, AI–mechanistic modeling framework for understanding and controlling nonlinear biological systems.

This project aims to:

- Link molecular interactions (e.g., peptide binding) to system-level functional responses (e.g., NF-κB signaling)
- Enable uncertainty-aware prediction and decision-making
- Support iterative, closed-loop discovery through integration of AI, mechanistic models, and experimental data

The TLR4–MD-2 signaling pathway is used as a testbed system, with the broader goal of developing a generalizable platform for biological discovery and design. This is significant bacuase excessive Toll-like receptor 4 (TLR4) activation drives harmful inflammation in pediatric conditions including septic shock and severe Gram-negative infections. Current approaches broadly suppress inflammation and risk impairing host defense. There is currently no approved therapy that selectively attenuates lipopolysaccharide (LPS)-driven signaling while preserving protective immune response. There is an urgent need to develop precision approaches to block pathogenic inflammation while preserving immunity. Conventional one-shot design pipelines optimize structural affinity but do not incorporate functional signaling feedback. As shown in Figure 1, we propose an iterative AI framework that integrates experimental signaling data to refine design hypotheses and improve immune modulation. Specifically, design hypotheses evolve from conventional structure-based assumptions (binding affinity) to system-level, mechanistic insights (e.g., dimerization thresholds, nonlinear signaling regimes) based on model predictions and experimental feedback.


![Picture2](https://github.com/user-attachments/assets/7f82896d-744a-4f20-a4e0-eaecd2562b64)


## 5. Phase I Objectives (9 Months)

MECHANISM-AI is designed to demonstrate measurable improvements in (i) prediction accuracy of functional biological responses, (ii) speed of scientific discovery, (iii) interpretability (discovery of governing rules), and (iv) reduction of experimental search space. This repository supports a Phase I DOE GENESIS project aimed at demonstrating a working AI-enabled scientific discovery workflow.

### Deliverables:

- Prototype multi-scale mechanistic model of TLR4 signaling  
- Hybrid AI–mechanistic modeling pipeline  
- Uncertainty-aware prediction system  
- Iterative design–test–learn workflow  
- Demonstration of AI advantage, including:
  - Improved prediction of NF-κB signaling response  
  - Reduced experimental search space  
  - Identification of nonlinear control regimes  

## 6. Scalability, DOE Integration and Future Directions (Phase II Vision)

This framework is designed for large-scale deployment using DOE leadership computing resources (e.g., ORNL Frontier) to enable high-dimensional parameter exploration, large-scale model evaluation and integration of multimodal datasets. The future directions (Phase II Vision) include 

- Expansion to multi-system biological and environmental models  
- Generalization to energy-relevant complex systems  
- Development of a shared AI–mechanistic model library  
- Deployment as a scalable scientific discovery platform  

## 7. Workflow and Interactive Demo (Binder)
We use the following workflow:
1. BindCraft generates candidates peptide binders for blocking LPS 
2. Mechanistic models and PINNs predict receptor activation, NF-κB response, and nonlinear effects
3. Uncertainty quantification (UQ) identifies high-confidence candidates and uncertain regions
4. Items 2 and 3 provide feedback to prioritize (i) which peptides to test, (ii) which peptide design space to explore, and (iii) which system behavior space (e.g., activation vs suppression zones or dimerization thresholds) to explore.
5. Item 4 feeds item 5

A prototype mechanistic model of TLR4–NF-κB signaling is available as an executable, browser-based demo using Binder:

👉 Launch:  
https://mybinder.org/v2/gh/mby74/MECHANISM-AI-Model-Library/HEAD?urlpath=tree/mechanistic_models/signaling/bagaev2019_tlr4_nfkb_bmdm

Navigate to:
mechanistic_models/signaling/bagaev2019_tlr4_nfkb_bmdm/notebooks/reproduce_bagaev2019_reduced.ipynb

The model produces time-course simulations of NF-κB activation under different perturbations, enabling comparison between predicted and experimentally observed signaling dynamics. 

This demo includes:

- A validated mechanistic model of TLR4-mediated NF-κB signaling (Bagaev et al., 2019)  
- Simulation of signaling dynamics under different perturbations  
- Reproducible computational environment (no local installation required)  

This serves as a **baseline mechanistic model** within the MECHANISM-AI framework for rapid testing of hypotheses, integration with AI-based surrogate models , and uncertainty-aware prediction and model refinement. 
This demonstrates early **execution readiness** for the iterative AI–mechanistic workflow proposed in Phase I.

PINN Demo (Binder) An interactive PINN demo is available:

Launch:
https://mybinder.org/v2/gh/mby74/MECHANISM-AI-Model-Library/HEAD?urlpath=tree/hybrid_models/pinns/notebooks/demo_pinn.ipynb

Navigate to:
hybrid_models/pinns/notebooks/demo_pinn.ipynb

This demonstrates:
- Physics-informed neural network training
- Learning dynamics from differential equations
- Integration of mechanistic constraints into AI models




## 8. Model Library Architecture

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
## 9. Model Compatibility and Integration

Compatibility across models is ensured by design through a unified architecture that enables interoperability across biological scales (molecular → receptor → signaling → cellular → tissue) and modeling paradigms (mechanistic and hybrid AI models). This framework is implemented across the repository structure (`models/`, `hybrid_models/`, `interfaces/`, `mappings/`, `mediator/`, and `uq/`) and is governed by the following principles.



### 9.1. Design for Interoperability from the Start (Shared Interfaces)

All models in the `models/` and `hybrid_models/` directories follow standardized input and output interfaces defined in `interfaces/input_schema.py` and `interfaces/output_schema.py`. Each model may use different internal formulations such as ordinary differential equations, stochastic models, or physics-informed neural networks, but must accept and return a consistent set of variables including molecular features, receptor activation states, signaling outputs, and uncertainty estimates. This ensures seamless integration across scales within a unified workflow.



### 9.2. Cross-Scale Mapping Functions

Compatibility across scales is enforced through mapping functions defined in the `mappings/` directory. These functions formalize how outputs from one scale become inputs to another, ensuring consistent propagation of biological information. For example, molecular-scale outputs such as binding affinity and interface geometry are mapped to receptor-scale variables such as probability of dimerization and activation likelihood in `molecular_to_receptor.py`. Receptor activation states are translated into signaling pathway rate constants in `receptor_to_signaling.py`, and signaling outputs such as NF-κB dynamics are mapped to cellular responses including cytokine production in `signaling_to_cellular.py`. These mappings preserve biological meaning while ensuring computational consistency.



### 9.3. Time-Scale Alignment Across Models

Models at different biological scales operate on different time resolutions, ranging from molecular dynamics at nanoseconds to microseconds, to signaling processes at minutes to hours, and cellular responses at hours to days. Compatibility is achieved through time-scale alignment strategies implemented within model wrappers and hybrid models. These include coarse-graining of fast molecular processes, surrogate modeling for efficient approximation, and time rescaling to match signaling and cellular dynamics. These approaches enable consistent information exchange without temporal mismatch.



### 9.4. Model Wrappers for Modular Integration

Each model is encapsulated within a standardized wrapper that enables plug-and-play integration via `mediator/integration_engine.py`. These wrappers define how models receive inputs, produce outputs, and expose metadata such as scale and purpose. This abstraction allows models from both `models/` and `hybrid_models/` to be easily compared, replaced, or combined without modifying the overall workflow, thereby supporting modularity and extensibility.



### 9.5. Model Metadata for Consistency and Selection

All models include structured metadata aligned with the `model_purpose/` classification. This metadata defines the role and compatibility of each model within the system and includes elements such as the model name (for example, `nfkb_model_v1`), the biological scale, the modeling purpose, the defined inputs and outputs consistent with interface specifications, the underlying assumptions, and the type of uncertainty representation. This structured description enables systematic model comparison, selection, and integration across the workflow.



### 9.6. Mediator Layer for System Integration

A central integration layer implemented in `mediator/integration_engine.py` coordinates all model interactions. Instead of directly connecting models across scales, the framework uses this mediator to manage execution, apply cross-scale mappings, enforce interface compatibility, and control iterative updates. The integration follows a structured pattern in which design outputs are passed to the mediator, evaluated by models, and then returned to the mediator for progression to the next stage. This ensures that all interactions are controlled, consistent, and traceable.



### 9.7. Uncertainty Quantification as the Organizing Principle

Uncertainty quantification, implemented in the `uq/` directory, serves as the primary mechanism for coordinating model interaction and decision-making. It is used to reconcile conflicting predictions across models, determine which models are most reliable under specific conditions, and combine outputs when appropriate. It also guides model selection through `uq/model_selection/` and informs experimental prioritization. By incorporating uncertainty throughout the workflow, the system becomes adaptive and data-driven.



## 10. Integration with Workflow

These principles are operationalized in `workflows/closed_loop_pipeline/`, where AI-guided design generates candidate perturbations, models from `models/` and `hybrid_models/` evaluate system responses, mappings and interfaces ensure cross-scale consistency, the mediator coordinates execution and data flow, and uncertainty quantification guides decision-making and refinement. In summary, this architecture ensures that the model library functions as a coherent, interoperable system rather than a collection of independent models.

# Hybrid Models

## Overview

The `hybrid_models/` module extends the mechanistic model library by introducing **AI-enhanced models** that are derived from, constrained by, and interoperable with mechanistic models.

Hybrid models are not replacements for mechanistic models. Instead, they:

- Learn from mechanistic simulations and experimental data  
- Accelerate computation  
- Enable scalable exploration and optimization  
- Preserve biological interpretability through structured design  

---

## Architecture

The hybrid modeling framework follows this structure:

```
mechanistic_models → data / constraints → hybrid_models
hybrid_models → fast predictions / optimization → mechanistic_models
```

Two primary hybrid model types are implemented:

```
hybrid_models/
├── pinns/
└── surrogate_models/
```

---

## 1. Physics-Informed Neural Networks (PINNs)

### Purpose

PINNs integrate mechanistic equations directly into the learning process.

They are used when:
- equations are known but incomplete  
- data is sparse or noisy  
- hidden variables need to be inferred  

### Key Idea

A PINN minimizes:

```
Loss = Data Loss + Physics Loss + Boundary Conditions
```

Where:
- Data Loss fits observed data  
- Physics Loss enforces mechanistic equations  
- Boundary Conditions enforce initial states  

### Role in this library

PINNs:
- enforce mechanistic consistency  
- recover dynamics from incomplete data  
- enable inference of hidden biological states  

---

## 2. Surrogate Models

### Purpose

Surrogate models provide fast approximations of mechanistic models.

They are used when:
- mechanistic simulations are computationally expensive  
- large parameter sweeps are required  
- real-time evaluation is needed  

### Key Idea

Surrogates learn:

```
inputs → outputs
```

based on mechanistic simulation data.

### Example

```
(basal NF-κB, stimulation, parameters) → (time-to-peak, peak NF-κB)
```

### Role in this library

Surrogates:
- accelerate simulation  
- enable optimization and search  
- support uncertainty propagation  

---

## 🔗 Connection to Mechanistic Models

Every hybrid model must explicitly link to a mechanistic model:

```
linked_mechanistic_model: mechanistic_models/...
```

This ensures:
- traceability  
- biological grounding  
- consistent interpretation  

---

## 🔄 Data Flow

### Training

```
Mechanistic Model → Simulation Data → Hybrid Model Training
```

### Inference

```
Hybrid Model → Fast Prediction → Candidate Selection → Mechanistic Validation
```

---

## 📁 Example Structure

```
hybrid_models/
└── surrogate_models/
    └── bagaev2019_time_to_peak_surrogate/
```

Each hybrid model contains:
- metadata.yaml  
- training scripts  
- prediction interface  
- training data  
- evaluation notebook  

---

## 🧠 Design Principles

- Mechanistic-first: biology defines the system  
- Hybrid augmentation: AI enhances, not replaces  
- Interface consistency: shared inputs/outputs  
- Traceability: every model linked to literature  
- Reproducibility: data, code, and results included  

---

## 🚀 Role in the Full System

Hybrid models enable:

- fast multi-scale simulation  
- parameter exploration  
- optimization workflows  
- AI-guided discovery  

They are essential for scaling the framework from:

```
single-model analysis → integrated biological system modeling
```

---

## 📌 Current Status

- Surrogate models: implemented  
- PINNs: planned  
- Multi-scale integration: in progress  

---

## 🔮 Next Steps

- Add uncertainty quantification (UQ)  
- Expand surrogate coverage across models  
- Implement PINN-based constrained learning  
- Integrate into closed-loop pipelines  

---

## 🧠 Key Insight

**Mechanistic models define the biology.  
Hybrid models make it scalable.**

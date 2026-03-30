# Dey 2022 LPS Macrophage Response Model

## Citation
Dey S, Boucher D, Pitchford J, Lagos D. *Mathematical modelling of activation-induced heterogeneity in TNF, IL6, NOS2, and IL1β expression reveals cell state transitions underpinning macrophage responses to LPS.* Wellcome Open Research. 2022;7:29. DOI: 10.12688/wellcomeopenres.17557.2

## External Resources
- Paper: Wellcome Open Research
- Public code repository: NoRM (Macrophage activation induced heterogeneity)

## What paper is this from?
This model is based on Dey et al. (2022), which combines experimental measurements and mathematical modeling to study activation-induced heterogeneity in macrophage responses to LPS.

## What scale is it?
Cellular scale. The model describes cell-state transitions underlying heterogeneous expression of inflammatory mediators in macrophage populations.

## What equations does it use?
The paper uses mathematical models of macrophage state transitions to explain heterogeneous expression patterns for TNF, IL-6, pro-IL-1β, and NOS2 after primary and secondary LPS stimulation. The associated public repository includes Gillespie-based and ODE-related implementations for these dynamics.

## What data supports it?
The paper uses empirical data from two in vitro macrophage systems, bone marrow-derived macrophages (BMDMs) and RAW264.7 cells, with measurements for TNF, IL-6, pro-IL-1β, and NOS2. The public repository includes corresponding CSV data files, including `bmdm_tnf.csv`, `bmdm_il6.csv`, `bmdm_il1b.csv`, and `bmdm_nos2.csv`.

## Can I reproduce one key figure?
Yes. A practical first target is reproduction of one BMDM response figure using one cytokine marker. Because the public repository explicitly points to figure-generation scripts, this model folder is designed to support reproduction of one key figure using a minimal extracted dataset and a reproduction notebook.

## Reproducibility status
Initial target: reproduce one BMDM marker figure using the published data files and a minimal wrapper notebook.

## Folder contents
- `equations.md`: model structure and state-transition summary
- `metadata.yaml`: standardized curation metadata
- `parameters.csv`: curated parameter table
- `data/`: minimal reproducible dataset
- `src/`: minimal code wrapper for a first reproduction
- `notebooks/`: one reproduction notebook

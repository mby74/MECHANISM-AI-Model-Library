## Live Demo

[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mby74/MECHANISM-AI-Model-Library/HEAD?urlpath=/tree/mechanistic_models/signaling/bagaev2019_tlr4_nfkb_bmdm/notebooks/reproduce_bagaev2019_reduced.ipynb)
# Bagaev 2019 TLR4–NF-κB Model in Primary Macrophages

## Citation
Bagaev AV, Garaeva AY, Lebedeva ES, Pichugin AV, Ataullakhanov RI, Ataullakhanov FI. *Elevated pre-activation basal level of nuclear NF-κB in native macrophages accelerates LPS-induced translocation of cytosolic NF-κB into the cell nucleus.* Scientific Reports. 2019;9:4563.

## External Model Resource
BioModels: MODEL1809230001

## What paper is this from?
This model is from Bagaev et al. (2019), who combined experiments and mathematical modeling to describe TLR4-dependent NF-κB activation in primary bone marrow-derived macrophages.

## What scale is it?
Signaling scale, with receptor-proximal input. It models LPS-triggered TLR4 signaling through receptor activation, TRAF6/TAK1, IKK, NF-κB phosphorylation, NF-κB nuclear translocation, and feedback regulation.

## What equations does it use?
The full mechanistic system is encoded in the SBML model deposited in BioModels. A human-readable summary is provided in `equations.md`.

## What data supports it?
The model is supported by experimental measurements in primary macrophages, including NF-κB phosphorylation and nuclear translocation kinetics across LPS doses. For the minimal reproducible dataset in this repository, we use a digitized version of the NF-κB nuclear translocation data shown in Figure 3B of the paper.

## Can I reproduce one key figure?
Yes. This folder is organized to reproduce one key figure from the paper, using the notebook:

`notebooks/reproduce_figure3B.ipynb`

## Reproducibility status
Partial reproducibility target at curation start: reproduce the published trend and fit against digitized Figure 3B data, then upgrade to full SBML-driven reproduction.

## Folder contents
- `equations.md`: readable summary of the model structure
- `metadata.yaml`: standardized curation metadata
- `parameters.csv`: curated parameter table
- `data/`: smallest reproducible dataset
- `src/`: minimal simulation code or SBML wrapper
- `notebooks/`: figure reproduction notebook

# Krüger 2017 TLR4 Dimerization Model (Single-Molecule Imaging)

## Citation
Krüger CL, Zeidler MP, et al. *Quantitative single-molecule imaging of TLR4 reveals ligand-specific receptor dimerization.* Science Signaling. 2017.

## What paper is this from?
This model is based on Krüger et al. (2017), which used single-molecule imaging to quantify TLR4 receptor dimerization behavior under different ligand conditions.

## What scale is it?
Receptor scale. The model describes receptor state transitions (monomer ↔ dimer) at the cell membrane.

## What equations does it use?
This implementation uses a reduced kinetic model of receptor dimerization:

Monomer + Monomer ⇌ Dimer

The dynamics are approximated using:

dD/dt = k_on * M^2 - k_off * D

where:
- M = monomer fraction
- D = dimer fraction

At steady state, the model predicts ligand-dependent dimer fractions.

## What data supports it?
The model is supported by single-molecule imaging measurements of TLR4 dimerization fractions under different ligand conditions (agonist, antagonist, no ligand).

The minimal dataset in this repository is derived from reported summary statistics in the paper.

## Can I reproduce one key figure?
Yes. This model aims to reproduce the ligand-dependent shift in monomer/dimer fractions reported in the paper.

Notebook:
`notebooks/reproduce_dimer_fraction.ipynb`

## Reproducibility status
Initial target: reproduce reported dimer fractions across ligand conditions using a minimal kinetic model.

## Folder contents
- `equations.md`: model formulation
- `metadata.yaml`: structured metadata
- `parameters.csv`: kinetic parameters
- `data/`: minimal dataset derived from literature
- `src/`: simulation code
- `notebooks/`: reproduction notebook

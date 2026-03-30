# Data Documentation

## Source
Data is derived from Krüger et al. (2017), which reports TLR4 monomer/dimer fractions under different ligand conditions.

## Was it digitized from a figure?
No. Initial dataset is constructed from reported summary values in the text and figures.

## Units
- Fraction of receptors (unitless)

## Preprocessing steps
- Values were extracted from reported percentages
- Converted to fractions (0–1 scale)

## Missing values
- No missing values in the minimal dataset

## Caveats
- This dataset is simplified and does not include full single-molecule trajectories
- It represents aggregate steady-state behavior only

## Files
- raw/original_source_notes.txt: extraction notes
- processed/cleaned_dimer_fraction.csv: processed dataset

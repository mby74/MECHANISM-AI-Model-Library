# Data README

## Source
The initial curated dataset in this folder is based on the published NoRM repository associated with Dey et al. (2022). That repository includes macrophage response CSV files such as `bmdm_tnf.csv`, `bmdm_il6.csv`, `bmdm_il1b.csv`, and `bmdm_nos2.csv`.

## Was it digitized from a figure?
No, the preferred first version should use the published CSV files from the public repository rather than digitizing figures.

## Units
Units should be recorded exactly as represented in the selected source CSV and corresponding figure legend. If the file reports fractions, percentages, or normalized response values, preserve that representation in the processed file and document it explicitly in the notebook.

## Preprocessing steps
The first curated version should use the smallest subset needed for one reproducible figure. Processing should be limited to:
1. selecting one marker,
2. selecting one cell type,
3. preserving original time points,
4. renaming columns clearly, and
5. saving the cleaned subset as `processed/cleaned_timeseries.csv`.

## Missing values
Do not impute missing values in version 1. If any are present, document them explicitly.

## Caveats
The repository contains multiple markers, cell types, and scripts. This curated folder is intentionally narrower: it should support one traceable reproduction target before expanding to the full model.

## Files
- `raw/original_source_notes.txt`: provenance notes for the selected source file
- `processed/cleaned_timeseries.csv`: smallest reproducible processed dataset for one figure

# Data README

## Source
The processed dataset in this folder was digitized from Figure 3B of Bagaev et al. (2019), which shows experimental NF-κB nuclear translocation kinetics in bone marrow-derived macrophages under the model condition with basal nuclear NF-κB included.

## Was it digitized from a figure?
Yes. The minimal reproducible dataset was digitized from the published figure because the underlying raw time-course table was not located in the paper or BioModels record.

## Units
- Time: minutes
- Response variable: normalized nuclear NF-κB signal, reported in relative fluorescence units or normalized signal as interpreted from the figure

## Preprocessing steps
The digitized coordinates were exported from the figure, checked manually against axis ticks, and saved as a cleaned CSV. No smoothing should be applied in the first curation version. Any normalization or baseline subtraction must be documented in the notebook.

## Missing values
No missing values are expected in the minimal digitized time series. If any points are unclear due to figure resolution, they should be omitted rather than interpolated in version 1.

## Caveats
Because this dataset is digitized from a published figure, values are approximate and do not replace the authors’ original raw measurements. This dataset is intended only for minimal figure reproduction and traceable model curation.

## Files
- `raw/original_source_notes.txt`: notes on figure source, panel, axes, and digitization decisions
- `processed/cleaned_timeseries.csv`: digitized and cleaned minimal dataset used for reproduction

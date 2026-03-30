# Training Data

## Source
This dataset is generated from the reduced mechanistic Bagaev 2019 model.

## How it was created
A grid of parameter combinations was simulated using the mechanistic model in:

`mechanistic_models/signaling/bagaev2019_tlr4_nfkb_bmdm/src/model.py`

## Inputs
- basal_nfkb_fraction
- lps_stimulation_strength
- k_act
- k_deg

## Outputs
- time_to_peak
- peak_nfkb

## Purpose
This dataset is used to train a surrogate model for rapid approximation of mechanistic model behavior.

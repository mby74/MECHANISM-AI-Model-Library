# Bagaev 2019 Time-to-Peak Surrogate Model

## Purpose
This surrogate model provides a fast approximation of the reduced mechanistic Bagaev 2019 signaling model.

## Linked Mechanistic Model
`mechanistic_models/signaling/bagaev2019_tlr4_nfkb_bmdm/`

## Inputs
- basal_nfkb_fraction
- lps_stimulation_strength
- k_act
- k_deg

## Outputs
- time_to_peak
- peak_nfkb

## What does this model do?
The surrogate learns the mapping from mechanistic model inputs to key signaling outputs, allowing rapid evaluation without rerunning the mechanistic simulation each time.

## Why is it useful?
This enables:
- fast parameter sweeps
- optimization
- uncertainty propagation
- candidate screening in closed-loop workflows

## Training source
The surrogate is trained on simulation data generated from the mechanistic model.

## Folder contents
- `generate_training_data.py`: generates mechanistic simulation dataset
- `train.py`: trains the surrogate model
- `predict.py`: loads trained model and predicts outputs
- `training_data/`: training dataset and documentation
- `saved_model/`: stored trained model
- `notebooks/`: evaluation notebook

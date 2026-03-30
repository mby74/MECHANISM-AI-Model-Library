from pathlib import Path
import pickle
import pandas as pd


def predict_single(basal_nfkb_fraction, lps_stimulation_strength, k_act, k_deg):
    base = Path(__file__).resolve().parent
    model_file = base / "saved_model" / "surrogate_model.pkl"

    with open(model_file, "rb") as f:
        model = pickle.load(f)

    X_new = pd.DataFrame(
        [
            {
                "basal_nfkb_fraction": basal_nfkb_fraction,
                "lps_stimulation_strength": lps_stimulation_strength,
                "k_act": k_act,
                "k_deg": k_deg,
            }
        ]
    )

    pred = model.predict(X_new)[0]

    return {
        "time_to_peak": float(pred[0]),
        "peak_nfkb": float(pred[1]),
    }


if __name__ == "__main__":
    result = predict_single(
        basal_nfkb_fraction=0.1,
        lps_stimulation_strength=1.0,
        k_act=0.05,
        k_deg=0.01,
    )
    print(result)

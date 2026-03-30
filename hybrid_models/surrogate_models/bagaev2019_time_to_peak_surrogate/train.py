from pathlib import Path
import pickle
import pandas as pd
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def main():
    base = Path(__file__).resolve().parent
    data_file = base / "training_data" / "inputs_outputs.csv"
    model_dir = base / "saved_model"
    model_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(data_file)

    X = df[["basal_nfkb_fraction", "lps_stimulation_strength", "k_act", "k_deg"]]
    y = df[["time_to_peak", "peak_nfkb"]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = MultiOutputRegressor(
        RandomForestRegressor(n_estimators=200, random_state=42)
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae_time = mean_absolute_error(y_test["time_to_peak"], y_pred[:, 0])
    mae_peak = mean_absolute_error(y_test["peak_nfkb"], y_pred[:, 1])

    with open(model_dir / "surrogate_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model saved to:", model_dir / "surrogate_model.pkl")
    print("MAE time_to_peak:", mae_time)
    print("MAE peak_nfkb:", mae_peak)


if __name__ == "__main__":
    main()

from pathlib import Path
import numpy as np
import pandas as pd
import itertools
import sys

ROOT = Path(__file__).resolve().parents[3]
MECH_SRC = ROOT / "mechanistic_models" / "signaling" / "bagaev2019_tlr4_nfkb_bmdm" / "src"
sys.path.append(str(MECH_SRC))

from model import simulate_nfkb, time_to_peak


def compute_peak_nfkb(N):
    return float(np.max(N))


def main():
    out_dir = Path(__file__).resolve().parent / "training_data"
    out_dir.mkdir(parents=True, exist_ok=True)

    basal_values = np.linspace(0.0, 0.4, 6)
    stim_values = np.linspace(0.5, 1.5, 5)
    k_act_values = np.linspace(0.03, 0.08, 5)
    k_deg_values = np.linspace(0.005, 0.02, 5)

    t = np.linspace(0, 180, 1801)

    rows = []

    for B, S, k_act, k_deg in itertools.product(
        basal_values, stim_values, k_act_values, k_deg_values
    ):
        N = simulate_nfkb(t=t, k_act=k_act, k_deg=k_deg, S=S, B=B)
        t_peak = float(time_to_peak(t, N))
        peak_nfkb = compute_peak_nfkb(N)

        rows.append(
            {
                "basal_nfkb_fraction": B,
                "lps_stimulation_strength": S,
                "k_act": k_act,
                "k_deg": k_deg,
                "time_to_peak": t_peak,
                "peak_nfkb": peak_nfkb,
            }
        )

    df = pd.DataFrame(rows)
    df.to_csv(out_dir / "inputs_outputs.csv", index=False)
    print(f"Saved {len(df)} rows to {out_dir / 'inputs_outputs.csv'}")


if __name__ == "__main__":
    main()

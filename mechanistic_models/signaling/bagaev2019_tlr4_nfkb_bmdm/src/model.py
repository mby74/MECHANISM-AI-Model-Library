import numpy as np


def simulate_nfkb(t, k_act, k_deg, S, B):
    """
    Simulate reduced NF-κB dynamics.

    Parameters:
        t : array of time points
        k_act : activation rate
        k_deg : degradation rate
        S : stimulation strength
        B : basal NF-κB level (initial condition)

    Returns:
        N : NF-κB nuclear timecourse
    """

    N = np.zeros_like(t)
    N[0] = B

    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        dN = k_act * (1 - N[i - 1]) * S - k_deg * N[i - 1]
        N[i] = N[i - 1] + dt * dN

    return N


def time_to_peak(t, N):
    """
    Compute time to peak NF-κB.
    """
    return t[np.argmax(N)]

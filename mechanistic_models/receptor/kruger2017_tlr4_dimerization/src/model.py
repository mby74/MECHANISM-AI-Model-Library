import numpy as np

def steady_state_dimer_fraction(k_on, k_off):
    # Solve k_on * M^2 = k_off * D with M + 2D = 1
    # Substitute M = 1 - 2D
    # k_on * (1 - 2D)^2 = k_off * D

    from scipy.optimize import fsolve

    def equation(D):
        return k_on * (1 - 2*D)**2 - k_off * D

    D_solution = fsolve(equation, 0.3)[0]
    M_solution = 1 - 2 * D_solution

    return M_solution, D_solution

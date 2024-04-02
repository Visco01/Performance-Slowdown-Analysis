from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt


class ProcessorSharing():
    def __init__(self, alpha: float, max_v: int, rho: float) -> None:
        self.alpha = alpha
        self.max_v = max_v
        self.rho = rho

    def slowdown(self):
        return 1/(1-self.rho)

    def get_slowdowns(self, x_values: list[float]) -> list[float]:
        return np.full_like(x_values, self.slowdown())


# def PS_slowdown(rho):
#     return 1/(1-rho)


# fig, ax = plt.subplots(1, 1)
# max_y_value = 15
# alfa = 1.4
# maxv = 10000
# rho = 0.7

# x_values = np.linspace(1, 20, 100)

# PS_slowdown = np.full_like(x_values, PS_slowdown(0.7))

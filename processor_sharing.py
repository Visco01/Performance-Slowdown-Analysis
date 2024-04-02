from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt

def PS_slowdown(rho):
    return 1/(1-rho)

fig, ax = plt.subplots(1, 1)
max_y_value = 15
alfa = 1.4
maxv = 10000
rho = 0.7

x_values = np.linspace(1,20,100)

PS_slowdown = np.full_like(x_values, PS_slowdown(0.7))

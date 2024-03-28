#!/usr/bin/env python3
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

ax.set_ylim(0, max_y_value)
x_values = np.linspace(1,20,100)

y_PS_values = np.full_like(x_values, PS_slowdown(0.7))

ax.plot(x_values, y_PS_values, 'b-', lw=2, alpha=0.6, label='PS_slowdown')
plt.show()

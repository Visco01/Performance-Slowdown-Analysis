#!/usr/bin/env python3
from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt
import math

def waiting_time(rho, l, mu, sigma):
    numerator = rho+l*mu*(sigma**2)
    denimenator = 2*(mu-l)
    return numerator/denimenator

def service_time(l, mu):
    return 1/(mu-l)

def response_time(rho, l, mu, sigma):
    return waiting_time(rho, l, mu, sigma) + service_time(l, mu)

def slowdown(rho, l, mu, sigma, job_size):
    return response_time(rho, l, mu, sigma)/job_size

fig, ax = plt.subplots(1, 1)
max_y_value = 15
alfa = 1.4
maxv = 10000
rho = 0.7
mu = truncpareto.mean(alfa, maxv)
l = rho * mu
sigma = math.sqrt(truncpareto.var(alfa, maxv))

# ax.set_yscale('log')
# ax.set_xscale('log')
x_values = np.linspace(1,20,100)

y_FCFS_values = []
for x in x_values:
    y_FCFS_values.append(slowdown(0.7, l, mu, sigma, x))

ax.plot(x_values, y_FCFS_values, 'b-', lw=2, alpha=0.6, label='FCFS_slowdown')

print(slowdown(0.7, l, mu, sigma, 2))

plt.show()

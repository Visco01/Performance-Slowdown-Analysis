from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt
import math

def waiting_time(rho, l, mu, sigma):
    numerator = rho+l*mu*(sigma)
    denimenator = 2*(mu-l)
    print(numerator)
    print(denimenator)
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


x_values = np.linspace(1,20,100)

FCFS_slowdown = []
for x in x_values:
    FCFS_slowdown.append(slowdown(0.7, l, mu, sigma, x))

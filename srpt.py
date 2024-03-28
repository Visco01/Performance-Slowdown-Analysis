from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt
import math

def calc_rho(x, l, alfa, maxv):
    ft = lambda t: t*truncpareto.pdf(t,alfa,maxv)
    integral= quad(ft, 1, x)
    return integral[0]*l

def m2(x, l, alfa, maxv):
    ft = lambda t: (t**2)*truncpareto.pdf(t,alfa,maxv)
    integral= quad(ft, 1, x)
    return integral[0]*l

def service_time(x, alfa, maxv):
    ft = lambda t: t*truncpareto.pdf(t,alfa,maxv)
    integral= quad(ft, 1, np.inf)
    return integral[0]

def last_integral(x, l, alfa, maxv):
    ft = lambda t: 1/(1-calc_rho(x, l, alfa, maxv))
    integral= quad(ft, 1, x)
    return integral[0]

def srpt_response_time(x, l, alfa, maxv):
    numerator = l*(m2(x, l, alfa, maxv)+(x**2)*(1-truncpareto.cdf(x, alfa, maxv)))
    denominator = 2*(1-calc_rho(x, l, alfa, maxv))**2
    return (numerator/denominator)+last_integral(x, l, alfa, maxv)

def slowdown(rho, l, mu, sigma, job_size):
    return srpt_response_time(job_size, l, alfa, maxv)/job_size

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

y_SRPT_values = []
for x in x_values:
    y_SRPT_values.append(slowdown(0.7, l, mu, sigma, x))

ax.plot(x_values, y_SRPT_values, 'b-', lw=2, alpha=0.6, label='SRPT_slowdown')

plt.show()

print(calc_rho(10, l, alfa, maxv))
print(service_time(2, alfa, maxv))
print(m2(10, l, alfa, maxv))

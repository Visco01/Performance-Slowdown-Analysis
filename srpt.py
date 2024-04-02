from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt
import math

alfa = 1.4
maxv = 10000
tft = lambda t: t * truncpareto.pdf(t, alfa, maxv)
ttft = lambda t: t * tft(t)
cdf = lambda x: truncpareto.cdf(x, alfa, maxv)
rho_x = lambda x: quad(tft, 1, x)[0] * l
last_integral_x = lambda x: 1/(1-rho_x(x))

rho = 0.7
mu = 1 / quad(tft, 0, np.inf)[0]
l = rho * mu
sigma = math.sqrt(truncpareto.var(alfa, maxv))


def m2(x):
    integral = quad(ttft, 1, x)
    return integral[0] * l

def last_integral(x):
    integral = quad(last_integral_x, 1, x)
    return integral[0]

def srpt_response_time(x):
    numerator = l * (m2(x) + (x**2) * (1 - cdf(x)))
    denominator = 2 * (1 - rho_x(x))**2
    return (numerator / denominator) + last_integral(x)

def srpt_slowdown(x):
    return srpt_response_time(x) / x


fig, ax = plt.subplots(1, 1)
x_values = np.linspace(1,20,100)

y_SRPT_values = []
for x in x_values:
    y_SRPT_values.append(srpt_slowdown(x))

ax.plot(x_values, y_SRPT_values, 'b-', lw=2, alpha=0.6, label='SRPT_slowdown')

plt.show()

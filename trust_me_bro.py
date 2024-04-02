from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt
import math
from multiprocessing import Pool
import os

from scipy.integrate import quad

ALPHA = 1.4
MAX_VALUE = 10000
RHO = 0.7


def f(t):
    """
    Define the probability density function (pdf) of the service time distribution.
    """
    # Define your probability density function here.
    # For example, you can use a normal distribution:
    # return 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (t - mu)**2 / (2 * sigma**2))
    return truncpareto.cdf(t, ALPHA, MAX_VALUE)


def F(t):
    """
    Define the cumulative distribution function (cdf) of the service time distribution.
    """
    # Define your cumulative distribution function here.
    # For example, you can integrate the pdf function up to t.
    return truncpareto.pdf(t, ALPHA, MAX_VALUE)


# def mu_inverse():
#     """
#     Calculate the average service time (in seconds).
#     """
#     mu_inv, _ = quad(lambda t: t * f(t), 0, np.inf)
#     return mu_inv


def rho(x, lmbda):
    """
    Calculate the load factor due to jobs up to size x.
    """
    rho_x, _ = quad(lambda t: t * f(t), 0, x)
    return lmbda * rho_x


def m2(x):
    """
    Calculate the second moment up to size x.
    """
    m2_x, _ = quad(lambda t: t**2 * f(t), 0, x)
    return m2_x


def srpt_response_time(x, lmbda):
    """
    Calculate the conditional expected response time using Shortest Remaining Processing Time (SRPT) algorithm.
    """
    rho_x = rho(x, lmbda)
    m2_x = m2(x)
    # mu_inv = mu_inverse()
    expected_response_time = (lmbda * (m2_x + x**2 * (1 - F(x)))) / (
        2 * (1 - rho_x)**2) + quad(lambda t: 1 / (1 - rho(t, lmbda)), 0, x)[0]
    return expected_response_time


def slowdown(x, lmbda):
    return srpt_response_time(x, lmbda)/x


def main():
    output_file = "out/trust-me-bro.csv"
    fig, ax = plt.subplots(1, 1)
    max_y_value = 15
    mu = truncpareto.mean(ALPHA, MAX_VALUE)
    l = RHO * mu
    sigma = math.sqrt(truncpareto.var(ALPHA, MAX_VALUE))

    # ax.set_yscale('log')
    # ax.set_xscale('log')

    if (os.path.exists(output_file)):
        with open(output_file, "r") as f:
            x_values = []
            y_values = []
            for line in f.readlines():
                x, _, y = line.split(",")
                x_values.append(float(x))
                y_values.append(float(y))
            ax.plot(x_values, y_values, 'b-', lw=2,
                    alpha=0.6, label='SRPT_slowdown')
    else:
        with Pool(24) as pool:
            x_values = np.linspace(1, 20, 100)
            values = [(x, l) for x in x_values]
            y_values = pool.starmap(slowdown, values)
            # y_values = pool.starmap(srpt_response_time, values)
            with open(output_file, "w") as f:
                for (x, y), y in zip(values, y_values):
                    print(f"{x},{y},{y}", file=f)
            ax.plot(x_values, y_values, 'b-', lw=2,
                    alpha=0.6, label='SRPT_slowdown')

    plt.show()


if __name__ == "__main__":
    main()

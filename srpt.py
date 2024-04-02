from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt
import math
from multiprocessing import Pool


def calc_rho(x, l, alpha, max_value):
    def ft(t): return t*truncpareto.pdf(t, alpha, max_value)
    integral = quad(ft, 1, x)
    return integral[0]*l


def calc_m2(x, alpha, max_value):
    def ft(t): return (t**2)*truncpareto.pdf(t, alpha, max_value)
    integral = quad(ft, 1, x)
    return integral[0]

# def calc_service_time(x, alpha, max_value):
#     def ft(t): return t*truncpareto.pdf(t, alpha, max_value)
#     integral = quad(ft, 1, np.inf)
#     return integral[0]


def srpt_response_time(x, l, alpha, max_value):
    m2 = calc_m2(x, alpha, max_value)
    # np.inf? Is it correct? Because it is F(x) so I do not think that max_value is appropriate in this case
    F_x = truncpareto.cdf(x, alpha, np.inf)
    rho = calc_rho(x, l, alpha, max_value)
    last_integral = quad(
        lambda t: 1/(1-calc_rho(t, l, alpha, max_value)), 1, x
    )[0]
    return (l*(m2+(x**2)*(1-F_x)))/(2*((1-rho)**2))+last_integral


def slowdown(x, l, alpha, max_value):
    return srpt_response_time(x, l, alpha, max_value)/x


def main():
    fig, ax = plt.subplots(1, 1)
    max_y_value = 15
    alpha = 1.4
    max_value = 10000
    rho = 0.7
    mu = truncpareto.mean(alpha, max_value)
    l = rho * mu
    sigma = math.sqrt(truncpareto.var(alpha, max_value))

    # ax.set_yscale('log')
    # ax.set_xscale('log')

    x_values = np.linspace(1, 20, 100)
    with Pool(24) as pool:
        values = [(x, l, alpha, max_value) for x in x_values]
        y_values = pool.starmap(slowdown, values)
        # y_values = pool.starmap(srpt_response_time, values)

        ax.plot(x_values, y_values, 'b-', lw=2,
                alpha=0.6, label='SRPT_slowdown')

    plt.show()


if __name__ == "__main__":
    main()

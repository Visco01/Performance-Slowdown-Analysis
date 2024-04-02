from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
from multiprocessing import Pool
import matplotlib.pyplot as plt


class SRPT():
    def __init__(self, alpha: float, max_v: int, rho: float, processes: int = 24) -> None:
        self.processes = processes

        self.alpha = alpha
        self.max_v = max_v
        self.rho = rho
        self.mu = 1 / quad(lambda t: t*self.f(t), 0, np.inf)[0]
        self.l = self.rho * self.mu

    def m2(self, t):
        return t**2 * self.f(t)

    def f(self, x):
        return truncpareto.pdf(x, self.alpha, self.max_v)

    def F(self, x):
        return truncpareto.cdf(x, self.alpha, np.inf)

    def rho_x(self, x):
        return quad(lambda t: t*self.f(t), 1, x)[0] * self.l

    def last_integral(self, x):
        integral = quad(lambda t: 1/(1-self.rho_x(t)), 1, x)
        return integral[0]

    def srpt_response_time(self, x):
        numerator = self.l * (self.m2(x) + (x**2) * (1 - self.F(x)))
        denominator = 2 * (1 - self.rho_x(x))**2
        return (numerator / denominator) + self.last_integral(x)

    def srpt_slowdown(self, x):
        return self.srpt_response_time(x) / x

    def get_slowdowns(self, x_values: list[float]) -> list[float]:
        res = []
        with Pool(self.processes) as pool:
            res = pool.map(self.srpt_slowdown, x_values)
        return res


def main():
    ALPHA = 1.4
    MAX_V = 10000
    RHO = 0.7

    _, ax = plt.subplots(1, 1)
    ax.set_ylim(0, 20)
    x_values = np.linspace(1, 20, 100)
    ax.plot(
        x_values,
        SRPT(ALPHA, MAX_V, RHO).get_slowdowns(x_values),
        'b-',
        lw=2,
        alpha=0.6,
        label='SRPT'
    )
    plt.show()


if __name__ == "__main__":
    main()

from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto


class SRPT():
    def __init__(self, alpha: float, max_v: int, rho: float) -> None:
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
        for x in x_values:
            res.append(self.srpt_slowdown(x))
        return res

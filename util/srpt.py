from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
from multiprocessing import Pool


class SRPT():
    def __init__(self, alpha: float, max_v: int, rho: float, processes: int = 24) -> None:
        self.processes = processes

        self.alpha = alpha
        self.max_v = max_v
        self.rho = rho
        self.mu = 1 / quad(lambda t: t*self.f(t), 0, np.inf)[0]
        self.l = self.rho * self.mu

    def m2(self, t: float) -> float:
        return t**2 * self.f(t)

    def f(self, x: float) -> float:
        return truncpareto.pdf(x, self.alpha, self.max_v)

    def F(self, x: float) -> float:
        return truncpareto.cdf(x, self.alpha, np.inf)

    def rho_x(self, x: float) -> float:
        return quad(lambda t: t*self.f(t), 1, x)[0] * self.l

    def response_time(self, x: float) -> float:
        numerator = self.l * (self.m2(x) + (x**2) * (1 - self.F(x)))
        denominator = 2 * (1 - self.rho_x(x))**2
        integral = quad(lambda t: 1/(1-self.rho_x(t)), 1, x)[0]
        return (numerator / denominator) + integral

    def slowdown(self, x: float) -> float:
        return self.response_time(x) / x

    def get_slowdowns(self, x_values: list[float]) -> list[float]:
        res = []
        with Pool(self.processes) as pool:
            res = pool.map(self.slowdown, x_values)
        return res
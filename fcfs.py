from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt
import math


class FCFS():
    def __init__(self, alpha: float, max_v: int, rho: float) -> None:
        self.alpha = alpha
        self.max_v = max_v
        self.rho = rho
        self.mu = truncpareto.mean(self.alpha, self.max_v)
        self.l = self.rho*self.mu
        self.sigma = math.sqrt(truncpareto.var(self.alpha, self.max_v))

    def waiting_time(self) -> float:
        numerator = self.rho+self.l*self.mu*self.sigma
        denominator = 2*(self.mu-self.l)
        return numerator/denominator

    def service_time(self) -> float:
        return 1/(self.mu-self.l)

    def response_time(self) -> float:
        return self.waiting_time() + self.service_time()

    def slowdown(self, x: float) -> float:
        return self.response_time()/x

    def get_slowdowns(self, x_values: list[float]) -> list[float]:
        res: list[float] = []
        for x in x_values:
            res.append(self.slowdown(x))
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
        FCFS(ALPHA, MAX_V, RHO).get_slowdowns(x_values),
        'r-',
        lw=2,
        alpha=0.6,
        label='FCFS'
    )
    plt.show()


if __name__ == "__main__":
    main()

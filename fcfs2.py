import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import truncpareto


class FCFS():
    def __init__(self, alpha: float, max_v: int, rho: float) -> None:
        self.alpha = alpha
        self.max_v = max_v
        self.rho = rho
        self.mu = truncpareto.mean(self.alpha, self.max_v)
        self.l = self.rho / self.mu

    def response_time(self) -> float:
        # Response time = waiting time + service time
        return self.waiting_time() + self.service_time()

    def waiting_time(self) -> float:
        # Mean waiting time using P-K formula
        return self.rho / ((1 - self.rho) * self.mu)

    def service_time(self) -> float:
        # Service time
        return 1 / (self.mu - self.l)

    def slowdown(self, x: float) -> float:
        # Slowdown
        return self.response_time() / x

    def get_slowdowns(self, x_values: list[float]) -> list[float]:
        # Calculate slowdown for a range of x values
        return [self.slowdown(x) for x in x_values]


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

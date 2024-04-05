from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt


class ProcessorSharing():
    def __init__(self, alpha: float, max_v: int, rho: float) -> None:
        self.alpha = alpha
        self.max_v = max_v
        self.rho = rho

    def slowdown(self) -> float:
        return 1/(1-self.rho)

    def get_slowdowns(self, x_values: list[float]) -> list[float]:
        return np.full_like(x_values, self.slowdown())


def main():
    ALPHA = 1.4
    MAX_V = 100_000
    RHO = 0.7

    _, ax = plt.subplots(1, 1)
    ax.set_ylim(0, 20)
    x_values = np.linspace(1, 300, 100)
    ax.plot(
        x_values,
        ProcessorSharing(ALPHA, MAX_V, RHO).get_slowdowns(x_values),
        'g-',
        lw=2,
        alpha=0.6,
        label='PS'
    )
    plt.title('Processor Sharing slowdon analysis')
    plt.xlabel('Job size')
    plt.ylabel('Slowdown')
    plt.grid()
    plt.legend()
    plt.savefig('plot.png')
    plt.show()


if __name__ == "__main__":
    main()

import numpy as np


class ProcessorSharing():
    def __init__(self, alpha: float, max_v: int, rho: float) -> None:
        self.alpha = alpha
        self.max_v = max_v
        self.rho = rho

    def slowdown(self) -> float:
        return 1/(1-self.rho)

    def get_slowdowns(self, x_values: list[float]) -> list[float]:
        return np.full_like(x_values, self.slowdown())

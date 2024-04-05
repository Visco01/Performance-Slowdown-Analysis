from scipy.stats import truncpareto


class FCFS():
    def __init__(self, alpha: float, max_v: int, rho: float) -> None:
        self.alpha = alpha
        self.max_v = max_v
        self.rho = rho
        self.mu = truncpareto.mean(self.alpha, self.max_v)
        self.l = self.rho*self.mu
        self.cv = truncpareto.var(self.alpha, self.max_v)

    def waiting_time(self) -> float:
        numerator = self.rho * (1 + self.cv)
        denominator = 2*(self.mu-self.l)
        return numerator/denominator

    def service_time(self) -> float:
        return 1 / self.mu

    def response_time(self) -> float:
        return self.waiting_time() + self.service_time()

    def slowdown(self, x: float) -> float:
        return self.response_time()/x

    def get_slowdowns(self, x_values: list[float]) -> list[float]:
        res: list[float] = []
        for x in x_values:
            res.append(self.slowdown(x))
        return res

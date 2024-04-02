from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt
import math


class FCFS():
    def __init__(self, alfa: float, max_v: int, rho: float) -> None:
        self.alfa = alfa
        self.max_v = max_v
        self.rho = rho
        self.mu = truncpareto.mean(self.alfa, self.max_v)
        self.l = self.rho*self.mu
        self.sigma = math.sqrt(truncpareto.var(self.alfa, self.max_v))

    def waiting_time(self):
        numerator = self.rho+self.l*self.mu*(self.sigma)
        denominator = 2*(self.mu-self.l)
        # print(numerator)
        # print(denimenator)
        return numerator/denominator

    def service_time(self):
        return 1/(self.mu-self.l)

    def response_time(self):
        return self.waiting_time() + self.service_time()

    # def slowdown(rho, l, mu, sigma, job_size):
    #     return response_time(rho, l, mu, sigma)/job_size
    def slowdown(self, job_size):
        return self.response_time()/job_size

    def get_slowdowns(self, x_values: list[float]) -> list[float]:
        res: list[float] = []
        for x in x_values:
            res.append(self.slowdown(x))
        return res


# fig, ax = plt.subplots(1, 1)
# max_y_value = 15
# alfa = 1.4
# maxv = 10000
# rho = 0.7
# mu = truncpareto.mean(alfa, maxv)
# l = rho * mu
# sigma = math.sqrt(truncpareto.var(alfa, maxv))


# x_values = np.linspace(1, 20, 100)

# FCFS_slowdown = []
# for x in x_values:
#     FCFS_slowdown.append(slowdown(0.7, l, mu, sigma, x))

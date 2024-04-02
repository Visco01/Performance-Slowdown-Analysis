from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt
import math

# from srpt import SRPT_slowdown
from srpt import SRPT
# from fcfs import FCFS_slowdown
from fcfs import FCFS
from processor_sharing import PS_slowdown


def main():
    ALPHA = 1.4
    MAX_V = 10000
    RHO = 0.7

    fig, ax = plt.subplots(1, 1)
    ax.set_ylim(0, 20)
    x_values = np.linspace(1, 20, 100)
    ax.plot(x_values, PS_slowdown, 'g-', lw=2, alpha=0.6, label='PS')
    ax.plot(x_values, FCFS(ALPHA, MAX_V, RHO).get_slowdowns(x_values),
            'r-', lw=2, alpha=0.6, label='FCFS')
    # ax.plot(x_values, SRPT_slowdown, 'b-', lw=2, alpha=0.6, label='SRPT')

    # mu = 1 / quad(lambda , 0, np.inf)[0]
    # l = rho * mu
    srtp = SRPT(ALPHA, MAX_V, RHO).get_slowdowns(x_values)

    ax.plot(x_values, srtp, 'b-', lw=2, alpha=0.6, label='SRPT')
    plt.show()


if __name__ == "__main__":
    main()

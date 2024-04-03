import numpy as np
import matplotlib.pyplot as plt
from srpt import SRPT
from fcfs import FCFS
from processor_sharing import ProcessorSharing


def main():
    ALPHA = 1.4
    MAX_V = 10000
    RHO = 0.7

    _, ax = plt.subplots(1, 1)
    ax.set_ylim(0, 30)
    x_values = np.linspace(1, 300, 100)
    ax.plot(
        x_values,
        ProcessorSharing(ALPHA, MAX_V, RHO).get_slowdowns(x_values),
        'g-',
        lw=2,
        alpha=0.6,
        label='PS'
    )
    ax.plot(
        x_values,
        FCFS(ALPHA, MAX_V, RHO).get_slowdowns(x_values),
        'r-',
        lw=2,
        alpha=0.6,
        label='FCFS'
    )
    ax.plot(
        x_values,
        SRPT(ALPHA, MAX_V, RHO).get_slowdowns(x_values),
        'b-',
        lw=2,
        alpha=0.6,
        label='SRPT'
    )
    plt.title('Queueing policies comparison')
    plt.xlabel('Job size')
    plt.ylabel('Mean Slowdown')
    plt.grid()
    plt.legend()
    plt.savefig('plot.png')
    plt.show()

if __name__ == "__main__":
    main()

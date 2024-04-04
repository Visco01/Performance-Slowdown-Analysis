import numpy as np
import matplotlib.pyplot as plt
from file_loading import load_output, save_output
from srpt import SRPT
from fcfs import FCFS
from processor_sharing import ProcessorSharing
import os


def main():
    PS_FILE = "out/ps.csv"
    FCFS_FILE = "out/fcfs.csv"
    SRPT_FILE = "out/srpt.csv"

    ALPHA = 1.4
    MAX_V = 100_000
    RHO = 0.7

    _, ax = plt.subplots(1, 1)
    ax.set_ylim(0, 30)
    x_values = np.linspace(1, 300, 100)
    ps: list[float] = []
    fcfs: list[float] = []
    srpt: list[float] = []
    if (os.path.exists(PS_FILE)):
        _, ps = load_output(PS_FILE)
    else:
        ps = ProcessorSharing(
            ALPHA, MAX_V, RHO
        ).get_slowdowns(x_values)
        save_output(PS_FILE, x_values, ps)
    if (os.path.exists(FCFS_FILE)):
        _, fcfs = load_output(FCFS_FILE)
    else:
        fcfs = FCFS(ALPHA, MAX_V, RHO).get_slowdowns(x_values)
        save_output(FCFS_FILE, x_values, fcfs)
    if (os.path.exists(SRPT_FILE)):
        _, srpt = load_output(SRPT_FILE)
    else:
        srpt = SRPT(ALPHA, MAX_V, RHO).get_slowdowns(x_values)
        save_output(SRPT_FILE, x_values, srpt)
    ax.plot(
        x_values,
        ps,
        'g-',
        lw=2,
        alpha=0.6,
        label='PS'
    )
    ax.plot(
        x_values,
        fcfs,
        'r-',
        lw=2,
        alpha=0.6,
        label='FCFS'
    )
    ax.plot(
        x_values,
        srpt,
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

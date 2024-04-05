import numpy as np
import matplotlib.pyplot as plt
from util.file_loading import load_output, save_output
from util.srpt import SRPT
from util.fcfs import FCFS
from util.processor_sharing import ProcessorSharing


def save_plots(file_path: str, title: str, x_values, resize: bool = True, **kwargs: dict[str, tuple[list:[float], str]]) -> None:
    _, ax = plt.subplots(1, 1)
    if resize:
        ax.set_ylim(0, 30)
    for label, (y_values, color) in kwargs.items():
        ax.plot(
            x_values,
            y_values,
            color,
            lw=2,
            alpha=0.6,
            label=label,
        )
    plt.title(title)
    plt.xlabel('Job size')
    plt.ylabel('Mean slowdown')
    plt.grid()
    plt.legend()
    plt.savefig(file_path)
    plt.close()


def main():
    PS_FILE = "out/ps.csv"
    FCFS_FILE = "out/fcfs.csv"
    SRPT_FILE = "out/srpt.csv"

    ALPHA = 1.4
    MAX_V = 100_000
    RHO = 0.7

    x_values = np.linspace(1, 400, 100)

    ps: list[float] = load_output(
        PS_FILE,
        lambda: ProcessorSharing(
            ALPHA, MAX_V, RHO
        ).get_slowdowns(x_values)
    )
    save_output(PS_FILE, ps)

    fcfs: list[float] = load_output(
        FCFS_FILE,
        lambda: FCFS(
            ALPHA, MAX_V, RHO
        ).get_slowdowns(x_values)
    )
    save_output(FCFS_FILE, fcfs)

    srpt: list[float] = load_output(
        SRPT_FILE,
        lambda: SRPT(
            ALPHA, MAX_V, RHO
        ).get_slowdowns(x_values)
    )
    save_output(SRPT_FILE, srpt)

    save_plots(
        "out/fcfs.png",
        "FCFS policy slowdown",
        x_values,
        fcfs=(fcfs, 'r-')
    )
    save_plots(
        "out/ps.png",
        "PS policy slowdown",
        x_values,
        ps=(ps, 'g-')
    )
    save_plots(
        "out/srpt.png",
        "SRPT policy slowdown",
        x_values,
        resize=False,
        srpt=(srpt, 'b-')
    )
    save_plots(
        "out/srpt2.png",
        "SRPT policy slowdown",
        x_values,
        srpt=(srpt, 'b-')
    )

    save_plots(
        "out/plots.png",
        "Queuing policies comparison",
        x_values,
        fcfs=(fcfs, 'r-'),
        srpt=(srpt, 'b-'),
        ps=(ps, 'g-'),
    )


if __name__ == "__main__":
    main()

def save_output(file_path: str, x_values: list[float], y_values: list[float]) -> None:
    with open(file_path, "w") as f:
        for x, y in zip(x_values, y_values):
            print(f"{x},{y}", file=f)


def load_output(file_path: str,) -> tuple[list[float], list[float]]:
    x_values: list[float] = []
    y_values: list[float] = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            x, y = line.split(",")
            x_values.append(float(x))
            y_values.append(float(y))
    return x_values, y_values
import os


def save_output(file_path: str, y_values: list[float]) -> None:
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            for y in y_values:
                print(f"{y}", file=f)


def load_output(file_path: str, callback) -> list[float]:
    if os.path.exists(file_path):
        y_values: list[float] = []
        with open(file_path, "r") as f:
            for line in f.readlines():
                y_values.append(float(line.strip()))
        return y_values
    else:
        return callback()

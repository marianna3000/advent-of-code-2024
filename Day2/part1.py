import numpy as np

with open("inputs/input", "r") as f:
    array = [list(map(int, line.split())) for line in f]

safe_reports = sum(
    np.all((diff >= 1) & (diff <= 3)) or np.all((diff >= -3) & (diff <= -1))
    for diff in map(np.diff, array)
)

print("Safe reports:", safe_reports)
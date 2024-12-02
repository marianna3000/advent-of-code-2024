import numpy as np

with open("inputs/input", "r") as f:
    array = [list(map(int, line.split())) for line in f]


def calculate_conditions_for_row(row):
    diffs = np.diff(row)
    return (
        np.all((diffs >= 1) & (diffs <= 3)),
        np.all((diffs >= -3) & (diffs <= -1))
    )


def check_row_valid(row):
    if any(calculate_conditions_for_row(row)):
        return True

    return any(
        any(calculate_conditions_for_row(row[:j] + row[j + 1:]))
        for j in range(len(row))
    )


safe_reports = sum(map(check_row_valid, filter(lambda row: len(row) >= 2, array)))

print(f"Safe Reports= {safe_reports}")
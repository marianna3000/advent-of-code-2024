import numpy as np


def load_input_numeric(filename):
    return np.loadtxt(f"inputs/{filename}", unpack=True)
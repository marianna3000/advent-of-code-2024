import numpy as np


def load_input(filename, type=None, unpack=True):
    return np.loadtxt(f"inputs/{filename}", unpack=unpack, dtype=type)
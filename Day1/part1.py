from utils import load_input_numeric

col1, col2 = load_input_numeric(filename="input")

col1.sort()
col2.sort()

distance = abs(col1[:len(col2)] - col2)
print(f"Distance: {distance.sum()}")
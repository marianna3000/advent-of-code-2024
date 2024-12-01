from utils import load_input_numeric
from collections import Counter

col1, col2 = load_input_numeric("input")

# For larger datasets go vectorized
counts = Counter(col2)

print(f"Similarity: {sum(number * counts[number] for number in col1)}")
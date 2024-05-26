# This code shows the comparison in run times between optimized
# and unoptimized versions of the Collatz sequence calculation
#
# Run as follows:
#   pip install numpy matplotlib
#   python comparison.py

import numpy as np
import matplotlib.pyplot as plt

# Provided execution times
input_sizes = np.array([1000, 10000, 100000, 1000000, 5000000, 10000000])

optimized_times = np.array([0.423, 1.806, 4.695, 165.343, 1110, 2061]) / 1000  # Converted to seconds
unoptimized_times = np.array([1.169, 3.758, 35.035, 2703, 18306, 38697]) / 1000  # Converted to seconds

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(input_sizes[:6], optimized_times, label='Optimized', marker='o')
plt.plot(input_sizes[:6], unoptimized_times, label='Unoptimized', marker='o', linestyle='--')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Collatz Sequence Calculation Time Comparison')
plt.legend()
plt.grid(True)
plt.show()


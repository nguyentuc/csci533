import matplotlib.pyplot as plt

# Given data
x_values = [10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9]
y_values = [0.0002, 0.0021, 0.0275, 0.3506, 4.3138, 50.9411, 593.0884, 6514.0786]

# Create a new figure
plt.figure()

# Plotting the data
plt.plot(x_values, y_values, marker='o')

# Adding labels and title
plt.xlabel('n (input size)')
plt.ylabel('Running Time (seconds)')
plt.title('Running Time of Algorithms')
plt.xscale('log')  # Setting x-axis to logarithmic scale as the x values are exponentially increasing
plt.grid(True)  # Adding a grid for better readability
plt.xticks(x_values, labels=[str(x) for x in x_values])  # Setting x-axis ticks to represent the exact values of n

# Displaying the plot
plt.show()

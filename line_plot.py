import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 50, 25, 30, 10]

# Create a line plot
plt.plot(x,y) # x is the x-axis data and y is the y-axis data
plt.title("Sample Line Plot") # Title of the plot
plt.xlabel("X-axis") # Label for the x-axis
plt.ylabel("Y-axis") # Label for the y-axis
plt.grid(True) # Show grid lines
plt.show() # Show the plot
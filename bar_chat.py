import matplotlib.pyplot as plt

# Sample data
names = ['Joyce', 'Frank', 'Flavian', 'Claire', 'Mark']
scores = [90, 80, 85, 95, 70]

# Create a bar chart
plt.bar(names, scores, color='blue')  # names are the x-axis data and scores are the y-axis data
plt.title('Student Scores')  # Title of the chart
plt.xlabel('Students')  # Label for the x-axis
plt.ylabel('Scores')  # Label for the y-axis
plt.show()  # Show the chart
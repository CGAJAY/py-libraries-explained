import matplotlib.pyplot as plt

# Sample data
activities = ['Sleeping', 'Eating', 'Coding', 'Gaming']
hours = [8, 2, 8, 6]

# Create a pie chart
plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title('Daily Activities')  # Title of the pie chart
plt.show()  # Show the pie chart
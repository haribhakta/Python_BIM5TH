import matplotlib.pyplot as plt
# Data for categories and values
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]
# Customize the bar graph
plt.bar(categories, values, color='skyblue', width=0.6, edgecolor='black')
# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Customized Bar Graph')
# Display the plot
plt.show()

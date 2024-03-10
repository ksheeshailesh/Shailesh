import matplotlib.pyplot as plt

def create_bar_graph(data, labels, title, xlabel, ylabel):
    plt.bar(range(len(data)), data, tick_label=labels)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Example data
data = [23, 45, 56, 78, 90]
labels = ['A', 'B', 'C', 'D', 'E']
title = 'Example Bar Graph'
xlabel = 'Categories'
ylabel = 'Values'

# Call the function to create the bar graph
create_bar_graph(data, labels, title, xlabel, ylabel)

import matplotlib.pyplot as plt
import numpy as np
import math

#state based interface

#-----------------------------------generate some data-----------------------------------
# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot using the state-based interface
plt.plot(x, y)

# Add some labels and title to the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave')

# Show the plot
plt.show()

#-----------------------------------create figure-----------------------------------
# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure and an axes object using the object-oriented interface
# fig: fig is the Figure object (the overall container)
# ax: ax is the Axes object (the actual plot area where data is drawn).
fig, ax = plt.subplots()

# Create a line plot using the axes object's plot method
ax.plot(x, y)

# Add some labels and title to the plot using the axes object's methods
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Sine Wave')

# Display the plot
plt.show()
#-----------------------------------create empty canvas-----------------------------------
# To begin with, we create a figure instance which provides an empty canvas.

fig = plt.figure()

#-----------------------------------add axix to the figure/canvas-----------------------------------
# Now add axes to figure.
# The add_axes() method requires a list object of 4 elements corresponding to left, bottom, width and height of the figure.
# left & bottom define the starting position (relative to the figure, from 0 to 1).
# width & height define the size (relative to the figure).
# Each number must be between 0 and 1

ax=fig.add_axes([0,0,1,1])
# Set labels for x and y axis as well as title −

ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')
# Invoke the plot() method of the axes object.

ax.plot(x,y)

#-----------------------------------
x=np.arange(0,math.pi*2,0.05)
y=np.sin(x)

fig=plt.figure()
ax=fig.add_axes([0,1,1,1])

ax.plot(x,y)
ax.set_title('sine wave3')
ax.set_xlabel('angle')
ax.set_ylabel('sine')
plt.show()

#-----------------------------------legend-----------------------------------
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.plot(x,y)
ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')
ax.legend(['sine wave'])

plt.show()
#-----------------------------------axes customized-----------------------------------
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

l1 = ax.plot(x,y,'y') # solid line with yellow colour and square marker

ax.set_title("sine wave",loc = 'left')
ax.set_xlabel('angle')
ax.set_ylabel('sine')
ax.legend(['sine wave'])
plt.show()

#-----------------------------------multiple plot-----------------------------------
#-----------------------------------subplot-----------------------------------
plt.subplot(1, 3, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.

plt.subplot(1, 3, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
plt.subplot(1, 3, 3)
plt.show()


#-----------------------------------plot1-----------------------------------
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
#-----------------------------------grid of subplots-----------------------------------
# Grid of subplots using plt.subplots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0,0].plot(x, y1)
axes[0,1].plot(x, y2)
axes[1,0].plot(x, y2)
axes[1,1].plot(x, y1)
fig.suptitle('Grid of Subplots using plt.subplots')
plt.show()
#-----------------------------------set limit-----------------------------------
x = np.linspace(-5, 5, 100)
y = x**2

# create a plot object and plot the data
fig, ax = plt.subplots()
ax.plot(x, y)

# set the limits using set_xlim() and set_ylim()
ax.set_xlim(-3, 3)
ax.set_ylim(0, 10)

# show the plot
plt.show()

#-----------------------------------setting ticks and tick labels-----------------------------------
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes

ax.plot(x, y)
ax.set_xlabel("angle")
ax.set_title('sine')
ax.set_xticks([0,2,4,6])
ax.set_xticklabels(['zero','two','four','six'])
ax.set_yticks([-1,0,1])

plt.show()
#-----------------------------------barplot-----------------------------------
# Create sample data
x = np.array(['A', 'B', 'C', 'D', 'E'])
y = np.array([5, 8, 3, 4, 6])

# Create a figure and axes objects
fig, ax = plt.subplots()

# Create a vertical bar chart
ax.bar(x, y)

# Add chart title and axis labels
ax.set_title('Vertical Bar Chart')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')

# Show the plot
plt.show()

#-----------------------------------horizontal bar-----------------------------------
# generate some data
y_labels = ['Label 1', 'Label 2', 'Label 3', 'Label 4']
y_pos = np.arange(len(y_labels))
x_values = [10, 20, 30, 40]

# create a figure and axis object
fig, ax = plt.subplots()

# plot the horizontal bar chart
ax.barh(y_pos, x_values)

# set the y-axis labels and tick positions
ax.set_yticks(y_pos)
ax.set_yticklabels(y_labels)

# set the x-axis label
ax.set_xlabel('Values')

# set the title of the plot
ax.set_title('Horizontal Bar Chart')

# display the plot
plt.show()

#-----------------------------------histogrsm-----------------------------------
# Create some random data
np.random.seed(123)
data = np.random.normal(0, 1, 1000)

# Create a figure and axis object
fig, ax = plt.subplots()

# Create a histogram
n, bins, patches = ax.hist(data, bins=20, density=False, alpha=0.5)

# Set the x-axis label
ax.set_xlabel('Data')

# Set the y-axis label
ax.set_ylabel('Frequency')

# Set the title of the plot
ax.set_title('Histogram of Random Data')

# Display the plot
plt.show()

#-----------------------------------pie chart-----------------------------------
# Sample data
sizes = [30, 20, 15, 10, 5]

# Create a figure and axis object
fig, ax = plt.subplots()

# Create pie chart with custom colors and explode one slice
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'pink']
explode = (0, 0.2, 0, 0.8, 0)
ax.pie(sizes, explode=explode, labels=None, colors=colors, autopct='%1.4f%%', shadow=False)

# Add legend
ax.legend(['Apple', 'Banana', 'C', 'D', 'E'], loc='upper right')

# Set aspect ratio to equal, to ensure pie is drawn as a circle.
ax.axis('equal')

# Show plot
plt.show()
 
#-----------------------------------scatter plot-----------------------------------
# Generate some random data
x = np.random.randn(100)
y = np.random.randn(100)

# Create a figure and axes object
fig, ax = plt.subplots()

# Create the scatter plot
ax.scatter(x, y)

# Set the title and labels for the axes
ax.set_title('Scatter Plot Example')
ax.set_xlabel('X Values')
ax.set_ylabel('Y Values')

# Display the plot
plt.show()

#-----------------------------------boxplot-----------------------------------
# Create some data
np.random.seed(123)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Create a figure and axes
fig, ax = plt.subplots()

# Create a box plot
ax.boxplot(data)

# Set the title and labels
ax.set_title('Box plot')
ax.set_xlabel('Data')
ax.set_ylabel('Value')

# Show the plot
plt.show()

#-----------------------------------Example-----------------------------------
# create example data
import pandas as pd
dates = pd.date_range(start='2022-01-01', end='2022-01-30', freq='D')
temps = [10, 12, 13, 15, 16, 18, 20, 22, 24, 23, 21, 19, 17, 16, 14, 12, 11, 10, 12, 14, 15, 17, 19, 20, 21, 23, 24, 22, 20, 18]
df = pd.DataFrame({'temperature': temps}, index=dates)

# create a figure and axis object
fig, ax = plt.subplots(figsize=(12,6))

# plot the daily average temperature
df.resample('D').mean().plot(kind='line', ax=ax)

# set the title, xlabel, and ylabel for the plot
ax.set_title('Daily Average Temperature for January 2022')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (Celsius)')

# display the plot
plt.show()

#-----------------------------------save-----------------------------------
fig.savefig('myplot.png')
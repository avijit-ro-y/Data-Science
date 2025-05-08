import matplotlib.pyplot as plt  # Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python.
import seaborn as sns            # Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive statistical graphics.
import numpy as np               # NumPy is a library for numerical computing in Python, useful for handling arrays and mathematical functions.
import pandas as pd              # Pandas is a data manipulation and analysis library that provides data structures like DataFrames.

# Set the default Seaborn style for plots
# This applies a clean and aesthetically pleasing style to all plots created using Seaborn.
sns.set()

# sns.set() is a function in Seaborn that sets the aesthetic parameters for plots, such as colors, grid styles, and background themes.

#---------------------------------Histograms, KDE, and Densities ---------------------------------
# Mean vector [0, 0] → The center of the distribution is at (0,0).
# Covariance matrix [[5, 2], [2, 2]] → Defines the spread and relationship between the two variables:
# Size 2000 → Generates 2000 samples (each with two values, x and y).
data = np.random.multivariate_normal(mean=[0, 0], cov=[[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

# Setting density=True in plt.hist() normalizes the histogram so that the total area under the bars sums to 1.
# This effectively turns the histogram into an estimate of the probability density function (PDF),
# making it useful for comparing distributions with different sample sizes.
for col in 'xy':
    plt.hist(data[col], density=True, alpha=0.5)
sns.kdeplot() #Seaborn does with sns.kdeplot (see the following figure
plt.show()

sns.displot(data=data)
plt.show()

sns.displot(data=data,kind='kde')
# The blue curve (x) has a wider spread, meaning x has a higher variance.
# The orange curve (y) is more peaked and narrow, indicating y has lower variance and is more concentrated around the mean.
# Both distributions appear approximately normal but with different spreads.
plt.show()

sns.kdeplot(data=data)
# The semicolon (;) at the end of seaborn (sns) method calls in Jupyter Notebook suppresses
# the text output that would otherwise be displayed (like <AxesSubplot:>).
# It helps keep the notebook cleaner by only showing the plot without unnecessary output.
plt.show()

sns.kdeplot(data=data, x='x', y='y')
# The contour lines indicate regions of high and low density (like a topographic map).
# Denser areas (more lines close together) suggest that more data points are concentrated there.
# The shape shows the bivariate distribution, revealing any correlations or clusters.
plt.show()

#---------------------------------Pair Plots---------------------------------
iris = sns.load_dataset("iris")
print(iris.head(),'\n')

print(iris.species.unique(),'\n')

sns.pairplot(iris, height=2.5)
'''
sns.pairplot: This function from the Seaborn library creates a matrix of scatter plots (for pairwise relationships) and histograms (for univariate distributions) for each feature in the provided dataset.

iris:
This is the dataset being visualized, which is the famous Iris dataset containing measurements of iris flowers (specifically, sepal length, sepal width, petal length, and petal width) along with their species (Setosa, Versicolor, Virginica).

height=2.5:
This parameter sets the height of each subplot in the pairplot to 2.5 inches. Adjusting the height can help improve visibility and accommodate larger datasets.
'''
plt.show()

sns.pairplot(iris, hue='species', height=2.5)
'''
The hue parameter allows you to color the data points in the scatter plots based on a specified categorical variable.
This is particularly useful for visualizing how different groups within your data are distributed across the feature space.
By using hue, you can observe the clustering or overlap of different species in the pairwise scatter plots.
'''
plt.show()

#---------------------------------Categorical Plots---------------------------------
tips = sns.load_dataset("tips")
print(tips.head(),'\n')

# In Python, a context manager is a construct that allows you to allocate and release resources precisely when you need them.
# It is most commonly used with the with statement to ensure that setup and cleanup tasks are handled properly.
# When working with Seaborn's sns.axes_style(), a context manager is useful for temporarily changing the style of plots.
# This ensures that the style changes apply only within a specific block of code, without affecting the rest of your script.
# Set the Seaborn style for the plot
# This context manager applies the specified style ('ticks') to the plots created within it.
with sns.axes_style(style='ticks'):
    # Create a categorical plot (catplot) using the tips dataset
    # x-axis: 'day' - days of the week (categorical variable)
    # y-axis: 'total_bill' - total bill amount (numerical variable)
    # hue: 'sex' - distinguishes between male and female customers using different colors
    # kind: 'box' - specifies that a box plot should be used to visualize the data
    g = sns.catplot(x="day", y="total_bill", hue="sex", data=tips, kind="box")
    # Set the axis labels for clarity
    # x-axis will be labeled "Day" and y-axis will be labeled "Total Bill"
    g.set_axis_labels("Day", "Total Bill");
# This plot is useful for spotting spending trends, variability, and potential outliers in restaurant bills.
plt.show()

g = sns.catplot(x="day", y="total_bill", hue="sex", data=tips, kind="swarm")
g.set_axis_labels("Day", "Total Bill")
plt.show()

#---------------------------------Box Plot---------------------------------
# Set the Seaborn style for the plot using a context manager
# The 'with' statement applies the specified style ('ticks') to the plots created within this block.
# This allows for a consistent aesthetic without permanently changing the style settings.
with sns.axes_style(style='ticks'):

    # Create a box plot to visualize the distribution of petal lengths across different species of iris flowers
    # x-axis: 'species' - the categorical variable representing the species of the iris flowers
    # y-axis: 'petal_length' - the numerical variable representing the length of the petals
    sns.boxplot(x="species", y="petal_length", data=iris)
'''
This box plot visually demonstrates the differences in petal lengths among the three species:
Setosa has the shortest petal lengths, while Virginica has the longest.
The presence of outliers in each species suggests variability within the measurements.
The clear separation between the species highlights the effectiveness of petal length as a feature for distinguishing between the iris species.
'''
plt.show()
print('\n')
#---------------------------------Joint Distributions---------------------------------
with sns.axes_style('white'):
    sns.jointplot(x="total_bill", y="tip", data=tips,hue="sex")
plt.show()

sns.jointplot(x="total_bill", y="tip", data=tips, kind='reg')
plt.show()

#---------------------------------Count Plots---------------------------------
planets = sns.load_dataset('planets')
print(planets.head(),'\n')

with sns.axes_style('dark'):
    g = sns.catplot(x="year", data=planets, aspect=2,
                    kind="count", color='steelblue')
    g.set_xticklabels(step=5)
plt.show()

# spect ratio of the plot, which is the ratio of the width to the height
# Increasing the aspect value makes the plot wider, while decreasing it makes the plot taller.
# The order parameter in sns.catplot is used to specify the order in which the categorical variables (e.g., categories on the x or y axis) should be displayed.
# You provide a list of categories in the desired order.
with sns.axes_style('white'):
    g = sns.catplot(
        x="year",
        data=planets,
        aspect=2.0,
        kind='count',
        hue='method',
        order=range(2001, 2015)
    )
    g.set_ylabels('Number of Planets Discovered')
plt.show()

#---------------------------------Violin Plot---------------------------------
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()

sns.violinplot(x="day", y="total_bill", hue='sex', data = tips)
plt.show()

#---------------------------------Heatmap---------------------------------
df = sns.load_dataset("glue")
print(df,'\n')


print(df[df["Model"] == "BiLSTM"])

# Load the 'glue' dataset from Seaborn's built-in datasets
# The 'glue' dataset is a benchmark for evaluating language models on various tasks.
glue = sns.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")

# The pivot() function reshapes the DataFrame:
# - index="Model": Sets the index of the new DataFrame to the 'Model' column.
# - columns="Task": Sets the columns of the new DataFrame to the 'Task' column.
# - values="Score": Uses the 'Score' column to fill the values in the new DataFrame.

# Create a heatmap to visualize the scores of different models across various tasks
sns.heatmap(glue, annot=True)

# The heatmap will display a color-coded representation of the scores,
# allowing for quick comparison of model performance on different tasks.
# Darker colors typically represent higher scores, while lighter colors indicate lower scores.

# Note: It might be useful to customize the heatmap with parameters like:
# - annot=True: to display the score values in the cells
# - cmap='coolwarm': to choose a specific color palette
# - cbar=True: to include a color bar that indicates the scale of the colors
plt.show()

#---------------------------------Explore---------------------------------
titanic = sns.load_dataset('titanic')
sns.barplot(x = "sex", y = "survived", hue = "class", data = titanic)
plt.show()

titanic = sns.load_dataset('titanic')
sns.barplot(x = "sex", y = "survived", data = titanic)
plt.show()

sns.countplot(x="class", data=titanic, hue="class", palette="Blues", legend=False)
plt.show()

sns.barplot(x = "sex", y = "survived", hue = "class", data = titanic)
plt.show()

# Create a regression plot to visualize the relationship between total bill and tip
# This plot will show both the scatter plot of the data points and the fitted regression line.
sns.regplot(x="total_bill", y="tip", data=tips)
plt.show()

sns.pairplot(iris,hue = 'species',diag_kind = "kde",kind = "scatter",palette = "husl")
plt.show()
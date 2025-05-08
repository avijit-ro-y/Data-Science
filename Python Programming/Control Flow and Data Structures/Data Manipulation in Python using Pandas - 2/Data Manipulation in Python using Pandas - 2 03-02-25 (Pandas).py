import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "P:\Intern\Python Programming\Control Flow and Data Structures\Data Manipulation in Python using Pandas 30-01-25\IMDB top 1000__1738559933-5ea65d4bfbba7875acb26a15.csv"
imdb_df = pd.read_csv(path, index_col=0)

#---------------------------------save data---------------------------------
imdb_df.to_csv("P:\Intern\Python Programming\Control Flow and Data Structures\Data Manipulation in Python using Pandas 30-01-25\imdb_123456.csv")

#---------------------------------Map and Apply---------------------------------
print(imdb_df['Certificate'].unique(),'\n')

print(imdb_df['Certificate'].map({'Not Rated': '0', 'R': 'R', 'Approved': 'Approve'}),'\n')

# Duration is not parsed, pandas doesn't know how to handle this as integer
print(imdb_df['Duration'],'\n')

#---------------------------------create int string seprate---------------------------------
def my_duration_func(x):
    if type(x) == int:
        return x
    return int(x.split(" ")[0])

# create a new column Duration_parsed
imdb_df['Duration_parsed'] = imdb_df['Duration'].apply(my_duration_func)

print(imdb_df['Duration_parsed'],'\n')

#---------------------------------upper---------------------------------
def my_upper_func(x):
    return x.upper()

print(imdb_df['Genre'].apply(my_upper_func),'\n')

#---------------------------------sorting data---------------------------------
print(imdb_df.sort_values('Metascore', ascending=False),'\n')

#---------------------------------Changing dtype---------------------------------
print(imdb_df['Duration_parsed'].astype(float),'\n')

#---------------------------------Plot and visualisations---------------------------------
# Rating distribution for a particular genre
imdb_df[imdb_df['Genre'] == 'Drama']['Rate'].plot()
plt.show()

# distribution of movies based on certificate
imdb_df['Certificate'].value_counts().plot(kind='bar', figsize=(18, 6))
plt.show()

#---------------------------------example---------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# create a sample DataFrame
data = {'Fruit': ['Apple', 'Banana', 'Orange', 'Apple', 'Orange', 'Banana', 'Apple', 'Orange', 'Banana', 'Orange'],
        'Quantity': [2, 3, 4, 1, 2, 3, 4, 1, 2, 3]}
df = pd.DataFrame(data)

# create a bar plot of the frequency of each fruit
df['Fruit'].value_counts().plot(kind='bar', figsize=(8, 6))

# set the x and y labels
plt.xlabel('Fruit')
plt.ylabel('Frequency')

# set the title
plt.title('Frequency of each fruit')

# show the plot
plt.show()

#---------------------------------GroupBy Operations---------------------------------
grouped = imdb_df.groupby('Genre')
print(grouped.agg('count'))

# accessing a single group
print(grouped.get_group('Western'))

# chain groupby operations
print(imdb_df.groupby('Certificate').get_group('R').groupby('Genre').get_group('Western'))

print(grouped.filter(lambda x: x['Rate'].mean() > 8.5))
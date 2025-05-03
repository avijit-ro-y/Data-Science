#---------------------------------Pandas---------------------------------

#used for data manupulation and for missing data
import os
import pandas as pd

#---------------------------------Series Create-------1D array------collumn
ser=pd.Series(data=[1,2,3,4,5],index=[10,11,12,13,14],dtype="int")
print(ser,"\n")

ser1=pd.Series(data=[1,2,3,4,5],dtype="int") #default index
print(ser1,"\n")

animal_size=["giant","big","medium","small","tiny"]
animal_name=["Dinosaur","Elephant","Cow","CAt","Chick"]
animal=pd.Series(data=animal_name,index=animal_size,dtype="str",name="animal")
print(animal,"\n")

data_dict={  #using dictionary
    "name":"a",
    "number":12,
    "state" :"fluid"
}
dict_series=pd.Series(data_dict)
print(dict_series,"\n")

dict_series_indx=pd.Series(data_dict,index=["name","number","state"])
print(dict_series_indx,"\n")

#---------------------------------size---------------------------------
print(dict_series_indx.size,"\n")

#---------------------------------shape---------------------------------
print(dict_series_indx.shape,"\n")

#---------------------------------DataFrame Create----2D array------Single Sheet
list_df=pd.DataFrame(data=[[1,2,3,4],[5,6,7,8]],columns=["one","two","three","four"])
print(list_df.head(),"\n") #return 5 rows

dict_data={
    "name":["apple","orrange","banana","onion"],
    "price":[10,20,30,40]
}
dict_df=pd.DataFrame(dict_data)
print(dict_df,"\n")

dict_df["age"]=["old","old",[{"eye":"blue"}],"small"]
print(dict_df,"\n")

#---------------------------------can handel multiple datatype---------------------------------
simple=pd.Series(data=[1,'2',3,'4',5],index=[20,21,22,23,24])
print(simple,"\n")

#---------------------------------change datatype---------------------------------
print(simple.astype('int'),"\n")

#---------------------------------read CSV file---------------------------------
path = "P:\Intern\Python Programming\Control Flow and Data Structures\Data Manipulation in Python using Pandas 30-01-25\IMDB top 1000__1738559933-5ea65d4bfbba7875acb26a15.csv"
imdb_df = pd.read_csv(path, index_col=0)

#---------------------------------save data---------------------------------
imdb_df.to_csv("P:\Intern\Python Programming\Control Flow and Data Structures\Data Manipulation in Python using Pandas 30-01-25\imdb_123456.csv")

#---------------------------------see data---------------------------------
print(imdb_df.head())
print(imdb_df.tail(5))

#---------------------------------index 0---------------------------------
print(pd.read_csv(path, index_col=0),'\n')

# ---------------------------------shape and size of the dateset---------------------------------
print(imdb_df.shape, imdb_df.size,'\n')

# ---------------------------------columns in the dataset---------------------------------
print(imdb_df.columns,"\n")
# accessing a single column or series
print(imdb_df['Title'],"\n")
# accessing columns
print(imdb_df.Rate,'\n')
print(imdb_df[['Title', 'Rate', 'Description']],'\n')

#---------------------------------loc-iloc---------------------------------
#loc : loc gets rows (and/or columns) with particular labels.
#iloc : iloc gets rows (and/or columns) at integer locations.

#access particular row
print(imdb_df.loc[5],"\n")
print(imdb_df[0:10:2],"\n")
print(imdb_df.iloc[4],"\n") # iloc - return rows at integer locations

# ---------------------------------creating new columns---------------------------------
imdb_df['test_column'] = range(0, 1000)
print(imdb_df['test_column'])

#---------------------------------access particular range  row---------------------------------
print(imdb_df.iloc[10:20:2],"\n")

#---------------------------------accessing row + columns---------------------------------
print(imdb_df.loc[2:10:2, 'Rate'],"\n")
print(imdb_df.iloc[10:20:2, :],"\n") # iloc can handle numeric based slicing on both axis

# ---------------------------------renaming a column---------------------------------
imdb_2=imdb_df.rename(columns={'Rate': 'Rating', 'Duration': 'Time'})
print(imdb_2.columns,'\n')

#---------------------------------dropping a column---------------------------------
imdb_df = imdb_df.drop('test_column', axis=1)
print(imdb_df.columns,'\n')

#---------------------------------adding a row---------------------------------
temp_df = pd.DataFrame({
    'Title': 'test',
    'Certificate': 'test',
    'Duration': 120,
    'Genre': 'Test',
    'Rate': 10,
    'Metascore': 100,
    'Description': 'test',
    'Cast': 'test',
    'Info': 'test'
}, index=[1000])
print(temp_df,"\n")

#---------------------------------concate with old data---------------------------------
imdb3=pd.concat([imdb_df, temp_df])

#---------------------------------dropping a row---------------------------------
imdb3.drop(1000, inplace=True)
print(imdb3.tail(5),"\n")

#---------------------------------number of titles available for each genre---------------------------------
print(imdb_df['Genre'].value_counts(),'\n')

#---------------------------------unique data---------------------------------
print(imdb_df.Genre.unique(),"\n")

#---------------------------------duplicate---------------------------------
print(imdb_df.duplicated(),"\n")
print(imdb_df[imdb_df.duplicated()],"\n")

#---------------------------------drop duplicate---------------------------------
print(imdb_df.drop_duplicates(),"\n")

#---------------------------------discribe---------------------------------
print(imdb_df.describe())
print(imdb_df['Rate'].mean())
print(imdb_df['Rate'].median(),"\n")

#---------------------------------subset of data---------------------------------
# movies having a certificate of PG-13
sample_index = imdb_df['Certificate'] == 'PG-13'
sample_df = imdb_df[sample_index]
print(sample_df)

sample_index = (imdb_df['Certificate'] == 'PG-13') & (imdb_df['Rate'] > 8.5)
sample_df = imdb_df[sample_index]
print(sample_df)

#---------------------------------value count---------------------------------
print(imdb_df['Certificate'].value_counts(),"\n")

#---------------------------------index handeling---------------------------------
print(sample_df.index,"\n")
print(sample_df.reset_index(),"\n")

#---------------------------------shape---------------------------------
print(sample_df.shape,"\n")
sample_df.index = range(0, sample_df.shape[0])
print(sample_df,"\n")

#---------------------------------count null values---------------------------------
print(imdb_df.isna())
print(imdb_df.isna().sum(),"\n")

#---------------------------------fill missing data---------------------------------
print(imdb_df['Metascore'].ffill(),"\n")

#---------------------------------fill with value---------------------------------
print(imdb_df['Certificate'].unique())
print(imdb_df['Certificate'].fillna('Not Rated'),'\n')

# ---------------------------------fill with mean---------------------------------
metascore_mean = imdb_df['Metascore'].mean()
print(imdb_df['Metascore'].fillna(metascore_mean),"\n")

import numpy as np
import pandas as pd
from numpy.random import randn
#DataFrames1
np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['a', 'b', 'c', 'd', 'e'], ['w', 'x', 'y', 'z'])

#Refrencing a column by indexing
df['w']

#Refrencing multiple columns by indexing
df[['w', 'z']]

#Defining a new column by adding the values of two existing columns
df['new'] = df['x'] + df['y']

#Removing a column -- axis1 refers to columns when axis0 refers to rows
df.drop('new', axis = 1)

#if intending to actually drop the column:
df.drop('new', axis = 1, inplace = True)

#if intending to drop a row:
df.drop('e', axis = 0)

#selecting a row
df.loc['a']

#selecting a row by index
df.iloc[2]

#selecting an instance in a particuar row and column
df.loc['b','y']

#selecting instances in particular rows and columns
df.loc[['a', 'b'], ['w', 'y']]

#returns the values that the conditions is true and false for
df > 0
df[df > 0]

#Only gets the rows where the condition is true
df[df['w'] > 0]

#using multiple conditions not with and but with &, not with or but with |
df[(df['w'] > 0) & (df['y'])] 

df[(df['w'] > 0) | (df['y'])]


#reset the index(rows)
df.reset_index()

#set a column as index

df.set_index('y')

#making a multilevel dataframe
outside = ['g1', 'g1', 'g1', 'g2', 'g2', 'g2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ["a", "b"])
df.loc['G1']
df.loc['G1'].loc[1]

df.index.names #returns none none

df.index.names = ["Groups", "Numbers"] #assigns names to the levels Gs and nums

#selecting a particular value
df.loc['g2'].loc[2]['b']

#cross-section
df.xs('g1')

df.xs(1, level='Number')

#
d = {'a':[1, 2, np.nan], 'b':[5, np.nan, np.nan], 'c':[1, 2, 3]}
df = pd.DataFrame(d);

#drops the whole row containing a null or nan and
#the second on drops the column
df.dropna()
df.dropna(axis = 1)

#drops if the row or column have at least two missing values
df.dropna(thresh=2)

#fills the missing values with what you put in the quotation
df.fillna(value="")

#fills the missing value with the mean of the row
df['a'].fillna(value=df['a'].mean())

#
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'FB', 'FB'], 'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}
df = pd.DataFrame(data)

#using groupy in pandas
byComp = df.groupby('Company')
byComp.mean()


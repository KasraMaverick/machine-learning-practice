import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
%matplotlib inline

#Downloading the data as a dataframe
df = pd.read_csv("USA_Housing.csv")

#Figuring out the data
df.info()
df.describe()
df.columns

#Demonstrating the whole dataframe
sns.pairplot(df)
sns.distplot(df['Price'])

sns.heatmap(sns.corr(), annot=True)

#Splitting the data 
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']

#grabbing 




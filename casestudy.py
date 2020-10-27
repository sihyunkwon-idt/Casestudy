import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


health = pd.read_csv('data.csv')
# drop some columns, and reshape the data into a panel format
health.drop(['Unnamed: 60','Country Name','Indicator Name'], axis = 1, inplace= True)
health = health.pivot(index = 'Country Code', columns = 'Indicator Code').unstack().reset_index()
health.columns = ['year','Indicator','Country','value']
health = health.pivot(index=['Country','year'], columns='Indicator')

health = health.reset_index().droplevel(level=0, axis=1)

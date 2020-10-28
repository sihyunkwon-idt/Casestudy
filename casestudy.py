import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


health = pd.read_csv('./data/data.csv')
# drop some columns, and reshape the data into a panel format
health.drop(['Unnamed: 60','Country Name','Indicator Name'], axis = 1, inplace= True)
health = health.pivot(index = 'Country Code', columns = 'Indicator Code').unstack().reset_index()
health.columns = ['year','Indicator','Country','value']
health = health.pivot(index=['Country','year'], columns='Indicator')

health = health.droplevel(level=0, axis=1).reset_index()

# These metrics
health = health[['Country','year','SH.DTH.COMM.ZS', 'SH.DTH.INJR.ZS', 'SH.MED.CMHW.P3', 'SH.CON.1524.FE.ZS', 'SH.CON.1524.MA.ZS','SP.DYN.TFRT.IN', 'NY.GNP.PCAP.CD', 'SH.XPD.PCAP', 'SH.MED.BEDS.ZS', 'SH.IMM.HEPB', 'SH.H2O.SAFE.ZS', 'SH.TBS.INCD', 'SP.DYN.LE00.IN', 'SH.MMR.RISK.ZS', 'SH.STA.STNT.ZS', 'SH.STA.MALN.ZS', 'SP.POP.0014.TO.ZS', 'SP.POP.GROW', 'SH.STA.ANVC.ZS', 'SH.DYN.AIDS.ZS', 'SH.STA.OW15.ZS', 'SH.PRG.SYPH.ZS', 'SH.TBS.PREV', 'SE.XPD.TOTL.GD.ZS', 'SE.ADT.1524.LT.FM.ZS', 'SP.RUR.TOTL.ZS', 'SE.PRM.ENRR', 'SH.PRV.SMOK.MA', 'SL.UEM.TOTL.ZS', 'SP.URB.GROW', 'SP.URB.TOTL.IN.ZS', 'SP.POP.TOTL']]


# Bar Plot for "Missing Value by an Indicator"
# Can we focus on some indicators having low missing value under 40%? 
missing_by_indi =  (health.isna().sum() / len(health)).sort_values()[2:]   
plt.figure(figsize=(20,10))
sns.barplot(x='Indicator', y=0, data=missing_by_indi.reset_index())
plt.tick_params(axis='x', bottom=False, labelbottom=False)
plt.ylabel('% of Missing')



# Bar Plot for "Missing value by a country"
# Filter some countries based on 60%?
missing_by_country = health.set_index(['Country','year']).T.isna().sum().reset_index().groupby('Country').sum()[0] / (health['year'].nunique() * len(health.columns[2:]))
missing_by_country = missing_by_country.sort_values()
plt.figure(figsize=(20,10))
sns.barplot(x='Country', y=0, data=missing_by_country.reset_index())
plt.tick_params(axis='x', bottom=False, labelbottom=False)
plt.ylabel('% of Missing')



# Heatmap(year * indicator): It's not easy to read beacuse of a number of indicators
# But, we can see that there are many missing value in certain "years * indicators" (for example, top left side)
# Blue color is 'missing value'
plt.figure(figsize=(50,20))
sns.heatmap(health.groupby('year').mean().isna(), cmap='Blues') 

# Heatmap(Country * indicator): Messy...
plt.figure(figsize=(50,20))
sns.heatmap(health.groupby('Country').mean().isna(), cmap='Blues')

# Heatmap (Country * year) doesn't have missung value in any combination.



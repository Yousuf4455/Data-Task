import pandas as pd

#load csv to dataframe
df = pd.read_csv("country_vaccination_stats.csv")

df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)

print(df)#print dataframe

df.to_csv('country_vaccination_stats_filled.csv', index=False)
#save as a new file

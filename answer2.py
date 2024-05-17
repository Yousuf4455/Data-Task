#answer of question 6
import pandas as pd

df = pd.read_csv("country_vaccination_stats.csv")

def fill_missing_vaccinations(data):
    min_vaccinations = data.groupby('country')['daily_vaccinations'].min()

    #fill the empy values as min values
    def fill_value(row):
        if pd.isna(row['daily_vaccinations']):
            if pd.notna(min_vaccinations[row['country']]):
                return min_vaccinations[row['country']]
            else:#if there is no vaccination value make the values 0
                return 0
        else:
            return row['daily_vaccinations']
    
    
    data['daily_vaccinations'] = data.apply(fill_value, axis=1)
    return data


df_filled = fill_missing_vaccinations(df)
print(df_filled)
def median_vac(data):
    median_vaccinations = data.groupby('country')['daily_vaccinations'].median().reset_index()
    top_3_countries = median_vaccinations.sort_values(by='daily_vaccinations', ascending=False).head(3)
    return top_3_countries


print(median_vac(df_filled))

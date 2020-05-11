import numpy as np
import pandas as pd
import scipy.stats as st

# read data from folder
data = pd.read_csv('covid_data.csv')

# ask user to select countries
raw_countries = input('Pick countries for selection: ')
countries = raw_countries.split(' ')

# switch date format to standart US yyyy-mm-dd
data['date'] = pd.to_datetime(data['date'])

def calcCountry(country):
    # find row with country on specified date
    info = data.loc[(data['date'] == '2020-05-01') & (data['country'] == country)]

    # fill in cases
    cases = []
    for i in range ((int)(info.iloc[0][3]) - (int)(info.iloc[0][4])):
        cases.append(0)

    for i in range ((int)(info.iloc[0][3])):
        cases.append(1)

    # calculate mean & interval
    mean = (int)(info.iloc[0][4]) / (int)(info.iloc[0][3])

    interval = st.t.interval(0.95, len(cases)-1, loc=mean, scale=st.sem(cases))

    return mean, interval[0], interval[1]

result = []

for country in countries:
    countryResult = calcCountry(country)
    result.append([country, countryResult[0], (countryResult[1], countryResult[2])])

output = pd.DataFrame(result, columns = ['Country', 'Mean', 'Confidence interval'])

print(output.head())
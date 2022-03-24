"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""


# TODO Import the necessary libraries

import pandas as pd
import re

# TODO Import the dataset 

path = r'./data/weather_dataset.data'

# Read file using built-in python tools and after create DataFrame
list_data = []
with open(path) as file:
    lines = file.readlines()
    for line in lines:
        line = re.sub(r',', '.', line)
        list_data.append(line.split())

data = pd.DataFrame(list_data[1:], columns=list_data[0])
data.to_csv('./data/data_csv.csv', index=False)
data = pd.read_csv('./data/data_csv.csv')
print('Loaded data: \n', data)

# TODO Write a function in order to fix date (this relate only to the year info) and apply it

def fix_year(year):
    year = '19' + str(year)
    return year

data['Yr'] = data['Yr'].apply(lambda year: fix_year(year))

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]

# Replace the first 3 columns by a proper datatime index, data type = datetime64[ns]
data.rename(columns = {'Yr':'year', 'Mo':'month', 'Dy':'day'}, inplace = True)
data['datetime'] = pd.to_datetime(data[['year', 'month', 'day']])
data = data.drop(data[['year', 'month', 'day']], axis=1)
print('\nType of "datetime" column is', data['datetime'].dtypes)

# TODO Compute how many values are missing for each location over the entire record

# Print missing values for each column
print('\nMissing values for each column:')
print(data.isna().sum())

# TODO Compute how many non-missing values there are in total

# Print non-missing values for each column
print('\nNon-missing values for each columns:')
print(data.notnull().sum())

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them

# There are many ways to fill in "Nan" values: using the average; median; ML algorithms,
# but it's better to drop "Nan" values unless the in-depth analysis is done
data.dropna(inplace=True)

# Also drop row where there are negative values because speed cannot be negative
# Also drop row where there are strange values
data.drop(data[data.loc11 == -123.1].index, inplace = True)
data.drop(data[data.loc12 == '-123*None'].index, inplace = True)
data.drop(data[data.loc9 == '-15.34'].index, inplace = True)

data.drop(data[data.loc10 == 'NONE'].index, inplace = True)
data.drop(data[data.loc9 == '9999999999999999'].index, inplace = True)
data.drop(data[data.loc9 == '1.0k'].index, inplace = True)
data.drop(data[data.loc5 == 'nodata'].index, inplace = True)
data.drop(data[data.loc4 == 'None'].index, inplace = True)

data[data.columns[:-1]] = data[data.columns[:-1]].astype('float64')
# I can create function and apply it for each row, but faster and easier use pandas function for few rows
# We save time and less CPU loaded

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times

print('\nMean windspeeds of all locations:')
print(data[data.columns[:-1]].mean())

print('\nMean windspeeds of all locations and all times:')
print(data.groupby('datetime').mean())

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days

print('\nMin, max, mean windspeeds and standard deviations of the windspeeds at each location over all the days:')
loc_stats = data.groupby(pd.PeriodIndex(data['datetime'], freq='D').dayofyear).describe()
print(loc_stats)

# TODO Find the average windspeed in January for each location

print('\nAverage windspeed for each location in January:')
print(data.groupby(pd.PeriodIndex(data['datetime'], freq='M').month == 1).mean().iloc[1])

# TODO Downsample the record to a yearly frequency for each location

print('\nAverage windspeed for each location by years:')
print(data.groupby(pd.PeriodIndex(data['datetime'], freq='Y')).mean())

# TODO Downsample the record to a monthly frequency for each location

print('\nAverage windspeed for each location by months:')
print(data.groupby(pd.PeriodIndex(data['datetime'], freq='M').month).mean())

# TODO Downsample the record to a weekly frequency for each location

print('\nAverage windspeed for each location by weeks:')
print(data.groupby(pd.PeriodIndex(data['datetime'], freq='D').week).mean())

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks

print('\nMin, max, mean windspeeds and standard deviations of the windspeeds across all locations for each week:')
print(data.groupby(pd.PeriodIndex(data['datetime'], freq='D').week).describe())

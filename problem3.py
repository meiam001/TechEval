from Database import MyDatabase
from Database import Problem1
import pandas as pd
import time
# Insert Data into
df = pd.read_csv('inputs/headstart_wa.csv')
df2 = pd.read_html('inputs/ncesdata_2D86566_wa.html', header=0)[0]
df2.columns = df2.columns.str.replace(' ', '')
df2.columns = df2.columns.str.replace('*', '')
df2.columns = df2.columns.str.replace('-', '')
df = df.rename(columns={'addressLineOne': 'StreetAddress'})

# 1. How many unique addresses are there in each file?

print('Number distinct addresses in headstart_wa.csv: ' +
      str(len(df.drop_duplicates(subset=['StreetAddress', 'zipFive']))))

# Number distinct addresses in headstart_wa.csv: 312

print('Number distinct addresses in ncesdata_2D86566_wa.xls: ' +
      str(len(df2.drop_duplicates(subset=['StreetAddress', 'ZIP']))))

# Number distinct addresses in ncesdata_2D86566_wa.xls: 2222

# 2. What is the overlap? (How many of the same address exists in both files?)
#     a. NOTE: For time purposes, feel free to choose the most simplistic way and simply
#     describe how you could make it better given more time.

matching_rows = df[df['StreetAddress'].isin(df2.StreetAddress)]
matching_rows2 = df2[df2['StreetAddress'].isin(df.StreetAddress)]

print('Number distinct matching addresses in both files: ' +
      str(len(matching_rows.drop_duplicates(subset=['StreetAddress', 'zipFive']))))

# Number distinct matching addresses in both files: 44
# Possible street addresses that match in different cities, also probably different formatting for street addresses
# Given more time I'd analyze the data to test for a reasonable fuzzy match threshold and match on that instead of exact

# 3. Create a query that includes everything from the Headstart data and an indicator whether there
#    is a match in the NCES data

df['match_flag'] = 0
df.loc[df['StreetAddress'].isin(df2.StreetAddress), 'match_flag'] = 1

# Headstart dataset now includes flag that shows there's a NCES match
from Database import ConnectDB
import pandas as pd

df = pd.read_csv('inputs/headstart_wa.csv')
df2 = pd.read_html('inputs/ncesdata_2D86566_wa.xls', header=0)[0]
df2.columns = df2.columns.str.replace(' ', '')
df2.columns = df2.columns.str.replace('*', '')
df2.columns = df2.columns.str.replace('-', '')

# dump data into sqlite database
db = ConnectDB()
df.to_sql('problem2_headstart', con=db.db_engine)
df2.to_sql('problem2_nces', con=db.db_engine)

# 1. How many unique addresses are there in each file?

# Headstart:
# SELECT SELECT COUNT(*)
#  FROM (SELECT DISTINCT addressLineOne, zipfive FROM problem2_headstart)
# returns 312

# NCES:
# SELECT COUNT(*)
#  FROM (SELECT DISTINCT streetaddress, zip FROM problem2_nces)
# returns 2222

#2.) What is the overlap? (How many of the same address exists in both files?)

#   a. NOTE: For time purposes, feel free to choose the most simplistic way and simply
#     describe how you could make it better given more time.

# SELECT count(*) FROM 'problem2_headstart'
# inner join problem2_nces
# on problem2_headstart.addresslineone = problem2_nces.streetaddress
# and problem2_headstart.zipfive = problem2_nces.zip
# _returns 43_

# 3. Create a query that includes everything from the Headstart data and an indicator whether there is a match in the NCES data

# select *,
# case when addresslineone in (SELECT addresslineone FROM 'problem2_headstart'
# inner join problem2_nces
# on problem2_headstart.addresslineone = problem2_nces.streetaddress
# and problem2_headstart.zipfive = problem2_nces.zip) then 1 else 0 end as flag
# from problem2_headstart

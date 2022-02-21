from Database import MyDatabase
from Database import Problem1
import pandas as pd

# Insert Data into sqlite database
df = pd.read_csv('prob1/prob1.csv')
db = MyDatabase()
session = MyDatabase.get_session(db.db_engine)
db.insert_df(session, df, Problem1, 'rowno', 'float1', 'word1', 'float2', 'int1', 'word2')

"""
Theory 1, normalize all number columns and see if they match, see if any patterns emerge with words
SELECT * FROM 'problem1' 
where (float1*100) = (CAST(int1/1000 AS int)) AND (float1*100) = (CAST(float2*1000 AS int))

Doesn't appear to do anything
"""
##############
"""
Theory 2, check for patterns in the words
Duplicates within a single row allowed (word1 = word2)
Duplicate words throughout rows (row x word 1 = row y word 1)
Doesn't appear to be any rhyme or reason behind what word goes into what column
Maybe a secret word in one of the word columns to indicate the other row is part of the answer?

"""

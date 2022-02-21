<h1>Database</h1>
Where object used to interact with database is stored.
There is also where I would store any explicitly definined tables.


<h1>Problem1</h1>
Work In Progress

<h1>Problem2</h1>
Deleted HTML headers from original NCES file
to allow for easier reading in, then used python's sqlalchemy and pandas to dump data into sqlite database.

##1.) How many unique addresses are there in each file?

Headstart:

SELECT SELECT COUNT(*)
FROM (SELECT DISTINCT addressLineOne, zipfive FROM problem2_headstart)

_returns 312_

NCES:
SELECT COUNT(*)
FROM (SELECT DISTINCT streetaddress, zip FROM problem2_nces)

_returns 2222_

##2.) What is the overlap? (How many of the same address exists in both files?)

   a. NOTE: For time purposes, feel free to choose the most simplistic way and simply
     describe how you could make it better given more time.

###Answer:

SELECT count(*) FROM 'problem2_headstart' 

inner join problem2_nces 

on problem2_headstart.addresslineone = problem2_nces.streetaddress

and problem2_headstart.zipfive = problem2_nces.zip

_returns 43_

## 3.) Create a query that includes everything from the Headstart data and an indicator whether there is a match in the NCES data

select *,  
case when addresslineone in (SELECT addresslineone FROM 'problem2_headstart'  
inner join problem2_nces  
on problem2_headstart.addresslineone = problem2_nces.streetaddress  
and problem2_headstart.zipfive = problem2_nces.zip) then 1 else 0 end as flag  
from problem2_headstart

<h1>Problem3</h1>

I decided to solve problem 2 in python, using a pandas. See file.

<h1>Problem4</h1>

TLDR: Pop culture, disease, and politics.
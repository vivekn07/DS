# 8A - Island Style Slicing - Organize Superstep
# Executed by Nikhil K Pawanikar
# MScIT Part 1 - Sem 1 
# University Department of Information Technology
# 11-Oct-2022

import sys
import os
import pandas as pd
import sqlite3 as sq

sDWName ='/content/datawarehouse.db'
sDbName ='/content/datamart.db'

conn1 = sq.connect(sDWName)
conn2 = sq.connect(sDbName)

sTable = 'Dim-BMI'
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)
PersonFrame0.shape

sSQL="SELECT \
       Height,\
       Weight,\
       Indicator\
  FROM [Dim-BMI]\
  WHERE Indicator > 2\
  ORDER BY  \
       Height,\
       Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)
PersonFrame1.shape

DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['Indicator'],inplace=False)

sTable = 'Dim-BMI-Island'
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")

sSQL="SELECT * FROM [Dim-BMI-Island];"
PersonFrame2=pd.read_sql_query(sSQL, conn2)

PersonFrame2.shape

print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print('################################')
print('Island Data Set (Rows):', PersonFrame2.shape[0])
print('Island Data Set (Columns):', PersonFrame2.shape[1])
print('################################')


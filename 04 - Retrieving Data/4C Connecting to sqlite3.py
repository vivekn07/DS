# -*- coding: utf-8 -*-
"""connecting to sqlite3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m2nzw_Q2wc4BpB6-3XVIIyMbRImgNpYT
"""

import sqlite3 as sq
import pandas as pd

InputFileName = 'Retrieve_IP_DATA.csv'
InputFileDir = 'C:/VKHCG/04-Clark/01-Retrieve'
OutputFileName = 'uvermeulen.db'
OutputFileDir = 'C:/VKHCG/04-Clark/01-Retrieve'
sFileName = InputFileDir + '/' + InputFileName
print(sFileName)
sDatabaseName= OutputFileDir + '/' + OutputFileName
print(sDatabaseName)
conn = sq.connect(sDatabaseName)

IP_DATA_ALL_FIX=pd.read_csv(sFileName,header=0,low_memory=False)
IP_DATA_ALL_FIX.head()

IP_DATA_ALL_FIX.shape

IP_DATA_ALL_FIX.index.names = ['RowIDCSV']
IP_DATA_ALL_FIX.head()

sTable='IP_DATA_ALL'
print('Storing into :',sDatabaseName,' Table:',sTable)

IP_DATA_ALL_FIX.to_sql(sTable, conn, if_exists="replace")
print('Loading into:',sDatabaseName,' Table:',sTable)
TestData=pd.read_sql_query("select * from IP_DATA_ALL;", conn)

TestData.shape

print('## Data Values')
print('################')
print(TestData)
print('################')
print('## Data Profile')
print('################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################')
print('### Done!! ############################################')

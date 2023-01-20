# PRACTICAL 2 - CONVERTING DATA TO HORUS
# 2D. DATABASE TO HORUS
# VIVEKSINGH NEGI - 16-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

import pandas as pd
import sqlite3 as sq

# Input Agreement ============================================

sInputFileName='/content/utility.db'
sInputTable='Country_Code'
conn = sq.connect(sInputFileName)
sSQL='select * FROM ' + sInputTable + ';'
InputData=pd.read_sql_query(sSQL, conn)
print(InputData)

# Processing Rules ===========================================
ProcessData=InputData

# Remove columns ISO-2-Code and ISO-3-CODE

ProcessData.drop('ISO-2-CODE', axis=1,inplace=True)
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)

# Rename Country and ISO-M49
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)

# Set new Index
ProcessData.set_index('CountryNumber', inplace=True)

# Sort data by CurrencyNumber
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)

print(ProcessData)

# Output Agreement ===========================================
OutputData=ProcessData

sOutputFileName= 'DB-TO-HORUS.csv'
OutputData.to_csv(sOutputFileName, index = False)

print('Database to HORUS - Done')
# Utility done ==============================================='
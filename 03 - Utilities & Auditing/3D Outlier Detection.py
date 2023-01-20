# PRACTICAL 3 - Utilities and Auditing
# 3D. OUTLIER DETECTION
# VIVEKSINGH NEGI - 27-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

import pandas as pd

InputFileName='/content/IP_DATA_CORE.csv'
OutputFileName='Outlier.csv'

IP_DATA_ALL=pd.read_csv(InputFileName,header=0,low_memory=False,
  usecols=['Country','Place Name','Latitude','Longitude'], encoding="latin-1")
IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)

IP_DATA_ALL.head()

LondonData=IP_DATA_ALL.loc[IP_DATA_ALL['Place_Name']=='London']
LondonData.shape

AllData=LondonData[['Country', 'Place_Name','Latitude']]
print('All Data')
print(AllData)

MeanData=AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
StdData=AllData.groupby(['Country', 'Place_Name'])['Latitude'].std()

MeanData

StdData

UpperBound=float(MeanData+StdData)
UpperBound

LowerBound=float(MeanData-StdData)
LowerBound

print('Lower than ', LowerBound)
OutliersLower=AllData[AllData.Latitude<LowerBound]
print(OutliersLower)

print('Greater than ', UpperBound)
OutliersUpper=AllData[AllData.Latitude>UpperBound]
print(OutliersUpper)

OutliersUpper.shape

print('Not Outliers')
OutliersNot=AllData[(AllData.Latitude>=LowerBound) & (AllData.Latitude<=UpperBound)]
print(OutliersNot)





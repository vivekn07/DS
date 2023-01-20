# -*- coding: utf-8 -*-
"""Practical_2B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w1rr6022QbIduT_Ns2LJm8YCpqt7MS04
"""

# PRACTICAL 2 - CONVERTING DATA TO HORUS
# 2B. XML TO HORUS
# VIVEKSINGH NEGI - 14-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

# IMPORTING LIBRARIES 
import pandas as pd
import xml.etree.ElementTree as ET

def xml2df(xml_data):
    root = ET.XML(xml_data) 
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    return pd.DataFrame(all_records)

# OPENING THE FILE
sInputFileName='/content/Country_Code.xml'
InputData = open(sInputFileName).read()
print(InputData)

# MOVING THE FILE CONTENT TO ANOTHER VARIABLE SO THAT IT WILL NOT CHANGE ORIGINAL FILE CONTENT
ProcessDataXML=InputData
ProcessData=xml2df(ProcessDataXML)
print(ProcessData)

# CHANGING THE FILE CONTENT BY DROPPING THE COLUMNS
ProcessData.drop('ISO-2-CODE', axis=1,inplace=True)
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)

# RENAMING THE EXISTING COLUMNS NAME
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
print(ProcessData)

# SORTING COUNTRY NUMBER IN ASCENDING NUMBER
ProcessData.set_index('CountryNumber', inplace=True)
ProcessData.sort_values('CountryNumber', axis=0, ascending=True, inplace=True)
ProcessData

# SORTING COUNTRY NAME IN ASCENDING NAME
ProcessData.sort_values('CountryName', axis=0, ascending=True, inplace=True)
print(ProcessData)

# OUTPUT AGREEMENT
OutputData=ProcessData

sOutputFileName='XML_HORUS_Country_Code.csv'
OutputData.to_csv(sOutputFileName, index = True)
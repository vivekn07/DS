# PRACTICAL 3 - Utilities and Auditing
# 3C. Logging
# VIVEKSINGH NEGI - 23-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

import logging
import pandas as pd

Log_Format ='%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename = "D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\3 UTILITIES AND AUDITING\\logs.log",level = logging.DEBUG,format = Log_Format)

#Creating an object 
logger=logging.getLogger() 
#test the logger
logger.info("First message")

InputFile='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\3 UTILITIES AND AUDITING\\IP_DATA_CORE.csv'

logger.info("Attempting to read file")
InputData = pd.read_csv(InputFile, encoding="latin-1")
print(InputData.head())
logger.info("Browsing file data")

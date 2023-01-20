# PRACTICAL 2 - CONVERTING DATA TO HORUS
# 2E. IMAGE TO HORUS
# VIVEKSINGH NEGI - 17-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

import pandas as pd
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

# Input
File = 'D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\Angus.jpg'
Data = io.imread(File)

print(Data.shape)


print('Input data values============')
print('X:' ,Data.shape[0])
print('Y:' ,Data.shape[1])
print('RGBA:' ,Data.shape[2])

RawData = Data.flatten()
print(RawData.shape)

y = Data.shape[2] + 2
x = int(RawData.shape[0]/y)

Pdata = pd.DataFrame(np.reshape(RawData, (x,y)))
sColumns= ['Xaxis', 'Yaxis', 'Red', 'Green', 'Blue']
print(Pdata)

Pdata.index.names = ['ID']
print(Pdata)

print('===========================')
print('Process Data Values =======')
print('===========================')
plt.imshow(Pdata)

OPdata = Pdata
OPdata.to_csv('D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\outputs\\imagetohorus', index = False)

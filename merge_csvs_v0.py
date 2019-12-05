# concatenates csv

import os
import pandas as pd

path_00 = os.path.join(os.getcwd(), '00_00000-04999', 'output_00')
path_01 = os.path.join(os.getcwd(), '01_05000-09999', 'output_01')
path_02 = os.path.join(os.getcwd(), '02_10000-14999', 'output_02')
path_03 = os.path.join(os.getcwd(), '03_15000-19999', 'output_03')
path_04 = os.path.join(os.getcwd(), '04_20000-24999', 'output_04')
path_05 = os.path.join(os.getcwd(), '05_25000-29999', 'output_05')
path_06 = os.path.join(os.getcwd(), '06_30000-34999', 'output_06')
path_07 = os.path.join(os.getcwd(), '07_35000-39999', 'output_07')
path_08 = os.path.join(os.getcwd(), '08_40000-44999', 'output_08')
path_09 = os.path.join(os.getcwd(), '09_45000-49999', 'output_09')
path_10 = os.path.join(os.getcwd(), '10_50000-69999', 'output_10')
path_11 = os.path.join(os.getcwd(), '11_70000-89999', 'output_11')
path_12 = os.path.join(os.getcwd(), '12_90000-109999', 'output_12')
path_13 = os.path.join(os.getcwd(), '13_110000-129999', 'output_13')
path_14 = os.path.join(os.getcwd(), '14_130000-149999', 'output_14')
path_15 = os.path.join(os.getcwd(), '15_150000-169999', 'output_15')
path_16 = os.path.join(os.getcwd(), '16_170000-194471', 'output_16')

df00 = pd.read_csv(path_00)
df01 = pd.read_csv(path_01)
df02 = pd.read_csv(path_02)
df03 = pd.read_csv(path_03)
df04 = pd.read_csv(path_04)
df05 = pd.read_csv(path_05)
df06 = pd.read_csv(path_06)
df07 = pd.read_csv(path_07)
df08 = pd.read_csv(path_08)
df09 = pd.read_csv(path_09)
df10 = pd.read_csv(path_10)
df11 = pd.read_csv(path_11)
df12 = pd.read_csv(path_12)
df13 = pd.read_csv(path_13)
df14 = pd.read_csv(path_14)
df15 = pd.read_csv(path_15)
df16 = pd.read_csv(path_16)

df00.columns = ['id','cveid','description','spans']
df01.columns = ['id','cveid','description','spans']
df02.columns = ['id','cveid','description','spans']
df03.columns = ['id','cveid','description','spans']
df04.columns = ['id','cveid','description','spans']
df05.columns = ['id','cveid','description','spans']
df06.columns = ['id','cveid','description','spans']
df07.columns = ['id','cveid','description','spans']
df08.columns = ['id','cveid','description','spans']
df09.columns = ['id','cveid','description','spans']
df10.columns = ['id','cveid','description','spans']
df11.columns = ['id','cveid','description','spans']
df12.columns = ['id','cveid','description','spans']
df13.columns = ['id','cveid','description','spans']
df14.columns = ['id','cveid','description','spans']
df15.columns = ['id','cveid','description','spans']
df16.columns = ['id','cveid','description','spans']

final_df = pd.concat([df00, df01, df02, df03, df04, df05, df06, df07, df08, df09, df10, df11, df12, df13, df14, df15, df16])

print(df00.shape)
print(df01.shape)
print(df02.shape)
print(df03.shape)
print(df04.shape)
print(df05.shape)
print(df06.shape)
print(df07.shape)
print(df08.shape)
print(df09.shape)
print(df10.shape)
print(df11.shape)
print(df12.shape)
print(df13.shape)
print(df14.shape)
print(df15.shape)
print(df16.shape)
print(final_df.shape)

final_df.to_csv('total_output_00000-194471', index = False)

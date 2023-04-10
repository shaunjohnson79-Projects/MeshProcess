import numpy as np

aa = np.array(['1', '4', '', '5'])
aa = np.where(aa == '', np.nan, aa) 
print
aa = aa.astype(float)  
print(aa)

aa = np.nan_to_num(aa, nan=0, posinf=None, neginf=None, copy=False)  # replace NaN with 0
aa = aa.astype(int)  # convert array to int data type

print(aa)

bb=np.array(1,2,0,4)
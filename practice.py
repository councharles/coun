#Binary search
import openpyxl
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows


def binarySearch(an_array, target):
    left = 0
    right = len(an_array)-1
    return myhelper(an_array,target,left,right)
def myhelper(an_array, target,left, right):
    if left>right:
        return -1
    middle = (left+right)//2
    if target == an_array[middle]:
        return middle
    if target> an_array[middle]:
        left = middle +1
        
        return myhelper(an_array,target,left,right)
    if target<an_array[middle]:
        right = middle -1
        return myhelper(an_array, target, left, right)


aa = openpyxl.load_workbook('Sankar/MyReport2023-05-31_10-59-58.xlsx')
sheet = aa['Result'].values
ns = aa.create_sheet(title='Sheet')
df = pd.DataFrame(sheet)
for a, b in df.iterrows():
   rr = b[1]
   if rr != None:
       b = 1
       for p in rr.split('\n'):
           if 'PID' in p:
               #print(b[0], '\t', p.replace('      , ', ' '))
               df.at[a,b]= p.replace('      , ', ' ')
               b+=1
   else:
       #print(b[0], '\t', 'Not Found')
       df.at[a, 1] = 'Not Found'

for row in dataframe_to_rows(df):
   ns.append(row)
print(df)
aa.save('Sankar/MyReport2023-05-31_10-59-58.xlsx')
aa.close()



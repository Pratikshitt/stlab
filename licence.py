import pandas as  pd
import re
print("Enter 16 character license key:")
x=input()
for i,d in pd.read_excel("lic.xlsx").iterrows():
    
    if(re.search('(.*([0-9]+).*-){3}.*([0-9]+).*',d[1])):
        if(d[1]==x):
            print(d[1])
                
        
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:13:06 2025

@author: ruina
"""

import glob
import pandas as pd

print('\nNamed with wildcard *:')

IXI = glob.glob('./Dataset/**/*.nii.gz')
for name in IXI:
    print(name)
    
# Replace backslashes with forward slashes
IXI = [path.replace("\\", "/") for path in IXI]
   
df = pd.read_csv("IXI_metadata.csv")

# Convert to formatted IXI IDs
df['Formatted_IXI_ID'] = df['IXI_ID'].apply(lambda x: f'IXI{x:03}')

# Find matching paths for each IXI_ID
df['filepath'] = df['Formatted_IXI_ID'].apply(
    lambda x: next((path for path in IXI if x in path), None)
)
df = df[['AGE', 'filepath']].dropna()

df.to_csv("IXI_cleaned.csv",index=False)

# print('\nNamed with wildcard *:')
# IXI = glob.glob('C:/Sean/PhD/Dataset/ixi_tiny/ixi_tiny/**/*.nii.gz')
# for name in IXI:
#     print(name)    

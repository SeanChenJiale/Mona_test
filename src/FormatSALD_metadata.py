import glob
import pandas as pd

### instructions place into ./Metadata/sub_information_SALD.xlsx
### preprocessed images should be in ./PreProcessedData/SALD/<all SALD_nii.gz files here>
print('SALD csv formatter')

SALD = glob.glob('./PreProcessedData/SALD/*.nii.gz') ## change to the file of the pre-processed images
for name in SALD:
    print(name)
    
# Replace backslashes with forward slashes
SALD = [path.replace("\\", "/") for path in SALD]

df = pd.read_excel("Metadata/sub_information_SALD.xlsx") ### metadatafolder here

# Convert to formatted IXI IDs #not needed 
df['Formatted_Sub_ID'] = df['Sub_ID'].apply(lambda x: f'sub-{x:06}')

# Find matching paths for each IXI_ID
df['filepath'] = df['Formatted_Sub_ID'].apply(
    lambda x: next((path for path in SALD if x in path), None)
)
df = df[['Age', 'filepath']].dropna()

df.to_csv("./Metadata/SALD_cleaned.csv",index=False)


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

ICBM = pd.read_csv("./Metadata/ICBM_Metadata.csv")
SALD = pd.read_excel("./Metadata/sub_information_SALD.xlsx")
AOMIC = pd.read_csv("./Metadata/participants_Aomic.csv")
IXI = pd.read_csv("./Metadata/IXI_cleaned.csv")

### for viewing column type and naming convention
# print(IXI.columns)
# print(ICBM.columns)
# print(SALD.columns)
# print(AOMIC.columns)

all_ages = pd.concat(
[IXI['AGE'],
ICBM['Age'],
SALD['Age'],
AOMIC['age']
],
ignore_index=True
)
# Create a new DataFrame with the stacked column
df = pd.DataFrame({'Age': all_ages})

subjectcount = len(df)
# Create the figure
plt.figure(figsize=(8,5))

# Plot histogram with KDE
sns.histplot(df['Age'], bins=30, kde=True, color='blue', edgecolor='black', alpha=0.6)

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title(f"Age Distribution ICBM,IXI,SALD,AOMIC , n={subjectcount}")

# Show plot
plt.show()
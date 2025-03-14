
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

df = pd.read_csv("./Metadata/ICBM_Metadata.csv")

subjectcount = len(df)
# Create the figure
plt.figure(figsize=(8,5))

# Plot histogram with KDE
sns.histplot(df['Age'], bins=30, kde=True, color='blue', edgecolor='black', alpha=0.6)

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title(f"Age Distribution ICBM, n={subjectcount}")

# Show plot
plt.show()



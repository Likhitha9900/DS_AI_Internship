import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Blood Transfusion Service Center Data Set.csv")

df.columns = [
    "Recency",
    "Frequency",
    "Monetary",
    "Time",
    "Class"
]

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nTarget Distribution:")
print(df["Class"].value_counts())

print("\nTarget Percentage:")
print(df["Class"].value_counts(normalize=True) * 100)

sns.countplot(x="Class", data=df)
plt.title("Donation Class Distribution")
plt.xlabel("Donation Class")
plt.ylabel("Number of Donors")
plt.show()

df[["Recency", "Frequency", "Monetary", "Time"]].hist(
    figsize=(10, 8)
)
plt.suptitle("Feature Distributions")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=df[["Recency", "Frequency", "Monetary", "Time"]])
plt.title("Feature Boxplots")
plt.xticks(rotation=45)
plt.show()
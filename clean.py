import pandas as pd

df = pd.read_csv("Blood Transfusion Service Center Data Set.csv")

df.columns = [
    "Recency",
    "Frequency",
    "Monetary",
    "Time",
    "Class"
]

print("Original Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("\nShape After Removing Duplicates:", df.shape)

X = df[[
    "Recency",
    "Frequency",
    "Monetary",
    "Time"
]]

y = df["Class"]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())

print("\nFeature Shape:", X.shape)
print("Target Shape:", y.shape)

print("\nTarget Distribution:")
print(y.value_counts())

df.to_csv("cleaned_blood_transfusion.csv", index=False)

print("\nCleaned dataset saved successfully.")
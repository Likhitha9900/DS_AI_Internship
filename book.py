import pandas as pd

# Problem Statement
print("PROBLEM STATEMENT")
print("Predict whether a book is Popular or Not Popular")
print("based on its Pages, Rating, Reviews and Price.")

# Load dataset
df = pd.read_csv("data.csv")

# Display dataset
print("\nDATASET:")
print(df)

# Display first 5 rows
print("\nFIRST 5 ROWS:")
print(df.head())

# Check shape
print("\nDATASET SHAPE:")
print(df.shape)

# Display column names
print("\nCOLUMN NAMES:")
print(df.columns)

# Display data types
print("\nDATA TYPES:")
print(df.dtypes)

# Identify numerical features
print("\nNUMERICAL FEATURES:")
print(df.select_dtypes(include="number").columns)

# Identify categorical columns
print("\nCATEGORICAL COLUMNS:")
print(df.select_dtypes(include="object").columns)

# Potential features
features = ["Pages", "Rating", "Reviews", "Price"]

print("\nPOTENTIAL FEATURES:")
print(features)

# Label column
label = "Popularity"

print("\nLABEL COLUMN:")
print(label)

# Justification
print("\nJUSTIFICATION:")
print("Popularity is selected as the label because it is the")
print("outcome that we want the machine learning model to predict.")
print("Pages, Rating, Reviews and Price are used as input features.")

# Insights
print("\nINSIGHTS:")

print("1. Books with higher ratings generally appear to be more popular.")

print("2. Books with a larger number of reviews generally show higher popularity.")

print("3. Price can be analyzed to see whether expensive or affordable books")
print("   are more likely to be popular.")

print("4. The number of pages can be studied to determine whether book length")
print("   has any relationship with popularity.")

print("5. Popularity is the target variable, while Pages, Rating, Reviews and")
print("   Price are the potential input features.")
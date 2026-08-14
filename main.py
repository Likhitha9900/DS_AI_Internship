import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS - TITANIC DATASET")
print("=" * 60)

print("\n1. FIRST 5 ROWS")
print(df.head())

print("\n2. LAST 5 ROWS")
print(df.tail())

print("\n3. SHAPE OF DATASET")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n4. COLUMN NAMES")
print(df.columns.tolist())

print("\n5. DATA TYPES")
print(df.dtypes)

print("\n6. DATASET INFORMATION")
df.info()

print("\n7. STATISTICAL SUMMARY")
print(df.describe())

print("\n8. MISSING VALUES")
print(df.isnull().sum())

print("\nMISSING VALUE PERCENTAGE")
print((df.isnull().sum() / len(df)) * 100)

print("\n9. DUPLICATE ROWS")
print("Number of duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)

if df["Age"].isnull().sum() > 0:
    df["Age"] = df["Age"].fillna(df["Age"].median())

if df["Embarked"].isnull().sum() > 0:
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\n10. MISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

numerical_columns = ["Age", "Fare", "SibSp", "Parch"]

print("\nNUMERICAL SUMMARY")
print(df[numerical_columns].describe())

print("\nGENDER DISTRIBUTION")
print(df["Sex"].value_counts())

print("\nPASSENGER CLASS DISTRIBUTION")
print(df["Pclass"].value_counts())

print("\nSURVIVAL DISTRIBUTION")
print(df["Survived"].value_counts())

print("\nEMBARKED DISTRIBUTION")
print(df["Embarked"].value_counts())

for column in numerical_columns:
    plt.figure(figsize=(7, 5))
    plt.hist(df[column], bins=10, edgecolor="black")
    plt.title("Distribution of " + column)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

categorical_columns = ["Sex", "Pclass", "Survived", "Embarked"]

for column in categorical_columns:
    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x=column)
    plt.title("Count Plot of " + column)
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()

for column in numerical_columns:
    plt.figure(figsize=(7, 5))
    sns.boxplot(y=df[column])
    plt.title("Box Plot of " + column)
    plt.ylabel(column)
    plt.show()

print("\nSURVIVAL BY GENDER")
print(pd.crosstab(df["Sex"], df["Survived"]))

print("\nSURVIVAL BY PASSENGER CLASS")
print(pd.crosstab(df["Pclass"], df["Survived"]))

print("\nSURVIVAL BY EMBARKED PORT")
print(pd.crosstab(df["Embarked"], df["Survived"]))

plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="Sex", y="Survived")
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Survival Rate")
plt.show()

plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="Pclass", y="Survived")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Survival Rate")
plt.show()

plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="Embarked", y="Survived")
plt.title("Survival Rate by Embarkation Port")
plt.xlabel("Embarked")
plt.ylabel("Average Survival Rate")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Age", y="Fare", hue="Survived")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Age", y="Survived")
plt.title("Age vs Survival")
plt.xlabel("Age")
plt.ylabel("Survived")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Pclass", y="Fare")
plt.title("Fare Distribution by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Survived", y="Age")
plt.title("Age Distribution by Survival")
plt.xlabel("Survived")
plt.ylabel("Age")
plt.show()

print("\nSKEWNESS ANALYSIS")

for column in numerical_columns:
    skew_value = df[column].skew()
    print(f"{column} skewness: {skew_value:.3f}")

    if skew_value > 1:
        print("Highly positively skewed")
    elif skew_value > 0.5:
        print("Moderately positively skewed")
    elif skew_value < -1:
        print("Highly negatively skewed")
    elif skew_value < -0.5:
        print("Moderately negatively skewed")
    else:
        print("Approximately symmetric")

print("\nCORRELATION MATRIX")

correlation = df[numerical_columns + ["Survived", "Pclass"]].corr()

print(correlation)

plt.figure(figsize=(10, 7))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

print("\nOUTLIER DETECTION")

for column in numerical_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print("\nColumn:", column)
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Number of Outliers:", len(outliers))

for column in numerical_columns:

    plt.figure(figsize=(7, 5))
    sns.boxplot(y=df[column])
    plt.title("Outlier Detection - " + column)
    plt.ylabel(column)
    plt.show()

survival_rate = df["Survived"].mean() * 100

print("\nOVERALL SURVIVAL RATE")
print(f"{survival_rate:.2f}%")

gender_survival = df.groupby("Sex")["Survived"].mean() * 100

print("\nSURVIVAL RATE BY GENDER")
print(gender_survival)

class_survival = df.groupby("Pclass")["Survived"].mean() * 100

print("\nSURVIVAL RATE BY PASSENGER CLASS")
print(class_survival)

print("\nPATTERN IDENTIFICATION")

print("""
1. Gender has an important relationship with survival.
2. Passenger class shows a noticeable relationship with survival.
3. Higher fare values are generally associated with higher passenger classes.
4. Fare contains extreme values.
5. Age has a weaker relationship with survival.
6. Fare is generally right-skewed.
7. Gender and passenger class are important patterns in the dataset.
""")

print("\nFINAL INSIGHTS")

print("""
The Titanic dataset contains numerical and categorical variables.
Missing values and duplicate records were checked and handled.
Univariate analysis showed the distribution of the variables.
Bivariate analysis showed relationships between survival and
other variables. Female passengers generally had a higher
survival rate than male passengers. Higher-class passengers
generally had better survival outcomes. Fare contained noticeable
outliers and showed positive skewness. Correlation analysis
helped identify relationships between numerical variables.
""")

print("\nCONCLUSION")

print("""
The EDA of the Titanic dataset revealed important patterns in
passenger survival. Gender and passenger class showed strong
relationships with survival. Fare had outliers and a right-skewed
distribution. Visualizations, correlation analysis, skewness
analysis, and outlier detection provided a better understanding
of the dataset. Overall, EDA helped identify trends, relationships,
distributions, and unusual observations in the Titanic dataset.
""")

print("\nEDA COMPLETED SUCCESSFULLY!")
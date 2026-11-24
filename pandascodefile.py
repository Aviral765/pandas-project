from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent

# load the csv file
df = pd.read_csv(PROJECT_DIR / "Titanic-Dataset.csv")

print("Before cleaning:", df.shape)
print(df.isnull().sum())

# remove extra index column if it is there
df = df.drop(columns=["Unnamed: 0"], errors="ignore")

# remove duplicate rows
df = df.drop_duplicates()

# remove extra spaces from column names
df.columns = df.columns.str.strip()

# remove extra spaces from text columns
text_cols = df.select_dtypes(include=["object", "string"]).columns
for col in text_cols:
    df[col] = df[col].str.strip()

# fill missing values instead of deleting rows
# Age: median is used because it is not affected by very old/young outliers
df["Age"] = df["Age"].fillna(df["Age"].median())
# Embarked: only 2 values missing, so fill with the most common port (mode)
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
# Cabin: most values are missing, so mark them as Unknown
df["Cabin"] = df["Cabin"].fillna("Unknown")

# keep only valid values
df = df[df["Age"] > 0]
df = df[df["Fare"] >= 0]
df = df[df["Survived"].isin([0, 1])]
df = df[df["Pclass"].isin([1, 2, 3])]

# fix the index numbers
df = df.reset_index(drop=True)

# save the clean file
df.to_csv(PROJECT_DIR / "cleaned_titanic.csv", index=False)

print("Cleaning done!")
print("After cleaning:", df.shape)
print(df.isnull().sum())

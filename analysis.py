"""
Titanic survival analysis.

Run pandascodefile.py first to create cleaned_titanic.csv,
then run this file:  python analysis.py
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


PROJECT_DIR = Path(__file__).resolve().parent

# load the cleaned data
df = pd.read_csv(PROJECT_DIR / "cleaned_titanic.csv")

print("Rows and columns:", df.shape)

# ---------- survival statistics ----------
print("\nOverall survival rate:", round(df["Survived"].mean(), 2))

print("\nSurvival rate by gender:")
by_sex = df.groupby("Sex")["Survived"].mean().round(2)
print(by_sex)

print("\nSurvival rate by class:")
by_class = df.groupby("Pclass")["Survived"].mean().round(2)
print(by_class)

print("\nSurvival rate by gender and class:")
by_sex_class = df.groupby(["Pclass", "Sex"])["Survived"].mean().round(2)
print(by_sex_class)

print("\nAverage age by survival:")
print(df.groupby("Survived")["Age"].mean().round(1))

print("\nAverage fare by class:")
print(df.groupby("Pclass")["Fare"].mean().round(2))

# ---------- charts (saved as images) ----------
# chart 1: survival rate by gender
plt.figure(figsize=(5, 4))
by_sex.plot(kind="bar", color=["#e07a9b", "#4a90d9"])
plt.title("Survival Rate by Gender")
plt.ylabel("Survival rate")
plt.xlabel("")
plt.ylim(0, 1)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(PROJECT_DIR / "survival_by_gender.png", dpi=150)
plt.close()

# chart 2: survival rate by class
plt.figure(figsize=(5, 4))
by_class.plot(kind="bar", color="#4a90d9")
plt.title("Survival Rate by Passenger Class")
plt.ylabel("Survival rate")
plt.xlabel("Passenger class")
plt.ylim(0, 1)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(PROJECT_DIR / "survival_by_class.png", dpi=150)
plt.close()

# chart 3: age distribution of survivors vs non-survivors
plt.figure(figsize=(6, 4))
plt.hist(df[df["Survived"] == 0]["Age"], bins=20, alpha=0.6, label="Did not survive")
plt.hist(df[df["Survived"] == 1]["Age"], bins=20, alpha=0.6, label="Survived")
plt.title("Age Distribution by Survival")
plt.xlabel("Age")
plt.ylabel("Number of passengers")
plt.legend()
plt.tight_layout()
plt.savefig(PROJECT_DIR / "age_distribution.png", dpi=150)
plt.close()

print("\nCharts saved: survival_by_gender.png, survival_by_class.png, age_distribution.png")

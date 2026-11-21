
print("\nOverall survival rate:", round(df["Survived"].mean(), 2))



print("\nSurvival rate by gender:")
print(df.groupby("Sex")["Survived"].mean().round(2))



print("\nSurvival rate by class:")
print(df.groupby("Pclass")["Survived"].mean().round(2))



print("\nAverage age by survival:")
print(df.groupby("Survived")["Age"].mean().round(1))
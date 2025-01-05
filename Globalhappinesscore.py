import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np


df = pd.read_csv("2015.csv")
happiness_score = df["Happiness Score"]
economy = df["Economy (GDP per Capita)"]
health = df["Health (Life Expectancy)"]
# print("Mean happines Score is: ",happiness_score.mean())
# print("Median happines Score is: ",happiness_score.median())
# print("Mode happines Score is: ",happiness_score.mode())
# print("Mean economy is: ",economy.mean())
# print("Median economy is: ",economy.median())
# print("Mode economy is: ",economy.mode())
# print("Mean health is: ",health.mean())
# print("Median health is: ",health.median())
# print("Mode health is: ",health.mode())
column_of_interest = ["Happiness Score", "Economy (GDP per Capita)", "Health (Life Expectancy)"]
print(df[column_of_interest].describe())
top_10_country = df.sort_values(by="Happiness Score", ascending=False).head(10)

#plotting a bar chart
plt.figure(figsize=(10,6))
plt.bar(top_10_country['Country'], top_10_country["Happiness Score"], color='skyblue')
plt.title("Top 10 Countries by happiness score", fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel("Happiness Score", fontsize=12)
plt.xticks(rotation=45)

plt.yticks(np.arange(6,8, step=0.2))
plt.tight_layout()
plt.show()

#correlation between GDP and happiness score
plt.figure(figsize=(10,6))
plt.scatter(top_10_country["Economy (GDP per Capita)"], top_10_country['Happiness Score'], color="red")
plt.xlabel("Economy")
plt.ylabel("happiness score")
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.title("Correlation between GDP and happiness score", fontsize=16)
plt.show()

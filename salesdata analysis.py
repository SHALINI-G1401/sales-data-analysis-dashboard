import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Project started successfully")

# Load dataset
df = pd.read_csv(
    r"C:\Users\SHALINI\OneDrive\Desktop\Sales Data Analysis Dashboard\sales.csv",
    encoding="latin1"
)

print(df.head())

# ---------- DATA ANALYSIS ----------

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# ---------- VISUALIZATION ----------

# Sales by Category
plt.figure()
sns.barplot(x="Category", y="Sales", data=df)
plt.title("Sales by Category")
plt.show()

# Profit by Region
plt.figure()
sns.barplot(x="Region", y="Profit", data=df)
plt.title("Profit by Region")
plt.show()
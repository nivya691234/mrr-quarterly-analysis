# Author: 24f1002781@ds.study.iitm.ac.in

import matplotlib.pyplot as plt
import pandas as pd

# Quarterly MRR Growth Data
quarters = ["Q1", "Q2", "Q3", "Q4"]
mrr_growth = [4.08, 6.77, 12.51, 13.36]
industry_target = 15

df = pd.DataFrame({"Quarter": quarters, "MRR Growth": mrr_growth})

# Compute average
average = df["MRR Growth"].mean()
print("Average MRR Growth:", average)

# Line plot
plt.figure(figsize=(8,5))
plt.plot(quarters, mrr_growth, marker='o', label='MRR Growth 2024')
plt.axhline(industry_target, color='red', linestyle='--', label='Industry Target (15)')
plt.title("2024 MRR Quarterly Growth vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("mrr_trend.png")
print("Visualization saved as mrr_trend.png")

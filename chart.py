# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic customer engagement data
np.random.seed(42)  # for reproducibility
num_customers = 200

data = pd.DataFrame({
    "Visits_Per_Month": np.random.poisson(5, num_customers),
    "Avg_Session_Duration": np.random.normal(15, 5, num_customers),  # minutes
    "Purchase_Frequency": np.random.poisson(2, num_customers),
    "Avg_Order_Value": np.random.normal(50, 20, num_customers),  # dollars
    "Loyalty_Score": np.random.uniform(0, 100, num_customers)  # 0-100 scale
})

# Compute correlation matrix
corr_matrix = data.corr()

# Create heatmap
plt.figure(figsize=(8, 8))  # 512x512 pixels at dpi=64
heatmap = sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="RdYlGn",
    linewidths=0.5,
    square=True,
    cbar_kws={"shrink": 0.8}
)

# Add title
plt.title("Customer Engagement Correlation Matrix", fontsize=16, pad=20)

# Save chart
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

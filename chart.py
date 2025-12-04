# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic customer engagement data
np.random.seed(42)
num_customers = 200

data = pd.DataFrame({
    "Visits_Per_Month": np.random.poisson(5, num_customers),
    "Avg_Session_Duration": np.random.normal(15, 5, num_customers),
    "Purchase_Frequency": np.random.poisson(2, num_customers),
    "Avg_Order_Value": np.random.normal(50, 20, num_customers),
    "Loyalty_Score": np.random.uniform(0, 100, num_customers)
})

# Compute correlation matrix
corr_matrix = data.corr()

# Create figure with exact pixel dimensions
fig = plt.figure(figsize=(512/100, 512/100), dpi=100)  # 5.12x5.12 inches at 100 dpi = 512px
ax = fig.add_subplot(111)

# Draw heatmap on this axis
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="RdYlGn",
    linewidths=0.5,
    square=True,
    cbar_kws={"shrink": 0.8},
    ax=ax
)

# Remove margins/padding to get exact pixel size
plt.axis('off')  # optional: remove axis lines/ticks if allowed
plt.title("Customer Engagement Correlation Matrix", fontsize=16, pad=20)

# Save exactly 512x512
fig.savefig("chart.png", dpi=100, bbox_inches='tight', pad_inches=0)
plt.close()

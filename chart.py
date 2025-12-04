import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. Configuration and Styling ---

# Set a professional Seaborn style for the executive presentation
sns.set_theme(style="white")
# Set the context for better text sizing in presentations
sns.set_context("talk") 

# --- 2. Data Generation: Realistic Synthetic Data ---

# Define the metrics names
metrics = [
    'Monthly Spend (USD)', 
    'Website Visits', 
    'Email Clicks', 
    'Support Tickets', 
    'App Sessions', 
    'Social Shares'
]

# Generate synthetic data for 1000 customers
# Create a base for highly correlated metrics (e.g., spend, visits, app sessions)
np.random.seed(42)  # For reproducibility
n_customers = 1000

# Base factor for engagement
base_engagement = np.random.normal(loc=5, scale=1.5, size=n_customers)

# Generate metrics with realistic correlations/distributions
data = pd.DataFrame({
    # High positive correlation with base_engagement
    'Monthly Spend (USD)': 100 + 50 * base_engagement + np.random.normal(0, 15, n_customers),
    
    # Positive correlation with spend
    'Website Visits': 10 + 2 * base_engagement + np.random.poisson(3, n_customers),
    
    # Moderate positive correlation
    'App Sessions': 5 + 1.5 * base_engagement + np.random.normal(0, 1, n_customers),

    # Low/Negative correlation (e.g., high engagement means fewer issues)
    'Support Tickets': np.maximum(0, 3 - 0.5 * base_engagement + np.random.poisson(1, n_customers)),
    
    # Moderate positive correlation
    'Email Clicks': 2 + 0.8 * base_engagement + np.random.poisson(2, n_customers),

    # Weak/Moderate correlation, often independent
    'Social Shares': np.random.poisson(2, n_customers) + np.random.normal(0, 0.5, n_customers),
})

# Ensure no negative values for count data
data = data.clip(lower=0)
data = data.round(2)

# --- 3. Correlation Matrix Calculation ---

# Calculate the Pearson correlation matrix
correlation_matrix = data.corr()

# --- 4. Heatmap Visualization ---

# Set figure size for the 512x512 output (8 inches * 64 dpi = 512 pixels)
plt.figure(figsize=(8, 8)) 

# Generate a mask for the upper triangle (for better readability/less redundancy)
mask = np.triu(correlation_matrix)

# Create the heatmap
sns.heatmap(
    correlation_matrix, 
    mask=mask, 
    annot=True,              # Show the correlation values on the heatmap
    fmt=".2f",               # Format the annotation to 2 decimal places
    cmap='coolwarm',         # Use a diverging color palette (good for correlation)
    vmax=1,                  # Max value for the color scale
    vmin=-1,                 # Min value for the color scale
    center=0,                # Center the color scale at 0
    linewidths=.5,           # Add lines between cells for clarity
    cbar_kws={"shrink": .8, "label": "Correlation Coefficient"} # Customize color bar
)

# Set the title for the executive presentation
plt.title(
    "Customer Engagement Correlation Matrix", 
    fontsize=18, 
    fontweight='bold',
    pad=20
)

# Adjust tick labels for better visibility
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(rotation=0, fontsize=12)

plt.tight_layout() # Adjust layout to prevent labels from being cut off

# --- 5. Export and Save ---

# Save the chart as PNG with exactly 512x512 pixel dimensions (8 inches * 64 dpi = 512 pixels)
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

# Optional: Display the chart (uncomment for local testing)
# plt.show()

print("chart.png saved successfully with 512x512 dimensions.")

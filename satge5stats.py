import pandas as pd
from scipy.stats import ttest_ind

# Define the data
data = {
    "Block 1 (time sec)": [12.25, 35.73, 31.23, 25.71, 25.21],
    "Block 2 (number of tasks)": [4, 1, 2, 5, 1],
    "Block 3 (time sec)": [2.61, 9.06, 9.81, 9.81, 5.56],
    "Block 4 (time sec)": [3.06, 10.26, 4.93, 9.06, 8.54],
    "Block 5 (yes 1 or no 0)": [1, 1, 1, 1, 1],
    "Block 6 (time sec)": [2.74, 7.99, 3.84, 11.09, 9.26],
    "Block 7 (scale 1-10)": [9, 8, 10, 3, 8],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate means and standard deviations
means = df.mean(numeric_only=True)
std_devs = df.std(numeric_only=True)

# Perform t-tests (pairwise comparisons between selected columns)
# Example: t-test between Block 1 and Block 6
t_stat, p_value = ttest_ind(df["Block 1 (time sec)"], df["Block 6 (time sec)"])

# Display results
print("Means:")
print(means)
print("\nStandard Deviations:")
print(std_devs)
print(f"\nT-test between Block 1 and Block 6:\nT-statistic = {t_stat:.4f}, P-value = {p_value:.4f}")

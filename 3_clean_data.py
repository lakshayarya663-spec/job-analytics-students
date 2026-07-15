"""
3_clean_data.py
----------------
Cleans the raw job data using Pandas:
  - removes duplicate rows
  - removes rows with missing salary
  - adds a salary_avg column (average of min and max)

HOW TO RUN:
    python 3_clean_data.py
"""

import pandas as pd

# ---- Step 1: Load the raw data ----
df = pd.read_csv("data/raw_jobs.csv")
print(f"Loaded {len(df)} rows")

# ---- Step 2: Remove duplicate job postings ----
df = df.drop_duplicates(subset=["title", "city", "salary_min", "salary_max"])

# ---- Step 3: Remove rows with missing important data ----
df = df.dropna(subset=["title", "salary_min", "salary_max"])

# ---- Step 4: Create a new column: average salary ----
df["salary_avg"] = (df["salary_min"] + df["salary_max"]) / 2

# ---- Step 5: Save the cleaned data ----
df.to_csv("data/clean_jobs.csv", index=False)

print(f"Saved {len(df)} clean rows -> data/clean_jobs.csv")
print(df.head())

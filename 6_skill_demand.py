"""
6_skill_demand.py
--------------------
Counts how many job postings mention each skill.

The "skills" column has multiple skills in one cell, separated by commas
(e.g. "Python, SQL, AWS"), so we can't just GROUP BY it in SQL. Instead
we split it apart using Pandas.

HOW TO RUN:
    python 6_skill_demand.py
"""

import pandas as pd

df = pd.read_csv("data/clean_jobs.csv")

# ---- Step 1: Split the comma-separated skills into a list ----
df["skills_list"] = df["skills"].apply(lambda s: [skill.strip() for skill in s.split(",")])

# ---- Step 2: Turn each skill into its own row (one job can have many rows now) ----
skills_exploded = df.explode("skills_list")

# ---- Step 3: Count how many times each skill appears ----
skill_counts = (
    skills_exploded["skills_list"]
    .value_counts()
    .reset_index()
)
skill_counts.columns = ["skill", "num_postings"]

# ---- Step 4: Save the result ----
skill_counts.to_csv("data/results/skill_demand.csv", index=False)

print("Top 10 most in-demand skills:")
print(skill_counts.head(10).to_string(index=False))
print("\nSaved data/results/skill_demand.csv")

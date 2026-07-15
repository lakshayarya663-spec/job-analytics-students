"""
4_load_to_sql.py
------------------
Loads the cleaned job data into a SQL database (SQLite) so we can run
SQL queries on it.

We use ONE simple table called "jobs" -- this keeps the SQL queries easy
to write and understand (no joins needed).

HOW TO RUN:
    python 4_load_to_sql.py
"""

import sqlite3
import pandas as pd

# ---- Step 1: Read the cleaned CSV data ----
df = pd.read_csv("data/clean_jobs.csv")

# ---- Step 2: Connect to (or create) the SQLite database file ----
conn = sqlite3.connect("data/jobs.db")

# ---- Step 3: Write the dataframe into a table called "jobs" ----
# if_exists="replace" means: if the table already exists, overwrite it
df.to_sql("jobs", conn, if_exists="replace", index=False)

conn.close()

print(f"Loaded {len(df)} rows into data/jobs.db (table: jobs)")

"""
5_run_queries.py
------------------
Runs each SQL query from queries.sql against data/jobs.db and saves the
result of each one as a CSV file inside data/results/.

These CSV files are what you would import into Power BI to build the
dashboard (File -> Get Data -> Text/CSV).

HOW TO RUN:
    python 5_run_queries.py
"""

import sqlite3
import pandas as pd
import os

conn = sqlite3.connect("data/jobs.db")
os.makedirs("data/results", exist_ok=True)

# Each query written out here (same as in queries.sql), with a name for
# the output file it should be saved as.
queries = {
    "avg_salary_by_title": """
        SELECT title, AVG(salary_avg) AS avg_salary, COUNT(*) AS num_postings
        FROM jobs
        GROUP BY title
        ORDER BY avg_salary DESC;
    """,
    "avg_salary_by_experience": """
        SELECT experience_level, AVG(salary_avg) AS avg_salary
        FROM jobs
        GROUP BY experience_level;
    """,
    "postings_by_city": """
        SELECT city, COUNT(*) AS num_postings, AVG(salary_avg) AS avg_salary
        FROM jobs
        GROUP BY city
        ORDER BY num_postings DESC;
    """,
    "postings_by_platform": """
        SELECT source_platform, COUNT(*) AS num_postings
        FROM jobs
        GROUP BY source_platform
        ORDER BY num_postings DESC;
    """,
    "top_10_highest_paying": """
        SELECT title, city, salary_avg
        FROM jobs
        ORDER BY salary_avg DESC
        LIMIT 10;
    """,
    "postings_by_employment_type": """
        SELECT employment_type, AVG(salary_avg) AS avg_salary, COUNT(*) AS num_postings
        FROM jobs
        GROUP BY employment_type;
    """,
}

for name, query in queries.items():
    result = pd.read_sql(query, conn)
    out_path = f"data/results/{name}.csv"
    result.to_csv(out_path, index=False)
    print(f"{name:<30} -> {len(result)} rows -> {out_path}")

conn.close()

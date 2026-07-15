# Job Market Analytics Platform

A mini data-analytics project: scrape job postings, clean them with Pandas,
analyze them with SQL, and visualize the results in an interactive
dashboard (with instructions to rebuild the same charts in Power BI).

**Tech used:** Python (Requests, BeautifulSoup, Pandas), SQL (SQLite),
Power BI

## What this project does

1. **Scrapes job postings** from an HTML page using `requests` +
   `BeautifulSoup` (Steps 1)
2. **Builds a larger dataset** of ~2,000 postings to have enough data to
   analyze (Step 2 — see note below on why)
3. **Cleans the data** with Pandas — removes duplicates, fixes missing
   values, adds an average-salary column (Step 3)
4. **Loads it into a SQL database** (SQLite) (Step 4)
5. **Runs SQL queries** to find salary trends, top locations, etc. (Step 5)
6. **Analyzes skill demand** with Pandas (Step 6)
7. **Displays everything on a dashboard** you can open in your browser, or
   rebuild in Power BI

## Why Step 2 exists (important — good to explain in your report/viva)

Real job sites (LinkedIn, Naukri, Indeed) block automated scrapers and
require login, and scraping them can break their Terms of Service. So this
project scrapes a **sample local HTML page** (`sample_page.html`) to show
the scraping technique works correctly (Step 1), and then uses
`2_generate_dataset.py` to generate a larger, realistic dataset in the
exact same format, so the rest of the pipeline (cleaning, SQL analysis,
dashboard) has enough data to actually be useful. This is a common and
honest approach for student projects — you can say in your report:
*"the scraper works and is demonstrated on a sample page; the full
analysis dataset was generated to simulate scraping at scale."*

If you get access to a real dataset later (e.g. from Kaggle, or an API
like Adzuna/USAJobs), you can just replace `data/raw_jobs.csv` with it —
as long as the column names match, everything downstream still works.

## Folder structure

```
job-analytics-student/
├── 1_scrape_jobs.py        # scrapes sample_page.html using BeautifulSoup
├── sample_page.html         # sample job listings page used for scraping demo
├── 2_generate_dataset.py    # builds the full ~2000-row dataset
├── 3_clean_data.py          # cleans data with Pandas
├── 4_load_to_sql.py         # loads clean data into a SQLite database
├── 5_run_queries.py         # runs SQL queries, saves results as CSV
├── 6_skill_demand.py        # counts skill demand using Pandas
├── queries.sql              # the raw SQL queries (readable on their own)
├── data/
│   ├── raw_jobs.csv          # generated dataset
│   ├── clean_jobs.csv        # cleaned dataset
│   ├── jobs.db                # SQLite database
│   └── results/                # CSV outputs of each SQL query
└── dashboard/
    ├── dashboard.html         # interactive dashboard (open in browser)
    ├── jobs_data.js            # data used by the dashboard
    └── powerbi_guide.md        # how to build the same charts in Power BI
```

## How to run it (in order)

```bash
pip install requests beautifulsoup4 pandas

python 1_scrape_jobs.py
python 2_generate_dataset.py
python 3_clean_data.py
python 4_load_to_sql.py
python 5_run_queries.py
python 6_skill_demand.py
```

Then open `dashboard/dashboard.html` in your browser to see the results.

## What each SQL query answers

Open `queries.sql` to read them — they're short and use only basic SQL
(`SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`, `AVG`, `COUNT`):

1. Average salary per job title
2. Average salary per experience level
3. Number of postings and average salary per city
4. Number of postings per platform
5. Top 10 highest-paying postings
6. How many postings need Python
7. Average salary per employment type

## Ideas to extend this project (good for a viva / report "future work" section)

- Replace the generated dataset with a real one from Kaggle
- Add more cities/roles/skills to `2_generate_dataset.py`
- Add a line chart of postings over time (add a `posted_date` column)
- Deploy the dashboard using GitHub Pages so it has a live link
- Turn `5_run_queries.py` into a Flask API that the dashboard calls live

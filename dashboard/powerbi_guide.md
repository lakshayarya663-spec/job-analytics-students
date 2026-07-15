# Building the Dashboard in Power BI

The files in `data/results/` (created by `5_run_queries.py`) and
`data/results/skill_demand.csv` (created by `6_skill_demand.py`) are plain
CSV files you can load straight into Power BI.

## Step 1: Load the data

1. Open Power BI Desktop
2. **Home → Get Data → Text/CSV**
3. Load each of these files:
   - `data/results/avg_salary_by_title.csv`
   - `data/results/avg_salary_by_experience.csv`
   - `data/results/postings_by_city.csv`
   - `data/results/postings_by_platform.csv`
   - `data/results/skill_demand.csv`

## Step 2: Build the visuals

| Visual | Fields |
|---|---|
| Bar chart | `avg_salary_by_title`: Axis = title, Value = avg_salary |
| Bar chart | `skill_demand`: Axis = skill, Value = num_postings (sort descending, keep top 10) |
| Column chart | `postings_by_city`: Axis = city, Value = num_postings |
| Pie/Donut chart | `avg_salary_by_experience`: Legend = experience_level, Value = avg_salary |
| Card visuals | Total postings, Average salary (use New Measure, see below) |

## Step 3: Add slicers (filters)

**Insert → Slicer**, then set the field to `title` (job role) or
`experience_level`. This lets you click a role and see all the charts
update — the same filtering behaviour as the `dashboard.html` preview
included in this project.

## Step 4: A couple of simple DAX measures

```dax
Total Postings = COUNTROWS(avg_salary_by_title)

Average Salary = AVERAGE(avg_salary_by_title[avg_salary])
```

## Step 5: Refreshing the data

Whenever you re-run the Python pipeline (`python 5_run_queries.py`), the
CSV files in `data/results/` get updated. In Power BI, click
**Home → Refresh** to pull in the latest numbers.

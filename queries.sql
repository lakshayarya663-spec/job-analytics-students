-- queries.sql
-- Basic SQL analysis queries for the jobs table.
-- Uses only simple SQL: SELECT, WHERE, GROUP BY, ORDER BY, AVG, COUNT.
-- You can run these directly in any SQLite tool (e.g. DB Browser for SQLite)
-- opened on data/jobs.db, or run 5_run_queries.py to run them all in Python.

-- 1. Average salary for each job title
SELECT title, AVG(salary_avg) AS avg_salary, COUNT(*) AS num_postings
FROM jobs
GROUP BY title
ORDER BY avg_salary DESC;

-- 2. Average salary for each experience level
SELECT experience_level, AVG(salary_avg) AS avg_salary
FROM jobs
GROUP BY experience_level;

-- 3. Number of job postings in each city
SELECT city, COUNT(*) AS num_postings, AVG(salary_avg) AS avg_salary
FROM jobs
GROUP BY city
ORDER BY num_postings DESC;

-- 4. Number of postings on each platform (LinkedIn, Naukri, etc.)
SELECT source_platform, COUNT(*) AS num_postings
FROM jobs
GROUP BY source_platform
ORDER BY num_postings DESC;

-- 5. Highest paying job postings (top 10)
SELECT title, city, salary_avg
FROM jobs
ORDER BY salary_avg DESC
LIMIT 10;

-- 6. How many jobs need Python (simple keyword search in the skills column)
SELECT COUNT(*) AS python_jobs
FROM jobs
WHERE skills LIKE '%Python%';

-- 7. Average salary by employment type
SELECT employment_type, AVG(salary_avg) AS avg_salary, COUNT(*) AS num_postings
FROM jobs
GROUP BY employment_type;

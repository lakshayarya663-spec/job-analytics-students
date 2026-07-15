"""
2_generate_dataset.py
----------------------
Creates a larger dataset of job postings (like scraping thousands of jobs
from multiple sites) so we have enough data to do real analysis and build
a dashboard.

A real project would scrape thousands of live job postings from many
sites. Since job sites block scrapers and this environment can't reach
the internet, this script generates realistic random job data instead --
same columns as the real scraper would produce.

HOW TO RUN:
    python 2_generate_dataset.py
"""

import random
import csv

random.seed(42)  # so results are the same every time we run this

job_titles = [
    "Data Analyst", "Data Scientist", "Data Engineer", "Software Engineer",
    "Web Developer", "Machine Learning Engineer", "Business Analyst",
    "Database Administrator", "Cloud Engineer", "QA Engineer",
]

# Skills that commonly go with each job title
skills_by_title = {
    "Data Analyst": ["SQL", "Excel", "Power BI", "Python", "Tableau"],
    "Data Scientist": ["Python", "SQL", "Machine Learning", "Statistics", "Pandas"],
    "Data Engineer": ["Python", "SQL", "ETL", "AWS", "Spark"],
    "Software Engineer": ["Java", "Python", "SQL", "Git", "React"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js"],
    "Machine Learning Engineer": ["Python", "TensorFlow", "PyTorch", "SQL", "AWS"],
    "Business Analyst": ["SQL", "Excel", "Power BI", "Communication", "Tableau"],
    "Database Administrator": ["SQL", "MySQL", "Backup & Recovery", "Linux", "Oracle"],
    "Cloud Engineer": ["AWS", "Azure", "Docker", "Kubernetes", "Python"],
    "QA Engineer": ["Selenium", "Manual Testing", "SQL", "Python", "Automation"],
}

experience_levels = ["Entry", "Mid", "Senior"]

cities = [
    "Bangalore", "Hyderabad", "Pune", "Mumbai", "Delhi",
    "Chennai", "Noida", "Gurgaon", "Kolkata", "Remote",
]

platforms = ["LinkedIn", "Naukri", "Indeed", "Glassdoor"]

employment_types = ["Full-time", "Internship", "Contract"]

# base salary range (in INR per year) for each experience level
salary_ranges = {
    "Entry": (300000, 600000),
    "Mid": (600000, 1200000),
    "Senior": (1200000, 2500000),
}

NUM_JOBS = 2000
rows = []

for job_id in range(1, NUM_JOBS + 1):
    title = random.choice(job_titles)
    experience = random.choice(experience_levels)
    city = random.choice(cities)
    platform = random.choice(platforms)
    employment_type = random.choice(employment_types)

    low, high = salary_ranges[experience]
    salary_min = random.randint(low, high - 100000)
    salary_max = salary_min + random.randint(50000, 300000)

    # pick 3 random skills for this job from the list that matches the title
    possible_skills = skills_by_title[title]
    num_skills = random.randint(2, len(possible_skills))
    job_skills = random.sample(possible_skills, num_skills)

    rows.append({
        "job_id": job_id,
        "title": title,
        "city": city,
        "experience_level": experience,
        "employment_type": employment_type,
        "salary_min": salary_min,
        "salary_max": salary_max,
        "skills": ", ".join(job_skills),   # stored as a simple comma-separated string
        "source_platform": platform,
    })

with open("data/raw_jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated {NUM_JOBS} job postings -> data/raw_jobs.csv")

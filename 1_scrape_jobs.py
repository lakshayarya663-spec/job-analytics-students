"""
1_scrape_jobs.py
----------------
Basic web scraper for job postings using Requests + BeautifulSoup.

This scrapes a sample job-listing HTML page and saves the jobs to a CSV
file. It's written step-by-step (no classes) so it's easy to read and
explain.

HOW TO RUN:
    python 1_scrape_jobs.py

WHY A SAMPLE PAGE?
Real job sites like LinkedIn/Indeed/Naukri block scrapers and require
login, and scraping them can violate their Terms of Service. So this
script scrapes a local sample_page.html file that has the same kind of
HTML structure a real job listing page would have. If you point this
same code at a real static webpage's URL (using requests.get(url)
instead of reading the local file), the scraping logic works the same
way.
"""

import requests
from bs4 import BeautifulSoup
import csv

# ---- Step 1: Get the HTML ----
# For a real website you would do:
#   response = requests.get("https://example.com/jobs")
#   html = response.text
# Here we read a saved sample page instead (see explanation above).

with open("sample_page.html", "r", encoding="utf-8") as f:
    html = f.read()

# ---- Step 2: Parse the HTML with BeautifulSoup ----
soup = BeautifulSoup(html, "html.parser")

# Each job posting is inside a <div class="job-card"> on the sample page
job_cards = soup.find_all("div", class_="job-card")

print(f"Found {len(job_cards)} job postings on the page.")

# ---- Step 3: Pull out the fields we need from each job card ----
jobs_list = []

for card in job_cards:
    title = card.find("h2", class_="job-title").get_text(strip=True)
    company = card.find("span", class_="company-name").get_text(strip=True)
    location = card.find("span", class_="job-location").get_text(strip=True)
    salary = card.find("span", class_="salary-range").get_text(strip=True)
    experience = card.find("span", class_="experience-level").get_text(strip=True)
    description = card.find("div", class_="job-description").get_text(strip=True)

    jobs_list.append({
        "title": title,
        "company": company,
        "location": location,
        "salary_range": salary,
        "experience_level": experience,
        "description": description,
    })

# ---- Step 4: Save the results to a CSV file ----
with open("scraped_jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=jobs_list[0].keys())
    writer.writeheader()
    writer.writerows(jobs_list)

print("Saved scraped_jobs.csv")

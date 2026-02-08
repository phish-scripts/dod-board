# phish.dev
'''
-------------------------------------------------------
this is a driver that runs both 
the scrapedJobDetails and getJobs scripts,
while also making sure the jobs 
being put into the database aren't duplicates/already in the database
---------------------------------------------------------
'''


import os
from dotenv import load_dotenv
load_dotenv()

from getJobs import getJobLinks
from scrapedJobDetails import job_details

from supabase_client import supabase_client

print("Executing driver script...")

def main(supabase_client, scrape_limit):
    keywords = ["Software"]

    for keyword in keywords:
        print("-----------------------------------------------------------")
        print(f"Starting Data Pipeline for: {keyword}")

        print("Fetching job links...")
        new_links = getJobLinks(keyword, supabase_client, scrape_limit)
        print("Finished fetching job links...")

        print(" ")
        print("Scraping job links....")
        scraped_jobs = job_details(new_links)
        print("finished scraping job links!")

        if scraped_jobs:
            try:
                jobs_upserted = supabase_client.table("usa_jobs").upsert(scraped_jobs).execute()
                print(f"Uploaded {jobs_upserted} to supabase!")
                print("------------------------------------------------------")
            except Exception as error:
                print(f"Error upserting data to Supabase: {error}")
        print(f"Finished upserting data for keyword: {keyword}")
    

    print("Finished scraping for all keywords...")

    
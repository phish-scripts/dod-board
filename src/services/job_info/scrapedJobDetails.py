# phish.dev
# this program scrapes each link given from getJobs.py, the crawler


import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

from getJobs import getJobLinks

job_list = set()

job_list = getJobLinks("Software")

def job_details(job_list):
    # remove GUI, dont need an actual chrome tab open each time
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    job_details_list = []

    for job_link in job_list:
        try:
            print(f"getting details of {job_link}")
            driver.get(job_link)
            time.sleep(2)

            page = driver.page_source
            soup = BeautifulSoup(page, "html.parser")

            # salary
            salary = soup.find('dt', string=lambda text: "Salary" in text)
            if salary:
                salary_info = salary.find_next_sibling('dd').get_text(strip=True)

            # location
            location_container = soup.find(id="allLocations")
            if location_container:
                location_elements = location_container.find_all("div", class_="font-bold")
                location_list=[location.get_text(strip=True) for location in location_elements]
            
            # remote status
            remote = soup.find('dt', string=lambda text: "Remote job" in text)
            if remote:
                remote_status = remote.find_next_sibling('dd').get_text(strip=True)
            pay_scale = soup.find(id="joaPayGrade").get_text(strip=True)
        

            # returning this job_data
            job_data = {
                "link": job_link,
                "job_title": soup.find("h1").get_text(strip=True),
                "where": soup.find("div", class_="uppercase usajobs-joa-banner__dept").get_text(strip=True),
                "Salary": salary_info,
                "Location": location_list if location_list else "N/A",
                "Remote": remote_status,
                "Pay Scale & Grade": pay_scale
            }

            print(job_data)
            job_details_list.append(job_data)
        
    
        finally:
            driver.close()
        return job_details_list
        

result = job_details(job_list)
print(result)





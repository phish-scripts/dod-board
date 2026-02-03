# phish.dev
# this program scrapes each link given from getJobs.py, the crawler


import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import random

from selenium_stealth import stealth

from getJobs import getJobLinks

job_list = set()

job_list = getJobLinks("Software")

def job_details(job_list):
    # remove GUI, dont need an actual chrome tab open each time
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # Masking the automation flag in Chrome options
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=chrome_options)

    # Apply Stealth Settings
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    job_details_list = []

    for job_link in job_list:
        try:
            print(f"getting details of {job_link}")
            driver.get(job_link)
            time.sleep(random.uniform(3.5, 6.2))

            page = driver.page_source

            # lesson learned
            if "Access Denied" in page:
                print("Blocked from scraping. Darn.")
                break



            soup = BeautifulSoup(page, "html.parser")

            # salary
            salary = soup.find('dt', string=lambda text: "Salary" in text)
            if salary:
                salary_info = salary.find_next_sibling('dd').get_text(strip=True)
            time.sleep(random.uniform(3.5, 6.2))

            # location
            location_container = soup.find(id="allLocations")
            if location_container:
                location_elements = location_container.find_all("div", class_="font-bold")
                location_list=[location.get_text(strip=True) for location in location_elements]
            time.sleep(random.uniform(3.5, 6.2))
            
            # remote status
            remote = soup.find('dt', string=lambda text: "Remote job" in text)
            if remote:
                remote_status = remote.find_next_sibling('dd').get_text(strip=True)
            pay_scale = soup.find(id="joaPayGrade").get_text(strip=True)
            time.sleep(random.uniform(3.5, 6.2))
        

            # returning this job_data
            job_data = {
                "link": job_link,
                "job_title": soup.find("h1").get_text(strip=True),
                "where": soup.find("div", class_="uppercase usajobs-joa-banner__dept").get_text(strip=True),
                "Salary": salary_info if salary_info else "N/A",
                "Location": location_list if location_list else "N/A",
                "Remote": remote_status if remote_status else "N/A",
                "Pay Scale & Grade": pay_scale
            }
            time.sleep(random.uniform(3.5, 6.2))

            print(job_data)
            job_details_list.append(job_data)
        
    
        finally:
            driver.close()
        return job_details_list
        

result = job_details(job_list)
print(result)





# phish.dev
# this script scrapes each link given from getJobs.py, the crawler

'''
Selenium is used to open a chrome instance that will be scraped

'''


import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import random
from supabase_client import supabase_client

from selenium_stealth import stealth

from getJobs import getJobLinks

job_list = set()

stored_json_result = []

def job_details(job_list):
    # remove GUI, dont need an actual chrome tab open each time
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # Masking the automation flag in Chrome options
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=chrome_options)

    

    length_of_job_list = len(job_list)
    counter = 0

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
        print("-----------------------------")
        print(f"|       Job #{counter + 1}  |")
        print("----------------------------")
        print(f"getting details of {job_link}")
        driver.get(job_link)
        time.sleep(random.uniform(3.5, 6.2))

        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")

        # salary
        print(f"getting salary info")
        salary = soup.find('dt', string=lambda text: "Salary" in text)
        if salary:
            salary_info = salary.find_next_sibling('dd').get_text(strip=True)
            print(f"Salary Info found: {salary_info}")
            time.sleep(random.uniform(3.5, 6.2))

        # location
        location_container = soup.find(id="allLocations")
        if location_container:
            location_elements = location_container.find_all("div", class_="font-bold")
            location_list=[location.get_text(strip=True) for location in location_elements]
            print(f"Location Info found: {location_list}")
            time.sleep(random.uniform(3.5, 6.2))
            
            # remote status
            
        remote = soup.find('dt', string=lambda text: "Remote job" in text)
        remote_value = ""
        if remote:
            remote_status = remote.find_next_sibling('dd').get_text(strip=True) if remote else "N/A"
            # yes, i know im making alot of redudant checks, but this is just to be safe
            remote_value = remote_status if remote_status else "N/A"
            print(f"Remote Status found: {remote_value}")

            time.sleep(random.uniform(1.5, 3.2))


        pay_scale = soup.find(id="joaPayGrade").get_text(strip=True)
        print(f"Pay Scale found: {pay_scale}")
        time.sleep(random.uniform(3.5, 6.2))
        

        # returning this job_data
        job_data = {
            "job_link": job_link,
            "job_title": soup.find("h1").get_text(strip=True),
            "description": soup.find("div", class_="uppercase usajobs-joa-banner__dept").get_text(strip=True),
            "location": location_list if location_list else "N/A",
            "salary": salary_info if salary_info else "N/A",
            "remote_status": remote_value if remote_value else "N/A" ,
            "pay_scale_grade": pay_scale
        }
        time.sleep(random.uniform(3.5, 6.2))

        print(f"job data found: {job_data}")

        print("Success! Appending job data to job data...")
        job_details_list.append(job_data)

        counter += 1
        print(f"jobs scraped: {counter}")
        print("-----------------------------")
        print(" ")
        print(" ")
        
    
        if counter >= length_of_job_list:
            driver.close()
        
        json_job_list = json.dumps(job_details_list)
        stored_json_result.append(json_job_list)
    return job_details_list

def return_json(stored_json_result):
    print("fetching json...")
    return stored_json_result

# phish.dev
# this script uses selenium to open an instance of chrome, and scrapes the details on the chrome instance

import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium_stealth import stealth
import random

from selenium.webdriver.chrome.options import Options

# so there isnt a window thats opened each time
chrome_options = Options()
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(options=chrome_options)
 

ban_list = ["https://www.usajobs.govhttps://help.usajobs.gov/faq/job-announcement/remote"]


def getJobLinks(keyword):
    # change limit as needed
    page_number = 1
    limit = 5
    driver = webdriver.Chrome(options = chrome_options)

    # applying stealth so it doesn't get nailed
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    job_links = set()


    print("Fetching jobs...")
    try:
        while(len(job_links) < limit):
            # each loop, the link should change
            usaJobLink = f"https://www.usajobs.gov/Search/Results?k={keyword}&p={page_number}"
            driver.get(usaJobLink)
            time.sleep(2)
            print(f"scraping page {page_number}...")

            # slowing the crawling and scraping
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            time.sleep(random.uniform(2.5, 5.0))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            page = driver.page_source
            soup = BeautifulSoup(page, "html.parser")

            # collecting all 'a' elements (CALLING ALL AUTOBOTS)
            found_on_page = 0
            collected_a_elements = soup.find_all('a', href=True)
            for link in collected_a_elements:
                var_href = link['href']
                # checks to see if the link is actually a job link
                # kept scraping unrelated links
                if "/job" in var_href and 'closing-types' not in var_href and 'faq' not in var_href:
                    # making sure that this link doesnt sneak its way into job_links
                    if 'job-announcement/closing-types' not in var_href and var_href not in ban_list: 
                        # making sure if the URL needs to be cleaned
                        new_url = var_href if var_href.startswith('http') else "https://www.usajobs.gov" + var_href
                        print(f"job found: {new_url}")
                        # checking to make sure that the new url isnt already in job_links, but i think set() already does that?
                        if new_url not in job_links:
                            print(f"Putting {new_url} in job_links")
                            job_links.add(new_url)
                            found_on_page += 1
                    if len(job_links) >= limit:
                        break
            
            if found_on_page == 0:
                print("No more jobs found")
                break

            # advancing to next page, page number will be updated in the link    
            page_number += 1 
           
        print("finished fetching jobs...")
        return job_links
    
    finally:
        driver.quit()
    










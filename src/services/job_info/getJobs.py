# phish.dev
# this script uses selenium to open an instance of chrome, and scrapes the details on the chrome instance

import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

# so there isnt a window thats opened each time
chrome_options = Options()
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(options=chrome_options)
 
def getJobLinks(keyword):
    # change limit as needed
    usaJobLink = f"https://www.usajobs.gov/Search/Results?k={keyword}&p={page_number}"
    limit = 100
    driver = webdriver.Chrome()
    page_number = 1
    try:
        driver.get(usaJobLink)
        time.sleep(1)

        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")

        job_links = set()

        # collecting all 'a' elements (CALLING ALL AUTOBOTS)
        collected_a_elements = soup.find_all('a', href=True)
        for link in collected_a_elements:
            var_href = link['href']
            # checks to see if the link is actually a job link
            if "/job" in var_href:
                new_url = "https://www.usajobs.gov" + var_href
                print(f"job found: {new_url}")
                job_links.add(new_url)
            if (len(collected_a_elements) == 0): 
                page_number += 1
            else:
                collected_a_elements.pop(0)
            
            
            if len(job_links) >= limit:
                break

        return job_links
    
    finally:
        driver.quit()

    # scraping for all the 'a' elements, and then sees if theres an 'href'/link.
results = getJobLinks("Software")
print(results)






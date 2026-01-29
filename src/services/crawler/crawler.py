# phish.dev
# this is a 'crawler' made using beautiful soup 4, and requests. 

import requests

# formatting the url so we only need /jobs 
import re

from bs4 import BeautifulSoup

# test target url
target_url = "https://www.usajobs.gov/search/results/?k=Software"
pattern = re.compile(r"/job/")

# simply so this script doesn't get blocked as a bot. 
header = {
    'User-Agent' : "Moxilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url_list = [target_url]

job_data = []

max_crawl = 20


def get_detail(soup, label_text):
    label = soup.find('dt', string=lambda t: t and label_text in t)
    if label: 
        return label.find_next_sibling('dd').get_text(strip=True)      
    return "N/A"


def crawl():

    count = 0
    while url_list and count <= max_crawl:
        current_url = url_list.pop(0)

        # HTTP request for the target url. thats how we are crawling in the first place
        response = requests.get(current_url, headers = header)
        response.raise_for_status()

        # parsing the HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # collecting all the links
        link_elements = soup.select("a[href]")
        for link_element in link_elements:
            url = link_element["href"]

            # converting to links to url
            if not url.startswith(('http://', 'https://')):
                #joining the current url with the target url, so that the link is turned into a URL
                absolute_url = requests.compat.urljoin(target_url, url)
            else:
                absolute_url = url

            # checking to see if the link has been visited
            if (absolute_url.startswith(target_url) and absolute_url not in url_list):
                # and if it hasnt been visited, add it to the url list  :D
                url_list.append(absolute_url)
        
        if pattern.search(current_url):
            # Going to pull job description, and put into variables? i have no idea, ill figure it out
            job_title = soup.find("h1").get_text(strip = True) if soup.find("h1") else "Unknown Title"

            loc_header = soup.find('div', string=lambda t: t and 'Location' in t)
            location = "Not Listed"
            if loc_header:
                 # Finding the specific text block near the icon
                target = loc_header.find_next('div', id='allLocations')
                if target:
                    location = target.get_text(strip=True)

            job = {
                "Summary": {
                    "Title": job_title,
                    "Salary": get_detail(soup, "Salary"),
                    "Grade": get_detail(soup, "Pay scale & grade")

                },
                "Details": {
                    "Location": location,
                    "Remote": get_detail(soup, "Remote Job")
                }
            }

            job_data.append(job)

                
        count += 1

    print(job_data)
    return job_data


crawl()

# phish.dev
# purpose of this script is to crawl for job links first

import re
import requests
from bs4 import BeautifulSoup


def crawl_for_jobs(url, keyword, headers, target=100):
    # preventing duplicates. wonder what the runtime is going to be lol
    job_links = set()
    page_number = 1

    while (len(job_links) <  target):
        query = { "k": keyword, "p": page_number}
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')

        # scrapes ALL the links on the page (starting at 1)
        found_on_page = soup.find_all('a', href=re.compile(r'/GetJob/ViewDetails/'))

        # checks the found_on_page list for any links, and sees if they start with "/"
        for link in found_on_page:
            href = link.get("href")
            if (href.startswith('/')):
                href = "https://www.usajobs.gov" + href
            job_links.add(href)
            # making sure we dont exceed 100. Might increase count later
            if (len(job_links) >= target_count):
                break
        page_number += 1

    return list(job_links)






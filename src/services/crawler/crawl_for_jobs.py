# phish.dev
# purpose of this script is to crawl for job links first

import re
import requests
from bs4 import BeautifulSoup


def crawl_for_jobs(url, target=100):
    # preventing duplicates. wonder what the runtime is going to be lol
    job_links = set()
    page_number 


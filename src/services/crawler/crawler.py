import requests

def crawler():
    response = requests.get("https://www.usajobs.gov/search/results/?k=It%20Data%20Analyst&p=1")
    response.raise_for_status()
    print(response.text)

crawler()

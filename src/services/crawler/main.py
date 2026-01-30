from crawl_for_jobs import crawl_for_jobs
import time



search_url = " "
header = {
    'User-Agent' : "Moxilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

job_queue = crawl_for_jobs(search_url, target=50)

job_data = []

while (job_queue):
    url = job_queue.pop()
    print(url)
    time.sleep(1)
    


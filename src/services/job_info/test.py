from getJobs import getJobLinks
from scrapedJobDetails import job_details

result = job_details("software")


counter = 1
for job in result:
    print(f"--------------------------------------------------")
    print(f"Job #{counter}: {job}")
    print(f"--------------------------------------------------")
    print(" ")
    print(" ")
    counter += 1


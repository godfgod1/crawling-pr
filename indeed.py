import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://www.indeed.com/jobs?q=python&limit=${LIMIT}"

def extract_indeed_pages():
    result = requests.get(INDEED_URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', {'class': 'pagination'})

    # print(pagination)

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        # print(link.find('span', {'class': 'pn'}))
        pages.append(int(link.find('span').string))
    # pages = pages[:-1]
    max_page = pages[-1]
    return max_page


def extract_job(html):
    job_title = html.find("h2").string
    if html.find("a",{"class":'turnstileLink'})  is not None:
            company_anchor = html.find("a",{"class":'turnstileLink'})
            company = str(company_anchor.string)
    else:
        company = str(html.find('span',{'class':'companyName'}).string)
    company = company.strip()
    location = html.find('div',{'class':'companyLocation'}).string
    job_id = html["data-jk"]
    # print(job_id)
    return {'title': job_title,'company':company,'location':location,'link':f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"}

    

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        # print(f"&start={page*LIMIT}")
        print(f"Scrapping page {page}")

        result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
    # print(result.status_code)
        soup = BeautifulSoup(result.text,'html.parser')
        results = soup.find_all('a',{'class':'tapItem'})
        for result in results:
           job = extract_job(result)
           jobs.append(job)
    return jobs












from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file


# print(max_indeed_pages)

# print(max_page)
# print(range(max_page))
# for n in range(max_page):
#     print(n)
# for n in range(max_page):
#     print(f"start={n*50}")
# indeed_jobs
indeed_jobs = get_indeed_jobs()
# so_jobs = get_so_jobs()

# jobs = so_jobs + indeed_jobs
jobs =  indeed_jobs

save_to_file(jobs)


























 





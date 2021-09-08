from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_pages = extract_indeed_pages()

# print(max_indeed_pages)

# print(max_page)
# print(range(max_page))
# for n in range(max_page):
#     print(n)

# for n in range(max_page):
#     print(f"start={n*50}")


indeed_jobs = extract_indeed_jobs(last_indeed_pages)

# indeed_jobs
print(indeed_jobs)


 
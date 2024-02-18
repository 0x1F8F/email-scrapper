from linkedin_scraper import Person,JobSearch,actions,Job
# import scrapy
# import regex as rg
# import requests as rq
import selenium
import dotenv


driver = webdriver.Chrome()

env = dotenv.load_dotenv("./secrets/.env")
email = env.get('EMAIL')
passwd = env.get('PASSWORD')

actions.login(driver, email=email,password=passwd)

job_search_provider = JobSearch(driver=driver, close_on_complete=False, scrape=False)
job_list: list[Job] = job_search_provider.search("UI/UX Engineer")

for job in job_list:
    print(job.company,job.job_title,job.job_description, sep="\n")
    print("-"*50)


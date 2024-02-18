import scrapy
import requests

class WebSpyder(scrapy.Spider):
    name = 'Web crawler'
    start_url = [ 'https://www.linkedin.com' ]
    def start_requests(self):
        self.session = requests

    def parse(self,request):
        pass

class EmailSpyder(scrapy.Spider):
    name = 'Email crawler'
    # TODO: fix
    pass


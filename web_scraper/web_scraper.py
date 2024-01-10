import requests
from duckduckgo_search import DDGS,exceptions
from bs4 import BeautifulSoup
from urllib.error import URLError,HTTPError
from fastapi import FastAPI, Request
import uvicorn
class web_scraper():
    def __init__(self,input_txt):
        self.input_txt = input_txt

    def extract_url_text(self):
        try:
            search_class = DDGS()
            search_query = f"system requirements for {self.input_txt} Processor (CPU)"
            print(search_query)
            results = list(search_class.text(search_query,safesearch='off',max_results=4))
            if results:
                self.url = results[0]["href"]
                print(self.url)
                self.filter_html()
            return self.filter_html()
        except exceptions as e:
                print(e.__str__())

    def filter_html(self):
        try:
            if self.url.startswith("http"):
                response = requests.get(self.url)
                html_content = response.text
                soup = BeautifulSoup(html_content, 'html.parser')
                selected_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'span', 'a', 'strong', 'em', 'ul', 'ol', 'li']
                selected_tags_content = soup.find_all(selected_tags)
                extracted_text = [tag.get_text(strip=True) for tag in selected_tags_content]
                text_content = list(set(extracted_text))
                return text_content
        except (URLError,HTTPError) as e:
                print(e.__str__())
class web_scraper_restapi():
    def __init__(self):
        description = """ Web Scraper API 🚀
        \n **Prerequisites**
        \n Python 3.9 - 3.10
        
        \n **Firewall rule**
        \n You need to open TCP port 2222 in your firewall in order to reach the API
         """
        tags_metadata = [
            {
                "name": "/power_on",
                "description": """Command to Power on in normal operating condition the host and the power supply using following protocols order: **IOT** - **WOL** - **IPMI** 
                \n**Note** To be used when the power supply of the host is completely off"""

            },]

        self.restAPIApp = FastAPI(
            title="Web Scraper API",
            description=description,
            version="0.0.1",
            terms_of_service="http://example.com/terms/",
            openapi_tags=tags_metadata,
            ssl_certfile="./ssl_certs/self.cert",
            ssl_keyfile="./ssl_certs/self-ssl.key",
            contact={
                "name": "Elemento",
                "url": "https://www.elemento.cloud/#contact-form",
                "email": "hello@elemento.cloud"},
            )
    # Execute RESTApi

    def run(self):
        @self.restAPIApp.get('/requirements')
        def get_application_name(application_name: str):
            try:
                if application_name is not None:
                    exec = web_scraper(application_name)
                    file_content = exec.extract_url_text()
            finally:
                return file_content   

        return self.restAPIApp

exec = web_scraper_restapi()
app = exec.run()

if __name__ == "__main__":
    uvicorn.run('web_scraper:app', host="0.0.0.0", port=1113, reload=True)
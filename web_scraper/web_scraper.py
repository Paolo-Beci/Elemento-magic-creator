import uvicorn
from duckduckgo_search import DDGS
from duckduckgo_search.exceptions import DuckDuckGoSearchException
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError
from fastapi import FastAPI
from playwright.sync_api import sync_playwright, TimeoutError


class web_scraper():
    def __init__(self, input_txt):
        self.input_txt = input_txt

    def extract_url_text(self):
        try:
            search_class = DDGS()
            search_query = "'"+self.input_txt+"'" + \
                "minimum recommended system requirements -forum -medium -troubleshooting"
            results = list(search_class.text(
                search_query, safesearch='off', backend="html", max_results=4))
            if results:
                self.url = results[0]["href"]
                print("url path retrieved " + self.url)
                self.filter_html()
            return self.filter_html()
        except DuckDuckGoSearchException as e:
            print(f"Duck Duck go search error occurred during search: {e}")
        except (Exception) as e:
            print(e.__str__())

    def filter_html(self):
        try:
            if self.url.startswith("http"):
                try:
                    with sync_playwright() as p:
                        browser = p.firefox.launch(headless=True)
                        context = browser.new_context(ignore_https_errors=True)
                        page = context.new_page()
                        page.goto(self.url, timeout=30000)
                        html_content = page.content()
                        browser.close()
                except TimeoutError as e:
                    print(f"Timeout error occurred during rendering: {e}")
                except KeyboardInterrupt:
                    print("Process interrupted")
                except Exception as e:
                    print(f"An general occurred during rendering: {e}")
                    return None
                soup = BeautifulSoup(html_content, 'html.parser')
                selected_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                                 'div', 'span', 'a', 'strong', 'em', 'ul', 'ol', 'li']
                selected_tags_content = soup.find_all(selected_tags)
                extracted_text = [tag.get_text(strip=True)
                                  for tag in selected_tags_content]
                text_content = list(set(extracted_text))
                return text_content
        except (URLError, HTTPError) as e:
            print(e.__str__())


class web_scraper_restapi():
    def __init__(self):
        description = """ Web Scraper API 🚀
        \n **Prerequisites**
        \n Python 3.9 - 3.10
        
        \n **Firewall rule**
        \n You need to open TCP port 1113 in your firewall in order to reach the API
         """
        tags_metadata = [
            {
                "name": "/requirements",
                "description": "Get request to retrive based on the application name the system requirements"
            },]

        self.restAPIApp = FastAPI(
            title="Web Scraper API",
            description=description,
            version="0.0.1",
            terms_of_service="",
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
            if application_name is not None:
                exec = web_scraper(application_name)
                file_content = exec.extract_url_text()
                return file_content

        return self.restAPIApp


exec = web_scraper_restapi()
app = exec.run()

if __name__ == "__main__":
    uvicorn.run('web_scraper:app', host="0.0.0.0", port=1113, reload=True)

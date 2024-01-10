import requests
from duckduckgo_search import DDGS,exceptions
from bs4 import BeautifulSoup
from urllib.error import URLError,HTTPError
class web_scraper():
    def __init__(self,input_txt):
        self.input_txt = input_txt

    def extract_url(self):
        try:
            search_class = DDGS()
            search_query = f"system requirements for {self.input_txt} Processor (CPU)"
            results = list(search_class.text(search_query,safesearch='off',max_results=4))
            if results:
                self.url = results[0]["href"]
                self.filter_html()
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
                text = list(set(extracted_text))
                print(text)
        except (URLError,HTTPError) as e:
                print(e.__str__())

if __name__ == "__main__":
    search1 = web_scraper('google chrome')
    search1.extract_url()


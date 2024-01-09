from duckduckgo_search import DDGS

class web_scraper():
    def __init__(self,input_txt):
        self.input_txt = input_txt

    def extract_url(self):
        try:
            search = DDGS()
            search_query = f"{self.input_txt} requirements"
            results = list(search.text(search_query,max_results=4))
            #print(results)
            if results:
                print(results[0]["href"])
        except Exception as e:
                print(f"Error during DuckDuckGo search: {e}")
        return None

if __name__ == "__main__":
    search1 = web_scraper('software requirements vmware player')
    search1.extract_url()


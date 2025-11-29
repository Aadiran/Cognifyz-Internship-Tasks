import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    print(f"Scraping quotes from {url}...\n")
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Check for HTTP errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        quotes = soup.find_all('div', class_='quote')
        
        if not quotes:
            print("No quotes found.")
            return

        for i, quote in enumerate(quotes, 1):
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            
            print(f"Quote {i}:")
            print(f"\"{text}\"")
            print(f"- {author}")
            print("-" * 40)
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_quotes()

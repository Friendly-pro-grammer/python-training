import requests
from bs4 import BeautifulSoup


def scrape_quotes_website():
    url = "https://quotes.toscrape.com/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for item in quotes:
        text = item.find("span", class_="text").text
        author = item.find("small", class_="author").text

        tags_elements = item.select("div.tags a.tag")
        tags = [tag.text for tag in tags_elements]

        print(f"Quote:  {text}")
        print(f"Author: {author}")
        print(f"Tags:   {', '.join(tags)}")
        print("-" * 40)


if __name__ == "__main__":
    scrape_quotes_website()

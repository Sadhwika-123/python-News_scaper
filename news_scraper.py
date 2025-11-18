import requests
from bs4 import BeautifulSoup
url = "https://www.bbc.com/news"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all("h2")

with open("headlines.txt", "w", encoding="utf-8") as file:
    for index, headline in enumerate(headlines, start=1):
        text = headline.get_text(strip=True)
        if text:    # Remove empty lines
            file.write(f"{index}. {text}\n")

print("Headlines scraped and saved to headlines.txt")

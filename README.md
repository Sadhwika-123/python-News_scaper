# 📰 Web Scraper for News Headlines  
### Python Developer Internship — Task 3

##  Objective  
Scrape top news headlines from a public news website using Python and save them into a `.txt` file.

---

##  Tools Used  
- Python  
- requests  
- BeautifulSoup (bs4)  
- File Handling  

---

##  Project Files  
- news_scraper.py — Python script for scraping  
- headlines.txt — Output file containing scraped headlines  
- **README.md — Project documentation  

---

##  How It Works  
1. Sends a GET request to the BBC News website  
2. Parses HTML using BeautifulSoup  
3. Extracts all `<h2>` tags (headline elements)  
4. Saves cleaned headlines into `headlines.txt`  

---

##  Python Script (news_scraper.py)

```python
import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://www.bbc.com/news"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all("h2")

        with open("headlines.txt", "w", encoding="utf-8") as f:
            for i, h in enumerate(headlines, 1):
                title = h.get_text(strip=True)
                if title:
                    f.write(f"{i}. {title}\n")

        print("Headlines scraped and saved to headlines.txt")

    except Exception as e:
        print("Error:", e)

scrape_headlines()


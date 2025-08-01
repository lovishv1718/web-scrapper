import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = "https://www.hindustantimes.com/"

# Headless browser setup
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--window-size=1920,1080")

# Start browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

print("🚀 Launching browser and opening Hindustan Times...")
driver.get(url)
time.sleep(6)  # wait for JS to load
print("✅ Page loaded. Parsing content...")

# Get page source
page_source = driver.page_source
driver.quit()

# Parse HTML
soup = BeautifulSoup(page_source, "html.parser")

# Write to CSV
headlines_found = 0
seen = set()

with open("headlines1.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Headline", "Link"])

    for tag in soup.select("h1 a, h2 a, h3 a, h4 a"):
        headline = tag.get_text(strip=True)
        link = tag.get("href")

        if headline and link and len(headline) > 15 and "don't miss" not in headline.lower():
            if not link.startswith("http"):
                link = "https://www.hindustantimes.com" + link
            if headline not in seen:
                seen.add(headline)
                writer.writerow([headline, link])
                headlines_found += 1

print(f"💾 Saved {headlines_found} clean headlines to headlines.csv ✅")

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 19:28:07 2025

@author: NIKITA
"""

import requests
from bs4 import BeautifulSoup
import csv

# Target website (example: BBC News homepage)
URL = "https://masterblogging.com/best-travel-blogs"

try:
    # Step 1: Fetch the webpage
    response = requests.get(URL, timeout=10)
    response.raise_for_status()  # Raise error if request fails

    # Step 2: Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Extract specific data (headlines)
    headlines = []
    for h in soup.find_all("a", class_="w_tle"):
       text = h.get_text(strip=True)
    link = h["href"]
    headlines.append([text, link])

    # Step 4: Save to CSV
    with open("headlines.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Headline"])  # Header row
        for headline in headlines:
            writer.writerow([headline])

    print(f"✅ Scraped {len(headlines)} headlines and saved to headlines.csv")

except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching webpage: {e}")
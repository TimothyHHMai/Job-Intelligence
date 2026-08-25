from bs4 import BeautifulSoup
import json
from playwright.sync_api import sync_playwright, Playwright 
import hashlib
import os

with open('apple_job_links.json', 'r', encoding='utf-8') as f:
    links = json.load(f)

def run(playwright: Playwright, link_list):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    
    for link in link_list:
        print(link)
        hash_obj = hashlib.sha256(link.encode("utf-8"))
        hex = hash_obj.hexdigest()

        html_link_path = "apple_job_html"
        scraped_links = os.listdir(html_link_path)

        if f"{hex}.html" in scraped_links:
            print("Already scraped")
            continue
        
        try:
            page.goto(
                link,
                wait_until="domcontentloaded",
                timeout=60000
            )
            page.wait_for_load_state("networkidle")

            content = page.content()
        except Exception as e:
            print("Error: ", e)
            continue

        os.makedirs("./apple_job_html", exist_ok=True)
        path = f"./apple_job_html/{hex}.html"
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    browser.close()

with sync_playwright() as playwright:

    with open('apple_job_links.json', 'r', encoding='utf-8') as f:
        links = json.load(f)

    run(playwright, links)   

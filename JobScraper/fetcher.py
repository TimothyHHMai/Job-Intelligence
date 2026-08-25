from playwright.sync_api import sync_playwright, Playwright
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json


def get_domain(string):
    domain = urlparse(string)
    return f"{domain.scheme}://{domain.netloc}"

'''
Get links from HTML pages
'''
def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')

    linked_list = []
    for l in soup.find_all('a', class_='link-inline'):
        linked_list.append(l.get('href'))

    return linked_list


def run(playwright: Playwright, base):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    link_list = []
    for n in range(1,304):
        url = f"{base}?page={n}"
        print(n, ": ", url)

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
            )
        content = page.content()

        domain = get_domain(base)
        
        for dom in get_links(content):
            print(f"{domain}{dom}")
            link_list.append(f"{domain}{dom}")

    with open("apple_job_links.json", "w", encoding="utf-8") as f:
        json.dump(link_list, f, indent=2)

    page.close()
    browser.close()
    return link_list


with sync_playwright() as playwright:
    links = run(playwright, "https://jobs.apple.com/en-us/search")   
    print(links) 
    





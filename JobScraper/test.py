from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

SEARCH_URL = "https://jobs.apple.com/en-us/search"

def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')

    linked_list = []
    for l in soup.find_all('a', class_='link-inline'):
        linked_list.append(l.get('href'))

    return linked_list


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        locale="en-US",
    )

    page = context.new_page()

    page.goto(
        SEARCH_URL,
        wait_until="domcontentloaded",
        timeout=60000
    )

    link_list = []
    base = "https://jobs.apple.com/en-us/search"
    for dom in get_links(page.content()):
        link_list.append(f"{base}{dom}")

    page.goto(link_list[0])

    page.wait_for_timeout(5000)

    print("URL:", page.url)
    print("TITLE:", page.title())

    page.screenshot(
        path="apple_search.png",
        full_page=True
    )

    input("Inspect the page, then press Enter...")

    browser.close()
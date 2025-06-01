from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import textstat
import time

ARTICLE_DIV_CLASS = "article-body"

def fetch_article_content(url: str) -> str:
    """Use Selenium to load and extract MoEngage article text."""
    options = Options()
    options.headless = True
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920x1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    try:
        driver.get(url)
        time.sleep(3)  # wait for JS to load content
        html = driver.page_source
    finally:
        driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    content = soup.find("div", {"class": ARTICLE_DIV_CLASS})
    if content is None:
        content = soup

    return content.get_text(separator="\n", strip=True)

def analyze_readability(text: str) -> dict:
    grade = textstat.flesch_kincaid_grade(text)
    verdict = (
        "Easy for a non-technical marketer."
        if grade <= 8
        else "May feel dense for a non-technical marketer."
    )
    return {"grade_level": grade, "verdict": verdict}

def analyze_structure(text: str) -> dict:
    headings = text.count("\n#") + text.count("\n##")
    paragraphs = len([p for p in text.split("\n\n") if p.strip()])
    bullets = text.count("- ") + text.count("* ")
    summary = (
        "Good use of lists and sub-headings."
        if bullets >= 2 and headings >= 2
        else "Could benefit from more lists or clear sub-headings."
    )
    return {
        "headings": headings,
        "paragraphs": paragraphs,
        "bullets": bullets,
        "summary": summary,
    }

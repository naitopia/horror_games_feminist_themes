import requests
from bs4 import BeautifulSoup
import wikipediaapi
from urllib.parse import quote

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://en.wikipedia.org/"
}

wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="HorrorGamesFeministThemesDataset/1.0 (contact: nbutt@gradcenter.cuny.edu)"
)

def title_to_url(title: str) -> str:
    return f"https://en.wikipedia.org/wiki/{quote(title.replace(' ', '_'))}"

def get_full_page_text_from_url(url: str) -> str:
    if not url or not isinstance(url, str):
        return ""

    resp = requests.get(url, headers=HEADERS)
    if resp.status_code != 200:
        print("Failed to fetch:", url)
        return ""

    soup = BeautifulSoup(resp.text, "lxml")

    # remove tables
    for t in soup.find_all("table"):
        t.decompose()

    # remove citations
    for s in soup.find_all("sup"):
        s.decompose()

    paragraphs = soup.find_all("p")
    return " ".join(p.get_text(" ", strip=True) for p in paragraphs)

def get_horror_games_with_subgenres():
    root = wiki.page("Category:Horror_video_games")
    visited = set()
    games = {}

    def crawl(cat, subgenre=None):
        if cat.title in visited:
            return
        visited.add(cat.title)

        for item in cat.categorymembers.values():

            if item.ns == wikipediaapi.Namespace.CATEGORY:
                crawl(item, item.title.replace("Category:", ""))

            elif item.ns == wikipediaapi.Namespace.MAIN:
                if item.title not in games:
                    games[item.title] = {"page": item, "subgenres": set()}
                if subgenre:
                    games[item.title]["subgenres"].add(subgenre)

    crawl(root)
    return games

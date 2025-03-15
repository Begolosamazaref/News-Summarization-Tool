import requests
import json
import config


class NewsRetriever:
    BASE_URL = "https://newsapi.org/v2/everything"

    def __init__(self):
        self.api_key = config.NEWS_API_KEY

    def fetch_articles(self, topic, page_size=5):
        """Fetches news articles for a given topic."""
        params = {
            "q": topic,
            "apiKey": self.api_key,
            "language": "en",
            "pageSize": page_size,
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        if data.get("status") != "ok":
            print("Error fetching news:", data.get("message"))
            return []

        return data.get("articles", [])


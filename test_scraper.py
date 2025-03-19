from utils import fetch_news

company = "Tesla"
news = fetch_news(company)
for article in news:
    print(article)

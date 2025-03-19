import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

def fetch_news(company_name):
    """Fetches top news articles related to a company"""
    search_url = f"https://www.bing.com/news/search?q={company_name}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for item in soup.find_all("a", {"class": "title"})[:10]:  # Get top 10 articles
        title = item.text.strip()
        link = item['href']
        
        # Fetch full article text
        article_text = get_article_text(link)

        # Perform Sentiment Analysis
        sentiment = analyze_sentiment(article_text)

        articles.append({
            "title": title,
            "link": link,
            "sentiment": sentiment
        })
    
    return articles

def get_article_text(url):
    """Extracts article content from a given URL (basic version)"""
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        article_text = " ".join([p.text for p in paragraphs])
        return article_text if article_text else "Content not available"
    except Exception as e:
        return "Error fetching article"

def analyze_sentiment(text):
    """Performs sentiment analysis using TextBlob"""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

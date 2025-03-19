from utils import fetch_news
from text_to_speech import convert_text_to_speech

company = "Tesla"
news = fetch_news(company)

# Collect all news titles for translation and speech synthesis
all_titles = ""

for article in news:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Sentiment: {article['sentiment']}")
    print("-" * 80)

    # Add title to summary
    all_titles += article['title'] + ". "

# Convert translated news summary to Hindi speech
convert_text_to_speech(all_titles, "news_summary_hindi.mp3")

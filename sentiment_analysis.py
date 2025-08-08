from newspaper import Article
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

def get_news_sentiment(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h3")

    sentiments = []
    for h in headlines[:5]:
        try:
            article_url = "https://finance.yahoo.com" + h.find("a")["href"]
            article = Article(article_url)
            article.download()
            article.parse()
            article.nlp()
            analysis = TextBlob(article.summary)
            sentiments.append(analysis.sentiment.polarity)
        except:
            continue
    if sentiments:
        return sum(sentiments) / len(sentiments)
    return 0

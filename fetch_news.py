import logging
from GoogleNews import GoogleNews

# Set up logging to a file
logging.basicConfig(filename='news_output.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize GoogleNews and get news results
googlenews = GoogleNews(lang='en')
googlenews.get_news('APPLE')
news_results = googlenews.results()

# Log the news results
for article in news_results:
    logging.info("Title: %s", article.get("title"))
    logging.info("Date: %s", article.get("date"))
    logging.info("Description: %s", article.get("desc"))
    logging.info("Link: %s\n", article.get("link"))

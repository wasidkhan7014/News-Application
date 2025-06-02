
##### Flask NEWS Application Using Newsapi  #####

from flask import Flask, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)

# Initialize the News API with your API key
newsapi = NewsApiClient(api_key='70fdb9ba81ba40b6bda148e672898bd9')

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        
        # First request to get totalResults
        related_news = newsapi.get_everything(
            q=keyword,
            language='en',
            sort_by='relevancy'
        )
        
        # Limit articles to 100 maximum
        no_of_articles = min(related_news['totalResults'], 100)
        
        # Second request to fetch the actual articles
        all_articles = newsapi.get_everything(
            q=keyword,
            language='en',
            sort_by='relevancy',
            page_size=no_of_articles
        )['articles']
        
        return render_template("home.html", all_articles=all_articles, keyword=keyword)
    
    else:
        # GET method - fetch top headlines
        top_headlines = newsapi.get_top_headlines(country="in", language="en")
        total_results = min(top_headlines['totalResults'], 100)
        
        all_headlines = newsapi.get_top_headlines(
            country="in",
            language="en",
            page_size=total_results
        )['articles']
        
        return render_template("home.html", all_headlines=all_headlines)

if __name__ == "__main__":
    app.run(debug=True)

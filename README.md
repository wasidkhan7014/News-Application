# News-Application

In this article, we will make a News Web App using Flask and NewsAPI.
The app will show top news headlines and have a search bar. When a user types something and searches, the app will show news articles related to that topic (up to 100 results).
We will build a simple and clean design using HTML and Bootstrap.
You can use any code editor you like, such as VS Code or Sublime Text.



Flask and NewsAPI Introduction

Flask: Flask is a Python tool that helps you build websites and web apps. It allows you to create pages and handle user requests on the server.
If you want to learn more, check this link:


NewsAPI: News API is a simple Rest API for retrieving live articles from all over the web. Using News API we can fetch top headlines of a country from a particular source like the Times of India, Hindustan Times, BBC News, and many more. We can also fetch articles related to a particular topic. visit


API key generation
In order to use the News API in our application, we need to generate a unique API key from https://newsapi.org/. Visit this website and create your free account, on successful registration and email verification you will get your API key on the screen. While registering you may need to choose a developer plan (choose according to your requirements). Save this API key somewhere so that it can be used further.


Flask and NewsAPI installation
We will simply install Flask using the pip command :

pip install flask 

After successful installation creates one folder for application name this folder flask_news or anything else of your choice. Inside this folder create a new file called app.py. We will write our entire back-end code in this file in the upcoming steps.

To install NewsAPI we will use a pip command like this :

pip install newsapi-python


Creating backend endpoints
There are two things we want from our application :

Display top headlines when the web application is opened.
Show results based on a search query.

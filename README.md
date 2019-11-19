# news
An application that will help users to list and preview news articles from various sources.
## Built By [John Gichuhi](https://github.com/Leina33/News-Highlight.git/)
## Description
News is a web application that displays a list of various news sources like BBC and ABC. On choosing a news source, it will preview the top news articles of the day. Clicking a news article will redirect the user to read it fully from the news source. It achieves this by using the [News API](https://newsapi.org/).
You can view the site at: https://Leinanews.herokuapp.com
## User Stories
These are the behaviours/features that the application implements for use by a user.
As a user I would like to:
* See various news sources
* Select the ones they prefer
* See the top news articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source
## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click on view articles on a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click Read Article** | Redirected to the news source's site to read the entire article |
| Go back to news sources | **Click on news** | Redirected to the news source list |
## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
### Cloning
* In your terminal:
    $ git clone https://github.com/Leina33/News-Highlight.git
    $ cd news
## Running the Application
* Creating the virtual environment
    $ python3.6 -m venv --without-pip virtual
    $ source virtual/bin/env
* Installing Flask and other Modules
    $ python3.6 -m pip install Flask
    $ python3.6 -m pip install Flask-Bootstrap
    $ python3.6 -m pip install arrow
    $ python3.6 -m pip install requests
* Setting up the API Key
    To be able to gather article info from the News API you will need an API Key.
    * Visit https://newsapi.org/ and register for an API key.
    * Insert the API Key you received from News Api where <Your-Api-Key> is.
* To run the application, in your terminal:
    $ python3.6 run.py
## Testing the Application
* To run the tests for the class files:
    $ cd app
    $ python3.6 test_models.py
## Technologies Used
* Python3.6
* Flask
## License
MIT &copy;2019 [Dominic Rutto](https://github.com/Leina33/News-Highlight.git)
News API
News API - A JSON API for live news and blog articles
Search worldwide news articles and headlines from all over the web in real-time with our free News API.
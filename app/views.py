from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting technology news
    technology_news = get_news()
    # print(technology_news)
    title = 'Home - Welcome to The best News Highlight  Website Online'
    return render_template('index.html', title = title, technology = technology_news)

#dynamc routes
@app.route('/news/<int:id>')
def news(id):

    '''
    View news  page function that returns the news details page and its data
    '''
    return render_template('news.html',news =technology_news)


from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

#process results
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description= news_item.get('description')
        url = news_item.get('url')
        
        if id:
            news_object = News(id, name, description, url)
            news_results.append(news_object)
        
    return news_results


#views function

def get_articles(source_id):
  url = f'https://newsapi.org/v2/everything?sources={source_id}&apiKey={api_key}'
  url_datas = requests.get(url)
  article_dict = url_datas.json()
  articles_list = article_dict.get('articles')
  return process_articles(articles_list)

# #FUNCTION TO GET MOVIES
# def get_news(id):
#     # get_news_url = base_url.format(id,api_key)
#     get_news_details_url = base_url.format(id,api_key)
#     with urllib.request.urlopen(get_news_details_url) as url:
#         news_details_data = url.read()
#         news_details_response = json.loads(news_details_data)
        
#         news_object = None
#         if news_details_response:
#             id = news_item.get('id')
#             name = news_item.get('name')
#             description= news_item.get('description')
#             url = news_item.get('url')
            
            
#             news_object = News(id,name,description,url)
            
#     return news_object
            
            

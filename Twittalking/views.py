from django.http import HttpResponse, request
from django.template import Template, Context, loader
from django.shortcuts import render
from pymongo import MongoClient
from pprint import pprint
from .get_single_user_data import getdata
from .get_followers_list import get_followers_list
from .search_tweets import search_tweets


def dashboard_view(request):

    # client = MongoClient(host='localhost', port=27017)
    # db = client['twitterdata']
    # collection = db['usersdata']

    # collection.insert_one(getdata())

    # list_db_names = client.list_database_names()
    # list_db_collections = db.list_collection_names()

    data = getdata()._json
    # collection.insert_one(data)
    user_name = data['screen_name']
    location = data['location']
    followers_count = data['followers_count']
    followees_count = data['friends_count']
    favourites_count = data['favourites_count']
    statuses_count = data['statuses_count']
    actual_status = data['status']['text']

    followers_list = get_followers_list()

    with open(file='C:/Twittalking/templates/dashboard.html', mode='r') as f:
        dashboard_template = Template(f.read())

    # dashboard_context = Context({})

    dashboard_context = Context({"user_name": user_name, "location": location,
                                 "followers_count": followers_count, "followees_count": followees_count,
                                 "favourites_count": favourites_count, "statuses_count": statuses_count,
                                 "actual_status": actual_status, "followers_list": followers_list})

    dashboard_render = dashboard_template.render(dashboard_context)

    return HttpResponse(dashboard_render)




#     dashboard_template = loader.get_template('./index.html')
#     return render(request, dashboard_template, {})

def search_tweets_view(request):
    with open(file='C:/Twittalking/templates/search_tweets.html', mode='r') as f:
        dashboard_template = Template(f.read())
    if request.method == 'POST':
        words_to_search = request.POST(['search_tweet'])
        query_result = search_tweets(words_to_search)
        dashboard_context = Context({"user_name": query_result})
        dashboard_render = dashboard_template.render(dashboard_context)
    else:
        dashboard_context = Context({"user_name": ""})
        dashboard_render = dashboard_template.render(dashboard_context)

    return render(dashboard_render, dashboard_context)

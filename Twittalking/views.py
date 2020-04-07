from django.http import HttpResponse, request
from django.template import Template, Context, loader
from django.shortcuts import render
from pymongo import MongoClient
from pprint import pprint
from .get_single_user_data import getdata
from .get_followers_list import get_followers_list
from .search_tweets import search_tweets


def index(request):
    context = {}
    return render(request=request, template_name='index.html', context=context)

def single_user_data(request):
                        # client = MongoClient(host='localhost', port=27017)
                        # db = client['twitterdata']
                        # collection = db['usersdata']
                        # collection.insert_one(getdata())
                        # list_db_names = client.list_database_names()
                        # list_db_collections = db.list_collection_names()
    # user_data = getdata()._json
                        # collection.insert_one(user_data)
    # user_name = user_data['screen_name']
    # location = user_data['location']
    # followers_count = user_data['followers_count']
    # followees_count = user_data['friends_count']
    # favourites_count = user_data['favourites_count']
    # statuses_count = user_data['statuses_count']
    # actual_status = user_data['status']['text']
    # followers_list = get_followers_list()
    # context = {"user_name": user_name, "location": location, "followers_count": followers_count,
    #            "followees_count": followees_count, "favourites_count": favourites_count,
    #            "statuses_count": statuses_count, "actual_status": actual_status,
    #            "followers_list": followers_list}
    return render(request=request, template_name='single_user_data.html', context={})


def search_tweets(request):
    if request.POST:
        print('Se ha hecho click en el botón <Buscar tweets>')
        print(request.POST['words_to_search'])
        context = {}
    else:
        context = {}
    return render(request=request, template_name='search_tweets.html', context=context)


def search_tweets_result(request):
    context = {}
    # if request.method == 'POST':
    #     print(request.method())
    #     captured_words = request.GET.get('words_to_search')
    #     print('\n', captured_words)
    #     words_to_search = captured_words.split()
    #     query_result = search_tweets(words_to_search)
    #     context = Context(query_result['text'])
    #     dashboard_render = search_tweets_result_template.render(context)
    # else:
    #     query_result = {"text": ""}
    #     context = Context(query_result['text'])
    #     dashboard_render = search_tweets_result_template.render(context)
    return render(request=request, template_name='search_tweets_result.html', context=context)

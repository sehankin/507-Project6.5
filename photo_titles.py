# Import statements necessary
import requests
import json
import random


def photo_titles(tag, num):
    FLICKR_KEY = "b23d6858b305a0cb8cc8fbee65e655ad" # TODO: fill in a flickr key
    baseurl = 'https://api.flickr.com/services/rest/'
    params = {}
    params['api_key'] = FLICKR_KEY
    params['method'] = 'flickr.photos.search'
    params['format'] = 'json'
    params['tag_mode'] = 'all'
    params['per_page'] = num
    params['tags'] = tag
    response_obj = requests.get(baseurl, params=params)
    trimmed_text = response_obj.text[14:-1]
    flickr_data = json.loads(trimmed_text)
    # TODO: Add some code here that processes flickr_data in some way
    # to get what you nested
    flickr_data_photo_list = flickr_data["photos"]["photo"]
    photo_titles = []
    for photo in flickr_data_photo_list:
        photo_titles.append(photo["title"])
    return photo_titles

#vader_result = photo_titles("vader", 10)
#print(vader_result)

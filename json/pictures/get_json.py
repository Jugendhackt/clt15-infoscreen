# coding=utf-8

# usage python [script.py] > pictures.json

import json
import urllib2
import sys

# this is just an api_key from the examples (you can make more data in shorten time)
api_key = "" 

events = '[{"name": "Berlin", "id": "72157659982826391"},{"name": "Nord", "id": "72157656615767034"},{"name": "West", "id": "72157658456916126"},{"name": "Ost", "id": "72157651802543473"},{"name": "Süd", "id": "72157654508365302"}]'
photos = "https://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key={}&photoset_id={}&user_id=99896278%40N06&format=json&nojsoncallback=1&extras=url_h,description"
get_url = "https://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key={}&photo_id={}&format=json&nojsoncallback=1"
description = "https://api.flickr.com/services/rest/?method=flickr.photos.getInfo&api_key={}&photo_id={}&secret={}&format=json&nojsoncallback=1"
photo_url = "https://farm1.staticflickr.com/{server}/{id}_{secret}_b.jpg"
pictures = []
for event in json.loads(events):
	photos_json = json.loads(urllib2.urlopen(photos.format(api_key, event['id'])).read())
	
	for photo in photos_json['photoset']['photo']:
		url = photo_url.format(**photo)
		photo_title = photo['title']
		photo_description = photo['description']['_content']
		pictures.append([event['name'], photo_title, photo_description, url])

_json = json.dumps([dict(url=x[3], description=x[2], title=x[1], event=x[0]) for x in pictures])

print _json.encode("UTF-8") # [{"event": "", "title": "", "description": "", "url": ""},{...},...]

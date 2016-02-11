# coding=utf-8

# usage [script.py] > pictures.json

import json
import urllib2
import sys

api_key = "f245236009f809c99375eb3b0a5b175c" 

events = '[{"name": "Berlin", "id": "72157659982826391"},{"name": "Nord", "id": "72157656615767034"},{"name": "West", "id": "72157658456916126"},{"name": "Ost", "id": "72157651802543473"},{"name": "Süd", "id": "72157654508365302"}]'
photos = "https://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key={}&photoset_id={}&user_id=99896278%40N06&format=json&nojsoncallback=1"
get_url = "https://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key={}&photo_id={}&format=json&nojsoncallback=1"
description = "https://api.flickr.com/services/rest/?method=flickr.photos.getInfo&api_key={}&photo_id={}&secret={}&format=json&nojsoncallback=1"

_json = '['
for event in json.loads(events):
	photos_json = json.loads(urllib2.urlopen(photos.format(api_key, event['id'])).read())
	for photo in photos_json['photoset']['photo']:
		url = ""
		for x in json.loads(urllib2.urlopen(get_url.format(api_key, photo['id'])).read())['sizes']['size']:
			if x['label'] == "Original":
				url = x['source']
				# just used to see it work
				sys.stderr.write(url)
		photo_title = photo['title']
		photo_description = json.loads(urllib2.urlopen(description.format(api_key, photo['id'], photo['secret'])).read())['photo']['description']['_content']
		# just used to see it work
		sys.stderr.write(photo_description)
		_json = _json + '{"event":"' + event["name"] + '","title":"' + photo_title + '","description":"' +  photo_description + '","url":"' +  url + '"},'
_json = _json[:-1]
_json += ']'

print _json.encode("UTF-8") # [{"event": "", "title": "", "description": "", "url": ""},{...},...]

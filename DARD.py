import os
import wget
import feedparser
import json

#=================================================================

taget_dir = "/home/user/DARD"			# Direction in witch files get saved
feed_file = "feedlist.txt"				# File witch contains feed-Urls
artist_name_file = "artistlist.txt"		# File witch contains Artistnames

#=================================================================

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def make_dir(sub_path):
	if not os.path.exists(sub_path):
		os.makedirs(sub_path)

def download(url,folder_dir, sub_dir):
	file_name = url.rsplit('/', 1)[1]
	sub_path = folder_dir + "/" + sub_dir
	file_path = sub_path + "/" + file_name
	make_dir(sub_path)
	if not os.path.exists(file_path):
		print "Download " + file_name + ":"
		filname = wget.download(url, out = sub_path)

	else:
		print "file "+ file_name + " already exists"

def get_feeds(feed_url):
	feed = feedparser.parse(feed_url)
	i = 0
	while i < len(feed['entries']):
		entry = feed.entries[i]
		artist_link = entry.links[0]['url']
		artist_name = artist_link.rsplit('http://',1)[1].rsplit('.deviantart',1)[0]
		media_url = entry.media_content[0]['url']
		download(media_url, taget_dir, artist_name)
		i += 1

def read_feed_list(feed_list):
	f = open(feed_list)
	lines = f.readlines()
	for i in lines:
		get_feeds(i)

def read_artist_feed_list(artist_feed_list):
	f = open(artist_feed_list)
	lines = f.readlines()
	for i in lines:
		get_feeds("http://backend.deviantart.com/rss.xml?q=gallery%3A" + i + "+sort%3Atime&type=deviation")



read_feed_list(__location__ + "/" + feed_file)

read_artist_feed_list(__location__ + "/" + artist_name_file)



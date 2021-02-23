import re
import sqlite3
import itertools
import mediacloud.api
import datetime
from dateutil import rrule

from settings import API_KEY, SEARCH_TERM, LANG, FROM_DATE, TO_DATE
from db_helper import write_url, write_text
from helper import url_filter

<<<<<<< HEAD


mediacloud = mediacloud.api.MediaCloud(API_KEY)

numOfStoriesTotal = int(mediacloud.storyCount(SEARCH_TERM, LANG, mediacloud.publish_date_query( datetime.date(2019, 1, 1), datetime.date(2019, 12, 31) ))["count"])
print(numOfStoriesTotal)

stories = []
for dt in rrule.rrule(rrule.DAILY,
					dtstart=datetime.datetime.strptime(FROM_DATE, '%Y-%m-%d'),
					until=datetime.datetime.strptime(TO_DATE, '%Y-%m-%d')):
	day = int(dt.strftime('%d'))
	month = int(dt.strftime('%m'))
	year = int(dt.strftime('%Y'))
	date1 = datetime.datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
	print(f"Getting stories: for {date1}")
	date2 = date1 + datetime.timedelta(days=1)
	print(date2)
	q_item = mediacloud.storyList(SEARCH_TERM, solr_filter=mediacloud.publish_date_query( date1, date2 ), rows = 100 )
	store(q_item)
	stories.append( q_item )



stories = list(itertools.chain.from_iterable(stories))
print(len(stories))

def store(story):
	url = story["url"]
	print(url)
	if url_filter(url):
		stories_id = int(story["stories_id"])
		print("Processing { story_id:%s } "%stories_id)
		title = re.sub('\s+', ' ', (story["title"])).strip()

		url = story["url"]
		publish_date = story["publish_date"]
		collect_date = story["collect_date"]

		media_id = int(story["media_id"])
		media_name = story["media_name"]
		media_url = story["media_url"]

	story_dict =  {
		"url" : url,
		"publish_date": publish_date,
		"collect_date": collect_date,
		"media_id": media_id,
	}

	media_dict = {
		"media_id": media_id,
		"media_name": media_name,
		"media_url": media_url,
	}

	write_url(stories_id, media_id, title, url, collect_date, publish_date)

mediacloud = mediacloud.api.MediaCloud(API_KEY)

numOfStoriesTotal = int(mediacloud.storyCount(SEARCH_TERM, LANG, mediacloud.publish_date_query( datetime.date(2019, 1, 1), datetime.date(2019, 12, 31) ))["count"])
print(numOfStoriesTotal)

stories = []
for dt in rrule.rrule(rrule.DAILY,
					dtstart=datetime.datetime.strptime(FROM_DATE, '%Y-%m-%d'),
					until=datetime.datetime.strptime(TO_DATE, '%Y-%m-%d')):
	day = int(dt.strftime('%d'))
	month = int(dt.strftime('%m'))
	year = int(dt.strftime('%Y'))
	date1 = datetime.datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
	print(f"Getting stories: for {date1}")
	date2 = date1 + datetime.timedelta(days=1)
	print(date2)
    q_item = mediacloud.storyList(SEARCH_TERM, solr_filter=mediacloud.publish_date_query( date1, date2 ), rows = 100 )
    store(q_item)
	stories.append( q_item )



stories = list(itertools.chain.from_iterable(stories))
print(len(stories))


from newsplease import NewsPlease
from db_helper import write_text, read_urls


urlDictList = read_urls()

print(len(urlDictList))

bs = 0
for x in range(0, len(urlDictList)):
	print(urlDictList[x]["url"])
	try:
		article = NewsPlease.from_url(urlDictList[x]["url"])
		text = article.text
		stories_id = urlDictList[x]["id"]
		print(f"Processing: {stories_id}")
		writeTextToDB(stories_id, text)
	except Exception as e:
		# print(e)
		bs += 1
		print("-- Bad Status code")

print(bs)

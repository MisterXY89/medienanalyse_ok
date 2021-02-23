
from newsplease import NewsPlease
from db_helper import write_text, read_urls


all_urls = read_urls()
if not all_urls:
    raise Exception(f"ReadError: No urls found.\n {all_urls=}")

print(len(all_urls))

bs = 0
for x in range(0, len(all_urls)):
	print(all_urls[x]["url"])
	try:
		article = NewsPlease.from_url(all_urls[x]["url"])
        print(article)
        print(dir(article))
		text = article.text
		stories_id = all_urls[x]["id"]
		print(f"Processing: {stories_id}")
		write_text(stories_id, text)
	except Exception as e:
		# print(e)
		bs += 1
		print("-- Bad Status code")

print(bs)

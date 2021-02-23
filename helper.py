
not_allowed_in_url_values = [".lu", ".li", ".va", "google.de", ".com",".gov",".org",".pdf",".ws", "ftp.", ".ru", ".se", ".bmp", ".img", ".io", ".edu", ".to", ".no", ".co.nz", ".la", ".fr", ".at", ".pl", ".pt", "wikipedia.org", "wikibooks.org", ".dk", ".ch"]

def url_filter(url):
	if any(x in url for x in not_allowed_in_url_values):
		return False
	return True

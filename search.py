import webbrowser
import sys

url = 'https://www.google.com/search?q='

sites = [
	'distrowatch.com',
	'reddit.com',
	'stackoverflow.com',
	'stackexchange.com',
	'wiki.ubuntu.com',
	'docs.python.org',
	'youtube.com',
]
firefox_path = '/usr/bin/firefox %s'
print(sys.argv[1:])

def create_filter():
	filter = '('
	for index, website in enumerate(sites):
		filter += 'site:' + website
		if index == len(sites) - 1:
			filter += ')'
		else:
			filter += ' OR '
	return filter

def create_query():
	query = sys.argv[1:]
	return ' '.join(query)

def create_url():
	if len(sys.argv[1:]) == 0:
		print("Error: please provide a valid search")
	else:
		final_url = url + create_query() + create_filter()
		webbrowser.get(firefox_path).open(final_url)

create_url()
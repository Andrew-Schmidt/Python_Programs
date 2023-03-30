#!/bin/python3
import praw

reddit = praw.Reddit(
    client_id="yD9lZR7hcD9NyM3nra3BpQ",
    client_secret="11YkVn9Q1i9qIfoYaweOoj5xgcjULQ",
    user_agent="<console:red_scrape_script>"
)
subreddit = reddit.subreddit("learnpython")
for post in subreddit.hot(limit=10):
	print("**********")
	print(post.title)

	for comment in post.comments:
		if hasattr(comment,"body"):
			print("**********")
			print(comment.body)


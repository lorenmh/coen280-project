import json
import praw
import os
import csv
import requests

def setup_praw():
    """Sets up praw and returns the Reddit instance."""
    config = json.load(open('creds.json', 'r'))
    return praw.Reddit(client_id=config['id'],
                         client_secret=config['secret'],
                         user_agent=config['user-agent'])

def get_recommendations(reddit, subreddits):
    """Returns dict of all recommended subreddits for the list of subreddits passed."""
    recommendations = {}
    for subreddit in reddit.subreddits.recommended(subreddits):
        print(subreddit)

def get_popular_subreddits():
    """Returns the list of subreddits in the file subreddits.txt."""

    if not os.path.isfile('./subreddits.txt'):
        print ('Could not find subreddits.txt file for popular subreddits.', file=sys.stderr)

    with open('./subreddits.txt', 'r', newline='') as csvfile:
        return [subreddit[0] for subreddit in csv.reader(csvfile)]

reddit = setup_praw()
popular = ','.join(get_popular_subreddits()[:100])
page = requests.get('https://www.reddit.com/api/recommend/sr/' + str(popular))
print(page.text.encode('ascii', 'ignore'))

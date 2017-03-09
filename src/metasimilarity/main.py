import csv
import json
import os
import praw
import re
import sys

def setup_praw():
    """Sets up praw and returns the Reddit instance."""
    config = json.load(open('creds.json', 'r'))
    return praw.Reddit(client_id=config['id'],
                         client_secret=config['secret'],
                         user_agent=config['user-agent'])

def get_popular_subreddits():
    """Returns the list of subreddits in the file subreddits.txt."""

    if not os.path.isfile('./subreddits.txt'):
        print ('Could not find subreddits.txt file for popular subreddits.', file=sys.stderr)

    with open('./subreddits.txt', 'r', newline='') as csvfile:
        return [subreddit[0] for subreddit in csv.reader(csvfile)]

def wiki_mentions(subreddit, reddit):
    """Goes through wiki pages and returns a list of mentioned subreddits."""
    srRegex = re.compile('(?:r\/).[^\(\)\]\.\s\:\+]*')
    mentions = set()
    for wikipage in reddit.subreddit(subreddit).wiki:
        for sr in srRegex.findall(wikipage.content_md):
            if subreddit not in sr and subreddit.lower() not in sr:
                try:
                    second_slash = sr.index('/', 3, len(sr))
                except:
                    second_slash = len(sr)
                mentions.add(sr[2:second_slash])

    return mentions

reddit = setup_praw()
print(wiki_mentions('AskReddit', reddit))

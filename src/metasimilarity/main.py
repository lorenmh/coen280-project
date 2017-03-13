import csv
import json
import os
import praw
import re
import sys
from collections import defaultdict

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

def get_mod_list(reddit, subreddits):
    """Get a a list of moderators for each of the subreddits passed in and write to mods.txt."""
    with open('mods.txt', 'w') as f:
        for sr in subreddits:
            f.write('{},{}\n'.format(sr,','.join([m.name for m in reddit.subreddit(sr).moderator()])))

def lcs(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ''
        for j in range(len2):
            if i + j < len1 and string1[i + j] == string2[j]:
                match += string2[j]
            else:
                if (len(match) > len(answer)):
                    answer = match
                match = ''
        if len(match) > len(answer):
            answer = match

    return answer

def get_affixes(subreddits, support):
    first_round = set()
    for i in range(len(subreddits)):
        print(i)
        for j in range(len(subreddits)):
            if i == j:
                continue
            sequence = lcs(subreddits[i].lower(), subreddits[j].lower())

            if len(sequence) > 3:
                first_round.add(sequence)

    first_round = list(first_round)
    d = {first_round[i]: 0 for i in range(len(first_round))}
    final_cut = {}
    for i in range(len(first_round)):
        print(i)
        for j in range(len(first_round)):
            if i == j:
                continue
            sequence = lcs(first_round[i], first_round[j])
            if len(sequence) > 3 and sequence in d:
                d[sequence] += 1

    for k, v in d.items():
        if v > support:
            final_cut[k] = v

    return final_cut

reddit = setup_praw()
with open('affixes.txt', 'w') as f:
    for k, v in get_affixes(get_popular_subreddits(), 2).items():
        f.write('{}: {}\n'.format(k, v))

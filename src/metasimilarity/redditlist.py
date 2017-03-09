import requests
from bs4 import BeautifulSoup
from bs4 import Comment
from bs4 import Tag

def popular_subreddits(num_pages):
    """
    Gets the first num_pages from redditlist.com and collects sfw subreddit names. Each page has
    150 subreddits.

    Positional Arguments:
        num_pages: number of pages from redditlist to scrape
    """

    subreddits = []

    with open('subreddits.txt', 'w') as f:
        for i in range(1,num_pages+1):
            listing = None
            page = requests.get('http://redditlist.com/?page=' + str(i))
            soup = BeautifulSoup(page.text, 'html.parser')
            nearby_tags = soup.find(string=lambda text:isinstance(text,Comment)
                                                        and 'Top Subscribers' in text).next_siblings

            while True:
                listing = next(nearby_tags)
                if listing == None:
                    break

                if isinstance(listing, Tag) and  listing['class'] == ['span4', 'listing']:
                    break

            for child in listing.contents:
                try:
                    if child.attrs['data-target-filter'] == 'sfw':
                        subreddits.append(child.attrs['data-target-subreddit'])
                except (KeyError, AttributeError):
                    continue


        f.write('\n'.join(subreddits))

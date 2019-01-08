from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re


IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    
    with open(RSS_FEED, 'r') as file:
        return re.findall(TAG_HTML, file.read().replace('-', ' ').lower())
                

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""

    sim_tags = []
    for singular, plural in product(tags, tags):
        if not singular.startswith(plural[0]) or singular.endswith('s'):
            continue
        ratio = round(SequenceMatcher(None, singular, plural).ratio(), 2)
        if ratio > SIMILAR and ratio < IDENTICAL:
            sim_tags.append((singular, plural))
    
    return sim_tags


if __name__ == "__main__":
    
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))

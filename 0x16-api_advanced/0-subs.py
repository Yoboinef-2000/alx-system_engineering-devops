#!/usr/bin/python3

"""
QUery the Reddit API and return
the number of subscirbers for a given
subreddit.
"""

import requests
# import sys


def number_of_subscribers(subreddit):
    """Refer to the commented out lines at the top."""

    # theSubreddit = sys.argv[1]
    theAPI = "https://www.reddit.com/r/"
    userResponse = requests.get('{}{}/about.json'.format(theAPI, subreddit),
                                allow_redirects=False)

    if userResponse.status_code == 200:
        print('OK')
        return (userResponse.json()['data']['subscribers'])
    
    else:
        print('OK')
        return 0

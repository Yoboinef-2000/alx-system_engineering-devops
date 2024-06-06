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
    # theAPI = "https://www.reddit.com/r/"
    # userResponse = requests.get('{}{}/about.json'.format(theAPI, subreddit),
    #                             allow_redirects=False)

    # if userResponse.status_code == 200:
    #     return (userResponse.json()['data']['subscribers'])
    
    # else:
    #     return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyScript/1.0)'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    else:
        return 0

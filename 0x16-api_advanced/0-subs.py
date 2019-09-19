#!/usr/bin/python3
# Finds total subscribers to a subreddit
import requests


def number_of_subscribers(subreddit):
    '''Function that returns total subscriber number'''
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    USERAGENT = {'User-Agent':
                 'Unix:com.holberton.apiadvanced:task0 (by /u/_marc_marc_)'}
    req = requests.get(URL, headers=USERAGENT).json()
    if req['error'] == 404:
        return (0)
    return (req['data']['subscribers'])

#!/usr/bin/python3
# Searches for keywords in hot titles
import requests


def count_words(subreddit, word_list, count=0, after_val=None):
    '''Searches for keywords in hot titles'''
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    USERAGENT = {'User-Agent':
                 'Unix:com.holberton.apiadvanced:task3 (by /u/_marc_marc_)'}
    params = {'limit': 100}
    

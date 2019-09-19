#!/usr/bin/python3
# Recursive call returns list of titles for hot articles
import requests


def recurse(subreddit, hot_list=[], count=0, after_val=None):
    '''returns list of titles for hot articles'''
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    USERAGENT = {'User-Agent':
                 'Unix:com.holberton.apiadvanced:task0 (by /u/_marc_marc_)'}
    params = {'limit': 100}
    if count > 0:
        params['after'] = after_val
    req = requests.get(URL,
                       headers=USERAGENT,
                       params=params)
    if req.status_code is not 200:
        return (None)
    jreq = req.json()
    data_path = jreq['data']['children']
    for i in range(len(data_path)):
        hot_list.append(data_path[i]['data']['title'])
    count += 1
    after_val = jreq['data']['after']
    if after_val is None:
        return (hot_list)
    else:
        return (recurse(subreddit, hot_list, count, after_val))

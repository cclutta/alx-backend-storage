#!/usr/bin/env python3
"""
Get page module

Contains get_page function
"""

import redis
import requests

rc = redis.Redis()
count = 0

def get_page(url: str) -> str:
    """ get a page and cache value"""
    rc.set("cached:{}".format(url), count)
    resp = requests.get(url)
    rc.incr("count:{}".format(url))
    rc.setex("cached:{}".format(url), 10, rc.get("cached:{}".format(url)))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')

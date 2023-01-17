#!/usr/bin/env python3
"""
Schools by topic module
Contains the function schools_by_topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    update many rows
    """
    return mongo_collection.find(
        {"topics": topic}
    )

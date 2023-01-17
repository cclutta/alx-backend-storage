#!/usr/bin/env python3
"""
Insert school module
Contains function insert_school
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert into school
    """
    return mongo_collection.insert_one(kwargs).inserted_id

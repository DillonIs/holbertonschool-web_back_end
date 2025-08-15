#!/usr/bin/env python3
"""Python function that inserts a new document into a MongoDB collection"""


def insert_school(mongo_collection, **kwargs):
    """Function to insert a new document based on kwargs"""
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id

#!/usr/bin/env python3
"""Change all topics of a document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Update topics by name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

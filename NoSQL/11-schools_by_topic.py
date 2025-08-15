#!/usr/bin/env python3
"""Python function that returns a list that include a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of school with topics"""
    return list(mongo_collection.find({"topics": topic}))

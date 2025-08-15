#!/usr/bin/env python3
"""Write a python function that lists all documents in a MongoDB collection"""


def list_all(mongo_collection):
    """Python function that lists all documents"""
    list_documents = []
    docs = mongo_collection.find()
    for doc in docs:
        list_documents.append(doc)
    return list_documents

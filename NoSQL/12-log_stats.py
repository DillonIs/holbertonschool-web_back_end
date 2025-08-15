#!/usr/bin/env python3
"""Python function that provides stats on Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def helper(a: dict) -> int:
    """Return logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(a)


def main():
    """Provides some stats on Nginx logs"""
    print(f"{helper({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {helper({'method': 'GET'})}")
    print(f"\tmethod POST: {helper({'method': 'POST'})}")
    print(f"\tmethod PUT: {helper({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {helper({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {helper({'method': 'DELETE'})}")
    print(f"{helper({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
#CODE BY RLZW

import twint
import os
import csv

def getTweets(username, destination):
    """Download all the tweets from username and saves it in a CSV File"""
    c = twint.Config()
    c.Since = "2018-01-01"
    c.Username = username
    c.Store_csv = True
    # CSV Fieldnames
    c.Custom["user"] = ["timezone", "date", "username", "tweet","retweets","likes"]
    c.Output = destination+".csv"
    twint.run.Search(c)


def getFollowers(username, destination):
    """Download all the followers from username and saves it in a CSV File"""
    c = twint.Config()
    c.Username = username
    c.Store_csv = True
    # CSV Fieldnames
    c.Custom = ["username"]
    c.Output = destination+".csv"
    twint.run.Followers(c)


def csvToList(filename):
    """Turns a CSV File to a list ignoring the header"""
    results = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:  # Each row is a list
            results.append(row[0])

    return results[1:]


def getTweetsFromFollowers(followerslist):

    files = os.listdir()


    for follower in followerslist:
        if follower+".csv" not in files:
            destination = follower+"tweets"
            getTweets(follower, destination)

if __name__ == "__main__":
    username = "El_Universal_Mx"
    getTweets(username, "ElUniversalTweets")


#!/usr/bin/python

from twython.twython import Twython
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--raw", help="spit out raw data", action = "store_true")
parser.add_argument("-d", "--dat", help="spit out raw data", action = "store_true")
args = parser.parse_args()

def findAll(s, s1):
  """
  Find a specified substring (s1) in a specified string (s)
  """
  count = -1
  place = 0
  s = ' ' + s
  while place != -1:
    s = s[place + 1:]
    place = s.find(s1)
    count = count + 1
  return count

t = Twython()

settings = json.load(open('settings.json')) # Loads the settings from the JSON file

def query():
  """
  Retrieve the most recent tweets
  """
  t = Twython()
  # Search twitter for recent tweets containing any letter in the latin alphabet
  biglist = []
  countdown = [5,4,3,2,1] # Get 7 pages of tweets
  for x in countdown:
    search = t.search(q="a+OR+b+OR+c+OR+d+OR+e+OR+f+OR+g+OR+h+OR+i+OR+j+OR+k+OR+l+OR+m+OR+n+OR+o+OR+p+OR+q+OR+r+OR+s+OR+t+OR+u+OR+v+OR+w+OR+x+OR+y+OR+z",rpp=30, result_type = "mixed" ,page = x)
    search = search['results']
    englishlist = []
    # Filter results to only english tweets
    # Note: average English tweets on a page is around 18
    for i in search:
      if i['iso_language_code'] == 'en': # If the tweet is english
        englishlist.append(i) # add the tweet 
    biglist.extend(englishlist) # don't want individual lists in a list; we want one big list
  texts = []
  for i in biglist:
    texts.append(i['text'].lower() + '\n\n')
  texts = ' '.join(texts)
  return texts

def count():
  emotions = settings['emotions']
  opposites = settings['opposites']

  scores = {} # Dict to hold the scores for the emotions
  tweets = query() # get the tweets

  for i in opposites:
    positive = i['positive']
    negative = i['negative']
    score = 0
    for x in emotions[positive]:
      score = score + findAll(tweets, x) # Find all instances of the positive keyword and add it to the score
    for x in emotions[negative]:
      score = score - findAll(tweets, x) # Find all instances of the negative keyword and subtract it from the score
    scores[positive] = score # Plop the score in the dict

  return scores
  # "surprise": ["wow", "can't believe", "wtf", "unbelievable"],  what's the opposite of surprise?
  # "envy": ["wish", "envious", "jealous", "want", "why can't i"]  what's the opposite of envy?


def raw_display():
  c = count()
  for k,v in c.items():
    print "%s: %d" % (k,v)

def display():
  print "Natural Language display!"


if args.raw:
  raw_display()
else:
  if args.dat:
    print query()
  else:
    display()




      

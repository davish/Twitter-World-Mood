#!/usr/bin/python

from twython.twython import Twython

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


def query():
  """
  Search twitter for 
  """
  t = Twython()
  # Search twitter for recent tweets containing any letter in the latin alphabet
  biglist = []
  countdown = [7,6,5,4,3,2,1]
  for x in countdown:
    search = t.search(q="a+OR+b+OR+c+OR+d+OR+e+OR+f+OR+g+OR+h+OR+i+OR+j+OR+k+OR+l+OR+m+OR+n+OR+o+OR+p+OR+q+OR+r+OR+s+OR+t+OR+u+OR+v+OR+w+OR+x+OR+y+OR+z",rpp=30, page = x)
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
    texts.append(i['text'].lower())
  texts = ' '.join(texts)
  return texts

def count():
  emotions = {
  "love": ["love"],
  "anger": ["hate", "angry", "mad"],
  "happiness": ["happiest", "happy", "excited", "woot", "w00t"],
  "sadness": ["sad", "heartbroken", "upset", "depressed", "cry"],
  "excitement": ["can't wait", "excited", "awaiting", "wait"],
  "fear": ["scared", "terrified", "afraid", "fearful"],

  "surprise": ["wow", "can't believe", "wtf", "unbelievable"], # what's the opposite of surprise?
  "envy": ["wish", "envious", "jealous", "want", "why can't i"] # what's the opposite of envy?
  }

  opposites = [{'positive': 'love', 'negative': 'anger'}, 
              {'positive': 'happiness', 'negative': 'sadness'}, 
              {'positive': 'excitement', 'negative': 'fear'}]


  return emotions
print query()

      

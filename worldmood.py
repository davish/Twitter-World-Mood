#!/usr/bin/python

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



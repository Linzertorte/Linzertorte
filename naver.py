# -*- coding: utf-8 -*-
import os, urllib2
from termcolor import colored
import requests
from bs4 import BeautifulSoup
def one_line(text):
  return ' '.join([x.lstrip().rstrip() for x in text.split('\n')])
while True:
  word = raw_input('>>> ')
  try:
    word = word.rstrip()
    url = 'http://cndic.naver.com/search/all?q='+word
    html = requests.get(url).text
    soup = BeautifulSoup(html,'lxml')
    dl =  soup.find('div', 'word_result').find('dl')
    t = dl.find_all("dt")
    d = dl.find_all("dd")
    print
    for i in xrange(len(t)):
      print colored(one_line(t[i].text),'green')
      print '\n'.join([ one_line(y.text) for y in d[i].find_all('li')])
      print
  except:
    print '404 Not Found.'
    pass


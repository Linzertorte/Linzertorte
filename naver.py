#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, urllib2, sys
from termcolor import colored
import requests
from bs4 import BeautifulSoup
'''
Usage
naver [word file]
If word file is provided, do batch lookup, otherwise
it is interactive and the successful lookup will
leave trace in TRACE file.

'''

TRACE = 'naver_tmp.txt'

def one_line(text):
  return ' '.join([x.lstrip().rstrip() for x in text.split('\n')])
def word_gen(fname):
  with open(fname,'r') as f:
    for line in f.readlines():
      yield(line.rstrip())

def main(auto=False,fname=''):
  gen = word_gen(fname)
  if not auto:
    trace = open(TRACE,'w')
  while True:
    word = raw_input('>>> ')
    try:
      word = word.rstrip()
      if auto:
        os.system('clear')
        word = next(gen, None)
        if word is None:
          print 'Bye'
          break
      if word == 'quit' or word == '안녕':
        print 'Bye'
        break
      print colored(word, 'blue')
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
      if not auto:
        trace.write(word+'\n')
    except:
      print '404 Not Found.'
      pass

if __name__ == '__main__':
  if len(sys.argv)==2:
    main(True, sys.argv[1])
  else:
    main()
                                   

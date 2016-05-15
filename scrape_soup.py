#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup

r = requests.get("http://www.capefearit.com/")

r.raise_for_status()

soup =  BeautifulSoup(r.text, 'html.parser')
#this is the tag being searched
text = soup.title
print text

#crucial... turn bs4 object into a true string 
made_string = str(text) 
#compile regex pattern into re object to compare to bs4-output-turned-string
re_pattern = re.compile(r'([H-Z]+)')
# can change the search type here.e.g. findall
match = re_pattern.search(made_string) 
# which will change output here (if findall then just variable name)
print match.group(0)

#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import re

page = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films')


soup = BeautifulSoup(page, "html.parser")


tableDiv = soup.findAll('table', class_='wikitable sortable')

csv_file = open('MovieList.csv', 'w')


# Generate lists

filmList = []
yearList = []
awardsList = []
nominationsList = []
atags = []
filmetest = []
td_list = []


# Get the data!
for row in tableDiv[0].findAll('td'):
    for films in row.findAll('i'):

            for film in films.findAll('a'):
                
                film_text = film.get_text()
                filmList.append(film_text)
    for years in row.findAll('a'):
        if years.parent.name == 'td':
            year_text = years.get_text()
            yearList.append(year_text)

for td in tableDiv[0].findAll('td'):
    td_text = td.get_text()
    td_list.append(td_text)


awardsList = [td_list[i] for i in xrange(2, len(td_list), 4)]
nominationsList = [td_list[i] for i in xrange(3, len(td_list), 4)]
  
diplicate_issue = 'The Devil and Daniel Webster'        
if diplicate_issue in filmList:
    filmList.remove(diplicate_issue)

first_title = 'All That Money Can Buy'
index_title =  filmList.index(first_title)

diplicate_issue = ' (The Devil and Daniel Webster)'        

filmList[index_title] = first_title + diplicate_issue

# Convert list to data frame

list_data = {'Films': filmList,
            'Year': yearList,
            'Awards': awardsList,
            'Nominations': nominationsList}
df = pd.DataFrame(list_data, columns = ['Films', 'Year', 'Awards', 'Nominations'])
#print df
df.to_csv('MovieData.csv', encoding='utf-8', index = False)




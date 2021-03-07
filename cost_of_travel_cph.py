# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

import requests
from bs4 import BeautifulSoup
import re

# --input --
home_city = 'Copenhagen'
destinations = ['Stockholm','Oslo','Berlin','Amsterdam']
# ----

def find_travel_methods(home_city,city):
  url = "https://www.rome2rio.com/map/{}/{}".format(home_city,city)
  try:
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    transport['method'] = soup.select('h3', {'class': 'route__title'})
    transport['price'] =  soup.find_all('span',{'class': 'route__price'})
    transport['duration'] = soup.find_all('span'{'class'='route__duration'})
    transport['city'] = len(transport['routes']) * [home_city]
    transport_df = pd.DataFrame([transport])
    return transport_df
  except:
    print("An error occured.")
    exit

def calculate_emission(transport_df):
  if transport_df['method'] == 'Train':
    return round(transport['duration']/60*1.9)
  elif transport_df['method'] == 'Bus':
    return round(transport['duration']/60*11)
  elif transport_df['method'] == 'Fly':
    return round(transport['duration']/60*42)

def make_spider( row, title, color):

  # number of variable
  categories=['TravelTime[min]','CO2[kg]','TravelCost']
  N = len(categories)

  # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
  angles = [n / float(N) * 2 * pi for n in range(N)]
  angles += angles[:1]

  # Initialise the spider plot
  ax = plt.subplot(4,3,row+1, polar=True )

  # If you want the first axis to be on top:
  ax.set_theta_offset(pi / 2)
  ax.set_theta_direction(-1)

  # Draw one axe per variable + add labels labels yet
  plt.xticks(angles[:-1], categories, color='grey', size=6 )

  # Draw ylabels
  ax.set_rlabel_position(0)
  plt.yticks([200,400,600,800], ["200","400","600","800"], color="grey", size=5)
  plt.ylim(0,800)

  # Ind1
  values=viz.loc[row].values.flatten().tolist()
  values += values[:1]
  ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
  ax.fill(angles, values, color=color, alpha=0.4)

  # Add a title
  plt.title(title, size=9, color=color, y=1.1)

my_dpi=96
plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
 
my_palette = plt.cm.get_cmap("Set2", len(destination.index))

for cities in destinations:
  transport_df = find_travel_methods(home_city,cities)
  transport_df['co2_emission'] = transport_df.apply(calculate_emission,axis = 0)

for row in range(0, len(destination.index)):
  make_spider( row=row, title= transport_df['city'] [row] + ' - '+ transport_df['method'][row], color=my_palette(row))
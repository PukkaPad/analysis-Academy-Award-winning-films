#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import textwrap
from bokeh.plotting import figure, output_file, show


# bar charts
fig = plt.figure()
df = pd.read_csv('MovieData.csv', encoding = 'utf-8')


df_s = df.sort_values(by=('Awards'), ascending=False) #


movies = np.array(df_s[df_s.columns[0]]) [:10]

num_oscars = np.array(df_s[df_s.columns[2]]).astype(int)[:10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)

plt.ylabel('# of Academy Awards')
plt.title('10 biggest awards winners of all the time')

# wrapping labels (some are too long)
movies=[textwrap.fill(text,17) for text in movies]

# label x-axis with names at bar centre
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies, rotation=45, fontsize=10, ha = 'right')

fig.tight_layout()
fig.savefig('10_biggest_winners.png', orientation = 'portrait')

# creating time series

fig = plt.figure()
grp_Year = df.groupby(['Year']).sum().plot(marker = 'o')
#print grp_Year
plt.title('Awards per Year')
plt.ylabel('# of Academy Awards')
plt.grid()
#plt.show()
plt.savefig('Awards_per_Year.png', orientation = 'portrait')


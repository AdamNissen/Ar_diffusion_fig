# -*- coding: utf-8 -*-
"""
Creating a multi-figure plate to compare Ar diffusion modeling and Ar-Ar spot
dates from mica within the Brazil Lake pegmatite. This is made following 
Ar_diff_model_fig.py, I felt that script was useful as a standalone archive, so
this is built as a new script.
"""

import pandas as pd
from matplotlib import pyplot as plt

#importing data
dif_data = pd.read_csv("Data\Ar_Diffusion.csv")
spot_data = pd.read_csv("Data\Spot_dates.csv")

#Building a list full of colourmap functions to be used later 
cmaps = [plt.cm.Purples,
         plt.cm.Reds,
         plt.cm.Greens,
         plt.cm.Oranges]

#Establishing the figure
fig = plt.figure(figsize = (16,12))

#Manually setting the axes due to the unconventional shape
ax1 = plt.subplot2grid(shape = (3,4), loc = (0,0), colspan = 3, rowspan = 2)
ax2 = plt.subplot2grid(shape = (3,4), loc = (0,3))
ax3 = plt.subplot2grid(shape = (3,4), loc = (1,3))
ax4 = plt.subplot2grid(shape = (3,4), loc = (2,0))
ax5 = plt.subplot2grid(shape = (3,4), loc = (2,1))
ax6 = plt.subplot2grid(shape = (3,4), loc = (2,2))
ax7 = plt.subplot2grid(shape = (3,4), loc = (2,3))
axs = [ax1, ax2, ax3, ax4, ax5, ax6, ax7]  #not sure if this is necessary, but I suspect it is

#Filling the axes
for i in range(7):
    ax = axs[i]
    
    if ax == ax1:
        pass
    
    else:
        pass
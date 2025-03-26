# -*- coding: utf-8 -*-
"""
Creating a multi-figure plate to compare Ar diffusion modeling and Ar-Ar spot
dates from mica within the Brazil Lake pegmatite. This is made following 
Ar_diff_model_fig.py, I felt that script was useful as a standalone archive, so
this is built as a new script.
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#importing data
dif_data = pd.read_csv("Data\Ar_Diffusion.csv")
spot_data = pd.read_csv("Data\Spot_dates.csv")

#Building a list full of colourmap functions to be used later 
cmaps = [plt.cm.Purples,
         plt.cm.Reds,
         plt.cm.Blues,
         plt.cm.Oranges]

n = len(dif_data['Mesh'].unique())+3

#Establishing the figure
fig = plt.figure(figsize = (12,9))

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
    
    #Filling the big subfigures
    if ax == ax1:
        
        #Setting parameters for the large subfigure
        ax.set_ylim(300, 400)
        ax.plot([1600, 2550, 2550, 1600, 1600], [310, 310, 370, 370, 310], color = 'k')
        ax.set_xlabel('Distance from grain core (μm)')
        ax.set_ylabel('Date (Ma)')
        
        #iterating over each scenario so the colourmaps line up nicely
        # for j in dif_data["Scenario"].unique(): #could use this line, but I think having a number will help more.
        for j in range(4):
            scenario = dif_data['Scenario'].unique()[j]
            
            #Making a colourmap for each scenario based on mesh number. The plus three is to make sure no colour is too pale to discern
            #n = len(dif_data.query("Scenario == @scenario")['Mesh'].unique())+3
            colours = cmaps[j](np.linspace(0, 1, n))
            
            #iterating over each mesh in a scenario so the colours match nicely.
            #This is overcomplicated because there is only partial sharing of mesh sizes across grain sizes
            for k in range(len(dif_data.query("Scenario == @scenario")['Mesh'].unique())):
                mesh = dif_data.query("Scenario == @scenario")['Mesh'].unique()[k]
                colour = colours[k+3]
                
                #Final iteration over "Identifier" which is just the grain size oddly formatted.                
                for l in dif_data.query("Scenario == @scenario and Mesh == @mesh")['Identifier'].unique():
                    
                    #defining a temporary dataset, and then plotting ar diffusion model lines with the data
                    temp = dif_data.query("Scenario == @scenario and Mesh == @mesh and Identifier == @l")
                    ax.plot(temp["um"], temp["Apparent_Age"], color = colour)
        
        #Plotting all of the spot data on the big figure
        for j in range(len(spot_data)):
            x = 2500-spot_data['Distance_um'][j]
            y = spot_data['Age'][j]
            y_err = spot_data['error_1sigma'][j]*2
            # ax.plot([x, x], [y+y_err, y-y_err], color = 'k', alpha = 0.5)
            ax.plot([x, x], [y+y_err, y-y_err], color = 'k', alpha = 0.5, linewidth = 4.0)
    
    #Plotting the small subfigures
    else:
        #Setting figure parameters for the small subfigs
        ax.set_xlim(1600, 2550)
        ax.set_ylim(310, 370)
        sample = spot_data['Sample'].unique()[i-1]
        #ax.text(1630, 312, 'Sample '+sample)
        ax.text(2100, 366, 'Sample '+sample)
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        
        #Getting data for the Ar models
        model_3 = dif_data.query("Scenario == 3 and Mesh == 40")
        model_4 = dif_data.query("Scenario == 4 and Mesh == 40")
        
        #Setting colours for the models
        colours_3 = cmaps[2](np.linspace(0, 1, n))
        colours_4 = cmaps[3](np.linspace(0, 1, n))
        colour_3 = colours_3[5]
        colour_4 = colours_4[5]
        
        #plotting the Ar diffusion models
        ax.plot(model_3['um'], model_3['Apparent_Age'], color = colour_3)
        ax.plot(model_4['um'], model_4['Apparent_Age'], color = colour_4)
        
        #Plotting individual spot data
        temp = spot_data.query('Sample == @sample')
        temp.reset_index(drop = True, inplace = True)
        for j in range(len(temp)):
            x = 2500-temp['Distance_um'][j]
            y = temp['Age'][j]
            y_err = temp['error_1sigma'][j]*2
            ax.plot([x, x], [y+y_err, y-y_err], color = 'k', linewidth = 4.0)
            
plt.tight_layout()
plt.savefig('Output/7_plate/diffusion_fig.jpg', dpi=600)
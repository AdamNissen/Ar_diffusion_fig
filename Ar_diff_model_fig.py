# -*- coding: utf-8 -*-
"""
Making a combined Ar spot date and Ar diffusion model figure using data from
the Brazil Lake pegmatite.
"""
#importing modules
import pandas as pd
from matplotlib import pyplot as plt

#importing data
dif_data = pd.read_csv("Data\Ar_Diffusion.csv")
spot_data = pd.read_csv("Data\Spot_dates.csv")

#selecting spot data
spot_data = spot_data.query('Sample == "12A07L"')
spot_data.reset_index(drop = True, inplace = True)

#Establishing the figure and axes (or subplots) of the figure
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize = (15, 12))
axs = [ax1, ax2, ax3, ax4]

#making each subplot
for i in range(4):
    
    #iteration variables
    ax = axs[i]
    diffusion_scenario = i+1
    ax.text(5, 305, 'Scenario '+str(diffusion_scenario))
    ax.set_ylim(300, 400)
    
    #Plotting Ar diffusion lines
    for j in dif_data.query("Scenario == @diffusion_scenario")['Mesh'].unique():
        temp = dif_data.query("Scenario == @diffusion_scenario and Mesh == @j")
        ax.plot(temp["um"], temp['Apparent_Age'])
        
    for j in range(len(spot_data)):
        x = 2500-spot_data['Distance_um'][j]
        y = spot_data['Age'][j]
        y_err = spot_data['error_1sigma'][j]*2
        # ax.plot([x, x], [y+y_err, y-y_err], color = 'k', alpha = 0.5)
        ax.plot([x, x], [y+y_err, y-y_err], color = 'k', alpha = 1)
        
plt.tight_layout()

#Saving the figure
save_plot = input("Enter plot name, or n to not save the plot: ")
if save_plot == "n":
    plt.show()
else:
    plt.savefig("Output/4_plate_output/"+save_plot+".jpg", dpi = 600)
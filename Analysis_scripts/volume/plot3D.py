#!/usr/bin/python

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Solv_df = pd.read_csv("wat-carb.csv")
solute_hb = np.loadtxt("interhbonds.dat", usecols=1)[1:45001:2]
volume = np.loadtxt("Volume.dat", usecols=1)[1:45001:2]
solute_hb = solute_hb/729
volume = volume - 151.98
print(volume)

Solv_df['Interhbonds'] = solute_hb
Solv_df['volume_change'] = volume
Solv_df['Wat_sum'] = Solv_df.iloc[:, 1:8].sum(axis=1)
print(Solv_df.columns)

def get_color_range(value):
    if value <= -15:
        return 'blue'
    elif value <= 0 and value > -15: 
        return 'green'
    elif value >= 1 and value <= 16:
        return 'red'
    else:
        return 'black'

Solv_df['color'] = Solv_df['volume_change'].apply(get_color_range)

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(Solv_df['Interhbonds'], Solv_df['Wat_sum'], c=Solv_df['color'], label=Solv_df['volume_change'], cmap='viridis')
plt.xlabel('Fraction of max solute-solute Hbonds')
plt.ylabel('Solute-Solvent Hbonds')
plt.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Range -25 to -15'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Range -16 to 0'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Range 1 to 15'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=10, label='Range > 16')
], title=r'$\Delta$Volume ($\AA^3$) ranges')
plt.tight_layout()
plt.savefig('Hbond_scatter_volume_map_x.png',dpi=300,transparent=True,format='png')
plt.show()


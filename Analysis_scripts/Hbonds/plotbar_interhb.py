#!/usr/bin/python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

a = [0.2, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.3, 0.2, 0.05, 0.06, 0.06, 0.04, 0.5, 0.7, 0.8, 0.7]

vals = a #+ b
hbonds = ['NH4--O4']*4 + ['NH--O6']*4 + ['NH--O5']*4 + ['O6H--O3']*4 + ['O6H--N']*4
pattern = ['Nofield']*1 + ['Efieldx']*1 + ['Efieldy']*1 + ['Efieldz']*1 + ['Nofield']*1 + ['Efieldx']*1 + ['Efieldy']*1 + ['Efieldz']*1 + ['Nofield']*1 + ['Efieldx']*1 + ['Efieldy']*1 + ['Efieldz']*1 + ['Nofield']*1 + ['Efieldx']*1 + ['Efieldy']*1 + ['Efieldz']*1 + ['Nofield']*1 + ['Efieldx']*1 + ['Efieldy']*1 + ['Efieldz']*1 

df = pd.DataFrame(zip(vals, hbonds, pattern), columns = ['Value', 'Hbond', 'condition'])


plt.figure(figsize = (3.0,1.5))
ax = sns.barplot(data = df, x = 'Hbond', y = 'Value', capsize = 0.5, edgecolor = 'none', lw = 2.0, errwidth = 2.0, palette = ['black', 'blue', 'cyan', 'red'], errcolor = '0.2', hue = 'condition')
bars = ax.patches
bars[0].set_facecolor('none') 
bars[0].set_edgecolor('black') 
bars[1].set_facecolor('none') 
bars[1].set_edgecolor('black') 
bars[2].set_facecolor('none') 
bars[2].set_edgecolor('black') 
bars[3].set_facecolor('none') 
bars[3].set_edgecolor('black')
bars[4].set_facecolor('none') 
bars[4].set_edgecolor('black') 

plt.ylim(0, 0.8)
ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8])
ax.set(xlabel=None)
ax.set(ylabel=None)
ax.set(xticklabels=[])
ax.set(yticklabels=[])
plt.legend([], [], frameon=False)
plt.tight_layout()



prev_lim = ax.get_ylim()[1]
max_val = max(vals)

for axis in ['bottom', 'left']:
    ax.spines[axis].set_linewidth(1.0)
    ax.spines[axis].set_color('0.2')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


plt.savefig('specific_hb_grouped.png', bbox_inches = 'tight', dpi=300, transparent=True)
#plt.show()

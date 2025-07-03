#!/usr/bin/python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

a = [0.74, 0.80, 0.80, 0.80]
#b = [0.2, 0.3, 0.2, 0.2]

vals = a #+ b
hbonds = ['O3H--O5']*4
pattern = ['Nofield']*1 + ['Efieldx']*1 + ['Efieldy']*1 + ['Efieldz']*1

df = pd.DataFrame(zip(vals, hbonds, pattern), columns = ['Value', 'Hbond', 'condition'])


plt.figure(figsize = (2,2))
ax = sns.barplot(data = df, x = 'Hbond', y = 'Value', width=0.5, capsize = 0.5, edgecolor = 'none', lw = 2.0, errwidth = 2.0, palette = ['black', 'blue', 'cyan', 'red'], errcolor = '0.2', hue = 'condition')
#kwargs = {'edgecolor':'0.2', 'linewidth':2.5, 'fc': 'none'}
#ax = sns.swarmplot(data = df, x = 'Hbond', y = 'Value', hue = 'PA', dodge=True, marker = 's', s = 10, **kwargs)
#plt.margins(x=0.5)
bars = ax.patches
# Unfill (set facecolor to none) for the bar you want to unfill (e.g., bar 'C')
bars[0].set_facecolor('none')  # Index 2 corresponds to category 'C' (third bar)
bars[0].set_edgecolor('black')  # Optionally, set the edge color to black




plt.ylim(0.6, 0.8)
ax.set_yticks([0.6, 0.7, 0.8])
ax.set(xlabel=None)
ax.set(ylabel=None)
ax.set(xticklabels=[])
ax.set(yticklabels=[])
plt.xticks([])
plt.legend([], [], frameon=False)
plt.tight_layout()



prev_lim = ax.get_ylim()[1]
max_val = max(vals)

#handles, labels = ax.get_legend_handles_labels()
#plt.legend(handles[2:], labels[2:]. loc = 10, bbox_to_anchor = (0.5, -0.25), ncol = 2, frameon = False, fontsize = 14)

for axis in ['bottom', 'left']:
    ax.spines[axis].set_linewidth(1.0)
    ax.spines[axis].set_color('0.2')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

#plt.xticks(size = 14, rotation = 35, rotation_mode = 'anchor', ha = 'center', weight = 'bold', color = '0.2')
#plt.yticks(size = 14, weight = 'bold', color = '0.2')

#ax.tick_params(width = 2.5, color = '0.2')

plt.savefig('specific_hb_grouped_intra.png', bbox_inches = 'tight', dpi=300, transparent=True)
#plt.show()

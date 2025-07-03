import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

datax = np.loadtxt('tmpx.dat')
datay = np.loadtxt('tmpy.dat')
dataz = np.loadtxt('tmpz.dat')
data1 = np.loadtxt('tmp1.dat')
data2 = np.loadtxt('tmp2.dat')
data3 = np.loadtxt('tmp3.dat')

data_mod_x = datax[:, -24:]
data_mod_y = datay[:, -24:]
data_mod_z = dataz[:, -24:]
data_mod_1 = data1[:, -24:]
data_mod_2 = data2[:, -24:]
data_mod_3 = data3[:, -24:]

datax_lst = np.ravel(data_mod_x.tolist())
datay_lst = np.ravel(data_mod_y.tolist())
dataz_lst = np.ravel(data_mod_z.tolist())
data1_lst = np.ravel(data_mod_1.tolist())
data2_lst = np.ravel(data_mod_2.tolist())
data3_lst = np.ravel(data_mod_3.tolist())
data_nofield = (data1_lst + data2_lst + data3_lst)/3

c = [*datax_lst, *datay_lst, *dataz_lst, *data_nofield]

data = pd.DataFrame({
    'distance': c,
    'Labels': ['efieldx'] * len(datax_lst) + ['efieldy'] * len(datax_lst) + ['efieldz'] * len(datax_lst) + ['no field'] * len(datax_lst)
})


color_palette = {
        'no field': 'black',
        'efieldx': 'blue',
        'efieldy': 'cyan',
        'efieldz': 'red'
        }


g = sns.displot(data=data, x='distance', hue='Labels',palette=color_palette, kind='kde', fill=False, legend=False, height=2, aspect=1)
plt.vlines(x = 110, ymin=0, ymax=0.18, color = 'black', linestyle = '--', lw = 4)
# X-Axis
g.set(xlim=(95, 110), ylim=(0, 0.18))  # Adjust limits as needed


# Remove tick labels
for ax in g.axes.flatten():
    ax.set_xlabel('')  
    ax.set_ylabel('')
    ax.set_xticks([95, 98, 101, 104, 107,110])
    ax.set_yticks([0, 0.06, 0.12, 0.18])
    ax.set_xticklabels([])  
    ax.set_yticklabels([]) 

ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

plt.savefig('ete_pub.png',dpi=300,transparent=True,format='png')
plt.show()


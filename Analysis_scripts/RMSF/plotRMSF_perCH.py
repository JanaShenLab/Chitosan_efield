import matplotlib.pyplot as plt
import string
import numpy as np

file1 = 'rmsf_x.dat'
file2 = 'rmsf_y.dat'
file3 = 'rmsf_z.dat'
file4 = 'rmsf_nofield1.dat'
file5 = 'rmsf_nofield2.dat'
file6 = 'rmsf_nofield3.dat'

with open(file1, 'r') as file:
    rms_x = [float(line.strip()) for line in file]

with open(file2, 'r') as file:
    rms_y = [float(line.strip()) for line in file]

with open(file3, 'r') as file:
    rms_z = [float(line.strip()) for line in file]

with open(file4, 'r') as file:
    rms_1 = [float(line.strip()) for line in file]

with open(file5, 'r') as file:
    rms_2 = [float(line.strip()) for line in file]

with open(file6, 'r') as file:
    rms_3 = [float(line.strip()) for line in file]

chain_ids = list(string.ascii_uppercase[:len(rms_x)])

rms_nofield = [(x + y + z) / 3 for x,y,z in zip(rms_1, rms_2, rms_3)]

fig, ax = plt.subplots(figsize=(5, 2))
plt.plot(chain_ids, rms_x, marker='o', linestyle='-', color='blue', label='efield x')
plt.plot(chain_ids, rms_y, marker='*', linestyle='--', color='cyan', label='efield y')
plt.plot(chain_ids, rms_z, marker='v', linestyle=':', color='red', label='efield z')
plt.plot(chain_ids, rms_nofield, marker='s', linestyle='-.', color='black', label='no field')
ax.set_yticks([0, 1.5, 3, 4.5])
ax.set_xticks([x for x in range(0, 24)])
ax.set_ylim(0, 4.5)
ax.set_xlim(0, 23)
ax.tick_params(labelleft=False, direction='out')
ax.tick_params(labelbottom=False, direction='out')
ax.grid(False)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

plt.savefig('RMSF_perChain.png',dpi=300,transparent=True,format='png')
plt.show()



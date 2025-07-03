import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data1 = pd.read_csv('sasa_x.dat')
data2 = pd.read_csv('sasa_y.dat')
data3 = pd.read_csv('sasa_z.dat')
data4 = pd.read_csv('Avg_sasa_nofield.dat')

# Extract the column of interest
data1_series = data1['SASA']
data2_series = data2['SASA']
data3_series = data3['SASA']
data4_series = data4['SASA']

# Plot the distributions
plt.figure(figsize=(10, 6))


plt.hist(data1_series, color='blue', alpha=0.5, label='efield x', bins=30)
plt.hist(data2_series, color='green', alpha=0.5, label='efield y', bins=30)
plt.hist(data3_series, color='red', alpha=0.5, label='efield z', bins=30)
plt.hist(data4_series, color='violet', alpha=0.5, label='no field', bins=30)

plt.xlabel(r'SASA ($\AA$)')
plt.ylabel('Frequency')
#plt.title('Distribution of Datasets')
plt.legend()

plt.savefig('sasa_distribution_efield.png',dpi=300,transparent=True,format='png')
plt.show()


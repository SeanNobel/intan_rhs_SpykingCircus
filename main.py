import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import load_intan_rhs_format as load

path = "./SpikeScope0930_210930_110218/merged.rhs"

f = load.read_data(path)
for key in f.keys():
    print("\n" + key + ":")
    print(f[key])

print(f"Channels: {len(f['amplifier_data'])}")


amplifier_data = f['amplifier_data']
print(amplifier_data.shape)

amplifier_data = amplifier_data[8:24]


#-----------------------------
# Plot
#-----------------------------
"""
n = 16

fig = plt.figure()
axes = []
for i in range(n):
    ax = fig.add_subplot(n, 1, i+1)
    # axes.append(ax)
    ax.plot(f['t'][:1000], f['amplifier_data'][i][:1000])

plt.show()
"""
#------------------------------

np.save("./SpikeScope0930_210930_110218/merged", amplifier_data)


#------------------
# Translate into pandas dataframe
#------------------
# df = pd.DataFrame(f.values(), index=f.keys()).T
# print(df.head())

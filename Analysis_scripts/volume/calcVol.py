import mdtraj as md
import numpy as np
import pandas as pd
import sys
from scipy.spatial import ConvexHull

# Load the trajectory file
traj = md.load('{}'.format(sys.argv[2]), top='{}'.format(sys.argv[1]))

# Define your custom function that will process each frame
def process_frame(frame):
    # Example function: calculate the center of mass of all atoms
    # You can replace this with any other processing you need
    positions = frame.xyz[0]  # Get the positions of atoms in the first (only) frame
    hull = ConvexHull(positions)
    volume = hull.volume
    return volume

# Loop through each frame in the trajectory and apply the function
results = []
frames = []
for i in range(len(traj)):
    frame = traj[i]  # Get the i-th frame
    result = process_frame(frame)  # Apply the function
    results.append(result)  # Store the result
    frames.append(i)

vol_df = pd.DataFrame({'Frame':frames, 'Volume': results})
vol_df.to_csv("Volume.dat", sep="\t", index=False)



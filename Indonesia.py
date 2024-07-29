import matplotlib.pyplot as plt
import geopandas as gpd

# Load a world map dataset
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter for Indonesia
indonesia = world[world['name'] == "Indonesia"]

# Plot the map of Indonesia
fig, ax = plt.subplots(figsize=(10, 10))
indonesia.boundary.plot(ax=ax, color="blue")
ax.set_title("Map of Indonesia", fontsize=15)
ax.set_axis_off()

plt.show()

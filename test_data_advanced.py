from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Normals

# Get Normals data
data = Normals('10637', 1961, 1990)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()
import numpy as np
import matplotlib.pyplot as plt

x = [250,500,750,1000,1250,1500,1750,2000,2250,2500,2750]
y = [0.790333,0.82739,0.847402,0.849417,0.860702,0.874632,0.873692,0.881758,0.879404,0.882933,0.885476]

fig, ax = plt.subplots()

# Using set_dashes() to modify dashing of an existing line
line1, = ax.plot(x, y, label='Val = 500 images')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

# Using plot(..., dashes=...) to set the dashing when creating a line
line2, = ax.plot(x, y - 0.2, dashes=[6, 2], label='Using the dashes parameter')

ax.legend()
plt.show()



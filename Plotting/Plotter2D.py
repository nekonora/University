import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

# General Style ------------------------------------
avenir = {'fontname':'Avenir'}
fig = plt.figure(figsize=(5,4), dpi=200)
ax = fig.add_subplot(111)

# Vectors ------------------------------------------
#
v1 = np.array([2,1])
v2 = np.array([0.5,1.5])

sum_12 = v1 + v2

ax.quiver((0,0), (0,0), (v1[0],v2[0]), (v1[1],v2[1]), units = 'xy', scale = 1, color="#ff5252", zorder=2)
ax.quiver(0, 0, sum_12[0], sum_12[1], units = 'xy', scale = 1, color="#5633ff", zorder=1)

# Shapes ------------------------------------------
#
verts = [
	(0, 0), # left, bottom
	(v1[0], v1[1]), # left, top
	(sum_12[0], sum_12[1]), # right, top
	(v2[0], v2[1]), # right, bottom
	(0., 0.), # ignored
	]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts, codes)
patch = patches.PathPatch(path, facecolor='#d6e4ff', alpha = 0.8, lw=0, zorder=1)
ax.add_patch(patch) # comment this to remove

# Annotations ------------------------------------------
#
ax.annotate("$\hat{j}$", xy=(1, 1), xytext=(v1[0] + .1, v1[1] + .1), size=16)
ax.annotate("$\hat{i}$", xy=(1, 1), xytext=(v2[0] + .1, v2[1] + .1), size=16)

# Axis limits ------------------------------------------
#
plt.axis('equal')
plt.xticks(range(-1, +5), zorder=0)
plt.yticks(range(-1, +5), zorder=0)

plt.grid(b=True, which='both', color='0.65',linestyle='--')

# Axis options ------------------------------------------
#

ax.set_xticklabels([]) # axis ticks text
ax.set_yticklabels([])

ax.set_axisbelow(True) # self-explanatory

ax.spines['bottom'].set_color('#ebebeb')
ax.spines['top'].set_color('#ebebeb')
ax.spines['left'].set_color('#ebebeb')
ax.spines['right'].set_color('#ebebeb')

plt.tick_params(
	axis='both',       # changes apply to the x-axis
	which='both',      # both major and minor ticks are affected
	bottom='off',      # ticks along the bottom edge are off
	top='off',         # ticks along the top edge are off
	left='off',
	right='off',
	labelleft='off',
	labelbottom='off') 

# Save Plot -----------------------------------------------
#

# plt.savefig("plot2D.png", dpi=300, bbox_inches="tight")
plt.show()

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from numpy.linalg import solve

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def drawVectors():
    vector1 = Arrow3D([0, v1[0]], [0, v1[1]], [0, v1[2]], mutation_scale=20, lw=4, arrowstyle="-|>", color="#ff5252")
    vector2 = Arrow3D([0, v2[0]], [0, v2[1]], [0, v2[2]], mutation_scale=20, lw=4, arrowstyle="-|>", color="#ff5252")
    vector3 = Arrow3D([0, v3[0]], [0, v3[1]], [0, v3[2]], mutation_scale=20, lw=4, arrowstyle="-|>", color="#ff5252")
    ax.add_artist(vector1)
    ax.add_artist(vector2)
    ax.add_artist(vector3)

def drawVolume():
    x = [0, v1[0], v2[0], v3[0], sum_12[0], sum_13[0], sum_23[0], sum_123[0]]
    y = [0, v1[1], v2[1], v3[1], sum_12[1], sum_13[1], sum_23[1], sum_123[1]]
    z = [0, v1[2], v2[2], v3[2], sum_12[2], sum_13[2], sum_23[2], sum_123[2]]
    vertices = [[0, 1, 4, 2, 0],
    			[0, 1, 5, 3, 0],
    			[0, 2, 6, 3, 0],
    			[1, 5, 7, 4, 1],
    			[3, 5, 7, 6, 3],
    			[2, 6, 7, 4, 2]]
    tupleList = list(zip(x, y, z))
    poly3d = [[tupleList[vertices[ix][iy]] for iy in range(len(vertices[0]))] for ix in range(len(vertices))]
    ax.scatter(x,y,z)
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='#e0fbff', linewidths=1, alpha=0.5))
    ax.add_collection3d(Line3DCollection(poly3d, colors='#ccdeff', linewidths=0.2, linestyles='--'))

def drawBVector():
    Bvector = Arrow3D([0, vB[0]], [0, vB[1]], [0, vB[2]], mutation_scale=20, lw=4, arrowstyle="-|>", color="#59d04b")
    ax.add_artist(Bvector)

def drawXVector():
    Bvector = Arrow3D([0, vX[0]], [0, vX[1]], [0, vX[2]], mutation_scale=20, lw=4, arrowstyle="-|>", color="#50abf6")
    ax.add_artist(Bvector)

fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='3d')

# Initiatiate program --------------------------
#

print("\n# Vector Plotter ---------#\n\n#           Matrix:\n")

# Vectors --------------------------------------
#
v1 = np.array([-3   ,0   ,6   ])
v2 = np.array([2 ,2   ,-2   ])
v3 = np.array([1   ,3   ,0   ])

vB = np.array([-1   ,-1   ,15   ])

vecMatrix = np.array([v1,v2,v3])

vX = solve(vecMatrix.T, vB)

print("Matrix is: \n{0}\n".format(vecMatrix.T))
print("Rank: {0}".format(np.linalg.matrix_rank(vecMatrix.T)))
print("B vector: {0}".format(vB))
print("X vector: {0}\n".format(vX))
for i in range(3) :
    print("Vector {0} is: {1}i + {2}j + {3}k".format(i, vecMatrix[i,0], vecMatrix[i,1], vecMatrix[i,2]))
    print("       Norm: {0}".format(np.linalg.norm(vecMatrix[i])))

# Vectors additions
sum_12 = v1 + v2
sum_13 = v1 + v3
sum_23 = v2 + v3
sum_123 = v1 + v2 + v3

print("\nSum of vectors: {0}i + {1}j + {2}k".format(sum_123[0], sum_123[1], sum_123[2]))
print("            Norm: {0}".format(np.linalg.norm(sum_123)))

# Axis style --------------------------------------
#
ax.set_xticklabels([]) # axis ticks text
ax.set_yticklabels([])
ax.set_zticklabels([])

axisDefinerVectorUp = np.array([np.amax([sum_123[0], vB[0], vX[0]]), np.amax([sum_123[1], vB[1], vX[1]]), np.amax([sum_123[2], vB[2], vX[2]])])
axisDefinerVectorDown = np.array([np.amin([sum_123[0], vB[0], vX[0]]), np.amin([sum_123[1], vB[1], vX[1]]), np.amin([sum_123[2], vB[2], vX[2]])])

ax.set_xlim3d(axisDefinerVectorDown[0] -0.5, axisDefinerVectorUp[0] +0.5)
ax.set_ylim3d(axisDefinerVectorDown[1] -0.5, axisDefinerVectorUp[1] +0.5)
ax.set_zlim3d(axisDefinerVectorDown[2] -0.5, axisDefinerVectorUp[2] +0.5)

#ax.set_xlabel('x_values')
#ax.set_ylabel('y_values')
#ax.set_zlabel('z_values')

#plt.title('Eigenvectors')

# What to draw?

drawVectors()
drawVolume()
drawBVector()
drawXVector()


plt.draw()
#plt.savefig("plot3D.png", dpi=300, bbox_inches="tight")
plt.show()

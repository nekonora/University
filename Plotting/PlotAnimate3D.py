import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from numpy.linalg import solve
import matplotlib.animation as animation
import time

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

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')




var = -100.0
plt.ion()

while var < 100.0:
    v1 = np.array([-10   ,0   ,20   ])
    v2 = np.array([0 , 0   ,0   ])
    v3 = np.array([10   ,10  ,10  ])

    #vB = np.array([-10   ,-10   ,50   ])

    vecMatrix = np.array([v1,v2,v3])

    #if np.linalg.det(vecMatrix.T) != 0:
    #    vX = solve(vecMatrix.T, vB)

    # Dot product
    vX = np.array([20, var, 10])
    vB = np.dot(vecMatrix.T, vX)

    # Vectors additions
    sum_12 = v1 + v2
    sum_13 = v1 + v3
    sum_23 = v2 + v3
    sum_123 = v1 + v2 + v3

    # Axis style --------------------------------------
    #
    ax.set_xticklabels([]) # axis ticks text
    ax.set_yticklabels([])
    ax.set_zticklabels([])

    axisDefinerVectorUp = np.array([np.amax([sum_123[0], vB[0], vX[0]]), np.amax([sum_123[1], vB[1], vX[1]]), np.amax([sum_123[2], vB[2], vX[2]])])
    axisDefinerVectorDown = np.array([np.amin([sum_123[0], vB[0], vX[0]]), np.amin([sum_123[1], vB[1], vX[1]]), np.amin([sum_123[2], vB[2], vX[2]])])

    #ax.set_xlim3d(axisDefinerVectorDown[0] -5, axisDefinerVectorUp[0] +5)
    #ax.set_ylim3d(axisDefinerVectorDown[1] -5, axisDefinerVectorUp[1] +5)
    #ax.set_zlim3d(axisDefinerVectorDown[2] -5, axisDefinerVectorUp[2] +5)

    ax.set_xlim3d(-100, 100)
    ax.set_ylim3d(-100, 100)
    ax.set_zlim3d(-100, 100)

    drawVectors()
    drawVolume()

    drawBVector()
    drawXVector()
    #if np.linalg.det(vecMatrix.T) != 0:
    #    drawXVector()

    plt.title("t = {0}\ndet = {1}\n{2}".format(var, np.linalg.det(vecMatrix.T), vB))
    plt.draw()

    #if np.linalg.det(vecMatrix.T) == 0:
    #    plt.pause(2)
    plt.pause(0.05)
    plt.cla()

    var += 1

plt.pause(0.05)

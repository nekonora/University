# coding: utf-8
#	Vectors calculations
#	Author: Filippo Zaffoni
#
#--------------------------------

import numpy as np
import matplotlib.pyplot as plt


# --- Vectors definition
class _2DVector (object):
	def __init__(self, xValue, yValue):
		self.x = float(xValue)
		self.y = float(yValue)
		
		# - Cartesian
		self.r = np.sqrt(self.x**2 + self.y**2)
		self.vector = np.array([self.x, self.y])
		self.alpha = np.arctan2(self.y, self.x) * (180 / np.pi)



class _3DVector (object):
	def __init__(self, xValue, yValue, zValue):
		self.x = float(xValue)
		self.y = float(yValue)
		self.z = float(zValue)
		
		# - Cartesian
		self.r = np.sqrt(self.x**2 + self.y**2 + self.z**2)
		self.vector = np.array([self.x, self.y, self.z])
	
		# - Polar
		# phi = angle on (x,y) plane
		#	theta = declination towards z axis
		self.phi = np.arctan2(self.y, self.x) * (180 / np.pi)
		self.theta = np.arctan2(self.z, self.r) * (180 / np.pi)
	
	
# --- Functions & vector operations	
#	np.vdot(a.vector, b.vector) = dot product => scalar
#	xProduct(a.vector, b.vector) = cross product => vector	
#

def _xProduct(a, b): # a & b must be 3D .vector !
	product = np.cross(a, b)
	resultVector = _3DVector(product[0], product[1], product[2])
	return resultVector

def _vecSum(a, b): # a & b must be .vector !
	sum = a + b
	if sum.size == 2 :
		resultVector = _2DVector(sum[0], sum[1])
	elif sum.size == 3 :
		resultVector = _3DVector(sum[0], sum[1], sum[2])
	return resultVector	

def _2Dplot(vector): # Must be in 2D .vector format!
	plt.figure()
	ax = plt.gca()
	ax.quiver(vector[0],vector[1], angles='xy',scale_units='xy',scale=1)
	ax.set_xlim([-1,int(vector[0] + vector[0] / 3)])
	ax.set_ylim([-1,int(vector[1] + vector[1] / 3)])
	plt.draw()
	plt.show()
	
def _dVec(vector):
	
	
# --- Main

myVec1 = _2DVector(5, 3)
myVec2 = _2DVector(4, 3)
#dotProduct = np.vdot(myVec1.vector, myVec2.vector)
#myCross = xProduct(myVec1.vector, myVec2.vector)


###########################################################################################
#    _ _             ___                               _             _                  _ _   
#  _| | |_     ___  / __|  _  _   _ __   ___   _ _    | |     __ _  | |__     ___     _| | |_ 
# |_  .  _|   |___| \__ \ | || | | '_ \ / -_) | '_|   | |__  / _` | | '_ \   |___|   |_  .  _|
# |_     _|         |___/  \_,_| | .__/ \___| |_|     |____| \__,_| |_.__/           |_     _|
# __|_|_|                  _     |_|                                                   |_|_|  
# \ \ / /  ___   __   __  | |_   (_)                                                          
#  \ V /  / -_) / _| / _| | ' \  | |                                                          
#  _\_/   \___| \__| \__| |_||_| |_|   _   _          _                                       
# | _ \  ___   _ __    ___   _ _    __| | (_)  _ _   (_)                                      
# |   / / -_) | '  \  / _ \ | ' \  / _` | | | | ' \  | |                                      
# |_|_\ \___| |_|_|_| \___/ |_||_| \__,_|_|_| |_||_| |_|                                      
# |_  /  __ _   / _|  / _|  ___   _ _   (_)                                                   
#  / /  / _` | |  _| |  _| / _ \ | ' \  | |                                                   
# /___| \__,_| |_|   |_|   \___/ |_||_| |_|                                                   
###########################################################################################

import numpy as np
import pylab as pl

# Funzioni e classi -----------------------------------------------------------------------
class misura:  
	def __init__(self, value, name):
		self.value = value
		self.name = name
		self.rad = value * np.pi / 180
		self.grad = value * 180 / np.pi

# Plotter - prende array 2D(+ stile linea) come args
def plot_graf(*args) :
	if args :
		for ar in args :
			pl.plot(ar[0], ar[1], ar[2])
	pl.xlabel("")
	pl.ylabel("")
	pl.title("")
	pl.grid(True)
	pl.show()

# Polynomial Regression - y = a+mx - restituisce un array [a,m,R^2]
def poly_fit(x, y, degree):
	results = np.empty(3)
	coeffs = np.polyfit(x, y, degree)
	# Polynomial Coefficients
	results[0] = coeffs[0]
	results[1] = coeffs[1]
	# r-squared
	p = np.poly1d(coeffs)
	# fit values, and mean
	yhat = p(x)                         # or [p(z) for z in x]
	ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
	ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
	sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
	results[2] = ssreg / sstot
	return results
	
# Constants -----------------------------------------------------------------------------
#
#
Lambda = 632.8E-6
print(Lambda)

# Variables -----------------------------------------------------------------------------
#
#
_L = np.array([1,4,3])
_Y = np.array([3,9,3])
_theta_i = np.array([1,2,3])

_DX = np.array([[],
								[],
								[],
								[],
								[],
								[],
								[],
								[],
								[],
								[],
								[]])
_Dx = np.array([0] * 11)
for i in _DX :
	sum = 0	
	for x in i :
		sum += i[x]
	_Dx[i] = sum / 5	

L = misura(value= _L, name="x")
y = misura(value= _Y / 2, name="y")
theta_i = misura(value= _theta_i, name="theta_i")
Dx = misura(value= _Dx, name= "DeltaX")

# Un array con tutte le variabili
varArray = np.array([L.value,y.value,theta_i.value])

# Calculations -------------------------------------------------------------------------
#
#
_l = np.array([0] * 11)
_DTheta = np.array([0] * 11)
_d = np.array([0] * 11)

for i in range(11) :
	_l[i] = Lambda / np.sin(theta_i.value.rad[i])

for i in range(11) :
	_DTheta[i] = _Dx[i] / _L[i]	
	
for i in range(11) :
	_d[i] = Lambda / _DTheta[i]
	
l = misura(value= _l, name= "l")
DTheta = misura(value= _DTheta, name= "Delta Theta")
d = misura(value= _d, name= "d")	
	
#fitLine = poly_fit(x,y,1)

# Errors -------------------------------------------------------------------------------
#
#
#errTheta = np.array([0.0] * 10)
#for i in range(10) :
#	errTheta[i] = np.sqrt((0.025) / (x[i] ** 2 + y[i] ** 2)) * 180 / np.pi

# Results ------------------------------------------------------------------------------
#
#


#print("| $\\theta_0$ | $\\theta '$ | $\\theta_i$ | $y$ | $x$ | $\\Theta$ | $\\sigma \\Theta$ | $2 \\theta_i - \\Theta$ |")
#print("|-----:|-----:|-----:|-----:|-----:|-----:|------:|-----:|")
#for row in zip(theta0,theta1,thetaI,y,x,Theta,errTheta,index) :
#	print("| {} | {} | {} | {} | {} | {:.2f} | $\\pm$ {:.2f} | {:.2f} |".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
	
#print("\nMedia indice: {}".format(np.mean(index)))
#print("R^2: {}\n".format(fitLine[2]))

# Plot: crea un array con argomenti (x, y, stile linea) - stile linea: colore + "o","-","--"
#plotArrayTheta = np.array([thetaI, Theta, "ko"])
#plot_graf(myArray)


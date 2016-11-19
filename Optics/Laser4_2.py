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
		#self.rad = value * np.pi / 180
		#self.grad = value * 180 / np.pi

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
_n_min = 22.0 - 1.0
Lambda = 632.8 * (10E-7) 
_l = np.array([0.041] * 11)
l = misura(value= _l, name= "l")

# Variables -----------------------------------------------------------------------------
#
#
_L = np.array([780.0, 700.0, 630.0, 560.0, 490.0, 420.0, 380.0, 340.0, 300.0, 220.0, 150.0]) 
_Y = np.array([23.0, 21.1, 18.4, 17.0, 15.0, 12.8, 11.1, 10.5, 8.6, 6.7, 4.8])

L = misura(value= _L, name="L")
y = misura(value= _Y / 2.0, name="y")

# Calculations -------------------------------------------------------------------------
#
#
_DTheta = []
_d = []
_Dx = []			
_theta_i = []

for i in range(11) :
	_Dx.append(float(_Y[i]) / _n_min)
	
for i in range(11) :
	_theta_i.append(np.arctan2(_Y[i] / 2, _L[i]))

for i in range(11) :
	_DTheta.append(_Dx[i] / _L[i])
	
for i in range(11) :
	_d.append(Lambda / _DTheta[i])
	
DTheta = misura(value= _DTheta, name= "Delta Theta")
d = misura(value= _d, name= "d")	
theta_i = misura(value= _theta_i, name="theta_i")
Dx = misura(value= _Dx, name= "DeltaX")

# Un array con tutte le misure
varArray = np.array([L, y, theta_i, l, Dx, DTheta, d])
	
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



for row in zip(L.value, y.value, theta_i.value, l.value, Dx.value, DTheta.value, d.value) :
	print("| {:.2f} | {:.2f} | {:.2f} | {:.2f} | {:.2f} | {:.2f} | {:.2f} |".format(*row))
	
#print("\nMedia indice: {}".format(np.mean(index)))
#print("R^2: {}\n".format(fitLine[2]))

# Plot: crea un array con argomenti (x, y, stile linea) - stile linea: colore + "o","-","--"
#plotArrayTheta = np.array([thetaI, Theta, "ko"])
#plot_graf(myArray)

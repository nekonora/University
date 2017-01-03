###########################################################################################
#    _ _             ___                               _             _                  _ _
#  _| | |_     ___  / __|  _  _   _ __   ___   _ _    | |     __ _  | |__    ___     _| | |_
# |_  .  _|   |___| \__ \ | || | | '_ \ / -_) | '_|   | |__  / _` | | '_ \  |___|   |_  .  _|
# |_     _|         |___/  \_,_| | .__/ \___| |_|     |____| \__,_| |_.__/          |_     _|
# __|_|_|                  _     |_|                                                  |_|_|
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
from uncertainties import ufloat
from uncertainties import unumpy as unp
from uncertainties.umath import *

#---------------------------------------------------------------------------------------#
#-/////////////////////// FUNCS & CLASSES /////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
class misura:
	def __init__(self, value, name):
		self.nominal = np.array(unp.nominal_values(value))
		self.err = np.array(unp.std_devs(value))
		self.value = np.array(value)		
		self.name = name
		
### Funzione per creare numeri con errori integrati
def ne(array, error) :
	result = []
	for i in range(len(array)) :
		result.append(ufloat(array[i], error))
	return result
						
### Plotter - prende array 2D(+ stile linea) come args
def plot_graf(xLabel, yLabel, *args) :
	if args :
		for ar in args :
			pl.plot(ar[0].nominal, ar[1].nominal, ar[2])
			if ar[3] :
				pl.errorbar(ar[0].nominal, ar[1].nominal, ar[1].err, ar[0].err, fmt=None, ecolor='k', capthick=2)
	pl.xlabel(xLabel)
	pl.ylabel(yLabel)
	pl.title("")
	pl.grid(True)
	pl.show()

### Polynomial Regression - y = a+mx - restituisce un array [a,m,R^2]
def poly_fit(x, y):
	results = np.empty(3)
	coeffs = np.polyfit(x.nominal, y.nominal, 1)
	### Polynomial Coefficients
	results[0] = coeffs[0]
	results[1] = coeffs[1]
	### r-squared
	p = np.poly1d(coeffs)
	### fit values, and mean
	yhat = p(x.nominal)
	ybar = np.sum(y.nominal)/len(y.nominal)
	ssreg = np.sum((yhat-ybar)**2)
	sstot = np.sum((y.nominal - ybar)**2)    
	results[2] = ssreg / sstot
	return results

### Result Printer
def print_results(array) :
	print("\n")
	title = "| "
	tableLine = "|"
	tableText = "|"
	valuesArray = []
	for i in array :
		title += "{}|".format(i.name)
		tableLine += "---|"
		tableText += "${:L}$|"
		valuesArray.append(i.value)
	print(title)
	print(tableLine)
	for row in zip(*valuesArray) :
		print(tableText.format(*row))
		
#---------------------------------------------------------------------------------------#
#-/////////////////////// CONSTANTS ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
Lambda = 632.8E-6

## Legge di riflessione
_theta0 = ne([0.0] * 10, 1.0)
_y = 			ne([25.0] * 10, 0.05)

theta0 = 	misura(value= _theta0, name= "$\\theta_0$")
y = 			misura(value= _y, name= "$y$")

#---------------------------------------------------------------------------------------#
#-/////////////////////// VARIABLES ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
# Legge di riflessione
_theta1 = ne([45,42,40,38,36,30,26,22,20,18], 1.0)
_x = 			ne([0,2.4,4.1,5.9,7.9,14.2,19.4,25.7,30.3,34.5], 0.05)

theta1 = 	misura(value= _theta1, name= "$\\theta '$")
x =				misura(value= _x, name="$x$")

#---------------------------------------------------------------------------------------#
#-/////////////////////// CALCULATIONS ////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
# Legge di riflessione
_thetaI =	 []
_Theta =	 []
_index = 	 []
_ThetaTh = []

for i in range(10) :
	_thetaI.append(_theta1[i])
	_Theta.append(unp.arctan2(_y[i], _x[i]) * 180 / np.pi)
	_index.append((_thetaI[i] * 2) - _Theta[i])
	_ThetaTh.append((_theta1[i] * 2))

thetaI = 	misura(value= _thetaI, name= "$\\theta_i$")
Theta = 	misura(value= _Theta, name="$\\Theta$")
index = 	misura(value= _index, name="$2\\theta_i - \\Theta$")
ThetaTh = misura(value= _ThetaTh, name= "$2 \\theta_i$")

### Correlazione lineare tra due valori (x,y)
fitLine = poly_fit(thetaI, Theta)

#---------------------------------------------------------------------------------------#
#-/////////////////////// RESULTS /////////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#

### Printa il risultato in forma di tabella
print_results([theta0, theta1, thetaI, y, x, Theta, index])

print("\nMedia indice: {}".format(np.mean(index.nominal)))
print("R^2: {}\n".format(fitLine[2]))

print(Theta.err)

### Plot: crea un array con argomenti (x, y, stile linea, ShowErr)
plotArrayTheta = np.array([thetaI, Theta, "ko", True])
plotArrayThetaTheoric = np.array([thetaI, ThetaTh, "r-", False])
plot_graf("$\\theta_i$", "$\\Theta$", plotArrayTheta, plotArrayThetaTheoric)

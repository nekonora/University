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
				pl.errorbar(ar[0].nominal, ar[1].nominal, ar[0].err, ar[1].err, fmt=None, ecolor='k', capthick=2)
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
dCD = ufloat(0.0015807, 0.0000012)
dDVD = ufloat(0.00073309, 0.00000014)

#---------------------------------------------------------------------------------------#
#-/////////////////////// VARIABLES ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
### Immettere valori come ne([valori], errore)
_LCD =   ne([160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360], 0.5)
_x1CD =  ne([69, 80, 87, 98, 105, 114, 125, 133, 139, 148, 157], 0.5)
_x2CD =  ne([227, 262, 288, 319, 347, 378, 410, 438, 456, 482, 508], 0.5)

_LDVD =  ne([250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150], 0.5)
_xDVD =  ne([486, 464, 439, 421, 398, 383, 360, 344, 327, 309, 287], 0.5)

LCD =  misura(value= _LCD, name="$L$ (mm)")
x1CD = misura(value= _x1CD, name="$x_1$ (mm)")
x2CD = misura(value= _x2CD, name="$x_2$ (mm)")

LDVD =  misura(value= _LDVD, name="$L$ (mm)")
xDVD = misura(value= _xDVD, name="$x_1$ (mm)")

#---------------------------------------------------------------------------------------#
#-/////////////////////// CALCULATIONS ////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_theta1CD = []
_theta2CD = []
_sin1CD = []
_sin2CD = []
_Lambda1CD = []
_Lambda2CD = []

_thetaDVD = []
_sinDVD = []
_LambdaDVD = []

for i in range(len(LCD.value)) :
	_theta1CD.append(atan(_x1CD[i] / _LCD[i]))
	_theta2CD.append(atan(_x2CD[i] / _LCD[i]))
	_sin1CD.append(sin(_theta1CD[i]))
	_sin2CD.append(sin(_theta2CD[i]))
	_Lambda1CD.append(dCD * _sin1CD[i])
	_Lambda2CD.append(dCD * _sin2CD[i] * 0.5)
	
for i in range(len(LDVD.value)) :
	_thetaDVD.append(atan(_xDVD[i] / _LDVD[i]))
	_sinDVD.append(sin(_thetaDVD[i]))
	_LambdaDVD.append(dDVD * _sinDVD[i])
	
theta1CD = misura(value= _theta1CD, name="$\\theta_1$")
theta2CD = misura(value= _theta2CD, name="$\\theta_2$")
sin1CD = misura(value= _sin1CD, name="$\\sin \\theta_1$")
sin2CD = misura(value= _sin2CD, name="$\\sin \\theta_2$")
Lambda1CD = misura(value= _Lambda1CD, name="$\\Lambda_1$")
Lambda2CD = misura(value= _Lambda2CD, name="$\\Lambda_2$")

thetaDVD = misura(value= _thetaDVD, name="$\\theta$")
sinDVD = misura(value= _sinDVD, name="$\\sin \\theta$")
LambdaDVD = misura(value= _LambdaDVD, name="$\\Lambda$")

### Correlazione lineare tra due valori (x,y)
#fitLine = poly_fit(x,y)

#---------------------------------------------------------------------------------------#
#-/////////////////////// RESULTS /////////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#

### Printa il risultato in forma di tabella
print_results([LCD, x1CD, x2CD, sin1CD, sin2CD, Lambda1CD, Lambda2CD])
print_results([LDVD, xDVD, sinDVD, LambdaDVD])

#print("R^2: {}\n".format(fitLine[2]))

### Plot: crea un array con argomenti (x, y, stile linea, xErr, yErr)
#plotArray = np.array([L, d2, "ko", True])
#plot_graf("$\\theta_1$", "$d_1$", plotArray)

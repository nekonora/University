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
Lambda = 632.8E-6

#---------------------------------------------------------------------------------------#
#-/////////////////////// VARIABLES ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
### Immettere valori come ne([valori], errore)
_LCD =  ne([160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360], 0.5)
_x1CD = ne([69, 78, 88, 97, 105, 114, 123, 132, 140, 149, 158], 0.5)
_x2CD = ne([212, 229, 267, 292, 322, 346, 379, 401, 420, 459, 486], 0.5)
_LDVD =  ne([290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190], 0.5)
_xDVD = ne([482, 473, 462, 451, 428, 413, 399, 382, 359, 338, 325], 0.5)

x1CD = misura(value= _x1CD, name="$x_1$ (mm)")
x2CD = misura(value= _x2CD, name="$x_2$ (mm)")
LCD =  misura(value= _LCD, name="$L$ (mm)")
xDVD = misura(value= _xDVD, name="$x_1$ (mm)")
LDVD =  misura(value= _LDVD, name="$L$ (mm)")

#---------------------------------------------------------------------------------------#
#-/////////////////////// CALCULATIONS ////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_theta1CD = []
_theta2CD = []
_sin1CD = []
_sin2CD = []
_d1CD = []
_d2CD = []

_thetaDVD = []
_sinDVD = []
_dDVD = []

for i in range(len(LCD.value)) :
	_theta1CD.append(atan(_x1CD[i] / _LCD[i]))
	_theta2CD.append(atan(_x2CD[i] / _LCD[i]))
	_sin1CD.append(sin(_theta1CD[i]))
	_sin2CD.append(sin(_theta2CD[i]))
	_d1CD.append(Lambda / _sin1CD[i])
	_d2CD.append( (2 * Lambda) / _sin2CD[i])

for i in range(len(LDVD.value)) :
	_thetaDVD.append(atan(_xDVD[i] / _LDVD[i]))
	_sinDVD.append(sin(_thetaDVD[i]))
	_dDVD.append(Lambda / _sinDVD[i])
	
_d1CDSum = 0.0
_d2CDSum = 0.0
for i in range(11) :
	_d1CDSum += _d1CD[i]
	_d2CDSum += _d2CD[i]
_d1CDMean = _d1CDSum / 11
_d2CDMean = _d2CDSum / 11	
_dCDMean = (_d1CDMean + _d2CDMean) / 2
	
_dDVDSum = 0.0
for i in range(11) :
	_dDVDSum += _dDVD[i]
_dDVDMean = _dDVDSum / 11			
	
theta1CD = misura(value= _theta1CD, name="$\\theta_1$")
theta2CD = misura(value= _theta2CD, name="$\\theta_2$")
sin1CD = misura(value= _sin1CD, name="$\\sin \\theta_1$")
sin2CD = misura(value= _sin2CD, name="$\\sin \\theta_2$")
d1CD = misura(value= _d1CD, name="$d_1$ (mm)")
d2CD = misura(value= _d2CD, name="$d_2$ (mm)")
		
thetaDVD = misura(value= _thetaDVD, name="$\\theta$")
sinDVD = misura(value= _sinDVD, name="$\\sin \\theta$")
dDVD = misura(value= _dDVD, name="$d$ (mm)")

### Correlazione lineare tra due valori (x,y)
#fitLine = poly_fit(x,y)

#---------------------------------------------------------------------------------------#
#-/////////////////////// RESULTS /////////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#

### Printa il risultato in forma di tabella
print_results([LCD, x1CD, x2CD, sin1CD, sin2CD, d1CD, d2CD])
print(_dCDMean)
print_results([LDVD, xDVD, sinDVD, dDVD])
print(_dDVDMean)

#print("R^2: {}\n".format(fitLine[2]))

### Plot: crea un array con argomenti (x, y, stile linea, xErr, yErr)
#plotArray = np.array([LCD, d2CD, "ko", True])
#plot_graf("$\\theta_1$", "$d_1$", plotArray)

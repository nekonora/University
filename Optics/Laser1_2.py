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

_h = 			ne([18.0] * 10, 0.5)
_h1_h2o = ne([6.2] * 10, 0.5)
_h1_ple = ne([11.75] * 10, 0.5)
_h1_sci = ne([0] * 10, 0.5)

h = 		 misura(value= _h, name= "$h$")
h1_h2o = misura(value= _h1_h2o, name= "$h'$")
h1_ple = misura(value= _h1_ple, name= "$h'$")
h1_sci = misura(value= _h1_sci, name= "$h'$")

#---------------------------------------------------------------------------------------#
#-/////////////////////// VARIABLES ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_d = 			ne([27.8, 24.1, 20.0, 17.5, 15.2, 12.9, 11.3, 9.9, 8.1, 6.7], 0.05)
_thetaI = ne([78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.9, 64.0, 62.0, 60.0], 1.0)
_l_h2o = 	ne([13.4, 12.0, 10.3, 9.2, 7.9, 7.0, 6.2, 5.5, 4.5, 3.6], 0.5)

d = 		 misura(value= _d, name= "$d$")
thetaI = misura(value= _thetaI, name= "$\\theta_i$")
l_h2o =  misura(value= _l_h2o, name= "$l$")

#---------------------------------------------------------------------------------------#
#-/////////////////////// CALCULATIONS ////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
_thetaT_h2o = []
_nT_h2o = []
_index = []
_thetaT_Th = []

for i in range(len(_l_h2o)) :
	_thetaT_h2o.append( unp.arctan2(_l_h2o[i], _h1_h2o[i]) * 180 / np.pi)
	_nT_h2o.append( unp.sin(_thetaI[i] / 180 * np.pi) / unp.sin(_thetaT_h2o[i] / 180 * np.pi) )
	_index.append( (1.334 - _nT_h2o[i]) / 1.334 )
	_thetaT_Th.append(  asin( 0.749625 *  unp.sin(_thetaI[i] / 180 * np.pi) ) / np.pi * 180 ) 
	
thetaT_h2o = 	misura(value= _thetaT_h2o, name="$\\theta_t$")
nT_h2o =			misura(value= _nT_h2o, name="$n_{exp}$")
index = 			misura(value= _index, name="$(n - n_{exp}) / n$")
thetaT_Th =		misura(value= _thetaT_Th, name="$\\theta_t$")

### Correlazione lineare tra due valori (x,y)
fitLine = poly_fit(thetaI,thetaT_h2o)

#---------------------------------------------------------------------------------------#
#-/////////////////////// RESULTS /////////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#

### Printa il risultato in forma di tabella
print_results([h, d, h1_h2o, l_h2o, thetaI, thetaT_h2o, nT_h2o, index])

print("R^2: {}\n".format(fitLine[2]))

print(thetaT_Th.nominal)

### Plot: crea un array con argomenti (x, y, stile linea, xErr, yErr)
plotArray = np.array([thetaI, thetaT_h2o, "ko", True])
plotArrayTh = np.array([thetaI, thetaT_Th, "r-", False]) 
plot_graf("$\\theta_i$", "$\\theta_t$", plotArray, plotArrayTh)

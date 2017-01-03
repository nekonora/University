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
# Focale Positiva e Negativa
_dP = ne([1.0] * 6, 0.05)
dP = misura(value=_dP, name="$d$")

# Focale Negativa
_f1 = ne([7.5] * 6, 0.0) # Lente positiva nota, errore sconosciuto
f1 = misura(value=_f1, name="$f'$")

# Keplero
d0 = ufloat(3.0, 0.05)

#---------------------------------------------------------------------------------------#
#-/////////////////////// VARIABLES ///////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
# Focale Positiva
_pP = ne([10.8, 11.2, 12.0, 13.0, 14.0, 15.0], 0.05)
_qP = ne([79.2, 68.8, 48.7, 38.0, 31.3, 27.7], 0.05)
_d1P = ne([7.2, 6.1, 4.6, 2.9, 2.0, 1.5], 0.05)

pP = misura(value= _pP, name="$p$")
qP = misura(value= _qP, name="$q$")
d1P = misura(value= _d1P, name="$d'$")

# Focale Negativa
_pN = ne([6.8, 7.2, 7.2, 7.2, 7.2, 7.2], 0.05)
_tN = ne([5.6, 6.1, 7.6, 7.2, 6.8, 6.4], 0.05)
_q1N = ne([77.3, 48.7, 26.1, 29.6, 34.5, 40.4], 0.05)
_d1N = ne([4.1, 2.3, 1.1, 1.3, 1.5, 1.9], 0.05)

pN = misura(value=_pN, name="$p$")
tN = misura(value=_tN, name="$t$")
q1N = misura(value=_q1N, name="$q'$")
d1N = misura(value=_d1N, name="$d'$")

# Keplero
_z = ne([62, 602, 2060, 3165, 4365, 5105, 5855, 6317], 0.5)
_d = ne([6.0, 9.1, 13.0, 16.9, 19.4, 22.6, 27.4, 29.2], 0.05)

z = misura(value= _z, name="$z$")
d = misura(value= _d, name="$d$")

#---------------------------------------------------------------------------------------#
#-/////////////////////// CALCULATIONS ////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#
# Focale Positiva
_fP = []
_MP = []
_sommaMediaP = 0.0

for i in range(len(pP.value)) :
	_fP.append( 1 / ( (1/_pP[i]) + (1/_qP[i]) ))
	_MP.append( _d1P[i] / _dP[i])
	_sommaMediaP += _fP[i]

_mediaP = _sommaMediaP / 6 

fP = misura(value=_fP, name="$f$")
MP = misura(value=_MP, name="$M$")
mediaP = misura(value=_mediaP, name="Media")

# Focale Negativa
_p1N = []
_qN = []
_fN = []
_MN = []
_sommaMediaN = 0.0

for i in range(len(pN.value)) :
	_p1N.append(1 / ( 1/_f1[i] - 1/_q1N[i] ))
	_qN.append(_tN[i] - _p1N[i])
	_fN.append(1 / (1/_pN[i] + 1/_qN[i]))
	_MN.append(_d1N[i] / _d1P[i])
	_sommaMediaN += _fN[i]
	
_mediaN = _sommaMediaN / 6

p1N = misura(value=_p1N, name="$p'$")
qN = misura(value=_qN, name="$q$")
fN = misura(value=_fN, name="$f$")
MN = misura(value=_MN, name="$M$")
mediaN = misura(value=_mediaN, name="Media")

# Keplero
_z2 = []
_d2 = []
_theta = []

for i in range(len(z.value)) :
	_z2.append(_z[i] ** 2)
	_d2.append(_d[i] ** 2)
	_theta.append( sqrt((- d0 ** 2 + _d2[i]) / _z2[i]) )
	
z2 = misura(value= _z2, name="$z^2$")
d2 = misura(value= _d2, name="$d^2$")
theta = misura(value = _theta, name="$\\theta$")

### Correlazione lineare tra due valori (x,y)
#fitLine = poly_fit(x,y)

#---------------------------------------------------------------------------------------#
#-/////////////////////// RESULTS /////////////////////////////////////////////////////-#
#---------------------------------------------------------------------------------------#

### Printa il risultato in forma di tabella
# Focale Positiva
print_results([pP, qP, fP, dP, d1P, MP])
print(mediaP.value)

print_results([pN, qN, fN, p1N, q1N, f1, tN, dP, d1N, MN])
print(mediaN.value)

# Keplero
print_results([z, d, z2, d2, theta])

#print("R^2: {}\n".format(fitLine[2]))

### Plot: crea un array con argomenti (x, y, stile linea, xErr, yErr)
#plotArray = np.array([x, y, "ko", True])
#plot_graf("$\\theta_i$", "$\\Theta$", plotArray)

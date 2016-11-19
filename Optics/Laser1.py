import numpy as np
import pylab as pl

# Plotter
def plot_graf(*args) :
	if args :
		for ar in args :
			pl.plot(ar[0], ar[1], ar[2])
	pl.xlabel("$\\theta_i$")
	pl.ylabel("$\\Theta$")
	pl.title("")
	pl.grid(True)
	pl.show()

# Polynomial Regression
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
	
# Varibles	
theta0 = np.array([0] * 10)
theta1 = np.array([45,42,40,38,36,30,26,22,20,18])
thetaI = theta1
y = np.array([25] * 10)
x = np.array([0,2.4,4.1,5.9,7.9,14.2,19.4,25.7,30.3,34.5])

# Calculations
Theta = np.arctan2(y,x) * 180 / np.pi
index = thetaI * 2 - Theta
fitLine = poly_fit(thetaI,Theta, 1)

# Errors
errTheta = np.array([0.0] * 10)
for i in range(10) :
	errTheta[i] = np.sqrt((0.025) / (x[i] ** 2 + y[i] ** 2)) * 180 / np.pi

# Results
print("| $\\theta_0$ | $\\theta '$ | $\\theta_i$ | $y$ | $x$ | $\\Theta$ | $\\sigma \\Theta$ | $2 \\theta_i - \\Theta$ |")
print("|-----:|-----:|-----:|-----:|-----:|-----:|------:|-----:|")
for row in zip(theta0,theta1,thetaI,y,x,Theta,errTheta,index) :
	print("| {} | {} | {} | {} | {} | {:.2f} | $\\pm$ {:.2f} | {:.2f} |".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
	
print("\nMedia indice: {}".format(np.mean(index)))
print("R^2: {}\n".format(fitLine[2]))

plotArrayTheta = np.array([thetaI, Theta, "ko"])
plotArrayThetaFit = np.array([thetaI, thetaI * fitLine[0] + fitLine[1], "-k"])
plotArrayThetaTheoric = np.array([thetaI, thetaI * 2, "-r"])
plot_graf(plotArrayTheta, plotArrayThetaFit, plotArrayThetaTheoric)



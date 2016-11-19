import numpy as np

# Variabili
# ---------
diamIniz = 0.2 																	# d_0
diametro = [0.2,0.58,1.1,1.8,2.9] 							# d
distanza = [80.0,324.0,572.0,1170.0,2426.0] 		# z

# Quadrati
# --------
d02 = diamIniz ** 2
dz2 =  [0.0,0.0,0.0,0.0,0.0] 
for i in range(5) :
	dz2[i] = diametro[i] ** 2
z2 =   [0.0,0.0,0.0,0.0,0.0] 
for i in range(5) :
	z2[i] = distanza[i] ** 2

# Angoli
# ------	
theta = np.array([0.0,0.0,0.0,0.0,0.0]) 
for i in range(5) :
	theta[i] = np.sqrt( (- d02 + dz2[i])  / z2[i] )

# Print
# -----
print("--- Telescopio Keplero ---\n")
print("z:      {:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}\n".format(*distanza))
print("d:      {:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}\n".format(*diametro))
print("z^2:    {:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}\n".format(*z2))
print("d^2:    {:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}\n".format(*dz2))
print("theta:  {:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}\n".format(*theta)) 

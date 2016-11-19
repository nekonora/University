import numpy as np

# Fenditura Orizzontale
# Variabili
# ---------

# mm, fenditura schermo
L = [780.0, 700.0, 630.0, 560.0, 490.0, 420.0, 380.0, 340.0, 300.0, 220.0, 150.0] 
# mm, diametro banda nera
d = np.array([40.5, 36.4, 32.6, 28.9, 25.6, 21.4, 20.0, 18.0, 15.2, 11.6, 7.7]) / 2.0

# Calcoli
# -------
ran = 11
lam = 632.8 * (10 ** (-6))
theta = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	theta[i] = np.arctan2((d[i] / 2), L[i])
D = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	D[i] = ((1.0 * lam) / np.sin(theta[i]))
indice = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	indice[i] = (D[i] ** 2) / (L[i] * lam)

# Print
# -----

print("- - - - Fenditura orizzontale (primo minimo) - - - -\n")
print("L (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*L))
print("x (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*d))
print("theta (rad):      {:.4f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*theta))
print("D (mm):           {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*D))


# FRAUNHOFER Opzionale
# Variabili
# ---------

# mm, fenditura schermo
op_L = [780.0, 700.0, 630.0, 560.0, 490.0, 420.0, 380.0, 340.0, 300.0, 220.0, 150.0] 
# mm, diametro banda nera
op_d = np.array([79.0, 71.2, 64.6, 57.6, 50.0, 42.6, 39.0, 34.3, 30.1, 22.1, 14.8]) / 2

# Calcoli
# -------
op_theta = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	op_theta[i] = np.arctan2((op_d[i] / 2), op_L[i])
op_D = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	op_D[i] = ((2.0 * lam) / np.sin(op_theta[i]))
op_indice = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(ran) :
	op_indice[i] = (op_D[i] ** 2) / (op_L[i] * lam)

# Print
# -----

print("- - - - Fenditrura orizzontale (secondo minimo) - - - -\n")
print("L (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*op_L))
print("x (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*op_d))
print("theta (rad):      {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*op_theta))
print("D (mm):           {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*op_D))

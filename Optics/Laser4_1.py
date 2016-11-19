import numpy as np

# Fenditura destra (sinistra coperta)
# Variabili
# ---------

L = np.array([780.0, 700.0, 630.0, 560.0, 490.0]) 
d = np.array([23.9, 21.8, 19.5, 17.3, 15.2]) / 2.0

# Calcoli
# -------
lam = 632.8 * (10 ** -6)
theta = np.array([0.0] * 5)
for i in range(5) :
	theta[i] = np.arctan2(d[i], L[i])
D = np.array([0.0] * 5)
for i in range(5) :
	D[i] = ((1.0 * lam) / np.sin(theta[i]))

# Print
# -----

print("\n\n- - - - Fenditura destra (sinistra coperta) - - - -\n")
print("L (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*L))
print("x (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*d))
print("theta (rad):      {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*theta))
print("l (mm):           {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*D))


# Fenditura destra (sinistra coperta)
# Variabili
# ---------

_L = np.array([780.0, 700.0, 630.0, 560.0, 490.0]) 
_d = np.array([23.2, 21.8, 19.8, 17.5, 15.1]) / 2.0

# Calcoli
# -------
_theta = np.array([0.0] * 5)
for i in range(5) :
	_theta[i] = np.arctan2(_d[i], _L[i])
_D = np.array([0.0] * 5)
for i in range(5) :
	_D[i] = ((1.0 * lam) / np.sin(_theta[i]))

# Print
# -----

print("\n\n- - - - Fenditura sinsitra (destra coperta) - - - -\n")
print("L (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*_L))
print("x (mm):           {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*_d))
print("theta (rad):      {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(*_theta))
print("l (mm):           {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(*_D))


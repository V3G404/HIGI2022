import numpy as np
import matplotlib.pyplot as plt
import scipy.constants

#Este es un comentario feliz :)

print("Hola mundo")

#Temperatura del Universo
	#Radiación cósmica de fondo de microondas.
	
''' Aquí tendremos una ecuación que describe la temperatura del universo: '''


def intensity(v, T):
	
	c=constants.value(u"speed of light in vacuum")
	h=constants.value(u"Planck constant")
	k=constants.value(u"Boltzmann constant")
	
	# v=v*c*100
	
	#Esta conversión es porque la frecuencia viene en unidades de 1/cm, se cambia 1/s a 1/cm
	fact = h*v/(k*T)
	I = (h*v**3/c**2)*(1/(np.exp(fact)-1))
	return intensity
	
def SI_to_MJanksy(value_SI):
	return value_SI/1e-26/1e6
	
data=np.loadtxt("IRCF.txt").T
v=data[0]
I=data[1]
Ierr=data[3]

plt.plot(v, intensity(v,5))
plt.show()
plt.errorbar(v, I, Ierr)
plt.show()

intensity2=SI_to_Mjansky(intensity(v,2))
plt.plot(v, intensity2)
plt.show()

plt.plot(v, intensity2)
plt.errorbar(v, I, Ierr)
plt.show()


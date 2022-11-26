import numpy as np
import matplotlib.pyplot as plt

def Ctok(T):
	return T+273.15
	
print("Hola mundo")
Ti=float(input("Dame la temperatura inicial"))
Tf = float(input("Dame la temperatura final"))
n=int(input("Dame el número de elementos))
delta = (Tf-Ti)/n

print("i TC TK")
for i in range(n):

T=Ti+i*delta
Tk=CtoK(T)
print(i,T,Tk)


#Definition of phi=rho'(x)/x and psi=phi'(x)/x
import numpy as np

def rho(x,gamma):
    if x<-gamma:return -x-gamma/3
    elif x<0:return x**3/3/gamma**2+x**2/gamma
    elif x<gamma:return -x**3/gamma**2/3+x**2/gamma
    else:return x-gamma/3
    
def phi(x,gamma):
    if x<-gamma:return -1/x
    elif x<0:return x/gamma**2+2/gamma
    elif x<gamma:return -x/gamma**2+2/gamma
    else:return 1/x

def psi(x,gamma):
    x=abs(x)
    if x<gamma:return -1/gamma**2/x
    else:return -1/x**3


#Vectorial functions
def rho_vec(x,gamma):
    x = np.abs(x)
    return np.where(x<gamma,-x**3/3/gamma**2+x**2/gamma,x-gamma/3)

def phi_vec(x,gamma):
    x = np.abs(x)
    return np.where(x<=gamma,-x/gamma**2+2/gamma,1/x)

def psi_vec(x,gamma):
    x = np.abs(x)
    return np.where(x<gamma,-1/x/gamma**2,-1/x**3)

#Def of psi(x).x since useful when we use only 1 linear operator and avoids singularity
def psix_vec(x,gamma):
    return np.where(np.abs(x)<gamma,-1/gamma**2,-1/x**2)
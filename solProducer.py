from  consts import *
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import scipy.linalg as slin
def hx(k):
    return mu+r*np.cos(k)
def hz(k):
    return r*np.sin(k)

def phi0(k):

    h1Val=hx(k)
    h3Val=hz(k)
    if h1Val !=0:
        xzsum2=h1Val**2+h3Val**2
        nn2=2*xzsum2+2*h3Val*np.sqrt(xzsum2)
        nn=np.sqrt(nn2)
        rst=[-h1Val/nn,(h3Val+np.sqrt(xzsum2))/nn]
        return np.array(rst)
    else:
        if h3Val>0:
            return np.array([0,1])
        else:
            return np.array([-1,0])

def Hf(k):
    sx=np.zeros((2,2),dtype=complex)
    sz=np.zeros((2,2),dtype=complex)
    sx[0,1]=1
    sx[1,0]=1
    sz[0,0]=1
    sz[1,1]=-1
    rst=hx(k)*sx+(hz(k)+1j*gam/2)*sz
    return rst

def U(s,k):
    return slin.expm(-1j*s*Hf(k))

def calZ(s,k):
    phi0k=phi0(k)
    UMat=U(s,k)

    zTmp=np.conj(phi0k.transpose()).dot(UMat).dot(phi0k)
    return zTmp



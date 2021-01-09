from solProducer import *


def realAndImag(vars):
    sEst = vars[0]
    kEst = vars[1]
    zTmp = calZ(sEst, kEst)
    return (np.real(zTmp), np.imag(zTmp))


sEst=2
kEst= 1.7907078125461822
inVars=[sEst,kEst]
s,k=fsolve(realAndImag,(sEst,kEst))
print("time = ",s)
print("momentum = ",k)


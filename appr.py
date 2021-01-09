from solProducer import *

def kAndSortZ(s):
    zAllAtQ=[]
    for kInd in range(0,N+1):
        zAllAtQ.append(calZ(s,kInd*dk))
    zAllAbs=[]
    for elem in zAllAtQ:
        zAllAbs.append(np.abs(elem))

    sort_ind=np.argsort(zAllAbs)
    return [sort_ind,zAllAtQ,zAllAbs]


sEst=2
inds,zs,zabs=kAndSortZ(sEst)
print("kEst = ",inds[0]*dk,zs[inds[0]],zabs[inds[0]])


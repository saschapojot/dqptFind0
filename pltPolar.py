from solProducer import *

s0=4.704184154472671
k0=1.2723755482642118
m=100
m1=50
kstart=k0-0.5
kend=k0+0.5
ksmallstart=k0-0.01
ksmallend=k0+0.01
ksmallSeq=np.linspace(start=ksmallstart,stop=ksmallend,num=m1)
tsmall=[np.real(-1j*np.log(calZ(s0,kVal)/np.abs(calZ(s0,kVal)))) for kVal in ksmallSeq]
r1=np.empty(len(tsmall))
r1.fill(1)
eps=1e-10
ktinystart=k0-eps
ktinyend=k0+eps
nnn=30
ktinyseq=np.linspace(start=ktinystart,stop=ktinyend,num=nnn)
ttiny=[np.real(-1j*np.log(calZ(s0,kVal)/np.abs(calZ(s0,kVal)))) for kVal in ktinyseq]
rtt=np.empty(len(ktinyseq))
rtt.fill(1)
kred=k0
tred=np.real(-1j*np.log(calZ(s0,kred)/np.abs(calZ(s0,kred))))
kSeq=np.linspace(start=kstart,stop=kend,num=m)
thSeq=[np.real(-1j*np.log(calZ(s0,kVal)/np.abs(calZ(s0,kVal)))) for kVal in kSeq]
r=np.empty(len(thSeq))
r.fill(1)

fig=plt.figure()
ax=fig.add_subplot(111,polar=True)
a=ax.scatter(thSeq,r,c="black",alpha=0.01)
b=ax.scatter(tsmall,r1,c="red",alpha=0.01)
c=ax.scatter(tred,1,c="red",alpha=0.01)
d=ax.scatter(ttiny,rtt,c="blue",alpha=0.5)
plt.show()
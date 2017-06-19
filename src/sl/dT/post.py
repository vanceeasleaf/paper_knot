import numpy as np
data=[]
kapitza=[]
i=-1
for dT in range(0,60,10):
	i+=1
	p=np.loadtxt(str(i)+'/tempAve.txt',skiprows=1)
	data.append([p[:,1],p[:,3],'dT='+str(dT)])
	dataT=p[30,3]-p[20,3]
	j=(p[:,4]*p[:,2]).sum()/p[:,2].sum()
	kapitza.append([dT,np.abs(j)/dataT])
kapitza=np.array(kapitza)
from aces.graph import series,plot,fig,pl
series(xlabel='x (Angstrom)',ylabel='Temperature (K)'
	,datas=data,
	filename='profile.png')
with fig('kapitza.png'):
	x=kapitza[:,0]
	y=kapitza[:,1]
	pl.plot(x,y,marker='v',ms=12,mec='b',mfc='w',mfcalt="w",mew=1.5,linewidth=1)
	pl.xlabel('dT(K)')
	pl.ylabel('Kapitza Conductance (W/m2K)')
	pl.xlim([-5,55])
#plot([kapitza[:,0],'dT(K)'],[kapitza[:,1],'Kapitza Conductance (W/m2K)'],'kapitza.png')

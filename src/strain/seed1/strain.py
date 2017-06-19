
import numpy as np
from aces.tools import *
x=np.load('cache.npz')
d=x['d']
c=[]
for s,v in d:
	c.append(s)
from aces.graph import fig,pl
#c=np.array(c)
#series(xlabel='Strain',
#	ylabel='Stress (GPa)',
#	datas=datas
#	,linewidth=1
#	,filename='stress_strain.png',legend=False,grid=True)
s=[]
for i,u in enumerate(c):
	if not len(u)==len(c[0]):print i;continue
	s.append(u)
s=np.array(s)
x=s[0,:,0]
y=s[:,:,1].mean(axis=0)
dy=s[:,:,1].std(axis=0)
y1=y+dy/2.0
y2=y-dy/2.0
with fig("ave_stress.png"):
	pl.fill_between(x,y1,y2,color="#cccccc")
	pl.plot(x,y,lw=2,color='r')
	pl.xlabel('Strain')
	pl.ylabel('Stress (GPa)')
	pl.xlim([0,0.8])
	pl.ylim([0,21])
with fig('stress_strain.png'):
	for y in s[:,:,1]:
		pl.plot(x,y,color="black",alpha=0.01)
		pl.xlabel('Strain')
		pl.ylabel('Stress (GPa)')
		pl.xlim([0,0.8])
		pl.ylim([0,30])


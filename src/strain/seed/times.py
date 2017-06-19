datas=[]
c=[]
import pandas as pd
import numpy as np

from aces.tools import *
breakstrains=[]
breaktimes=[]
def getBreakStrains(s):
	v=[]
	n=30
	for j,u in enumerate(s[n:-n,1]):
		var=abs(s[j+n,1]-s[j+n-1,1])
		if var>2.5 and var>s[j:j+n,1].std():
			if len(v)>0 and j-v[-1]<n:continue
			v.append(j+n)
	return np.array(v)
i=0
for T in range(100,300,40):
	for seed in range(100,110):
		s=np.loadtxt(str(i)+"/cal_stress.txt",skiprows=1)
		v=getBreakStrains(s)
		breakstrains.append(v)
		if abs(s[-1,1])<.5:
			breaktimes.append(len(v)) # break up
		else:
			breaktimes.append(-len(v)) #not break up
		i+=1
		print s[v,0],breaktimes[-1]
for u in s:
	pass

from aces.graph import series,plot

series(xlabel='Strain',
	ylabel='Stress (GPa)',
	datas=datas
	,linewidth=1
	,filename='stress_strain.png',legend=False,grid=True)
x=c[:,0,:].mean(axis=0)
y=c[:,1,:].mean(axis=0)
plot([x,'Strain'],[y,'Stress (GPa)'],filename='ave_stress.png')

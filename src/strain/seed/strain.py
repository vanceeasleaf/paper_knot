datas=[]
c=[]
import pandas as pd
import numpy as np
from aces.tools import *
i=0
for T in range(100,300,40):
	for seed in range(100,110):
		#if not T==260:
		#	i+=1
		#	continue;
		df=pd.read_csv(str(i)+"/cal_stress.txt",sep=r"[ \t]",engine="python");
		datas.append([df['Strain'],df['Stress_GPa'],"seed="+str(seed)])
		c.append([df['Strain'],df['Stress_GPa']])
		i+=1
c=np.array(c)

from aces.graph import series,plot

series(xlabel='Strain',
	ylabel='Stress (GPa)',
	datas=datas
	,linewidth=1
	,filename='stress_strain.png',legend=False,grid=True)
x=c[:,0,:].mean(axis=0)
y=c[:,1,:].mean(axis=0)
plot([x,'Strain'],[y,'Stress (GPa)'],filename='ave_stress.png')

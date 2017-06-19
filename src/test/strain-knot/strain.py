datas=[]
import pandas as pd
import numpy as np
from aces.tools import *
youngs=[]
temps=np.arange(100,300,20)
sel=np.arange(0,10,2)
for i in sel:
	print i
	cd(str(i*2+1))
	#from aces.App import App
	#App().runner.post()
	
	df=pd.read_csv("cal_stress.txt",sep=r"[ \t]",engine="python");
	datas.append([df['Strain'],df['Stress_GPa'],str(temps[i])+'K'	])
	cd('..')
for i in np.arange(0,10):
	print i
	cd(str(i*2))
	youngs.append(float(read("YoungsModulus.txt")))
	cd('..')
from aces.graph import series,plot

series(xlabel='Strain',
	ylabel='Stress (GPa)',
	datas=datas
	,linewidth=1
	,filename='stress_strain.png',legend=True,grid=True)
plot((np.array(temps),'Temperature (K)'),(np.array(youngs),'Young\'s Modulus (GPa)'),'youngs.png')
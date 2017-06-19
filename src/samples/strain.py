datas=[]
c=[]
import pandas as pd
import numpy as np
from aces.tools import *
i=0
for lx in range(60,200,30):
	dir=str(i)
	#if not T==260:
	#	i+=1
	#	continue;
	df=np.loadtxt(dir+"/cal_stress.txt",skiprows=1)
	datas.append([df[:,0],df[:,1],"lx="+str(lx)])
	c.append(df)
	i+=1
from aces.graph import series,plot
#c=np.array(c)
series(xlabel='Strain',
	ylabel='Stress (GPa)',
	datas=datas
	,linewidth=1
	,filename='stress_strain.png',legend=True,grid=True)
from aces.modify import atoms_from_dump as afd
from aces.f import writevasp
def dump2POSCAR(dumpname,poscar='POSCAR'):
	atoms=afd(filename=dumpname,elements=['C'])
	atoms.center(vacuum=1.0,axis=[1,2])
	writevasp(atoms,poscar)
	atoms.write(poscar+'.png')
from aces.strain import strain as sss
i=-1
for lx in range(60,200,30):
	print lx
	i+=1
	dir=str(i)
	dump=sss(dir+'/dump.lammpstrj')
	N=8
	for j in range(N):
		index=int(500000/2000+j*2000000.0/4/2000/N)
		s=dump.grep(index)
		file='data/%s_%s'%(lx,0.05*j/N)
		write(s,file+".trj")
		dump2POSCAR(file+".trj",poscar=file+".poscar")





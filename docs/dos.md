
# Density of States 


## graphene
> auto-correlation function with the two ends fixed

``` python
from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene",
			method="nvt",
			nodes=1,
			procs=12,
			queue="q1.1",
			runTime=500000
			,runner="correlation"
		)
		app=dict(userMini=False,corrNVT=True,timestep=.182e-3,latx=70,laty=2)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()

```
## knot
> same but with the knot

``` python
from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene_knot",
			method="nvt",
			nodes=1,
			procs=12,
			queue="q3.4",
			runTime=500000
			,runner="correlation"
		)
		app=dict(corrNVT=True,timestep=.182e-3,latx=70,laty=2)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
```
`regiondos.py` calculates the dos of the two regions

``` python
from ase import io
import numpy as np 
atoms=io.read('minimize/POSCAR')
bulk=np.abs(atoms.positions[:,0]-20)<20 
knot=np.abs(atoms.positions[:,0]-70)<20
index=np.arange(len(atoms),dtype='int')-10
def filt(a):
	return a[(a>=0) *(a<520)]
from aces.dos import plot_regiondos
plot_regiondos([(filt(index[bulk]),'bulk'),(filt(index[knot]),'knot')])
```
`muldos.py` draw graphene dos and two region dos of knot

``` python
import pandas as pd
df=pd.read_csv("region_dos.txt",sep=r"[ \t]",engine="python");
npair=len(df.columns)/2
datas=[]
for i in range(npair):
	rname=df.columns[i*2][5:]
	datas.append((df['freq_'+rname],df['dos_'+rname],"region:"+rname))
dc=pd.read_csv("graphenedos.txt",sep=r"[ \t]",engine="python");
datas.append((dc[dc.columns[0]],dc[dc.columns[1]],'GNR'))
from aces.graph import series
series(xlabel='Frequency (THz)',
	ylabel='Phonon Density of States',
	datas=datas
	,linewidth=1
	,filename='camparedos.png',legend=True,xmax=60)
```
### result
![](images/camparedos.png)
<style>img{background:white;width:100%;}</style>

## lc
> method=greekubo so it's periodic along x direction

``` python
from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene_knot",
			method="greenkubo",
			nodes=1,
			procs=12,
			queue="q1.1",
			runTime=500000
			,runner="correlation"
		)
		app=dict(usephana=False,atomfile='POSCAR',corrNVT=False,timestep=.182e-3,)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
```

## ph
> phonopy calculation at gamma point of knot

``` python
from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene_knot",
			method="greenkubo",
			nodes=1,
			procs=12,
			queue="q1.1",
			runTime=500000
			,runner="phonopy"
		)
		app=dict(kpoints=[1,1,1],gamma_only=True,useMini=True,boxOpt=False,timestep=.182e-3,atomfile="POSCAR")
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
```

## ph_graphene
> the same but with the graphene ribbon

``` python
from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene_knot",
			method="greenkubo",
			nodes=1,
			procs=4,
			queue="q1.1",
			runTime=500000
			,runner="phonopy"
		)
		app=dict(kpoints=[1,1,1],gamma_only=True,
		useMini=True,boxOpt=False,timestep=.182e-3,atomfile="POSCAR")
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
```
## ph_graphene_bulk
> the participation ratio of the above result is found not exactly 1.0, the reason is the periodic condiction is p s s but not p p p. So another calculation is carried out

``` python
from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene",
			method="greenkubo",
			nodes=1,
			procs=4,
			queue="q1.1",
			runTime=500000
			,runner="phonopy"
		)
		app=dict(kpoints=[1,1,1],gamma_only=True,
		useMini=True,boxOpt=False,timestep=.182e-3,atomfile="POSCAR")
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
```

## ph_g
> the participation ratio of the above result is found not exactly 1.0, the partial_dos is right. to verify the phonopy code, we calculate the result of unitcell graphene . and the result is 1.0. 

``` python
from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene",
			method="greenkubo",
			nodes=1,
			procs=4,
			queue="q1.1",
			runTime=500000
			,runner="phonopy"
		)
		app=dict(kpoints=[30,30,1],useMini=True,
		boxOpt=False,timestep=.182e-3,supercell=[5,5,1])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()

```

## ph1
> use boxOpt=True to overcome negative frequency

## ph_graphene_bulk1
> use boxOpt=True to overcome negative frequency


--




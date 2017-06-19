from aces.tools import *
from ase import io
for i in [60,90,120,150]:
	atoms=io.read('data/%d_0.0.poscar'%i,format='vasp')
	lx=atoms.positions[:,0].max()-atoms.positions[:,0].min()
	latx=int(lx/(152.489753098/60))
	write("%d\t%d\n"%(i,latx),'lxs.txt','a')
	

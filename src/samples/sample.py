# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-05-29 19:29:27
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-05-29 19:41:06
from aces.tools import *
from aces.modify import atoms_from_dump as afd
from aces.f import writevasp
def dump2POSCAR(dumpname,poscar='POSCAR'):
	atoms=afd(filename=dumpname,elements=['C'])
	atoms.center(vacuum=10,axis=[1,2])
	atoms.center(vacuum=2,axis=[0])
	writevasp(atoms,poscar)
	atoms.write(poscar+'.png')
from aces.strain import strain as sss
dump=sss('0/drag/dump.lammpstrj')
index=115
s=dump.grep(index)
file='data/drag_60_%s'%index
write(s,file+".trj")
dump2POSCAR(file+".trj",poscar=file+".poscar")
# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-03 20:02:55
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-03 20:07:13
from ase import io 
atoms=io.read('POSCAR')
filter=atoms.positions[:,0]<atoms.positions[:,0].max()-5.17286
del atoms[filter]
atoms.cell[0,0]=5.17286
atoms.center(axis=0)
from aces.io.vasp import writevasp
writevasp(atoms,'POSCAR1')
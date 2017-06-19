# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-05-30 21:36:47
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-05-30 21:40:40
from aces.phononyaml import phononyaml
import numpy as np
mesh=phononyaml('mesh.yaml')
vec=[]
for i in range(0,mesh.natom):
	vec.append(mesh.atom(0,0,i)) 
vec=np.array(vec).real
from ase import io 
atoms=io.read('POSCAR')
atoms.positions+=vec*5 
from aces.f import writevasp
writevasp(atoms,'POSCARvec')
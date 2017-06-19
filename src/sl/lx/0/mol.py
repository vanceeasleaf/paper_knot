# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2016-06-03 19:59:11
# @Last Modified by:   YangZhou
# @Last Modified time: 2016-06-03 19:46:53
from ase import io,Atoms
atoms=io.read('minimize/POSCAR')
atoms.write('atoms.mol')
# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-07 14:53:47
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-07 14:54:02
from aces import Aces
#the origin BP structure is optimized and we use it directly
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="Bi4I4_computed",
			method="greenkubo",
			nodes=1,
			procs=12,
			queue="q1.4",
			runTime=10000000
			,runner="negf"
		)
		app=dict(fmax=5.0,useMini=False,shengcut=-4,kpoints=[8,8,8],engine='vasp',supercell=[4,3,3],th=True,mekpoints=[4,4,4],ekpoints=[2,2,2])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()

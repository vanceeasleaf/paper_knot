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

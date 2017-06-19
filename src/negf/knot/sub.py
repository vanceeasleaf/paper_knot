from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene",
			method="greenkubo_knot",
			nodes=1,
			procs=4,
			queue="q1.1",
			runTime=500000
			,runner="negf"
		)
		app=dict(atomfile="POSCAR",kpoints=[1,1,1],gamma_only=True,useMini=True,boxOpt=True,timestep=.182e-3)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()

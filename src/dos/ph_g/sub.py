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
		app=dict(kpoints=[20,20,1],useMini=True,boxOpt=True,timestep=.182e-3,supercell=[5,5,1])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()

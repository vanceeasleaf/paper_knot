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

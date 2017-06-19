from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="Ar",
			method="greenkubo",
			nodes=1,
			procs=12,
			queue="q1.4",
			runTime=10000
			,runner="negf"
		)
		app=dict(supercell=[1,1,1],latx=3,laty=1,latz=1)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()


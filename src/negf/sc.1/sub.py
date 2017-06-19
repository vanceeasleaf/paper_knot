from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="SC",
			method="greenkubo",
			nodes=1,
			procs=12,
			queue="q1.4",
			runTime=10000
			,runner="negf"
		)
		app=dict(fmax=0.2,supercell=[1,1,1],latx=4,laty=3,latz=1)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()


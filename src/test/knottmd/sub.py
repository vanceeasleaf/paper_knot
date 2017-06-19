from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene_knot",
			method="nvt",
			nodes=1,
			procs=12,
			queue="q1.1",
			runTime=10000000
			,runner="mdTc"
		)
		app=dict(latx=70,laty=2)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()

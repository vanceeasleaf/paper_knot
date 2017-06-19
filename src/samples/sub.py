from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene_knot",
			method="nvt",
			nodes=1,
			procs=4,
			queue="q1.4",
			runTime=10000000
			,runner="strain"
		)
		for lx in range(60,200,30):
			app=dict(latx=lx,laty=2,maxStrain=.2)
			self.commit(opt,app);
if __name__=='__main__':
	sub().run()

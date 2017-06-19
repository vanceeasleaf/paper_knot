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
			runTime=500000
			,runner="strain"
		)
		for T in range(100,300,20):
			app=dict(vStrain=True,reverseStrain=True,equTime=200000,T=T,strainStep=1000,minStrain=0.05,maxStrain=-0.15,timestep=.3e-3,latx=70,laty=2)
			self.commit(opt,app);
if __name__=='__main__':
	sub().run()

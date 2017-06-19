from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene",
			method="nvt",
			nodes=1,
			procs=4,
			queue="q1.4",
			runTime=500000
			,runner="strain"
		)
		app=dict(reverseStrain=True,vStrain=True,maxStrain=0.1,minStrain=-0.1,equTime=000000,strainStep=1000,timestep=.5e-3,latx=30,laty=2)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()

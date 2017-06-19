#for different temperatures(100,140,180,220,260) and different seed 
from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene_knot",
			method="nvt",
			nodes=1,
			procs=2,
			queue="q1.1",
			runTime=500000
			,runner="strain"
		)
		for T in range(100,300,40):
			for seed in range(100,110):
				app=dict(vStrain=True,seed=seed,equTime=200000,T=T,strainStep=1000,maxStrain=0.3,timestep=.3e-3,latx=70,laty=2)
				self.commit(opt,app);
if __name__=='__main__':
	sub().run()

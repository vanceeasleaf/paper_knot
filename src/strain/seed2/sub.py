#for different temperatures(100,140,180,220,260) and different seed 
from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene_knot",
			method="nvt",
			nodes=1,
			procs=1,
			queue="q1.4",
			runTime=500000
			,runner="strain"
		)
		for seed in range(400,600):
			app=dict(useMini=False,atomfile='POSCAR',vStrain=True,seed=seed,equTime=200000,strainStep=1000,maxStrain=0.9,timestep=.3e-3,latx=70,laty=2)
			self.commit(opt,app);
if __name__=='__main__':
	sub().run()

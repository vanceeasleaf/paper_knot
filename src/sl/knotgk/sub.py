#for different temperatures(100,140,180,220,260) and different seed 
from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene_knot",
			method="greenkubo",
			nodes=1,
			procs=4,
			queue="q1.1",
			runTime=10000000,nvt=True
			,xp=1,runner="mdTc",latx=1,useMini=False,timestep=.1e-3,laty=1,latz=1
		)
		N=8
		for i in range(20):
				file='60_0.0.poscar'
				app=dict(atomfile=file,seed=100+i)
				self.commit(opt,app);
if __name__=='__main__':
	sub().run()

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
			queue="q1.1",
			runTime=10000000
			,runner="mdTc",dT=100,useMini=False,laty=1,latz=1,latx=3
		)
		for i in range(3,20,4):
			app=dict(atomfile='POSCAR',timestep=.3e-3/i)
			self.commit(opt,app);
if __name__=='__main__':
	sub().run()

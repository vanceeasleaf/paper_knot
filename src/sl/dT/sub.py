#for different temperatures(100,140,180,220,260) and different seed 
from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene_knot",
			method="nvt",
			nodes=1,
			procs=6,
			queue="q1.4",
			runTime=20000000,nvt=True
			,runner="mdTc",atomfile='POSCAR',latx=1,useMini=False,timestep=.1e-3,laty=1,latz=1
		)
		for dT in range(0,60,10):
			app=dict(dT=dT)
			self.commit(opt,app);
if __name__=='__main__':
	sub().run()

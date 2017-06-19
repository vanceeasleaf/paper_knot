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
			queue="q1.1",
			runTime=10000000,nvt=True
			,runner="mdTc",dT=50,latx=1,useMini=False,timestep=.1e-3,laty=1,latz=1
		)
		file='drag_60_115.poscar'
		app=dict(atomfile=file,equTime=0)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()

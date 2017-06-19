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
			,runner="mdTc",dT=100,nvt=True,useMini=False,timestep=.1e-3,laty=1,latz=1
		)
		for lx,procs,nodes in [(1,4,1),(2,4,1),(3,6,1),(5,6,1),(9,12,1),(13,12,3)]:
			app=dict(nodes=nodes,procs=procs,atomfile='POSCAR',latx=lx)
			self.commit(opt,app);
if __name__=='__main__':
	sub().run()

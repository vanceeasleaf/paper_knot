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
			runTime=20000000,nvt=True
			,runner="mdTc",dT=50,latx=1,useMini=False,timestep=.1e-3,laty=1,latz=1
		)
		N=8
		for lx,procs,nodes in [(60,6,1),(90,6,1),(120,12,1),(150,12,1)]:
			for j in range(N):
				file='%s_%s.poscar'%(lx,0.05*j/N)
				app=dict(atomfile=file,nodes=nodes,procs=procs)
				self.commit(opt,app);
if __name__=='__main__':
	sub().run()

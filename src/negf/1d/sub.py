from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="FPU",
			method="greenkubo",
			nodes=1,
			procs=4,
			queue="q1.4",
			runTime=10000
			,runner="negf"
		)
		app=dict(fpug=0.0,fpua=True,kpoints=[131,1,1],fpubeta=0.0,dumpRate=100,supercell=[1,1,1],T=20,dimension=1,useMini=False,latx=20,laty=1)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()


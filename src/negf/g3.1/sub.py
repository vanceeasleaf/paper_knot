from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene",
			method="greenkubo",
			nodes=1,
			procs=12,
			queue="q1.1",
			runTime=500000
			,runner="negf"
		)
		app=dict(kpoints=[1,1,1],laty=1,latx=3,leadlat=[1,1,1],gamma_only=False,useMini=True,boxOpt=True,timestep=.182e-3)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()

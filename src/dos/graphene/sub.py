from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="graphene",
			method="nvt",
			nodes=1,
			procs=12,
			queue="q1.1",
			runTime=500000
			,runner="correlation"
		)
		app=dict(userMini=False,corrNVT=True,timestep=.182e-3,latx=70,laty=2)
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()

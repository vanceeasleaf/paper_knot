from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="C2Nh2d",
			method="nvt",
			nodes=16,
			procs=1,
			queue="q3.4",
			runTime=10000000
			,runner="negf"
		)
		app=dict(kpoints=[15,15,1],latx=1,laty=1,latz=1,supercell=[1,1,1])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()

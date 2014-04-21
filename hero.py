import enemy
from enemy import *
class CHero(CEnemy):
	def clean(self,fair=True):
		if fair:
			self.skill = dice()+6
			self.stamina = dice(2)+12
			self.luck = dice()+6
		else:
			self.skill = 12
			self.stamina = 24
			self.luck = 12
		self.maxskill = self.skill
		self.maxstamina = self.stamina
		self.maxluck = self.luck
		self.damage = 2
		self.alive = True
	def __init__(self,fair=True):
		self.clean(fair)
	def heal(self,diff):
		self.stamina = self.stamina + diff
		self.stamina = min(self.stamina,self.maxstamina)
	def testluck(self):
		self.luck = self.luck-1
		return(self.luck > dice(2))
	def testskill(self):
		return self.skill>=dice(2)






from random import randint
def dice(n=1):
	result = 0
	for i in range(0,n):
		result = result+randint(1,6)
	return result
class CEnemy():
	def __init__(self,sk,st,d=2):
		self.skill = sk
		self.stamina = st
		self.maxstamina = st
		self.damage = d
		self.alive = True
	def clean(self):
		self.stamina = self.maxstamina
		self.alive=True
	def strike(self):
		return self.skill+dice(2)
	def wound(self,diff):
		self.stamina = self.stamina - diff
		if self.stamina<1:
			self.stamina = 0
			self.alive = False
	def battle(self,enemy,stopstam=0,stopround=0):
		while self.alive and enemy.alive and self.stamina>stopstam and stopround!=1:
			st = self.strike()
			st1 = enemy.strike()
			#print str(st)+','+str(st1)
			if st>st1:
				enemy.wound(self.damage)
			if st1>st:
				self.wound(enemy.damage)
			stopround = stopround-1		
	def battle2(self,enemy1,enemy2,stopstam=0,stopround=0):
		while self.alive and enemy1.alive and self.stamina>stopstam and stopround!=1:
			st = self.strike()
			st1 = enemy1.strike()
			st2 = enemy2.strike()
			#print str(st)+','+str(st1)+','+str(st2)
			if st>st1:
				enemy1.wound(self.damage)
			if st1>st:
				self.wound(enemy1.damage)
			if st2>st:
				self.wound(enemy2.damage)
			stopround = stopround-1
		#print str(enemy1.alive)
		if not enemy1.alive:
			self.battle(enemy2,stopstam,stopround)
	def battle3(self,enemy1,enemy2,enemy3,stopstam=0,stopround=0):
		while self.alive and enemy1.alive and self.stamina>stopstam and stopround!=1:
			st = self.strike()
			st1 = enemy1.strike()
			st2 = enemy2.strike()
			st3 = enemy3.strike()
			#print str(st)+','+str(st1)+','+str(st2)
			if st>st1:
				enemy1.wound(self.damage)
			if st1>st:
				self.wound(enemy1.damage)
			if st2>st:
				self.wound(enemy2.damage)
			if st3>st:
				self.wound(enemy3.damage)
			stopround = stopround-1
		#print str(enemy1.alive)
		if not enemy1.alive:
			self.battle2(enemy2,enemy3,stopstam,stopround)		
	def log(self):
		print str(self.skill) + ',' + str(self.stamina) + ',' + str(self.alive)

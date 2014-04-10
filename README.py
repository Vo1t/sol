#!/usr/bin/env python
import random
def dice():
	return random.randint(1,6)
def dice2():
	return dice() + dice()
class Hero:
	def __init__(self,fair):
		if fair:
			self.skill = dice() + 6
			self.stamina = dice2() + 12
			self.luck = dice() + 6
		else:
			self.skill = 12
			self.stamina = 24
			self.luck = 12

		self.damage = 2
	def battle(self,sk,st,end=0,d=2):
		r = 0
		while self.stamina>end and st>0:
			b1 = self.skill + dice2()
			b2 = sk + dice2()
			if b1>b2:
				st = st-self.damage
			if b2>b1:
				self.stamina = self.stamina-d
			r = r+1
		return r
	def battle2(self,sk1,st1,sk2,st2,end=0,d1=2,d2=2):
		r = 0
		while self.stamina>end and st1>0:
			bh = self.skill + dice2()
			b1 = sk1 + dice2()
			b2 = sk2 + dice2()
			if bh>b1:
				st1 = st1-self.damage
			if b1>bh:
				self.stamina = self.stamina-d1
			if b2>bh:
				self.stamina = self.stamina-d2
			r = r+1
		return r + self.battle(sk2,st2,end,d2)
h1 = Hero(False)
h1.battle2(10,15,10,15)
print h1.stamina
 

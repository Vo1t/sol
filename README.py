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
	def testluck(self):
		self.luck = self.luck-1
		return (self.luck > dice()+4)
	def testskill(self):
		return (self.skill > dice()+5)
	def clean(self):
		self.skill = 12
		self.stamina = 24
		self.luck = 12
		self.damage = 2
	def st_change(self,diff):
		self.stamina = self.stamina + diff
	def tks(self):
		self.clean()
		self.battle(6,10)
		self.st_change(-2)
		self.battle(8,9)
		self.skill = self.skill+1
		self.stamina = 24
		self.battle2(11,15,11,15,4)
		return (self.stamina > 4)

h1 = Hero(False)
w = 0
l = 0
for i in range(1,10000):
	if h1.tks():
		w = w+1
print w/100 

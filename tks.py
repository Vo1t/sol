from hero import *
starik = CEnemy(6,10)
dogfish = CEnemy(8,7)
barracuda1 = CEnemy(11,15)
barracuda2 = CEnemy(11,15)
pirania1 = CEnemy(10,10)
pirania2 = CEnemy(10,10)
drakon = CEnemy(9,8)
pauk = CEnemy(9,9)
akula = CEnemy(10,10)
condor = CEnemy(9,9)
pirat1 = CEnemy(10,8)
pirat2 = CEnemy(9,8)
pirat3 = CEnemy(10,8)
voin1 = CEnemy(10,10)
voin2 = CEnemy(10,10)
vod1 = CEnemy(9,10)
vod2 = CEnemy(8,8)
vod3 = CEnemy(7,9)
unicorn = CEnemy(10,8)
skat = CEnemy(9,9)
hero = CHero(False)
def enemies():
	starik.clean()
	dogfish.clean()
	barracuda1.clean()
	barracuda2.clean()
	drakon.clean()
	pauk.clean()
	pirania1.clean()
	pirania2.clean()
	akula.clean()
	condor.clean()
	pirat1.clean()
	pirat2.clean()
	voin1.clean()
	voin2.clean()
	vod1.clean()
	vod2.clean()
	vod3.clean()
	unicorn.clean()
	skat.clean()
def tks():
	hero.clean(True)
	enemies()
	alien = False
	hero.battle(starik)
	hero.wound(2)
	hero.battle(dogfish)
	hero.skill = hero.skill+1
	hero.heal(2)
	if hero.stamina<hero.maxstamina:  
		hero.heal(3)
		meal = False
	else: 
		meal = True
	hero.battle2(barracuda1,barracuda2,4)
	if hero.stamina<5: return False
	if not hero.testluck: return False
	hero.heal(3)
	if(meal): hero.heal(3)
	if hero.stamina >9: 
		hero.wound(dice(2))
		alien = True
	hero.wound(2)
	hero.heal(9)
	hero.wound(3)
	hero.battle(drakon)
	hero.wound(1)
	hero.battle(pauk)
	hero.heal(10)
	if not hero.testluck(): return False
	hero.battle2(pirania1,pirania2)
	if not hero.alive: return False
	hero.heal(10)
	hero.battle(akula)
	hero.battle(condor)
	if not alien:
		hero.battle3(pirat1,pirat2,pirat3)
	else:
		hero.battle(pirat1)
	hero.battle2(voin1,voin2)
	return hero.alive
def tks2():
	hero.clean(False)
	enemies()
	hero.battle(vod1,0,5)
	hero.battle3(vod1,vod2,vod3)
	hero.battle(unicorn)
	hero.wound(2)
	hero.battle(skat)
def tks_test():
	hero.clean(False)
	hero.stamina = 4
	enemies()
	hero.battle2(test1,test2)
	return hero.alive
w = 0
for i in range(1,50000):
	if tks(): w=w+1
print w/500

	


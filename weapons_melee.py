import random

class MeleeWeapon:
    def __init__(self, name, description, hit_dice, active_affects):
        self.name = name
        self.description = description
        self.hit_dice = hit_dice
        self.active_affects = active_affects
        
class Bat(MeleeWeapon):
    def __init__(self):
        super().__init__(name='Bat', description='An aluminium baseball bat.', hit_dice='d4', active_affects='N/A')
    
    def bat_hit(self):
        possible_damage = [0, 10, 20, 30]
        damage_rolled = random.choice(possible_damage)
        if possible_damage == possible_damage[0]:
            print("You missed, bozo! | 0 damage")
        if possible_damage == possible_damage[1]:
            print("You hit your target once! | 10 damage")
        if possible_damage == possible_damage[2]:
            print("You hit your target twice! | 20 damage")
        if possible_damage == possible_damage[3]:
            print("BONK!!! BONK!!! BONK!!! | 30 damage")
        
        print(damage_rolled)
        
class Shovel(MeleeWeapon):
    def __init__(self):
        super().__init__(name='Shovel', description='A combat shovel.', hit_dice='d4', active_affects='N/A')
    
    def shovel_hit(self):
        possible_damage = [0, 10, 20, 30]
        damage_rolled = random.choice(possible_damage)
        if possible_damage == possible_damage[0]:
            print("You missed, MAGGOT! | 0 damage")
        if possible_damage == possible_damage[1]:
            print("You hit your target once! | 10 damage")
        if possible_damage == possible_damage[2]:
            print("You hit your target twice! | 20 damage")
        if possible_damage == possible_damage[3]:
            print("TINK!!! TINK!!! TINK!!! | 30 damage")
        
        print(damage_rolled)
        
class FireAxe(MeleeWeapon):
    def __init__(self):
        super().__init__(name='Fire Axe', description='A fire axe.', hit_dice='d4', active_affects='N/A')
    
    def fire_axe_hit(self):
        possible_damage = [0, 15, 30, 45]
        damage_rolled = random.choice(possible_damage)
        if possible_damage == possible_damage[0]:
            print("You missed, HAHA! | 0 damage")
        if possible_damage == possible_damage[1]:
            print("You hit your target once! | 15 damage")
        if possible_damage == possible_damage[2]:
            print("You hit your target twice! | 30 damage")
        if possible_damage == possible_damage[3]:
            print("MMMMPHHH MPHMPHH, HAHAHA!!! | 45 damage")
        
        print(damage_rolled)
        
class Bottle(MeleeWeapon):
    def __init__(self, is_broken):
        self.is_broken = is_broken
        
        super().__init__(name='Bottle', description='A whiskey bottle.', hit_dice='d4', active_affects='N/A', is_broken=False)
    
    
    
    def bottle_hit(self):
        possible_damage = [0, 15, 30, 45]
        damage_rolled = random.choice(possible_damage)
        if possible_damage == possible_damage[0]:
            print("You missed, HAHA! | 0 damage")
        if possible_damage == possible_damage[1] or possible_damage[2] or possible_damage[3] and Bottle().is_broken == False:
            Bottle().is_broken = True
            print("CRUNCH! THE GLASS BROKE!!! | 30 damage")
        if possible_damage == possible_damage[1]:
            print("You hit your target once! | 15 damage")
        if possible_damage == possible_damage[2]:
            print("You hit your target twice! | 30 damage")
        if possible_damage == possible_damage[3]:
            print("MMMMPHHH MPHMPHH, HAHAHA!!! | 45 damage")
        
        print(damage_rolled)
        
    def is_broken_reset(self):
        if Bottle().is_broken == True:
            Bottle().is_broken = False        
        else:
            message = 'ITS NOT BROKEN YOU DINGUS!!!'
            print(message)
    
class Fists(MeleeWeapon):
    def __init__(self):
        super().__init__(name='Fists', description='Just plain old fists. A real mans way of fighting.', hit_dice='d4', active_affects='N/A')
        
    def fists_hit(self):
        possible_damage = [0, 20, 40, 60]
        damage_rolled = random.choice(possible_damage)
        if possible_damage == possible_damage[0]:
            print("You missed, HAHA! | 0 damage")
        if possible_damage == possible_damage[1]:
            print("You hit your target once! | 20 damage")
        if possible_damage == possible_damage[2]:
            print("You hit your target twice! | 40 damage")
        if possible_damage == possible_damage[3]:
            print("How ease dat for knuckle sandvich!!! | 60 damage")
        
        print(damage_rolled)
        
class Wrench(MeleeWeapon):
    def __init__(self):
        super().__init__(name='Wrench', description='A wrench.', hit_dice='d4', active_affects='N/A')
        
    def wrench_hit(self):
        possible_damage = [0, 10, 20, 30]
        damage_rolled = random.choice(possible_damage)
        if possible_damage == possible_damage[0]:
            print("You missed, HAHA! | 0 damage")
        if possible_damage == possible_damage[1]:
            print("You hit your target once! | 10 damage")
        if possible_damage == possible_damage[2]:
            print("You hit your target twice! | 20 damage")
        if possible_damage == possible_damage[3]:
            print("Wooo Weeee Partner!!! | 30 damage")
        
        print(damage_rolled)
        
class Bonesaw(MeleeWeapon):
    def __init__(self):
        super().__init__(name='Bonesaw', description='A bonesaw. A serrated blade to grind through bone.', hit_dice='d4', active_affects='N/A')
        
    def bonesaw_hit(self):
        possible_damage = [0, 15, 30, 45]
        damage_rolled = random.choice(possible_damage)
        if possible_damage == possible_damage[0]:
            print("You missed, Shtupid! | 0 damage")
        if possible_damage == possible_damage[1]:
            print("You hit your target once! | 15 damage")
        if possible_damage == possible_damage[2]:
            print("You hit your target twice! | 30 damage")
        if possible_damage == possible_damage[3]:
            print("How iz zat fur medicine!!! | 45 damage")
        
        print(damage_rolled)
        
class Kukiri(MeleeWeapon):
    def __init__(self):
        super().__init__(name='Kukiri', description='A kukiri.', hit_dice='d4', active_affects='N/A')
        
    def kukiri_hit(self):
        possible_damage = [0, 15, 30, 45]
        damage_rolled = random.choice(possible_damage)
        if possible_damage == possible_damage[0]:
            print("You missed, are ya takin the piss! | 0 damage")
        if possible_damage == possible_damage[1]:
            print("You hit your target once! | 15 damage")
        if possible_damage == possible_damage[2]:
            print("You hit your target twice! | 30 damage")
        if possible_damage == possible_damage[3]:
            print("Now im takin your piss!!! | 45 damage")
        
        print(damage_rolled)
        
class Knife(MeleeWeapon):
    def __init__(self):
        super().__init__(name='Knife', description='A knife.', hit_dice='d4', active_affects='N/A')
        
    def knife_hit(self):
        possible_damage = [0, 25, 50, 75]
        damage_rolled = random.choice(possible_damage)
        if possible_damage == possible_damage[0]:
            print("You missed, uncultured swine! | 0 damage")
        if possible_damage == possible_damage[1]:
            print("You hit your target once! | 25 damage")
        if possible_damage == possible_damage[2]:
            print("You hit your target twice! | 50 damage")
        if possible_damage == possible_damage[3]:
            print("Stab stab stab!!! | 75 damage")
        
        print(damage_rolled)
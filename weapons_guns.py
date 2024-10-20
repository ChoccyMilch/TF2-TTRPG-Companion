from random import *
import random

class Weapon:
    def __init__(self, name, current_magazine, magazine_size, max_magazines, trigger_pulls, reload_time, damage_close, damage_medium, damage_long, crit_chance, crit_multiplier, crit_offset, last_damage_total, range_penalty, active_effect, description):
        self.name = name
        self.current_magazine = current_magazine
        self.magazine_size = magazine_size
        self.max_magazines = max_magazines
        self.trigger_pulls = trigger_pulls
        self.reload_time = reload_time
        self.damage_close = damage_close
        self.damage_medium = damage_medium
        self.damage_long = damage_long
        self.last_damage_total = last_damage_total
        self.active_effect = active_effect
        self.description = description
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        self.crit_offset = crit_offset
        self.range_penalty = range_penalty
    
#----COMMON RANGED FIREARMS    
    def attack_close(self): # Close range attack function
        self.damage_rolls = [] # Initializes an array
        
        self.crit_roll = randint(self.crit_chance[0], self.crit_chance[1]) # on every function run crit_roll is initialized with a new integer between the minimum and maximum values of crit_chance. if crit_roll is more than the crit_offset then a crit will occur.
        for r in range(self.trigger_pulls): # Rolls the damage randint 10 times and stores them inside damage_rolls
            self.damage_rolls.append( (randint(self.damage_close[0], self.damage_close[1]))) # Rolls a damage number between the minimum and maximum index value of the damage_close array.
        self.damage_rolled = list(filter((1).__ne__, self.damage_rolls)) # Filters through the damage values and drops all 1's rolled
        self.damage_total = sum(self.damage_rolled) # Gets the sum of the filtered array
        if self.crit_roll > self.crit_offset:
            self.damage_total * self.crit_multiplier 
            return print(f"Rolls: {self.damage_rolled} | WOW A CRIT! Critical Damage Total: {self.damage_total}")
        else:
            return print(f"Rolls: {self.damage_rolled} | Damage Total: {self.damage_total}")
    
    def attack_mid(self): # Medium range attack function
        self.damage_rolls = [] # Initializes an array
        
        self.crit_roll = randint(self.crit_chance[0], self.crit_chance[1]) # on every function run crit_roll is initialized with a new integer between the minimum and maximum values of crit_chance. if crit_roll is more than the crit_offset then a crit will occur.
        for r in range(round(self.trigger_pulls / 2)): # Rolls the damage randint 10 times and stores them inside damage_rolls
            self.damage_rolls.append( (randint(self.damage_medium[0], self.damage_medium[1]))) # Rolls a damage number between the minimum and maximum index value of the damage_close array.
        self.damage_rolled = list(filter((1).__ne__, self.damage_rolls)) # Filters through the damage values and drops all 1's rolled
        self.damage_total = sum(round(self.damage_rolled - self.range_penalty / 2)) # Gets the sum of the filtered array
        if self.crit_roll > self.crit_offset:
            self.damage_total * self.crit_multiplier 
            return print(f"Rolls: {self.damage_rolled} | WOW A CRIT! Critical Damage Total: {self.damage_total}")
        else:
            return print(f"Rolls: {self.damage_rolled} | Damage Total: {self.damage_total}")
        
    def attack_far(self): # long range attack function
        self.damage_rolls = [] # Initializes an array
        
        self.crit_roll = randint(self.crit_chance[0], self.crit_chance[1]) # on every function run crit_roll is initialized with a new integer between the minimum and maximum values of crit_chance. if crit_roll is more than the crit_offset then a crit will occur.
        for r in range(round(self.trigger_pulls / 3)): # Rolls the damage randint 10 times and stores them inside damage_rolls
            self.damage_rolls.append( (randint(self.damage_medium[0], self.damage_medium[1]))) # Rolls a damage number between the minimum and maximum index value of the damage_close array.
        self.damage_rolled = list(filter((1).__ne__, self.damage_rolls)) # Filters through the damage values and drops all 1's rolled
        self.damage_total = sum(round(self.damage_rolled - self.range_penalty / 3)) # Gets the sum of the filtered array
        if self.crit_roll > self.crit_offset:
            self.damage_total * self.crit_multiplier 
            return print(f"Rolls: {self.damage_rolled} | WOW A CRIT! Critical Damage Total: {self.damage_total}")
        else:
            return print(f"Rolls: {self.damage_rolled} | Damage Total: {self.damage_total}")    

class Launcher():
    def __init__(self, name, current_magazine, magazine_size, max_magazines, reload_time, possible_damage,crit_chance, crit_multiplier, crit_offset, last_damage_total, active_effect, description):
        self.name = name
        self.current_magazine = current_magazine
        self.magazine_size = magazine_size
        self.max_magazines = max_magazines
        self.reload_time = reload_time
        self.possible_damage = possible_damage
        self.last_damage_total = last_damage_total
        self.active_effect = active_effect
        self.description = description
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        self.crit_offset = crit_offset

#----ROCKET LAUNCHERS
    def shoot_rocket(self):
        
        self.possible_damage # An array of the possible damage outcomes
        self.damage_rolled = random.choice(self.possible_damage) # Selects a random damage number from damage_possible
        self.crit_roll = randint(self.crit_chance[0], self.crit_chance[1]) # Rolls for crit chance
        
        if self.crit_roll > self.crit_offset and self.damage_rolled != self.possible_damage:
            print(f"CRIT!!! GET GIBBED! {str(self.damage_rolled * self.crit_multiplier)} damage | Anyone within 10 feet takes {str(self.damage_rolled / 2)} ")
        if self.damage_rolled == self.possible_damage[0]: # If the 1st outcome is chosen
            print(f"DIRECT HIT!!! 112 damage | Anyone within 10 feet takes {str(self.damage_rolled / 2)} ")
        if self.damage_rolled == self.possible_damage[1]: # If the 2nd outcome is chosen
            print(f"Close hit: 56 damage | Anyone within 10 feet takes {str(self.damage_rolled / 2)} ")
        if self.damage_rolled == self.possible_damage[2]: # If the 3rd outcome is chosen
            print(f"Grazing blow: 28 damage | Anyone within 10 feet takes {str(self.damage_rolled / 2)} ")
        if self.damage_rolled == self.possible_damage[3]: # If the 4th outcome is chosen
            print(f"You missed! Get some glasses MAGGOT!")

#----GRENADE LAUNCHERS        
    def shoot_pill(self):
        self.possible_damage # An array storing the possible amounts of damage
        self.damage_rolled = random.choice(self.possible_damage) # Chooses one of the damage possibilities
        self.crit_roll = randint(self.crit_chance[0], self.crit_chance[1]) # Rolls for crit chance
        
        if self.crit_roll > self.crit_offset and self.damage_rolled != self.possible_damage:
            print(f"CRIT!!! GET GIBBED! {str(self.damage_rolled * self.crit_multiplier)} damage | Anyone within 10 feet takes {str(self.damage_rolled / 2)} ")
        if self.damage_rolled == self.possible_damage[0]: # If it chooses the 1st
            print(f"DIRECT HIT!!! 100 damage | Anyone within 10 feet takes {int(self.damage_rolled / 2)} ")
        if self.damage_rolled == self.possible_damage[1]: # If it chooses the 2nd
            print(f"Close hit: 50 damage | Anyone within 10 feet takes {int(self.damage_rolled / 2)} ")
        if self.damage_rolled == self.possible_damage[2]: # If it chooses the 3rd
            print(f"Grazing blow: 25 damage | Anyone within 10 feet takes {int(self.damage_rolled / 2)} ")
        if self.damage_rolled == self.possible_damage[3]: # If it chooses the 4th
            print(f"You missed! Oi, get a second eye ye nitwit!")

#----STICKYBOMB LAUNCHERS
    def detonate_sticky(self):

        # Tells the users the damage conditions depending the situation
        print("Anyone within 0-5ft takes 40 damage.\n")
        print("Anyone within 10-15ft takes 20 damage\n")
        # Prints the extra info about the sticky launchers' stickys
        print(StickyBombLauncher().active_effect)
            
##----SNIPERS    
    def sniper_attack_super_close(self):
        self.possible_damage # An array of possible damages
        self.damage_rolled = random.choice(self.possible_damage) # Chooses a damage from the array
        self.crit_roll = randint(self.crit_chance[0], self.crit_chance[1]) # Rolls for crit chance
        
        if self.crit_roll > self.crit_offset and self.damage_rolled != self.possible_damage:
            print(f"CRIT!!! MOM GET THE CAMERA! {str(self.damage_rolled * self.crit_multiplier)} damage.")
        if self.damage_rolled == self.possible_damage[0]: # If the 1st is chosen
            print(f"Headshot! You dealt {self.damage_rolled}damage to your target.")
        if self.damage_rolled == self.possible_damage[1]: # If the 2nd is chosen
            print("Man you suck. Maybe its time to retire?")
        if self.damage_rolled == self.possible_damage[2]: # If the 3rd is chosen
            print("Man you suck. Maybe its time to retire?")
    
    def snipe_close(self):
        self.possible_damage # An array of possible damages
        self.damage_rolled = random.choice(self.possible_damage) # Chooses a damage from the array
        self.crit_roll = randint(self.crit_chance[0], self.crit_chance[1]) # Rolls for crit chance
        
        if self.crit_roll > self.crit_offset and self.damage_rolled != self.possible_damage:
            print(f"CRIT!!! MOM GET THE CAMERA! {str(self.damage_rolled * self.crit_multiplier)} damage.")
        if self.damage_rolled == self.possible_damage[0]: # If the 1st is chosen
            print(f"Headshot! You dealt {self.damage_rolled}damage to your target.")
        if self.damage_rolled == self.possible_damage[1]: # If the 2nd is chosen
            print(f"Bodyshot! You dealt {self.damage_rolled}damage to your target.")
        if self.damage_rolled == self.possible_damage[2]: # If the 3rd is chosen
            print(f"Bodyshot! You dealt {self.damage_rolled}damage to your target.")
        if self.damage_rolled == self.possible_damage[3]: # If the 4th is chosen
            print("Man you suck. Maybe its time to retire?")
    
    def snipe_medium(self):
        self.possible_damage # An array of possible damages
        self.damage_rolled = random.choice(self.possible_damage) # Chooses a damage from the array
        self.crit_roll = randint(self.crit_chance[0], self.crit_chance[1]) # Rolls for crit chance
        
        if self.crit_roll > self.crit_offset and self.damage_rolled != self.possible_damage:
            print(f"CRIT!!! MOM GET THE CAMERA! {str(self.damage_rolled * self.crit_multiplier)} damage.")
        if self.damage_rolled == self.possible_damage[0]: # If the 1st is chosen
            print(f"Headshot! You dealt {self.damage_rolled}damage to your target.")
        if self.damage_rolled == self.possible_damage[1]: # If the 2nd is chosen
            print(f"Bodyshot! You dealt {self.damage_rolled}damage to your target.")
        if self.damage_rolled == self.possible_damage[2]: # If the 3rd is chosen
            print(f"Bodyshot! You dealt {self.damage_rolled}damage to your target.")
        if self.damage_rolled == self.possible_damage[3]: # If the 4th is chosen
            print("Man you suck. Maybe its time to retire?")

    def sniper_charged_attack(self):
        self.possible_damage # An array of possible damages
        self.damage_rolled = random.choice(self.possible_damage[0], self.possible_damage[4]) # Chooses a damage from the array
        self.crit_roll = randint(self.crit_chance[0], self.crit_chance[1]) # Rolls for crit chance
        
        if self.crit_roll > self.crit_offset and self.damage_rolled == self.possible_damage[0]:
            print(f"CRIT!!! GET DOMED NERD! {str(self.damage_rolled * self.crit_multiplier)} damage.")
        if self.damage_rolled == self.possible_damage[0]: # If the 1st is chosen
            print(f"Headshot! You dealt a whopping {self.damage_rolled} damage to your target.")
        if self.damage_rolled == self.possible_damage[4]: # If the 2nd is chosen
            print(f"You missed. What a waste of a charged shot.")  

class Gadget(Weapon): 
        def __init__(self, name, hp, current_magazine, magazine_size, max_magazines, trigger_pulls, reload_time, damage_close, damage_medium, damage_long, crit_chance, crit_multiplier, crit_offset, last_damage_total, range_penalty, active_effect, description):
            self.name = name
            self.hp = hp
            self.current_magazine = current_magazine
            self.magazine_size = magazine_size
            self.max_magazines = max_magazines
            self.trigger_pulls = trigger_pulls
            self.reload_time = reload_time
            self.damage_close = damage_close
            self.damage_medium = damage_medium
            self.damage_long = damage_long
            self.last_damage_total = last_damage_total
            self.active_effect = active_effect
            self.description = description
            self.crit_chance = crit_chance
            self.crit_multiplier = crit_multiplier
            self.crit_offset = crit_offset
            self.range_penalty = range_penalty
            
        def attack_sentry_lvl1_close(self):
        
            # Prints damage
            print("The sentry deals 30 damage to the target.")
            # Prints extra info about the sentry
            print(SentryLevel1().active_effect)
    
        def attack_sentry_lvl1_med(self):
        
            # Prints damage
            print("The sentry deals 30 damage to the target.")
            # Prints extra info about the sentry
            print(SentryLevel1().active_effect)
    
        def attack_sentry_lvl2_close(self):
            # Prints damage
            print("The sentry deals 45 damage to the target.")
            # Prints extra info about the sentry
            print(SentryLevel2().active_effect)
    
        def attack_sentry_lvl2_med(self):
        
            # Prints damage
            print("The sentry deals 45 damage to the target.")
            # Prints extra info about the sentry
            print(SentryLevel2().active_effect)
        
        def attack_sentry_lvl3_close(self):
        
            # Prints damage
            print("0-25ft: 60 damage + 15 damage with rockets.\n")
            # Prints extra info about the sentry
            print(SentryLevel3().active_effect)
    
        def attack_sentry_lvl3_med(self):
        
            # Prints damage
            print(f"25-35ft: 45 damage + 15 damage with rockets")
            # Prints extra info about the sentry
            print(SentryLevel3().active_effect)

class ScatterGun(Weapon):
    def __init__(self):
        super().__init__(name='Scatter Gun', current_magazine=6, magazine_size=6, max_magazines=5, trigger_pulls=10, reload_time=1, damage_close=[1, 10], damage_medium=[1, 10], damage_long=False, crit_chance=[1, 50], crit_multiplier=3, crit_offset=47, last_damage_total=[], range_penalty=4, active_effect=False, description='A scatter gun.')
        
    def attack_close(self):
        return super().attack_close()
    
    def attack_mid(self):
        return super().attack_mid()
    
    # No long range fire on the scattergun 
        
class Pistol(Weapon):
    def __init__(self):
        super().__init__(name='Pistol', current_magazine=12, magazine_size=12, max_magazines=3, reload_time=1, trigger_pulls=10,  damage_close=[1, 3], damage_medium=[1, 3], damage_long=[1, 3], crit_chance=[1, 50], crit_multiplier=2, crit_offset=40, active_effect=False, range_penalty=2, last_damage_total=[], description='A pistol.')
        
    def attack_close(self):
        return super().attack_close()
    
    def attack_mid(self):
        return super().attack_mid()
        
    def attack_far(self):
        return super().attack_far()
    
class RocketLauncher(Launcher):
    def __init__(self):
        super().__init__(name='Rocket Launcher', current_magazine=4, magazine_size=4, max_magazines=5, reload_time=1, possible_damage=[112, 56, 28, 0], crit_chance=[1, 12], crit_multiplier=2, last_damage_total=[], crit_offset=11, active_effect='"\n-Enemies and the user within 10 ft of the target take half damage\n-Can fire from distance at any target. Must roll d4 to determine accuracy\n-When firing at his own feet as an attack, he deals 56 self inflicted damage and 28 dmg to enemies within 10 ft\n-Soldier can choose to fire a tile to deal 28 dmg in a 3x3 square"', description='A Rocket Launcher.')
    
    def shoot_rocket(self):
        return super().shoot_rocket()
                
class Shotgun(Weapon):
    def __init__(self):
        super().__init__(name='Shotgun', current_magazine=6, magazine_size=6, max_magazines=5, reload_time='3, bullets', trigger_pulls=4, damage_close=[1, 10], damage_medium=[1, 10], damage_long=False, crit_chance=[1,45], crit_multiplier=3, crit_offset=42, active_effect=False, range_penalty=2, last_damage_total=[], description='A shotgun.')
        
    def attack_close(self):
        return super().attack_close()
    
    def attack_mid(self):
        return super().attack_mid()
    
class Flamethrower(Weapon):
    def __init__(self):
        super().__init__(name='Flamethrower', current_magazine=200, magazine_size=200, max_magazines='N/A', reload_time='N/A', damage_close='2d12 per person in range. -25 ammo per use', damage_medium=False, damage_long=False, active_effect="Afterburn:\n-Lasts 3 turns\n-If burned again, afterburn refreshes\n-1d12 every target's turn\n-Reduces health gained from the medigun by 10 hp\nAirblast (10 ammo): \n-Bonus or Reaction\n-If used as Bonus action, can not be used as a reaction.\n-Able to airblast any projectile including sticky traps, flying guillotines, etc. \n-Reaction can not airblast enemies. If airblast rockets, follow rocket damage rules\n-Bonus action to airblast enemies or allies 5 feet in range, blasts enemies 10 feet away (5 ft for Heavy)", description='A Flamethrower.')
        
    def shoot_flamethrower(self):
        
        print("How many targets are in range?\n") # Prompts the user to get the number of targets damaged
        targets = input() # Get user input
        targetsInt = int(targets) # Converts the input obtained by the user from a string data type into an integer data type
        damage_rolls = [] # Initializes an array called damage_rolls
        for r in range(targetsInt): # rolls corresponding to the number the user input
            damage_rolls.append( (randint(1, 12)))
        
        print(f"\nDamage done, the player can order these as they choose: {damage_rolls}")
    
class GrenadeLauncher(Launcher):
    def __init__(self):
        super().__init__(name='Grenade Launcher', current_magazine=4, magazine_size=4, max_magazines='16 pills', reload_time='2 pills per turn', possible_damage=[100, 50, 25, 0], crit_chance=[1, 12], crit_multiplier=2, crit_offset=11, active_effect='-Enemies and the user within 10 ft of the target take half damage\n-Can fire from any distance at any target. Must roll d4 to determine accuracy\n-Demoman can bounce the pills around corners and over cliffs', last_damage_total=[], description='A grenade launcher.')
        
    def shoot_pill(self):
        return super().shoot_pill()
        
class StickyBombLauncher(Launcher):
    def __init__(self):
        super().__init__(name='Sticky Bomb Launcher', current_magazine=8, magazine_size=8, max_magazines='24 stickys', reload_time='NULL', damage_close='d3: 40', damage_medium='d2: 20', damage_long='d1: null', active_effect='"Sticky Trap\n-Using stickies as a trap, you can use a reaction to detonate them. He can set traps 20 feet from him\n-Can set up a maximum of 8 bombs\n-Can be set on a single tile or spread out\nCharged Stickybombs:\n-Demoman can expend a bonus action to charge the launcher before firing. He rolls a d4 to determine how long he charges it\nd4 = +20 dmg\nd3 = +15 dmg \nd2 = +10 dmg\nd1 = +5 dmg\nOTHER NOTES\n-Using stickies takes an action and then a bonus action to detonate\n-When firing directly under the enemies feet, they must make a DEX save of dc 13 to be able to move 10 ft from the stickybombs\n-Roll d4 to determine how many stickybombs you place\n-Targets must make a DEX save \n-Enemies make a perception check of dc 13 if stickybomb traps are set outside encounters, set up time or in a surprise attack."', description='A sticky bomb launcher.')
    
    def detonate_sticky(self):
        return super().detonate_sticky()
    
class Minigun(Weapon):
    def __init__(self):
        super().__init__(name='Minigun', current_magazine=200, magazine_size=200, max_magazines='N/A', reload_time='N/A', trigger_pulls=50, damage_close=[1, 2], damage_medium=[1, 2], damage_long=False, crit_chance=[1,125], crit_multiplier=2, crit_offset=100, active_effect="-Roll 50d2 for # of bullets that hit\n", range_penalty=2, last_damage_total=[], description='A minigun.')
        
    def attack_close(self):
        return super().attack_close()
    
    def attack_mid(self):
        return super().attack_mid()
        
class SentryLevel1(Gadget):
    def __init__(self):
        super().__init__(name='Sentry level 1', hp=100, current_magazine=200, magazine_size=200, max_magazines='N/A', reload_time='N/A', damage_close='0-25ft: 30 damage', damage_medium='25-30ft: 30 damage', damage_long=False, active_effect='\n"-Targets closest target if multiple are in range\n-Sentries have the same initiative as Engineer. It can also attack as a reaction when someone steps into its range."\n', description='A sentry gun.')
    
    def attack_sentry_lvl1_close(self):
        return super().attack_sentry_lvl1_close()
    
    def attack_sentry_lvl1_med(self):
        return super().attack_sentry_lvl1_med()

class SentryLevel2(Gadget):
    def __init__(self):
        super().__init__(name='Sentry level 2', hp = 180, current_magazine=200, magazine_size=200, max_magazines='N/A', reload_time='N/A', damage_close='0-25ft: 45 damage', damage_medium='25-30ft: 45 damage', damage_long=False, active_effect='\n"-Targets closest target if multiple are in range\n-Sentries have the same initiative as Engineer. It can also attack as a reaction when someone steps into its range."\n', description='A sentry gun.')
    
    def attack_sentry_lvl2_close(self):
        return super().attack_sentry_lvl2_close()
    
    def attack_sentry_lvl2_med(self):
        return super().attack_sentry_lvl2_med()
        
class SentryLevel3(Gadget):
    def __init__(self):
        super().__init__(name='Sentry level 3', hp=216, current_magazine=200, magazine_size=200, max_magazines='N/A', reload_time='-1 turn to reload 4 rockets', damage_close='0-25ft: 60 damage + 15 damage with rockets', damage_medium='25-35ft: 45 damage + 15 damage with rockets', damage_long=False, active_effect='\n"-Targets closest target if multiple are in range\n-Sentries have the same initiative as Engineer. It can also attack as a reaction when someone steps into its range."\n', description='A sentry gun.')
    
    def attack_sentry_lvl3_close(self):
        return super().attack_sentry_lvl3_close()
    
    def attack_sentry_lvl3_med(self):
        return super().attack_sentry_lvl3_med()
   
class SyringeGun(Weapon):
    def __init__(self):
        super().__init__(name='Syringe gun', current_magazine=45, magazine_size=45, max_magazines='5 magazines (200 syringes)', reload_time='1', trigger_pulls=15, damage_close=[1, 2], damage_medium=[1, 2], damage_long=False, crit_chance=[1, 25], crit_multiplier=3, crit_offset=20, active_effect="", range_penalty=2, last_damage_total=[], description='A syringe gun.')
        
    def attack_close(self):
        return super().attack_close()
    
    def attack_mid(self):
        return super().attack_mid()
        
class SniperRifle(Launcher):
    def __init__(self):
        super().__init__(name='Sniper rifle', current_magazine=1, magazine_size=25, max_magazines='NULL', reload_time='1', possible_damage=[150,75,0,0], crit_chance=[1,12],crit_multiplier=2, crit_offset=11, active_effect='\n"Charged Shots\n-Sniper can use a charged shot once per encounter. He rolls a d2 to determine accuracy. d2 = 250 dmg\n-Sniper can not use a bonus action during this turn"\n', description='A sniper rifle.')
    def sniper_attack_super_close(self):
        return super().sniper_attack_super_close()
    
    def snipe_close(self):
        return super().snipe_close()
    
    def snipe_medium(self):
        return super().snipe_medium()
    
    def sniper_charged_attack(self):
        return super().sniper_charged_attack()

class Revolver(Weapon):
    def __init__(self):
        super().__init__(name='Revolver', current_magazine=6, magazine_size=6, max_magazines=4, reload_time=1, trigger_pulls=3, damage_close=[1, 25], damage_medium=[1, 15], damage_long=[1, 7], crit_chance=[1, 6], crit_multiplier=2, crit_offset=5, active_effect=False, range_penalty=2, last_damage_total=[], description='A revolver.')
        
    def attack_close(self):
        return super().attack_close()
    
    def attack_mid(self):
        return super().attack_mid()
    
    def attack_far(self):
        return super().attack_far()
        
class SMG(Weapon):
    def __init__(self):
        super().__init__(name='SMG', current_magazine=30, magazine_size=30, max_magazines=3, reload_time=1, trigger_pulls=15, damage_close=[1, 2], damage_medium=[1, 2], damage_long=False, crit_chance=[1, 30], crit_multiplier=2.5, crit_offset=28, active_effect=False, range_penalty=2, last_damage_total=[], description='An SMG.')
        
    def attack_close(self):
        return super().attack_close()
    
    def attack_mid(self):
        return super().attack_mid()
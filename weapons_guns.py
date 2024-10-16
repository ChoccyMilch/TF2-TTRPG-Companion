from random import *
import random

class Weapon:
    def __init__(self, name, current_magazine, magazine_size, max_magazines, trigger_pulls, reload_time, damage_close, damage_medium, damage_long, crit_chance, crit_multiplier, crit_offset, last_damage_total, active_effect, description):
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
        
    def attack_close(self):
        self.damage_rolls = [] # Initializes an array
        
        self.crit_roll = randint(self.crit_chance[0], self.crit_chance[1])
        for r in range(self.trigger_pulls): # Rolls the damage randint 10 times and stores them inside damage_rolls
            self.damage_rolls.append( (randint(self.damage_close[0], self.damage_close[1])))
        self.damage_rolled = list(filter((1).__ne__, self.damage_rolls)) # Filters and drops all 1's rolled
        self.crit_roll
        self.damage_total = sum(self.damage_rolled) # Gets the sum of the filtered array
        if self.crit_roll > self.crit_offset:
            self.damage_total * self.crit_multiplier 
            return print(f"Rolls: {self.damage_rolled} | WOW A CRIT! Critical Damage Total: {self.damage_total}")
        else:
            return print(f"Rolls: {self.damage_rolled} | Damage Total: {self.damage_total}")
        
            
            
        
    
            
            
            
     
class ScatterGun(Weapon):
    def __init__(self):
        super().__init__(name='Scatter Gun', current_magazine=6, magazine_size=6, max_magazines=5, trigger_pulls=10, reload_time=1, damage_close=[1, 10], damage_medium='10d5', damage_long=False, crit_chance=[1, 50], crit_multiplier=2, crit_offset=47, last_damage_total = 0, active_effect=False, description='A scatter gun.')
        
    def attack_close(self):
        return super().attack_close()
    
    def shoot_close(self):
        
        damage_rolls = [] # Initializes an array
        for r in range(10): # Rolls the damage randint 10 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 10)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters and drops all 1's rolled
        crit_chance = randint(1, 50)
        damage_total = sum(damage_rolled) # Gets the sum of the filtered array
        if crit_chance > 47:
            damage_total * 2 
            print(f"Rolls: {damage_rolled} | WOW A CRIT! Critical Damage Total: {damage_total}")
        else: 
            print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
    
    def shoot_medium(self):
        
        damage_rolls = [] # Initializes an array
        for r in range(5): # Rolls the damage randint 5 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 10))) # Filters and drops all 1's rolled
        damage_rolled = list(filter((1).__ne__, damage_rolls))
        damage_total = sum(damage_rolled) # Gets the sum of the filtered array
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")      
        
class Pistol(Weapon):
    def __init__(self):
        super().__init__(name='Pistol', current_magazine=12, magazine_size=12, max_magazines=3, reload_time=1, damage_close='3d10', damage_medium='3d8', damage_long='3d6', active_effect=False, description='A pistol.')
        
    def shoot_close(self):
        
        damage_rolls = [] # Initializes an array
        for r in range(10): # Rolls the damage randint 10 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 3)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters and drops all 1's rolled
        damage_total = sum(damage_rolled) # Gets the sum of the filtered array
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
    
    def shoot_medium(self):
        
        damage_rolls = [] # Initializes an array
        for r in range(8): # Rolls the damage randint 8 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 3)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters and drops all 1's rolled
        damage_total = sum(damage_rolled)  # Gets the sum of the filtered array
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
        
    def shoot_long(self):
        
        damage_rolls = [] # Initializes an array
        for r in range(6): # Rolls the damage randint 6 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 3)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters and drops all 1's rolled
        damage_total = sum(damage_rolled) # Gets the sum of the filtered array
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
    
class RocketLauncher(Weapon):
    def __init__(self):
        super().__init__(name='Rocket Launcher', current_magazine=4, magazine_size=4, max_magazines=5, reload_time=1, damage_close='1d4: 112', damage_medium='1d3: 56', damage_long='1d2: 28', active_effect='"\n-Enemies and the user within 10 ft of the target take half damage\n-Can fire from distance at any target. Must roll d4 to determine accuracy\n-When firing at his own feet as an attack, he deals 56 self inflicted damage and 28 dmg to enemies within 10 ft\n-Soldier can choose to fire a tile to deal 28 dmg in a 3x3 square"', description='A Rocket Launcher.')
        
    def shoot_rocket(self):
        
        damage_possible = [112, 56, 28, 0] # The possible damage outcomes
        damage_rolled = random.choice(damage_possible) #selects a random damage number from damage_possible
        if damage_rolled == damage_possible[0]: # If the 1st outcome is chosen
            print(f"DIRECT HIT!!! 112 damage | Anyone within 10 feet takes {str(damage_rolled / 2)} ")
        if damage_rolled == damage_possible[1]: # If the 2nd outcome is chosen
            print(f"Close hit: 56 damage | Anyone within 10 feet takes {str(damage_rolled / 2)} ")
        if damage_rolled == damage_possible[2]: # If the 3rd outcome is chosen
            print(f"Grazing blow: 28 damage | Anyone within 10 feet takes {str(damage_rolled / 2)} ")
        if damage_rolled == damage_possible[3]: # If the 4th outcome is chosen
            print(f"You missed! Get some glasses bozo.")
            
class Shotgun(Weapon):
    def __init__(self):
        super().__init__(name='Shotgun', current_magazine=6, magazine_size=6, max_magazines=5, reload_time='3 bullets', damage_close='10d4', damage_medium='10d3', damage_long=False, active_effect=False, description='A shotgun.')
        
    def shoot_close(self):
        
        damage_rolls = [] # Initializes an array
        for r in range(4): # Rolls the damage randint 4 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 10)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters and drops all 1's rolled
        damage_total = sum(damage_rolled) # Gets the sum of the filtered array
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
    
    def shoot_medium(self):
        
        damage_rolls = [] # Initializes an array
        for r in range(3): # Rolls the damage randint 3 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 10)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters and drops all 1's rolled and stores them inside damage_rolled
        damage_total = sum(damage_rolled) # Gets the sum of the filtered array
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
    
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
    
class GrenadeLauncher(Weapon):
    def __init__(self):
        super().__init__(name='Grenade Launcher', current_magazine=4, magazine_size=4, max_magazines='16 pills', reload_time='2 pills per turn', damage_close='1d4: 100', damage_medium='1d3: 50', damage_long='1d2: 25', active_effect='-Enemies and the user within 10 ft of the target take half damage\n-Can fire from any distance at any target. Must roll d4 to determine accuracy\n-Demoman can bounce the pills around corners and over cliffs', description='A grenade launcher.')
        
    def shoot_pill(self):
        
        damage_possible = [100, 50, 25, 0] # An array storing the possible amounts of damage
        damage_rolled = random.choice(damage_possible) # Chooses one of the damage possibilities
        if damage_rolled == damage_possible[0]: # If it chooses the 1st
            print(f"DIRECT HIT!!! 100 damage | Anyone within 10 feet takes {int(damage_rolled / 2)} ")
        if damage_rolled == damage_possible[1]: # If it chooses the 2nd
            print(f"Close hit: 50 damage | Anyone within 10 feet takes {int(damage_rolled / 2)} ")
        if damage_rolled == damage_possible[2]: # If it chooses the 3rd
            print(f"Grazing blow: 25 damage | Anyone within 10 feet takes {int(damage_rolled / 2)} ")
        if damage_rolled == damage_possible[3]: # If it chooses the 4th
            print(f"You missed! Get a second eye bozo.")
        
class StickyBombLauncher(Weapon):
    def __init__(self):
        super().__init__(name='Sticky Bomb Launcher', current_magazine=8, magazine_size=8, max_magazines='24 stickys', reload_time='NULL', damage_close='d3: 40', damage_medium='d2: 20', damage_long='d1: null', active_effect='"Sticky Trap\n-Using stickies as a trap, you can use a reaction to detonate them. He can set traps 20 feet from him\n-Can set up a maximum of 8 bombs\n-Can be set on a single tile or spread out\nCharged Stickybombs:\n-Demoman can expend a bonus action to charge the launcher before firing. He rolls a d4 to determine how long he charges it\nd4 = +20 dmg\nd3 = +15 dmg \nd2 = +10 dmg\nd1 = +5 dmg\nOTHER NOTES\n-Using stickies takes an action and then a bonus action to detonate\n-When firing directly under the enemies feet, they must make a DEX save of dc 13 to be able to move 10 ft from the stickybombs\n-Roll d4 to determine how many stickybombs you place\n-Targets must make a DEX save \n-Enemies make a perception check of dc 13 if stickybomb traps are set outside encounters, set up time or in a surprise attack."', description='A sticky bomb launcher.')
        
    def detonate_sticky(self):

            # Tells the users the damage conditions depending the situation
            print("Anyone within 0-5ft takes 40 damage.\n")
            print("Anyone within 10-15ft takes 20 damage\n")
            # Prints the extra info about the sticky launchers' stickys
            print(StickyBombLauncher().active_effect)
            
class Minigun(Weapon):
    def __init__(self):
        super().__init__(name='Minigun', current_magazine=200, magazine_size=200, max_magazines='N/A', reload_time='N/A', damage_close='50*2', damage_medium='50*1', damage_long=False, active_effect="-Roll 50d2 for # of bullets that hit\n", description='A minigun.')
        
    def shoot_close(self):
        
        damage_rolls = [] # Initializes an array
        for r in range(50): # Rolls the damage randint 50 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 2)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters and drops all 1's rolled and stores them inside damage_rolled
        damage_total = sum(damage_rolled) # Gets the sum of the filtered array
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
    
    def shoot_medium(self):
        
        damage_rolls = [] # Initializes an array
        for r in range(50): # Rolls the damage randint 50 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 2))) 
        damage_rolled = list(filter((2).__ne__, damage_rolls)) # Filters and drops all 2's rolled and stores them inside damage_rolled
        damage_total = sum(damage_rolled) # Gets the sum of the filtered array
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
        
class SentryLevel1(Weapon):
    def __init__(self):
        super().__init__(name='Sentry level 1', current_magazine=200, magazine_size=200, max_magazines='N/A', reload_time='N/A', damage_close='0-25ft: 30 damage', damage_medium='25-30ft: 30 damage', damage_long=False, active_effect='\n"-Targets closest target if multiple are in range\n-Sentries have the same initiative as Engineer. It can also attack as a reaction when someone steps into its range."\n', description='A sentry gun.')
    
    def shoot_sentry_lvl1_close(self):
        
        # Prints damage
        print("The sentry deals 30 damage to the target.")
        # Prints extra info about the sentry
        print(SentryLevel1().active_effect)
    
    def shoot_sentry_lvl1_med(self):
        
        # Prints damage
        print("The sentry deals 30 damage to the target.")
        # Prints extra info about the sentry
        print(SentryLevel1().active_effect)

class SentryLevel2(Weapon):
    def __init__(self):
        self.hp = 180
        super().__init__(name='Sentry level 2', current_magazine=200, magazine_size=200, max_magazines='N/A', reload_time='N/A', damage_close='0-25ft: 45 damage', damage_medium='25-30ft: 45 damage', damage_long=False, active_effect='\n"-Targets closest target if multiple are in range\n-Sentries have the same initiative as Engineer. It can also attack as a reaction when someone steps into its range."\n', description='A sentry gun.')
    
    def shoot_sentry_lvl2_close(self):
        # Prints damage
        print("The sentry deals 45 damage to the target.")
        # Prints extra info about the sentry
        print(SentryLevel2().active_effect)
    
    def shoot_sentry_lvl2_med(self):
        
        # Prints damage
        print("The sentry deals 45 damage to the target.")
        # Prints extra info about the sentry
        print(SentryLevel2().active_effect)
        
class SentryLevel3(Weapon):
    def __init__(self):
        self.hp = 216
        super().__init__(name='Sentry level 3', current_magazine=200, magazine_size=200, max_magazines='N/A', reload_time='-1 turn to reload 4 rockets', damage_close='0-25ft: 60 damage + 15 damage with rockets', damage_medium='25-35ft: 45 damage + 15 damage with rockets', damage_long=False, active_effect='\n"-Targets closest target if multiple are in range\n-Sentries have the same initiative as Engineer. It can also attack as a reaction when someone steps into its range."\n', description='A sentry gun.')
    
    def shoot_sentry_lvl3_close(self):
        
        # Prints damage
        print("0-25ft: 60 damage + 15 damage with rockets.\n")
        # Prints extra info about the sentry
        print(SentryLevel3().active_effect)
    
    def shoot_sentry_lvl3_med(self):
        
        # Prints damage
        print(f"25-35ft: 45 damage + 15 damage with rockets")
        # Prints extra info about the sentry
        print(SentryLevel3().active_effect)
    
class SyringeGun(Weapon):
    def __init__(self):
        super().__init__(name='Syringe gun', current_magazine=45, magazine_size=45, max_magazines='5 magazines (200 syringes)', reload_time='1', damage_close='15d2', damage_medium='15d1', damage_long=False, active_effect="", description='A syringe gun.')
        
    def shoot_close(self):
        
        damage_rolls = [] # Initializes an array
        for r in range(15): # Rolls the damage randint 15 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 2)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters and drops all 1's rolled and stores them inside damage_rolled
        damage_total = sum(damage_rolled) # Gets the sum of the filtered array
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
    
    def shoot_medium(self):
        
        damage_rolls = []
        for r in range(15): # Rolls the damage randint 15 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 2)))
        damage_rolled = list(filter((2).__ne__, damage_rolls)) # Filters and drops all 2's rolled and stores them inside damage_rolled
        damage_total = sum(damage_rolled) # Gets the sum of the filtered array
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
        
class SniperRifle(Weapon):
    def __init__(self):
        super().__init__(name='Sniper rifle', current_magazine=1, magazine_size=25, max_magazines='NULL', reload_time='1', damage_close='25-100ft: 1d4', damage_medium='100-150ft: 1d4', damage_long=False, active_effect='\n"Charged Shots\n-Sniper can use a charged shot once per encounter. He rolls a d2 to determine accuracy. d2 = 250 dmg\n-Sniper can not use a bonus action during this turn"\n', description='A sniper rifle.')
    
    def shoot_super_close(self):
        damage_possible = [75, 0, '0'] # An array of possible damages
        damage_rolled = random.choice(damage_possible) # Chooses a damage from the array
        if damage_rolled == damage_possible[0]: # If the 1st is chosen
            print(f"Headshot! You dealt {damage_rolled}damage to your target.")
        if damage_rolled == damage_possible[1]: # If the 2nd is chosen
            print("Man you suck. Maybe its time to retire?")
        if damage_rolled == damage_possible[2]: # If the 3rd is chosen
            print("Man you suck. Maybe its time to retire?")

    
    def shoot_close(self):
        
        damage_possible = [150, 75, '75', 0] # An array of possible damages
        damage_rolled = random.choice(damage_possible) # Chooses a damage from the array
        if damage_rolled == damage_possible[0]: # If the 1st is chosen
            print(f"Headshot! You dealt {damage_rolled}damage to your target.")
        if damage_rolled == damage_possible[1]: # If the 2nd is chosen
            print(f"Bodyshot! You dealt {damage_rolled}damage to your target.")
        if damage_rolled == damage_possible[2]: # If the 3rd is chosen
            print(f"Bodyshot! You dealt {damage_rolled}damage to your target.")
        if damage_rolled == damage_possible[3]: # If the 4th is chosen
            print("Man you suck. Maybe its time to retire?")
    
    def shoot_medium(self):
        
        
        damage_possible = [100, 35, '35', 0] # An array of possible damages
        damage_rolled = random.choice(damage_possible) # Chooses a damage from the array
        if damage_rolled == damage_possible[0]: # If the 1st is chosen
            print(f"Headshot! You dealt {damage_rolled}damage to your target.")
        if damage_rolled == damage_possible[1]: # If the 2nd is chosen
            print(f"Bodyshot! You dealt {damage_rolled}damage to your target.")
        if damage_rolled == damage_possible[2]: # If the 3rd is chosen
            print(f"Bodyshot! You dealt {damage_rolled}damage to your target.")
        if damage_rolled == damage_possible[3]: # If the 4th is chosen
            print("Man you suck. Maybe its time to retire?")

    def shoot_sniper_charged(self):
        
        damage_possible = [250, 0] # An array of possible damages
        damage_rolled = random.choice(damage_possible) # Chooses a damage from the array
        if damage_rolled == damage_possible[0]: # If the 1st is chosen
            print(f"Headshot! You dealt a whopping {damage_rolled} damage to your target.")
        if damage_rolled == damage_possible[1]: # If the 2nd is chosen
            print(f"You missed. What a waste of a charged shot.")

class Revolver(Weapon):
    def __init__(self):
        super().__init__(name='Revolver', current_magazine=6, magazine_size=6, max_magazines=4, reload_time=1, damage_close='3d25', damage_medium='3d15', damage_long='3d7', active_effect=False, description='A revolver.')
        
    def shoot_close(self):
        
        damage_rolls = [] # Initializes the array, damage rolls
        for r in range(3): # Rolls damage 3 times
            damage_rolls.append( (randint(1, 25)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters out all the 1's from damage_rolls and stores the rest inside of damage_rolled
        damage_total = sum(damage_rolled) # Gets the sum of damage_rolled
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
    
    def shoot_medium(self):
        
        damage_rolls = [] # Initializes the array, damage rolls
        for r in range(3): # Rolls damage 3 times
            damage_rolls.append( (randint(1, 15)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters out all the 1's from damage_rolls and stores the rest inside of damage_rolled
        damage_total = sum(damage_rolled) # Gets the sum of damage_rolled
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
        
    def shoot_long(self):
        
        damage_rolls = [] # Initializes the array, damage rolls
        for r in range(3): # Rolls damage 3 times
            damage_rolls.append( (randint(1, 7)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters out all the 1's from damage_rolls and stores the rest inside of damage_rolled
        damage_total = sum(damage_rolled) # Gets the sum of damage_rolled
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
        
class SMG(Weapon):
    def __init__(self):
        super().__init__(name='SMG', current_magazine=30, magazine_size=30, max_magazines=3, reload_time=1, damage_close='15d2', damage_medium='15d1', damage_long='null', active_effect=False, description='An SMG.')
        
    def shoot_close(self):
        
        damage_rolls = [] # Initializes the array, damage rolls
        for r in range(15): # Rolls damage 15 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 2)))
        damage_rolled = list(filter((1).__ne__, damage_rolls)) # Filters out all the 1's from damage_rolls and stores the rest inside of damage_rolled
        damage_total = sum(damage_rolled) # Gets the sum of damage_rolled
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
    
    def shoot_medium(self):
        
        damage_rolls = [] # Initializes the array, damage rolls
        for r in range(15): # Rolls damage 15 times and stores them inside damage_rolls
            damage_rolls.append( (randint(1, 2)))
        damage_rolled = list(filter((2).__ne__, damage_rolls)) # Filters out all the 1's from damage_rolls and stores the rest inside of damage_rolled
        damage_total = sum(damage_rolled) # Gets the sum of damage_rolled
        print(f"Rolls: {damage_rolled} | Damage Total: {damage_total}")
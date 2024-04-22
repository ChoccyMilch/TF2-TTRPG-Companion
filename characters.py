
from typing import Any


class Character:
    def __init__(self, name, hp, current_hp, overheal_max, speed, initiative , prof_bonus, description):
        self.name = name
        self.hp = hp
        self.current_hp = current_hp
        self.overheal_max = overheal_max
        self.speed = speed
        self.initiative = initiative
        self.prof_bonus = prof_bonus
        self.description = description 
            
class Scout(Character):
    def __init__(self):
        super().__init__(name='Scout', hp=125, current_hp=125, overheal_max=185, speed='40', initiative=3, prof_bonus=2, description='\n"As the youngest of eight boys from the south side of Boston, the Scout learned early how to solve problems with his fists. With seven older brothers on his side, fights tended to end before the runt of the litter could maneuver into punching distance, so the Scout trained himself to run. He ran everywhere, all the time, until he could beat his pack of mad dog siblings to the fray."\n')
    
    def ability_scores(self):
        print('\nStrength	12 (+1)\nDexterity*	16 (+3)\nConstitution*	14 (+2)\nIntelligence	8 (-1)\nWisdom	10 (+0)\nCharisma   14 (+2)\n')
    
    def abilities(self):
        print('\n- Swift\n- Dodge\n- Double Jump(Bonus Action)\n- Double Capture Rate\n')
    
    def Swift(self):
            print('\n-Scout can make an acrobatics check of a dc 13 to run over a stickybomb trap and avoid being exploded\n-He is immune to opportunity attacks\n-He is immune to difficult terrain\n')
        
    def Dodge(self):
        print('\n-Use an action to dodge attacks. Enemies will roll disadvantage when attacking Scout for that round.\n')
    
    def Double_Jump(self):
        print('\n-Can be used outside encounters\n-2 Per encounter\n')
        
    def Double_Capture(self):
        print('\n-+5 ft Payload\n-+2 control point capture rate\n')
        
class Soldier(Character):
    def __init__(self):
        super().__init__(name='Soldier', hp=200, current_hp=200, overheal_max=300, speed=25, initiative=1, prof_bonus=2, description='\n"Though he wanted desperately to fight in World War 2, the Soldier was rejected from every branch of the U.S. military. Undaunted, he bought his own ticket to Europe. After arriving and finally locating Poland, the Soldier taught himself how to load and fire a variety of weapons before embarking on a Nazi killing spree for which he was awarded several medals that he designed and made himself. His rampage ended immediately upon hearing about the end of the war in 1949."\n')
        
    def ability_scores(self):
        print('\nStrength*	16 (+3)\nDexterity	12 (+1)\nConstitution*	14 (+2)\nIntelligence	8 (-1)\nWisdom	10 (+0)\nCharisma   12 (+1)\n')
    
    def abilities(self):
        print('\n- Merasmus\' Roommate\n- Rocket Jump\n')
    
    def merasmus_roommate(self):
            print('\n-Take -15 magic damage\n-Immune to status conditions inflicted by magic or supernatural enemies\n-Unable to be intimidated by the supernatural\n')
        
    def rocket_jump(self):
        print('\n"-Can be used outside encounters\n-2 rocket jumps per encounter, counts as bonus action\n-Uses up one ammo, deals medium range self inflicted damage\n-Jumps 15 feet, can choose to land on top of enemy\n-When used outside encounters, the explosion will alert enemies and still inflict self damage/use ammo"\n')
    
class Pyro(Character):
    def __init__(self):
        super().__init__(name='Pyro', hp=175, current_hp=175, overheal_max=260, speed=30, initiative=0, prof_bonus=2, description='\n"Only two things are known for sure about the mysterious Pyro: he sets things on fire and he doesn\'t speak. In fact, only the part about setting things on fire is undisputed. Some believe his occasional rasping wheeze may be an attempt to communicate through a mouth obstructed by a filter and attached to lungs ravaged by constant exposure to his asbestos-lined suit. Either way, he\'s a fearsome, inscrutable, on-fire Frankenstein of a man. If he even is a man"\n')
        
    def ability_scores(self):
        print('\nStrength	10 (+0)\nDexterity	14 (+2)\nConstitution	16 (+3)\nIntelligence	8 (-1)\nWisdom	8 (-1)\nCharisma   16 (+3)\n')
    
    def abilities(self):
        print('\n- Pyroland\n- Flame Retardant\n')
    
    def pyroland(self):
            print('\n-Unable to be intimidated\n-Merciless and probably isn\'t mentally affected by horrific images or committing atrocities.\n')
        
    def flame_retardant(self):
        print('\n-Immune to afterburn\n')
        
class Demoman(Character):
    def __init__(self):
         super().__init__(name='Demoman', hp=175, current_hp=175, overheal_max=260, speed=30, initiative=0, prof_bonus=2, description='\n"A fierce temper, a fascination with all things explosive, and a terrible plan to kill the Loch Ness Monster cost the six year old Demoman his original set of adoptive parents. Later, back at the Crypt Grammar School for Orphans near Ullapool in the Scottish Highlands, the boy\'s bomb-making skills improved dramatically. His disposition and total number of intact eyeballs, however, did not."\n')

    def ability_scores(self):
        print('\nStrength*	16 (+3)\nDexterity	10 (+0)\nConstitution*	16 (+3)\nIntelligence	10 (+0)\nWisdom	8 (-1)\nCharisma   12 (+1)\n')
    
    def abilities(self):
        print('\n- High Blood Alcohol Content\n- Sticky Jump\n')
    
    def high_blood_alcohol(self):
            print('\n-Normal food and water is poison to him when not drunk\n-Gains disadvantage on all weapons when sober\n-Blood suckers do NOT like biting him. If blood is sucked, the enemy will gain disadvantage for 3 rounds.\n')
        
    def sticky_jump(self):
        print('\n-Can be used outside encounters\n-2 sticky jumps per encounter, counts as bonus action\n-Uses up one ammo, deals self inflicted damage at point blank\n-Jumps 15 feet, can choose to land on top of enemy\n-When used outside encounters, the explosion will alert enemies and still inflict self damage/use ammo\n')
        
class Heavy(Character):
    def __init__(self):
         super().__init__(name='Heavy', hp=300, current_hp=300, overheal_max=450, speed=25, initiative='-1', prof_bonus='+2', description='\n"Like a hibernating bear, the Heavy appears to be a gentle giant. Also like a bear, confusing his deliberate, sleepy demeanor with gentleness will get you ripped limb from limb. Though he speaks simply and moves with an economy of energy that\'s often confused with napping, the Heavy isn\'t dumb; he\'s not your big friend and he generally wishes that you would just shut up before he has to make you shut up."\n')
         
    def ability_scores(self):
        print('\nStrength*	16 (+3)\nDexterity	8 (-1)\nConstitution	16 (+3)\nIntelligence	14 (+2)\nWisdom	12 (+1)\nCharisma   8 (-1)\n')
    
    def abilities(self):
        print('\n- Body Block\n- Fat\n')
    
    def body_block(self):
            print('\n-When within 5 feet of an ally about to be hit, he can use a reaction to use his body and shield them from damage\n')
        
    def fat(self):
        print('\n-Can not be knocked back/jostled. Only takes half distance from Pyro\'s airblast (5 Feet)\n-When standing directly in front of an enemy, he can body block and prevent them from moving forward"\n')
        
class Engineer(Character):
    def __init__(self):
         super().__init__(name='Engineer', hp=125, current_hp=125, overheal_max=185, speed='30 \(when moving buildings -5 speed)', initiative='-1', prof_bonus='+2', description='\n"This amiable, soft-spoken good ol\' boy from tiny Bee Cave, Texas loves barbeque, guns, and higher education. Natural curiosity, ten years as a roughneck in the west Texas oilfields, and eleven hard science PhDs have trained him to design, build and repair a variety of deadly contraptions."\n')
         
    def ability_scores(self):
        print('\nStrength	15 (+2)\nDexterity	8 (-1)\nConstitution	10 (+0)\nIntelligence*	16 (+3)\nWisdom	12 (+1)\nCharisma   12 (+1)\n')
    
    def abilities(self):
        print('\n- Salvager\n')
    
    def salvager(self):
            print('\n-Can salvage 100 metal from enemies\' bodies \n-Can salvage 100 metal from destroyed buildings\n-Can be done outside of encounters\n')

class Medic(Character):
    def __init__(self):
         super().__init__(name='Medic', hp=150, current_hp=150, overheal_max=225, speed='35', initiative='+2', prof_bonus='+2', description='\n"What he lacks in compassion for the sick, respect for human dignity, and any sort of verifiable formal training in medicine, the Medic more than makes up for with a bottomless supply of giant needles and a trembling enthusiasm for plunging them into exposed flesh. Raised in Stuttgart, Germany during an era when the Hippocratic oath had been downgraded to an optional Hippocratic suggestion, the Medic considers healing a generally unintended side effect of satisfying his own morbid curiosity."\n')
         
    def ability_scores(self):
        print('\nStrength	8 (-1)\nDexterity	14 (+2)\nConstitution	12 (+1)\nIntelligence	14 (+2)\nWisdom	16 (+3)\nCharisma   10 (+0)\n')
    
    def abilities(self):
        print('\n- Explosive Surfing\n- Dodge\n- Team Player\n- Regeneration\n')
    
    def explosive_surfing(self):
            print('\n-When knocked back by any source, Medic can gain control on where he lands in a 3x15 ft cone.\n')
            
    def Dodge(self):
        print('\n-Use an action to dodge attacks. Enemies will roll disadvantage when attacking Scout for that round.\n')
        
    def team_player(self):
        print('\n-Anyone within 10 feet range of Spy when he fails a backstab on Medic, can react attack on spy\n')
    
    def regeneration(self):
        print('\n-10 health regenerated every turn\n-When attacked, must wait one additional turn before he can begin to passively regenerate\n')
    
class Sniper(Character):
    def __init__(self):
         super().__init__(name='Sniper', hp=125, current_hp=125, overheal_max=185, speed='40', initiative='+3', prof_bonus='+2', description='\n"In his former life as a tracker of dangerous game in the unforgiving Australian outback, the Sniper would spend months by himself. Prolonged isolation taught him a valuable lesson: You don\'t have to rely on other people if you never miss."\n')
         
    def ability_scores(self):
        print('\nStrength	10 (+0)\nDexterity*	16 (+3)\nConstitution	10 (+0)\nIntelligence	14 (+2)\nWisdom*	16 (+3)\nCharisma   10 (+0)\n')
    
    def abilities(self):
        print('\n- Spy Checker\n- Focus\n- Charged Shots\n')
    
    def spy_checker(self):
            print('\n- Sniper can use a bonus action to spy check for disguised spies. Rolls insight while Spy counters with deception.\n-Sniper can use a bonus action to spy check for invisible spies. Rolls investigation while Spy counters with stealth.\n')
            
    def Focus(self):
        print('\n-When an enemy goes behind cover in Sniper\'s view, Sniper can use an action to focus on that enemy, waiting for them to come out behind cover while scoped in and charging. While focused, Sniper can not attack other enemies or Spy check.\n-When the enemy comes out of cover, his sniper deals charged damage\n-When Sniper is attacked or knocked back, he must make a WIS saving throw of dc 13 to keep his focus\n-A Spy attempting a backstab on Sniper and fails breaks his focus\n-Sniper can use a bonus action on his turn in order to unfocus\n')
        
    def charged_shots(self):
        print('\n-Sniper can use a charged shot once per encounter. He rolls a d2 to determine accuracy. Rolling a d2 deals 300 damage. He cannot use a bonus action during this turn.\n')
    
class Spy(Character):
    def __init__(self):
         super().__init__(name='Spy', hp=125, current_hp=125, overheal_max=185, speed=30, initiative='+3', prof_bonus='+2', description='\n"He is a puzzle, wrapped in an enigma, shrouded in riddles, lovingly sprinkled with intrigue, express mailed to Mystery, Alaska, and LOOK OUT BEHIND YOU! but it is too late. You\'re dead. For he is the Spy - globetrotting rogue, lady killer (metaphorically) and mankiller (for real)."\n')
         
    def ability_scores(self):
        print('\nStrength	8 (-1)\nDexterity*	16 (+3)\nConstitution	8 (-1)\nIntelligence	14 (+2)\nWisdom	12 (+1)\nCharisma*   16 (+3)\n')
    
    def abilities(self):
        print('\n- Spy\'s Tools\n')
    
    def spys_tools(self):
            print('\n-Can backstab someone, instantly killing them. Enemies must roll a perception check to counter, Spy can counter this however with an advantageous stealth roll\n-Sappers destroy buildings after 2 turns. Saps adjacent buildings\n-Sappers can be used outside of encounters. If spotted or applying a sapper to buildings, it will alert enemies and starts an encounter. Enemies can also roll insight to spy check outside encounters. \n-Cloak can be used outside of encounters. The DM can determine how long it lasts based on the situation\n')
            
    

from random import *
import weapons_guns
import weapons_melee
import characters
import sys

# Valid menu input  for the startup menu
valid_input = ['weapons menu', 'character menu', 'help', 'quit']

# Valid menu input for the character menu
valid_character_input = ['scout', 'soldier', 'pyro', 'demoman', 'heavy', 'engineer', 'medic', 'sniper', 'spy', 'back', 'help characters', 'quit']

# Valid menu input for the weapons menu
valid_weapons_input = ['scattergun close', 'scattergun med', 'pistol close', 'pistol med', 'pistol far', 'rocket launcher', 'rocket', 'shotgun close', 'shotgun med', 'flamethrower', 'grenade launcher','grenade', 'sticky bomb', 'minigun close', 'minigun med', 'sentry 1 close', 'sentry 1 med', 'sentry 2 close', 'sentry 2 med', 'sentry 3 close', 'sentry 3 med',  'syringe gun close','syringe close' ,'syringe gun med','syringe med', 'sniper super close', 'sniper close', 'sniper med', 'sniper charged', 'smg close', 'smg med', 'revolver close', 'revolver med', 'revolver far', 'shovel', 'bat', 'fire axe', 'bottle', 'bottle reset', 'fists', 'wrench', 'bonesaw', 'kukiri', 'knife', 'help weapons', 'back', 'quit']

# Startup menu
def general_menu():

    print('              _           _       _     _             _             _     _____        _      ')
    print('     /\      | |         (_)     (_)   | |           | |           ( )   |  __ \ /\   | |     ')
    print('    /  \   __| |_ __ ___  _ _ __  _ ___| |_ _ __ __ _| |_ ___  _ __|/ ___| |__) /  \  | |     ')
    print('   / /\ \ / _` | \'_ ` _ \| | \'_ \| / __| __| \'__/ _` | __/ _ \| \'__| / __|  ___/ /\ \ | | ')
    print('  / ____ \ (_| | | | | | | | | | | \__ \ |_| | | (_| | || (_) | |    \__ \ |  / ____ \| |____ ')
    print(' /_/    \_\__,_|_| |_| |_|_|_| |_|_|___/\__|_|  \__,_|\__\___/|_|    |___/_| /_/    \_\______|')
    print('                                                                                              ')
    print('                                                                                              ')
    print('\nWelcome to Administrator\'s PAL! A companion for a custom TTRPG based on the TF2 universe!\nUse \'character menu\', or \'weapons menu\' to start.\nTry \'back\' at any point to be brought back to the mode selection menu at any time\n\n\nAt any point type \'help\' to see a list of valid commands if you get lost!\n')
    print('\n\n\n                 Copyright 2024 - @ChoccyMilch. All rights reserved.                  ')
    
    # User input
    usr_input = input('> ')
    
    # While user input doesnt match valid_input, loop through these things
    while usr_input != valid_input:
        match usr_input.lower():
            case 'weapons menu':
                weapons_menu()
            case 'character menu':
                character_menu()
            case 'help':
                print(*valid_input, sep=', ')
                usr_input = input('> ')
            case 'quit':
                sys.exit()
            case _:
                print('Invalid input.')
                usr_input = input('> ')    

# Weapons menu
def weapons_menu():
        print('\nWelcome to the weapons menu! type \'help weapons\' for valid weapons commands!\n')
        
        # User input
        usr_input = input('> ')

        # While usr_input doesnt match valid_weapons_input then loop through these things
        match usr_input.lower():
            case 'scattergun close':
                print(weapons_guns.ScatterGun().attack_close())
            case 'scattergun med':
                weapons_guns.ScatterGun().attack_mid
            case 'pistol close':
                weapons_guns.Pistol().attack_close()
            case 'pistol med':
                weapons_guns.Pistol().attack_mid
            case 'pistol far':
                weapons_guns.Pistol().attack_far
            case 'rocket launcher' | 'rocket':
                weapons_guns.RocketLauncher().shoot_rocket()
            case 'shotgun close':
                weapons_guns.Shotgun().attack_close()
            case 'shotgun med':
                weapons_guns.Shotgun().attack_mid()
            case 'flamethrower':
                weapons_guns.Flamethrower().shoot_flamethrower()
            case'grenade launcher' | 'grenade':
                weapons_guns.GrenadeLauncher().shoot_pill()
            case 'sticky bomb':
                weapons_guns.StickyBombLauncher().detonate_sticky()
            case 'minigun close':
                weapons_guns.Minigun().attack_close()
            case 'minigun med':
                weapons_guns.Minigun().attack_mid()
            case 'sentry 1 close':
                weapons_guns.SentryLevel1().attack_sentry_lvl1_close()
            case 'sentry 1 med':
                weapons_guns.SentryLevel1().attack_sentry_lvl1_med()
            case 'sentry 2 close':
                weapons_guns.SentryLevel2().attack_sentry_lvl2_close()
            case 'sentry 2 med':
                weapons_guns.SentryLevel2().attack_sentry_lvl2_med()
            case 'sentry 3 close':
                weapons_guns.SentryLevel3().attack_sentry_lvl3_close()
            case 'sentry 3 med':
                weapons_guns.SentryLevel3().attack_sentry_lvl3_med()
            case 'syringe gun close' | 'syringe close':
                weapons_guns.SyringeGun().attack_close()
            case 'syringe gun med' | 'syringe med':
                weapons_guns.SyringeGun().attack_mid()
            case 'sniper hipfire':
                weapons_guns.SniperRifle().sniper_attack_super_close
            case 'sniper close':
                weapons_guns.SniperRifle().snipe_close()
            case 'sniper med':
                weapons_guns.SniperRifle().snipe_medium()
            case 'sniper charged':
                weapons_guns.SniperRifle().sniper_charged_attack()
            case 'smg close':
                weapons_guns.SMG().attack_close()
            case 'smg med':
                weapons_guns.SMG().attack_mid()
            case 'revolver close':
                weapons_guns.Revolver().attack_close()
            case 'revolver med':
                weapons_guns.Revolver().attack_mid()
            case 'revolver far':
                weapons_guns.Revolver().attack_far()
            case 'bat':
                weapons_melee.Bat().melee_attack_hit()
            case 'shovel':
                weapons_melee.Shovel().melee_attack_hit()
            case 'fire axe' | 'fireaxe':
                weapons_melee.FireAxe().melee_attack_hit()
            case 'bottle':
                weapons_melee.Bottle().melee_attack_hit()
            case 'bottle reset':
                pass
                # weapons_melee.Bottle().is_broken_reset()
            case 'fists':
                weapons_melee.Fists().melee_attack_hit()
            case 'wrench':
                weapons_melee.Wrench().melee_attack_hit()
            case 'bonesaw':
                weapons_melee.Bonesaw().melee_attack_hit()
            case 'kukiri':
                weapons_melee.Kukiri().melee_attack_hit()
            case 'knife':
                weapons_melee.Knife().melee_attack_hit()
            case 'back':
                general_menu()
                return False
            case 'help weapons':
                print(*valid_weapons_input, sep=', ')
            case 'quit':
                sys.exit()
            case _:
                print('Invalid weapon command. Please try again...')  

# Character menu
def character_menu():

    print('\nWelcome to the character menu! type \'help characters\' for valid character commands!\n')
    
    # User input
    usr_input = input()
    
    # While usr_input does not match valid_character_input then loop through these things
    match usr_input.lower():
        case 'scout':
            scout = characters.Scout().description
            print(scout)
        case 'soldier':
            soldier = characters.Soldier().description
            print(soldier)
        case 'pyro':
            pyro = characters.Pyro().description
            print(pyro)
        case 'demoman':
            demoman = characters.Demoman().description
            print(demoman)
        case 'heavy':
            heavy = characters.Heavy().description
            print(heavy)
        case 'engineer':
            engineer = characters.Engineer().description
            print(engineer)
        case 'medic':
            medic = characters.Medic().description
            print(medic)
        case 'sniper':
            sniper = characters.Sniper().description
            print(sniper)
        case 'spy':
            spy = characters.Spy().description
            print(spy) 
        case 'back':
            general_menu()  
        case 'help characters':
            print(*valid_character_input, sep=', ')
        case 'quit':
            sys.exit()
        case _:
            print('Invalid character command. Please try again...')

# Startup
general_menu()

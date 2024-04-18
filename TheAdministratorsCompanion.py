from random import *
import weapons_guns
import sys

valid_input = ['help', 'quit', 'scattergun close', 'scattergun med', 'pistol close', 'pistol med', 'pistol far', 'rocket launcher', 'rocket', 'shotgun close', 'shotgun med', 'flamethrower', 'grenade launcher','grenade', 'sticky bomb', 'minigun close', 'minigun med', 'sentry 1 close', 'sentry 1 med', 'sentry 2 close', 'sentry 2 med', 'sentry 3 close', 'sentry 3 med',  'syringe gun close','syringe close' ,'syringe gun med','syringe med', 'sniper super close', 'sniper close', 'sniper med', 'sniper charged', 'smg close', 'smg med', 'revolver close', 'revolver med', 'revolver far']

usr_input = input('> ')

while True:

    
    match usr_input.lower():
        case 'scattergun close':
            print(weapons_guns.ScatterGun().shoot_close())
            usr_input = input('> ')
        case 'scattergun med':
            weapons_guns.ScatterGun().shoot_medium()
            usr_input = input('> ')
        case 'pistol close':
            weapons_guns.Pistol().shoot_close()
            usr_input = input('> ')
        case 'pistol med':
            weapons_guns.Pistol().shoot_medium()
            usr_input = input('> ')
        case 'pistol far':
            weapons_guns.Pistol().shoot_long()
            usr_input = input('> ')
        case 'rocket launcher' | 'rocket':
            weapons_guns.RocketLauncher().shoot_rocket()
            usr_input = input('> ')
        case 'shotgun close':
            weapons_guns.Shotgun().shoot_close()
            usr_input = input('> ')
        case 'shotgun med':
            weapons_guns.Shotgun().shoot_medium()
            usr_input = input('> ')
        case 'flamethrower':
            weapons_guns.Flamethrower().shoot_flamethrower()
            usr_input = input('> ')
        case'grenade launcher' | 'grenade':
            weapons_guns.GrenadeLauncher().shoot_pill()
            usr_input = input('> ')
        case 'sticky bomb':
            weapons_guns.StickyBombLauncher().detonate_sticky()
            usr_input = input('> ')
        case 'minigun close':
            weapons_guns.Minigun().shoot_close()
            usr_input = input('> ')
        case 'minigun med':
            weapons_guns.Minigun().shoot_medium()
            usr_input = input('> ')
        case 'sentry 1 close':
            weapons_guns.SentryLevel1().shoot_sentry_lvl1_close()
            usr_input = input('> ')
        case 'sentry 1 med':
            weapons_guns.SentryLevel1().shoot_sentry_lvl1_med()
            usr_input = input('> ')
        case 'sentry 2 close':
            weapons_guns.SentryLevel2().shoot_sentry_lvl2_close()
            usr_input = input('> ')
        case 'sentry 2 med':
            weapons_guns.SentryLevel2().shoot_sentry_lvl2_med()
            usr_input = input('> ')
        case 'sentry 3 close':
            weapons_guns.SentryLevel3().shoot_sentry_lvl3_close()
            usr_input = input('> ')
        case 'sentry 3 med':
            weapons_guns.SentryLevel3().shoot_sentry_lvl3_med()
            usr_input = input('> ')
        case 'syringe gun close' | 'syringe close':
            weapons_guns.SyringeGun().shoot_close()
            usr_input = input('> ')
        case 'syringe gun med' | 'syringe med':
            weapons_guns.SyringeGun().shoot_medium()
            usr_input = input('> ')
        case 'sniper hipfire':
            weapons_guns.SniperRifle().shoot_super_close()
            usr_input = input('> ')
        case 'sniper close':
            weapons_guns.SniperRifle().shoot_close()
            usr_input = input('> ')
        case 'sniper med':
            weapons_guns.SniperRifle().shoot_medium()
            usr_input = input('> ')
        case 'sniper charged':
            weapons_guns.SniperRifle().shoot_sniper_charged()
            usr_input = input('> ')
        case 'smg close':
            weapons_guns.SMG().shoot_close()
            usr_input = input('> ')
        case 'smg med':
            weapons_guns.SMG().shoot_medium()
            usr_input = input('> ')
        case 'revolver close':
            weapons_guns.Revolver().shoot_close()
            usr_input = input('> ')
        case 'revolver med':
            weapons_guns.Revolver().shoot_medium()
            usr_input = input('> ')
        case 'revolver far':
            weapons_guns.Revolver().shoot_long()
            usr_input = input('> ')
        case 'help':
            print(*valid_input, sep=', ')
            usr_input = input()
        case 'quit':
            sys.exit()
        case _:
            print('Invalid input.')
            usr_input = input('> ')

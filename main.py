#libraries
import pygame
import character
import button
import time
import object
import math
import random


pygame.init()
screen_width = 1100
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Combat X")
clock = pygame.time.Clock()


#Variables
hb_full_width = 390
ab_full_width = 275
hb_r_x = 655
ab_r_x = 774
hb_l_x = 55
ab_l_x = 54
left_ulta_arc = math.pi/2
right_ulta_arc = math.pi/2
left_super_ulta_arc = math.pi/2
right_super_ulta_arc = math.pi/2

selected_character_left = "noone"
selected_character_right = "noone"
selected_background = "none"

scene = "main_menu"
cleared = True
num_of_players = 0
interval = 0
setup_lobby = False
characters_chosen = False
turn = "left"
key_pressed = False
collision = False
attacked = False
skip_turn = False
death_animation_played = False
icon_id = "none"
choose_random_character = 0
code_skip = False
salvo_soldier = False
num_of_salvo_shots = 0
characters_setup = False

des_setup = False


attacks_list = [1, 2]
appended_3 = False
appended_4 = False
bot_attacked = False
check_if_attack_finished = True

run = True


#Initialising Objects
bg_image = pygame.image.load('assets/Bg_ready/street_bg_r.png').convert_alpha()
bg_street_image = pygame.image.load('assets/Bg_ready/street_bg_r.png').convert_alpha()
bg_fountain_image = pygame.image.load('assets/Bg_ready/fountain_bg_r.png').convert_alpha()
bg_hell_image = pygame.image.load('assets/Bg_ready/hell_bg_r.png').convert_alpha()
bg_roof_image = pygame.image.load('assets/Bg_ready/roof_bg_r.png').convert_alpha()

back_img, back_img_hg = pygame.image.load('assets/back_btn_1.png').convert_alpha(), pygame.image.load('assets/back_btn_2.png').convert_alpha()
text_img, text_img_hg = pygame.image.load('assets/text.png').convert_alpha(), pygame.image.load('assets/text.png').convert_alpha()
frame_img, frame_img_hg = pygame.image.load('assets/frame.png').convert_alpha(), pygame.image.load('assets/frame_hg.png').convert_alpha()


jonny_preview = object.Object(0, 0, pygame.image.load('assets/fighter_preview.png').convert_alpha(), 0.85, 0.9)
wizard_preview = object.Object(0, 0, pygame.image.load('assets/mage_preview.png').convert_alpha(), 1.11, 1.1)
jonny_preview_extra = object.Object(0, 0, pygame.image.load('assets/fighter_preview.png').convert_alpha(), 0.85, 0.9)
wizard_preview_extra = object.Object(0, 0, pygame.image.load('assets/mage_preview.png').convert_alpha(), 1.11, 1.1)
golem_preview = object.Object(0, 0, pygame.image.load('assets/golem_preview.png').convert_alpha(), 0.935, 1.07)
golem_preview_extra = object.Object(0, 0, pygame.image.load('assets/golem_preview.png').convert_alpha(), 0.935, 1.07)
soldier_preview = object.Object(0, 0, pygame.image.load('assets/soldier_preview.png').convert_alpha(), 1, 0.95)
soldier_preview_extra = object.Object(0, 0, pygame.image.load('assets/soldier_preview.png').convert_alpha(), 1, 0.95)


jonny_preview_characters = object.Object(0, 0, pygame.image.load('assets/fighter_preview.png').convert_alpha(), 1.15, 1.15)
wizard_preview_characters = object.Object(0, 0, pygame.image.load('assets/mage_preview.png').convert_alpha(), 1.4, 1.4)
golem_preview_characters = object.Object(0, 0, pygame.image.load('assets/golem_preview.png').convert_alpha(), 1.29, 1.45)
soldier_preview_characters = object.Object(0, 0, pygame.image.load('assets/soldier_preview.png').convert_alpha(), 1.35, 1.315)
stand_place = object.Object(140, 75, pygame.image.load('assets/frame.png').convert_alpha(), 1, 1.4)


frame_health_bar_left = object.Object(50, 50, pygame.image.load('assets/frame_health_bar.png').convert_alpha(), 1, 1)
frame_health_bar_right = object.Object(650, 50, pygame.image.load('assets/frame_health_bar.png').convert_alpha(), 1, 1)
frame_armor_bar_left = object.Object(50, 125, pygame.image.load('assets/frame_health_bar.png').convert_alpha(), 0.7, 0.8)
frame_armor_bar_right = object.Object(1050-400*0.7, 125, pygame.image.load('assets/frame_health_bar.png').convert_alpha(), 0.7, 0.8)
frame_ulta_left = object.Object(50, 200, pygame.image.load('assets/ulta.png').convert_alpha(), 1.75, 1.75)
frame_ulta_right = object.Object(975, 200, pygame.image.load('assets/ulta.png').convert_alpha(), 1.75, 1.75)
frame_super_ulta_left = object.Object(150, 200, pygame.image.load('assets/super_ulta.png').convert_alpha(), 1.75, 1.75)
frame_super_ulta_right = object.Object(875, 200, pygame.image.load('assets/super_ulta.png').convert_alpha(), 1.75, 1.75)
p1_icon = object.Object(510, 40, pygame.image.load('assets/p1_icon.png').convert_alpha(), 1, 1)
p2_icon = object.Object(510, 40, pygame.image.load('assets/p2_icon.png').convert_alpha(), 1, 1)
left_ulta_active = object.Object(45, 195, pygame.image.load('assets/active_u_su.png').convert_alpha(), 2, 2)
left_super_ulta_active = object.Object(145, 195, pygame.image.load('assets/active_u_su.png').convert_alpha(), 2, 2)
right_ulta_active = object.Object(970, 195, pygame.image.load('assets/active_u_su.png').convert_alpha(), 2, 2)
right_super_ulta_active = object.Object(870, 195, pygame.image.load('assets/active_u_su.png').convert_alpha(), 2, 2)
ko_title = object.Object(350, 125, pygame.image.load('assets/ko_image.png').convert_alpha(), 1, 1)


wizards_sphere = object.DamagingObject(0, 0, pygame.image.load('assets/sphere.png').convert_alpha(), 1.2, 1.2)
wizards_arrow = object.DamagingObject(0, 0, pygame.image.load('assets/arrow.png').convert_alpha(), 1.2, 1.2)
jonnys_punch = object.DamagingObject(0, 0, pygame.image.load('assets/punchwave.png').convert_alpha(), 1.2, 1.2)
fireray = object.AppearingDamagingObject(0, 0, pygame.image.load('assets/fireray_1.png').convert_alpha(), 1, 1)
fireball_1 = object.DamagingObject(0, 0, pygame.image.load('assets/fireball_2.png').convert_alpha(), 0.6, 0.6)
fireball_2 = object.DamagingObject(0, 0, pygame.image.load('assets/fireball_1.png').convert_alpha(), 0.8, 0.8)
explosion = object.AppearingDamagingObject(0, 0, pygame.image.load('assets/explosion.png').convert_alpha(), 2, 2)


#Initialising characters
jonny = character.Fighter(0, 120, 1)
wizard = character.Mage(0, 120, 1.2)
golem = character.Golem(350, 350, 1)
soldier = character.Soldier(350, 350, 1)

#Initialising buttons
options = button.Button(pygame.image.load('assets/options_btn_1.png').convert_alpha(), pygame.image.load('assets/options_btn_2.png').convert_alpha(), 150, 275, 1.2)
start = button.Button(pygame.image.load('assets/start_btn_1.png').convert_alpha(), pygame.image.load('assets/start_btn_2.png').convert_alpha(), 150, 100, 1.2)
exit = button.Button(pygame.image.load('assets/exit_btn_1.png').convert_alpha(), pygame.image.load('assets/exit_btn_2.png').convert_alpha(), 150, 450, 1.2)
how_to_play = button.Button(pygame.image.load('assets/howtoplay_btn_1.png').convert_alpha(), pygame.image.load('assets/howtoplay_btn_2.png').convert_alpha(), 450, 100, 1.2)
characters = button.Button(pygame.image.load('assets/characters_btn_1.png').convert_alpha(), pygame.image.load('assets/characters_btn_2.png').convert_alpha(), 450, 275, 1.2)
credits = button.Button(pygame.image.load('assets/credits_btn_1.png').convert_alpha(), pygame.image.load('assets/credits_btn_2.png').convert_alpha(), 450, 450, 1.2)
p_1 = button.Button(pygame.image.load('assets/p_1_btn_1.png').convert_alpha(), pygame.image.load('assets/p_1_btn_2.png').convert_alpha(), 150, 50, 1)
p_2 = button.Button(pygame.image.load('assets/p_2_btn_1.png').convert_alpha(), pygame.image.load('assets/p_2_btn_2.png').convert_alpha(), 650, 50, 1)
random_left = button.Button(pygame.image.load('assets/random_btn_1.png').convert_alpha(), pygame.image.load('assets/random_btn_2.png').convert_alpha(), 135, 395, 0.5)
random_right = button.Button(pygame.image.load('assets/random_btn_1.png').convert_alpha(), pygame.image.load('assets/random_btn_2.png').convert_alpha(), 795, 395, 0.5)
fight_btn = button.Button(pygame.image.load('assets/fight_btn_1.png').convert_alpha(), pygame.image.load('assets/fight_btn_2.png').convert_alpha(), 50, 475, 0.7)
back_1 = button.Button(back_img, back_img_hg, 50, 550, 0.7)

characters_jonny_btn = button.Button(frame_img, frame_img_hg, 450, 75, 0.7)
characters_wizard_btn = button.Button(frame_img, frame_img_hg, 750, 75, 0.7)
characters_golem_btn = button.Button(frame_img, frame_img_hg, 450, 325, 0.7)
characters_soldier_btn = button.Button(frame_img, frame_img_hg, 750, 325, 0.7)

frame_lobby_jonny_left = button.Button(frame_img, frame_img_hg, 50, 50, 0.5)
frame_lobby_wizard_left = button.Button(frame_img, frame_img_hg, 250, 50, 0.5)
frame_lobby_jonny_right = button.Button(frame_img, frame_img_hg, 700, 50, 0.5)
frame_lobby_wizard_right = button.Button(frame_img, frame_img_hg, 900, 50, 0.5)
frame_lobby_golem_left = button.Button(frame_img, frame_img_hg, 50, 215, 0.5)
frame_lobby_golem_right = button.Button(frame_img, frame_img_hg, 700, 215, 0.5)
frame_lobby_soldier_left = button.Button(frame_img, frame_img_hg, 250, 215, 0.5)
frame_lobby_soldier_right = button.Button(frame_img, frame_img_hg, 900, 215, 0.5)

bg_fountain_btn = button.Button(pygame.image.load('assets/Bg_ready/fountain_bg_r.png'), pygame.image.load('assets/Bg_ready/fountain_bg_r_hg.png'), 500, 500, 0.15)
bg_hell_btn = button.Button(pygame.image.load('assets/Bg_ready/hell_bg_r.png'), pygame.image.load('assets/Bg_ready/hell_bg_r_hg.png'), 700, 500, 0.15)
bg_street_btn = button.Button(pygame.image.load('assets/Bg_ready/street_bg_r.png'), pygame.image.load('assets/Bg_ready/street_bg_r_hg.png'), 900, 500, 0.15)
bg_roof_btn = button.Button(pygame.image.load('assets/Bg_ready/roof_bg_r.png'), pygame.image.load('assets/Bg_ready/roof_bg_r_hg.png'), 300, 500, 0.15)


health_bar_left = pygame.Rect(hb_l_x, 55, hb_full_width, 40)
health_bar_right = pygame.Rect(hb_r_x, 55, hb_full_width, 40)
armor_bar_left = pygame.Rect(ab_l_x, 129, ab_full_width, 50*0.8-5)
armor_bar_right = pygame.Rect(ab_r_x, 129, ab_full_width, 50*0.8-5)



#Sprite Groups
options_sprites = pygame.sprite.Group()
main_menu_sprites = pygame.sprite.Group()
how_to_play_sprites = pygame.sprite.Group()
credits_sprites = pygame.sprite.Group()
characters_sprites = pygame.sprite.Group()
start_sprites = pygame.sprite.Group()
lobby_sprites = pygame.sprite.Group()
arena_sprites = pygame.sprite.Group()
damaging_objects_sprites = pygame.sprite.Group()
finish_sprites = pygame.sprite.Group()
dam_obj_test = pygame.sprite.Group()
jonny_description_sprites = pygame.sprite.Group()
wizard_description_sprites = pygame.sprite.Group()
golem_description_sprites = pygame.sprite.Group()
soldier_description_sprites = pygame.sprite.Group()


main_menu_sprites.add(start, exit, options)
dam_obj_test.add()
options_sprites.add(how_to_play, characters, credits, back_1)
how_to_play_sprites.add(back_1)
credits_sprites.add(back_1)
characters_sprites.add(characters_jonny_btn, characters_wizard_btn, back_1, characters_golem_btn, characters_soldier_btn, jonny_preview_characters, wizard_preview_characters, golem_preview_characters, soldier_preview_characters)
start_sprites.add(back_1, p_1, p_2)
lobby_sprites.add(back_1, random_left, random_right, fight_btn, frame_lobby_jonny_left, frame_lobby_jonny_right, frame_lobby_wizard_left, frame_lobby_wizard_right, jonny_preview, wizard_preview, jonny_preview_extra, frame_lobby_golem_left, frame_lobby_golem_right, wizard_preview_extra, golem_preview, golem_preview_extra, frame_lobby_soldier_left, frame_lobby_soldier_right, soldier_preview_extra, soldier_preview, bg_fountain_btn, bg_hell_btn, bg_street_btn, bg_roof_btn)
arena_sprites.add( left_ulta_active, left_super_ulta_active, right_super_ulta_active, right_ulta_active, frame_health_bar_left, frame_health_bar_right, frame_armor_bar_left, frame_armor_bar_right, frame_super_ulta_left, frame_super_ulta_right, frame_ulta_left, frame_ulta_right, p1_icon, p2_icon)
damaging_objects_sprites.add()
jonny_description_sprites.add(stand_place, jonny, back_1)
wizard_description_sprites.add(stand_place, wizard, back_1)
golem_description_sprites.add(stand_place, golem, back_1)
soldier_description_sprites.add(stand_place, soldier, back_1)






#General Functions 
def checkArcsLessZeroToMakeInvisible():
    global right_ulta_arc
    global right_super_ulta_arc
    global right_ulta_active
    global right_super_ulta_active
    global left_ulta_arc
    global left_super_ulta_arc
    global left_ulta_active
    global left_super_ulta_active

    if right_ulta_arc < 2.5*math.pi:
        right_ulta_active.visible = False

    if right_super_ulta_arc < 2.5*math.pi:
        right_super_ulta_active.visible = False

    if left_ulta_arc < 2.5*math.pi:
        left_ulta_active.visible = False

    if left_super_ulta_arc < 2.5*math.pi:
        left_super_ulta_active.visible = False

def checkArcsLessZeroToRestoreInitial():
    global right_ulta_arc
    global right_super_ulta_arc
    global right_ulta_active
    global left_ulta_arc
    global left_super_ulta_arc
    global left_ulta_active
    

    if left_ulta_arc < math.pi/2:
        left_ulta_arc = math.pi/2
    if left_super_ulta_arc < math.pi/2:
        left_super_ulta_arc = math.pi/2

    if right_ulta_arc <= math.pi/2:
        right_ulta_arc = math.pi/2           
    if right_super_ulta_arc <= math.pi/2:
        right_super_ulta_arc = math.pi/2

def checkArcsFullToCalibrate():
    global right_ulta_arc
    global right_super_ulta_arc
    global right_ulta_active
    global right_super_ulta_active
    global left_ulta_arc
    global left_super_ulta_arc
    global left_ulta_active
    global left_super_ulta_active

    if right_ulta_arc >= 2.5*math.pi:
        right_ulta_arc = 2.5*math.pi
        right_ulta_active.visible = True

    if right_super_ulta_arc >= 2.5*math.pi:
        right_super_ulta_arc = 2.5*math.pi
        right_super_ulta_active.visible = True

    if left_ulta_arc >= 2.5*math.pi:
        left_ulta_arc = 2.5*math.pi
        left_ulta_active.visible = True

    if left_super_ulta_arc >= 2.5*math.pi:
        left_super_ulta_arc = 2.5*math.pi
        left_super_ulta_active.visible = True
  
def restoreInitialArmorIfZero():
    global armor_bar_left
    global armor_bar_right

    if armor_bar_left.width <= 0:
        armor_bar_left.width = 0
    if armor_bar_right.width <= 0:
        armor_bar_right.width = 0

def commitDamageToLeft():
    global health_bar_left
    global armor_bar_left
    global hb_damage
    global ab_damage
    global left_super_ulta_arc
    global left_ulta_arc
    global damage_u
    global damage_su

    health_bar_left.width -= hb_damage
    armor_bar_left.width -= ab_damage

    left_ulta_arc -= damage_u
    left_super_ulta_arc -= damage_su

    hb_damage = 0
    ab_damage =0
    damage_u = 0
    damage_su = 0

def commitDamageToRight():
    global health_bar_right
    global armor_bar_right
    global hb_damage
    global ab_damage
    global right_super_ulta_arc
    global right_ulta_arc
    global damage_u
    global damage_su

    health_bar_right.width -= hb_damage
    health_bar_right.x += hb_damage
    armor_bar_right.width -= ab_damage
    armor_bar_right.x += ab_damage

    right_ulta_arc -= damage_u
    right_super_ulta_arc -= damage_su
            
    hb_damage = 0
    ab_damage = 0
    damage_u = 0
    damage_su = 0

def chargeUpLeft():
    global left_super_ulta_arc
    global left_ulta_arc
    global charge_u
    global charge_su

    left_ulta_arc += charge_u
    left_super_ulta_arc += charge_su

    charge_u = 0
    charge_su = 0

def chargeUpRight():
    global right_super_ulta_arc
    global right_ulta_arc
    global charge_u
    global charge_su

    right_ulta_arc += charge_u
    right_super_ulta_arc += charge_su

    charge_u = 0
    charge_su = 0


#Before loop
left_super_ulta_active.visible = False
right_super_ulta_active.visible = False
ko_title.visible = False
left_ulta_active.visible = False
right_ulta_active.visible = False
p1_icon.visible = False
p2_icon.visible = False



#Main loop
while run:
    
    screen.blit(bg_image, (0,0))
    key = pygame.KEYDOWN
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
           
    if scene == "main_menu":
       
        main_menu_sprites.draw(screen)
        main_menu_sprites.update()

    

        if interval < 4000:
            interval += 1
        
        if start.check_clicked() and interval >= 2:
            scene = "start"
            cleared= False
            interval = 0
        
        if options.check_clicked() and interval >= 2:
            scene = "options"
            cleared = False
            interval = 0
    
        if exit.check_clicked() and interval >= 2:
            run=False
            cleared = False
            interval = 0

    if scene == "options":
        options_sprites.draw(screen)
        options_sprites.update()

        if interval < 10:
            interval += 1
        
        if how_to_play.check_clicked() and interval >= 2:
            scene = "how_to_play"
            cleared = False
            interval = 0
    
        if characters.check_clicked() and interval >= 2:
            scene = "characters"
            cleared = False
            interval = 0

        if credits.check_clicked() and interval >= 2:
            scene = "credits"
            cleared = False
            interval = 0
    
        if back_1.check_clicked() and interval >= 2:
            scene = "main_menu"
            cleared = False
            interval = 0
   
    if scene == "how_to_play":
        
        how_to_play_sprites.draw(screen)
        how_to_play_sprites.update()
        
        if interval < 10:
            interval += 1
       
    
        if back_1.check_clicked() and interval >= 2:
            scene = "options"
            cleared = False
        
    if scene == "credits":
        
        credits_sprites.draw(screen)
        credits_sprites.update()

        if interval < 10:
            interval += 1

        if back_1.check_clicked() and interval >= 2:
            scene = "options"
            cleared = False
            interval = 0
        
    if scene == "characters":
        #to be redone
        if characters_setup == False:

            jonny_preview_characters.changeCordinates(460, 91)
            wizard_preview_characters.changeCordinates(750, 73)
            golem_preview_characters.changeCordinates(461, 315)
            soldier_preview_characters.changeCordinates(765, 336)
            

            characters_setup = True
            characters_sprites.update()

        characters_sprites.draw(screen)
        
        if interval < 10:
            interval += 1

        if characters_jonny_btn.check_clicked() and interval >= 2:
            scene = "jonny_description"
            cleared = False
            interval = 0

        if characters_wizard_btn.check_clicked() and interval >= 2:
            scene = "wizard_description"
            cleared = False
            interval = 0
        
        if characters_golem_btn.check_clicked() and interval >= 2:
            scene = "golem_description"
            cleared = False
            interval = 0

        if characters_soldier_btn.check_clicked() and interval >= 2:
            scene = "soldier_description"
            cleared = False
            interval = 0
        
        

        if back_1.check_clicked() and interval >= 2:
            scene = "options"
            cleared = False
            interval = 0

        characters_sprites.update()

    if scene == "jonny_description":
        if interval < 10:
            interval += 1

        if des_setup == False:
            jonny.changeCordinates(325, 275)
            des_setup = True


        jonny_description_sprites.draw(screen)
        jonny_description_sprites.update()

        if back_1.check_clicked() and interval >= 2:
            scene = "characters"
            interval = 0
            des_setup = False

    if scene == "wizard_description":
        if interval < 10:
            interval += 1

        if des_setup == False:
            wizard.changeCordinates(405, 245)
            des_setup = True


        wizard_description_sprites.draw(screen)
        wizard_description_sprites.update()

        if back_1.check_clicked() and interval >= 2:
            scene = "characters"
            interval = 0
            des_setup = False
        
    if scene == "golem_description":
        if interval < 10:
            interval += 1

        if des_setup == False:
            golem.changeCordinates(350, 275)
            des_setup = True


        golem_description_sprites.draw(screen)
        golem_description_sprites.update()

        if back_1.check_clicked() and interval >= 2:
            scene = "characters"
            interval = 0
            des_setup = False

    if scene == "soldier_description":
        if interval < 10:
            interval += 1

        if des_setup == False:
            soldier.changeCordinates(340, 275)
            des_setup = True


        soldier_description_sprites.draw(screen)
        soldier_description_sprites.update()

        if back_1.check_clicked() and interval >= 2:
            scene = "characters"
            interval = 0
            des_setup = False

    if scene == "start":

        start_sprites.draw(screen)
        start_sprites.update()

        if interval < 10:
            interval += 1

        if p_1.check_clicked() and interval >= 2:
            scene = "lobby"
            cleared = False
            num_of_players = 1
            interval = 0

        if p_2.check_clicked() and interval >= 2:
            scene = "lobby"
            cleared = False
            num_of_players = 2
            interval = 0

        if back_1.check_clicked():
            scene = "main_menu"
            cleared = False
            interval = 0

    if scene == "lobby":

        if interval < 10:
            interval += 1

        if setup_lobby == False:
            jonny_preview.changeCordinates(55, 50)
            wizard_preview.changeCordinates(243, 35)
            golem_preview.changeCordinates(57, 203)
            soldier_preview.changeCordinates(255, 223)
            
            jonny_preview_extra.flip()
            wizard_preview_extra.flip()
            golem_preview_extra.flip()
            soldier_preview_extra.flip()
            
            jonny_preview_extra.changeCordinates(710, 50)
            wizard_preview_extra.changeCordinates(898, 35)
            golem_preview_extra.changeCordinates(709, 203)
            soldier_preview_extra.changeCordinates(885, 223)

            
            setup_lobby = True

        lobby_sprites.draw(screen)
        
        if back_1.check_clicked() and interval >= 2:
            scene = "start"
            interval = 0
            random_left.deselect()
            random_right.deselect()
            frame_lobby_jonny_left.deselect()
            frame_lobby_wizard_left.deselect()
            frame_lobby_golem_left.deselect()
            frame_lobby_jonny_right.deselect()
            frame_lobby_golem_right.deselect()
            frame_lobby_wizard_right.deselect()
            bg_hell_btn.deselect()
            bg_fountain_btn.deselect()
            bg_street_btn.deselect()
            bg_roof_btn.deselect()

        if random_left.check_clicked() and interval >=2:
            random_left.select_deselect()
            frame_lobby_jonny_left.deselect()
            frame_lobby_golem_left.deselect()
            frame_lobby_wizard_left.deselect()
            if selected_character_left == "random":
                selected_character_left = "noone"  
            else:
                selected_character_left = "random"
            interval = 0
            
        if random_right.check_clicked() and interval >=2:
            random_right.select_deselect()
            frame_lobby_jonny_right.deselect()
            frame_lobby_golem_right.deselect()
            frame_lobby_wizard_right.deselect()
            if selected_character_right == "random":
                selected_character_right = "noone"
            else:
                selected_character_right = "random"
            interval = 0
        

        if frame_lobby_jonny_left.check_clicked() and interval >=2:
            frame_lobby_jonny_left.select_deselect()
            frame_lobby_golem_left.deselect()
            frame_lobby_wizard_left.deselect()
            frame_lobby_soldier_left.deselect()
            random_left.deselect()
            if selected_character_left == "jonny":
                selected_character_left = "noone"  
            else:
                selected_character_left = "jonny"
            interval = 0

        if frame_lobby_jonny_right.check_clicked() and interval >=2:
            frame_lobby_jonny_right.select_deselect()
            frame_lobby_golem_right.deselect()
            frame_lobby_wizard_right.deselect()
            frame_lobby_soldier_right.deselect()
            random_right.deselect()
            if selected_character_right == "jonny":
                selected_character_right = "noone"  
            else:
                selected_character_right = "jonny"
            interval = 0

        if frame_lobby_wizard_left.check_clicked() and interval >=2:
            frame_lobby_wizard_left.select_deselect()
            frame_lobby_golem_left.deselect()
            frame_lobby_jonny_left.deselect()
            frame_lobby_soldier_left.deselect()
            random_left.deselect()
            if selected_character_left == "wizard":
                selected_character_left = "noone"  
            else:
                selected_character_left = "wizard"
            interval = 0

        if frame_lobby_wizard_right.check_clicked() and interval >=2:
            frame_lobby_wizard_right.select_deselect()
            frame_lobby_jonny_right.deselect()
            frame_lobby_golem_right.deselect()
            frame_lobby_soldier_right.deselect()
            random_right.deselect()
            if selected_character_right == "wizard":
                selected_character_right = "noone"  
            else:
                selected_character_right = "wizard"
            interval = 0

        if frame_lobby_golem_left.check_clicked() and interval >=2:
            frame_lobby_golem_left.select_deselect()
            frame_lobby_wizard_left.deselect()
            frame_lobby_jonny_left.deselect()
            frame_lobby_soldier_left.deselect()
            random_left.deselect()
            if selected_character_left == "golem":
                selected_character_left = "noone"  
            else:
                selected_character_left = "golem"
            interval = 0
        
        if frame_lobby_golem_right.check_clicked() and interval >=2:
            frame_lobby_golem_right.select_deselect()
            frame_lobby_wizard_right.deselect()
            frame_lobby_jonny_right.deselect()
            frame_lobby_soldier_right.deselect()
            random_right.deselect()
            if selected_character_right == "golem":
                selected_character_right = "noone"  
            else:
                selected_character_right = "golem"
            interval = 0
        
        if frame_lobby_soldier_left.check_clicked() and interval >=2:
            frame_lobby_soldier_left.select_deselect()
            frame_lobby_wizard_left.deselect()
            frame_lobby_jonny_left.deselect()
            frame_lobby_golem_left.deselect()
            random_left.deselect()
            if selected_character_left == "soldier":
                selected_character_left = "noone"  
            else:
                selected_character_left = "soldier"
            interval = 0
        
        if frame_lobby_soldier_right.check_clicked() and interval >=2:
            frame_lobby_soldier_right.select_deselect()
            frame_lobby_wizard_right.deselect()
            frame_lobby_jonny_right.deselect()
            frame_lobby_golem_right.deselect()
            random_right.deselect()
            if selected_character_right == "soldier":
                selected_character_right = "noone"  
            else:
                selected_character_right = "soldier"
            interval = 0

        if bg_hell_btn.check_clicked() and interval >=2:
            bg_hell_btn.select_deselect()
            bg_fountain_btn.deselect()
            bg_street_btn.deselect()
            bg_roof_btn.deselect()
            if selected_background == "hell":
                selected_background = "none"  
            else:
                selected_background = "hell"
            interval = 0
        
        if bg_street_btn.check_clicked() and interval >=2:
            bg_street_btn.select_deselect()
            bg_fountain_btn.deselect()
            bg_hell_btn.deselect()
            bg_roof_btn.deselect()
            if selected_background == "stree":
                selected_background = "none"  
            else:
                selected_background = "street"
            interval = 0
        
        if bg_fountain_btn.check_clicked() and interval >=2:
            bg_fountain_btn.select_deselect()
            bg_hell_btn.deselect()
            bg_street_btn.deselect()
            bg_roof_btn.deselect()
            if selected_background == "fountain":
                selected_background = "none"  
            else:
                selected_background = "fountain"
            interval = 0
        
        if bg_roof_btn.check_clicked() and interval >=2:
            bg_roof_btn.select_deselect()
            bg_fountain_btn.deselect()
            bg_street_btn.deselect()
            bg_hell_btn.deselect()
            if selected_background == "roof":
                selected_background = "none"  
            else:
                selected_background = "roof"
            interval = 0

        if fight_btn.check_clicked() and selected_character_left != "noone" and selected_character_right != "noone" and selected_background != "none":
            scene = "arena"
            interval = 0
            

        lobby_sprites.update()

    if scene == "arena":
        
        if interval < 200:
            interval += 1
        icon_id = "none"
        
        #setup arena
        if characters_chosen == False:
            if selected_background == "street":
                bg_image = bg_street_image
            elif selected_background == "roof":
                bg_image = bg_roof_image
            elif selected_background == "fountain":
                bg_image = bg_fountain_image
            elif selected_background == "hell":
                bg_image = bg_hell_image
            
            if selected_character_left == "jonny":
                selected_character_left = jonny

                selected_character_left.changeCordinates(300, 440)
                arena_sprites.add(selected_character_left)
                choose_random_character = 1

            elif selected_character_left == "wizard":
                selected_character_left = wizard

                selected_character_left.changeCordinates(350, 405)
                arena_sprites.add(selected_character_left)
                choose_random_character = 2

            elif selected_character_left == "golem":
                selected_character_left = golem

                selected_character_left.changeCordinates(280, 440)
                arena_sprites.add(selected_character_left)
                choose_random_character = 3

            elif selected_character_left == "soldier":
                selected_character_left = soldier

                selected_character_left.changeCordinates(280, 440)
                arena_sprites.add(selected_character_left)
                choose_random_character = 4
            
           
                

            if selected_character_right == "jonny":
                selected_character_right = jonny

                selected_character_right.flip()
                selected_character_right.changeCordinates(840, 440)
                arena_sprites.add(selected_character_right)
                choose_random_character = 1
                

            elif selected_character_right == "wizard":
                selected_character_right = wizard

                selected_character_right.flip()
                selected_character_right.changeCordinates(760, 405)
                arena_sprites.add(selected_character_right)
                choose_random_character = 2

            elif selected_character_right == "golem":
                selected_character_right = golem

                selected_character_right.flip()
                selected_character_right.changeCordinates(800, 440)
                arena_sprites.add(selected_character_right)
                choose_random_character = 3
            
            elif selected_character_right == "soldier":
                selected_character_right = soldier

                selected_character_right.flip()
                selected_character_right.changeCordinates(800, 440)
                arena_sprites.add(selected_character_right)
                choose_random_character = 4

            
            if selected_character_left == "random":
                buffer = choose_random_character
                while choose_random_character == buffer:
                    choose_random_character = random.randint(1, 4)
                print(choose_random_character)
                if choose_random_character == 1:
                    selected_character_left = jonny
                    selected_character_left.changeCordinates(300, 440)
                    arena_sprites.add(selected_character_left)
                elif choose_random_character == 2:
                    selected_character_left = wizard
                    selected_character_left.changeCordinates(350, 405)
                    arena_sprites.add(selected_character_left)
                elif choose_random_character == 3:
                    selected_character_left = golem
                    selected_character_left.changeCordinates(280, 440)
                    arena_sprites.add(selected_character_left)
                elif choose_random_character == 4:
                    selected_character_left = soldier
                    selected_character_left.changeCordinates(280, 440)
                    arena_sprites.add(selected_character_left)

            if selected_character_right == "random":
                buffer = choose_random_character
                while choose_random_character == buffer:
                    choose_random_character = random.randint(1,4)

                if choose_random_character == 1:
                    selected_character_right = jonny
                    selected_character_right.flip()
                    selected_character_right.changeCordinates(840, 440)
                    arena_sprites.add(selected_character_right)
                elif choose_random_character == 2:
                    selected_character_right = wizard
                    selected_character_right.flip()
                    selected_character_right.changeCordinates(760, 405)
                    arena_sprites.add(selected_character_right)
                elif choose_random_character == 3:
                    selected_character_right = golem
                    selected_character_right.flip()
                    selected_character_right.changeCordinates(800, 440)
                    arena_sprites.add(selected_character_right)
                elif choose_random_character == 4:
                    selected_character_right = soldier
                    selected_character_right.flip()
                    selected_character_right.changeCordinates(800, 440)
                    arena_sprites.add(selected_character_right)


                

            characters_chosen = True
            damaging_objects_sprites.add(wizards_arrow, wizards_sphere, jonnys_punch, fireball_1, fireball_2)
            arena_sprites.add(fireray, explosion, ko_title)
            print(selected_character_left, selected_character_right)
        

        pygame.draw.rect(screen, (0,255,0), health_bar_left)
        pygame.draw.rect(screen, (0,255,0), health_bar_right)
        pygame.draw.rect(screen, (90, 90, 90), armor_bar_left)
        pygame.draw.rect(screen, (90, 90, 90), armor_bar_right)
        
        arena_sprites.update()
        damaging_objects_sprites.update(collision)
        damaging_objects_sprites.draw(screen)
        arena_sprites.draw(screen)
        
        collision = False

        pygame.draw.arc(screen, (0,0,255), (50, 200, 72, 72), math.pi/2, left_ulta_arc, width = 11)
        pygame.draw.arc(screen, (0,0,255), (975, 200, 72, 72), math.pi/2, right_ulta_arc, width = 11)
        pygame.draw.arc(screen, (0,0,255), (150, 200, 72, 72), math.pi/2, left_super_ulta_arc, width = 11)
        pygame.draw.arc(screen, (0,0,255), (875, 200, 72, 72), math.pi/2, right_super_ulta_arc, width = 11)


        key = pygame.key.get_pressed()

        checkArcsLessZeroToMakeInvisible()
        checkArcsFullToCalibrate()
        

        if pygame.sprite.spritecollide(selected_character_left, damaging_objects_sprites, False, pygame.sprite.collide_mask) and turn =="left":
            selected_character_left.hurt()

            commitDamageToLeft()
            chargeUpRight()
            

            checkArcsLessZeroToRestoreInitial()
            checkArcsFullToCalibrate()

            restoreInitialArmorIfZero()

            collision = True
            check_if_attack_finished = True
            interval = 0
            

        if pygame.sprite.spritecollide(selected_character_right, damaging_objects_sprites, False, pygame.sprite.collide_mask) and turn == "right":
            selected_character_right.hurt()
            
            commitDamageToRight()
            chargeUpLeft()
            

            checkArcsLessZeroToRestoreInitial()
            checkArcsFullToCalibrate()
            restoreInitialArmorIfZero()

            collision = True
            check_if_attack_finished = True
            interval = 0
            
        

        if attacked == True and wait_to_hurt < interval:
            if hurt_who == "hurt_right":
                selected_character_right.hurt()
                commitDamageToRight()
                chargeUpLeft()
                
                checkArcsLessZeroToRestoreInitial()
                checkArcsFullToCalibrate()
                restoreInitialArmorIfZero()

            elif hurt_who == "hurt_left":
                selected_character_left.hurt()
                commitDamageToLeft()
                chargeUpRight()

                checkArcsLessZeroToRestoreInitial()
                checkArcsFullToCalibrate()
                restoreInitialArmorIfZero()
                
            attacked = False
            interval = 0
            
        if salvo_soldier == True and wait_to_hurt < interval and num_of_salvo_shots != 0:
            if hurt_who == "hurt_right":
                if num_of_salvo_shots > 1:
                    selected_character_right.hurt()
                    commitDamageToRight()
                    chargeUpLeft()
                
                    checkArcsLessZeroToRestoreInitial()
                    checkArcsFullToCalibrate()
                    restoreInitialArmorIfZero()

                    damage = selected_character_left.getDamageTotal()
                    hb_damage = selected_character_left.getDamageHB()
                    ab_damage = selected_character_left.getDamageAB()
                    charge_u = selected_character_left.getChargeU()
                    charge_su = selected_character_left.getChargeSU()
                    damage_u = selected_character_left.getDamageU()
                    damage_su = selected_character_left.getDamageSU()  

                    num_of_salvo_shots -= 1
                    interval = 0

                elif num_of_salvo_shots == 1:
                    selected_character_right.hurt()
                    commitDamageToRight()
                    chargeUpLeft()
                
                    checkArcsLessZeroToRestoreInitial()
                    checkArcsFullToCalibrate()
                    restoreInitialArmorIfZero()

                    num_of_salvo_shots -= 1
                    interval = 0
                    turn = "right"
                    salvo_soldier = False


            elif hurt_who == "hurt_left":
                if num_of_salvo_shots > 1:
                    selected_character_left.hurt()
                    commitDamageToLeft()
                    chargeUpRight()
                
                    checkArcsLessZeroToRestoreInitial()
                    checkArcsFullToCalibrate()
                    restoreInitialArmorIfZero()

                    damage = selected_character_right.getDamageTotal()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU()  

                    num_of_salvo_shots -= 1
                    interval = 0

                elif num_of_salvo_shots == 1:
                    selected_character_left.hurt()
                    commitDamageToLeft()
                    chargeUpRight()
                
                    checkArcsLessZeroToRestoreInitial()
                    checkArcsFullToCalibrate()
                    restoreInitialArmorIfZero()

                    num_of_salvo_shots -= 1
                    interval = 0
                    turn = "left"
                    salvo_soldier = False


        if health_bar_left.width <= 0 and turn != "dead" and death_animation_played == False:
            turn = "dead"
            who_dead = "left_dead"
            interval = 0


        
        if turn == "left" and interval > 30 and check_if_attack_finished == True and attacked == False:
            icon_id = "p1"

            if key[pygame.K_1]:
                
                
                selected_character_left.basic_attack(armor_bar_right.width, hb_full_width)
                if selected_character_left == wizard:
                    attacked = True
                    wait_to_hurt = 27
                    hurt_who = "hurt_right"
                
                if selected_character_left == soldier:
                    attacked = True
                    wait_to_hurt = 15
                    hurt_who = "hurt_right"
                    
                    
                    
                if selected_character_left == jonny:
                    jonnys_punch.changeCordinates(400, 310)
                    jonnys_punch.rate = 0.17
                    jonnys_punch.speed = 13
                    jonnys_punch.move()
                    check_if_attack_finished = False
                
                if selected_character_left == golem:
                    fireball_1.changeCordinates(360, 330)
                    fireball_1.rate = 0.17
                    fireball_1.speed = 12
                    fireball_1.move()
                    check_if_attack_finished = False
                    
                    
                    
                damage = selected_character_left.getDamageTotal()
                hb_damage = selected_character_left.getDamageHB()
                ab_damage = selected_character_left.getDamageAB()
                charge_u = selected_character_left.getChargeU()
                charge_su = selected_character_left.getChargeSU()
                damage_u = selected_character_left.getDamageU()
                damage_su = selected_character_left.getDamageSU()  
                print(damage, ab_damage, hb_damage)
                
                turn = "right"
                interval = 0

            if key[pygame.K_2]:
                
                
                selected_character_left.unique_attack(armor_bar_right.width, hb_full_width)
                if selected_character_left == wizard:
                    attacked = True
                    wait_to_hurt = 25
                    hurt_who = "hurt_right"

                if selected_character_left == jonny:
                    jonnys_punch.changeCordinates(410, 410)
                    jonnys_punch.rate = 0.17
                    jonnys_punch.speed = 13
                    jonnys_punch.move()
                    check_if_attack_finished = False

                if selected_character_left == golem:
                    fireball_2.changeCordinates(190, 320)
                    fireball_2.rate = 0.23
                    fireball_2.speed = 9
                    fireball_2.move()
                    check_if_attack_finished = False

                if selected_character_left == soldier: 
                    salvo_soldier = True
                    num_of_salvo_shots = 6
                    wait_to_hurt = 10
                    hurt_who = "hurt_right"
                    


                interval = 0
                turn = "right"

                damage = selected_character_left.getDamageTotal()
                hb_damage = selected_character_left.getDamageHB()
                ab_damage = selected_character_left.getDamageAB()
                charge_u = selected_character_left.getChargeU()
                charge_su = selected_character_left.getChargeSU()
                damage_u = selected_character_left.getDamageU()
                damage_su = selected_character_left.getDamageSU()  
                print(damage, ab_damage, hb_damage)
              
            if key[pygame.K_3] and left_ulta_arc == 2.5*math.pi:
                
                
                selected_character_left.ulta(armor_bar_right.width, hb_full_width)
                if selected_character_left == wizard:
                    wizards_arrow.changeCordinates(385, 440)
                    wizards_arrow.rate = 0.15
                    wizards_arrow.speed = 12
                    wizards_arrow.move()
                    damage = selected_character_left.getDamageTotal()
                    hb_damage = selected_character_left.getDamageHB()
                    ab_damage = selected_character_left.getDamageAB()
                    charge_u = selected_character_left.getChargeU()
                    charge_su = selected_character_left.getChargeSU()
                    damage_u = selected_character_left.getDamageU()
                    damage_su = selected_character_left.getDamageSU()
                    left_ulta_arc += charge_u
                    charge_u = 0
                    check_if_attack_finished = False
                    interval = 0

                if selected_character_left == jonny:
                    charge_u = selected_character_left.getChargeU()
                    charge_su = selected_character_left.getChargeSU() 
                    chargeUpLeft()
                    armor_bar_left.width += ab_full_width*(0.5+round(random.uniform(-0.1, 0.1), 4))
                    health_bar_left.width += hb_full_width*(0.1+round(random.uniform(-0.1, 0.1), 4))

                    if health_bar_left.width >= hb_full_width:
                        health_bar_left.width = hb_full_width
                    if armor_bar_left.width >= ab_full_width:
                        armor_bar_left.width = ab_full_width

                    interval = -50

                if selected_character_left == golem:
                    fireray.changeCordinates(370, 362)
                    fireray.appear_while(20, 40)
                    damage = selected_character_left.getDamageTotal()
                    hb_damage = selected_character_left.getDamageHB()
                    ab_damage = selected_character_left.getDamageAB()
                    charge_u = selected_character_left.getChargeU()
                    charge_su = selected_character_left.getChargeSU()
                    damage_u = selected_character_left.getDamageU()
                    damage_su = selected_character_left.getDamageSU()
                    attacked = True
                    wait_to_hurt = 35
                    hurt_who = "hurt_right"
                    skip_turn = True
                    interval = 0

                if selected_character_left == soldier:
                    
                    damage = selected_character_left.getDamageTotal()
                    hb_damage = selected_character_left.getDamageHB()
                    ab_damage = selected_character_left.getDamageAB()
                    charge_u = selected_character_left.getChargeU()
                    charge_su = selected_character_left.getChargeSU()
                    damage_u = selected_character_left.getDamageU()
                    damage_su = selected_character_left.getDamageSU()
                    chargeUpLeft()
                    armor_bar_left.width += ab_full_width*(0.6+round(random.uniform(-0.15, 0.1), 4))
                    health_bar_left.width += hb_full_width*(0.05+round(random.uniform(-0.05, 0.05), 4))

                    if health_bar_left.width >= hb_full_width:
                        health_bar_left.width = hb_full_width
                    if armor_bar_left.width >= ab_full_width:
                        armor_bar_left.width = ab_full_width

                    interval = -100

                    

                if skip_turn == False:
                    turn = "right"
                elif skip_turn == True:
                    turn = "left"
                    skip_turn = False

                
                print(damage, ab_damage, hb_damage)

            if key[pygame.K_4] and left_super_ulta_arc == 2.5*math.pi:
                
                
                selected_character_left.super_ulta(armor_bar_right.width, hb_full_width)
                
                if selected_character_left == wizard:
                    wizards_sphere.changeCordinates(372, 386)
                    wizards_sphere.rate = 0.062
                    wizards_sphere.speed = 9
                    wizards_sphere.move()
                    armor_bar_left.width -= armor_bar_left.width*0.75
                    damage = selected_character_left.getDamageTotal()
                    hb_damage = selected_character_left.getDamageHB()
                    ab_damage = selected_character_left.getDamageAB()
                    charge_u = selected_character_left.getChargeU()
                    charge_su = selected_character_left.getChargeSU()
                    damage_u = selected_character_left.getDamageU()
                    damage_su = selected_character_left.getDamageSU() 
                    left_super_ulta_arc += charge_su
                    charge_su = 0
                    check_if_attack_finished = False
                    interval = 0

                if selected_character_left == jonny:
                    charge_u = selected_character_left.getChargeU()
                    charge_su = selected_character_left.getChargeSU()
                    chargeUpLeft()
                    checkArcsLessZeroToRestoreInitial()
                    checkArcsFullToCalibrate()
                    interval = -30
                
                if selected_character_left == golem:
                    damage = selected_character_left.getDamageTotal()
                    hb_damage = selected_character_left.getDamageHB()
                    ab_damage = selected_character_left.getDamageAB()
                    charge_u = selected_character_left.getChargeU()
                    charge_su = selected_character_left.getChargeSU()
                    damage_u = selected_character_left.getDamageU()
                    damage_su = selected_character_left.getDamageSU() 
                    attacked = True
                    wait_to_hurt = 12
                    hurt_who = "hurt_right"
                    interval = 0

                if selected_character_left == soldier:
                    explosion.changeCordinates(600, 330)
                    explosion.appear_while(22, 110)
                    damage = selected_character_left.getDamageTotal()
                    hb_damage = selected_character_left.getDamageHB()
                    ab_damage = selected_character_left.getDamageAB()
                    charge_u = selected_character_left.getChargeU()
                    charge_su = selected_character_left.getChargeSU()
                    damage_u = selected_character_left.getDamageU()
                    damage_su = selected_character_left.getDamageSU()
                    chargeUpLeft()
                    charge_u = 0
                    charge_su = 0

                    attacked = True
                    wait_to_hurt = 110
                    hurt_who = "hurt_right"
                    interval = 0
                    


                turn = "right"
                
                
                print(damage, ab_damage, hb_damage)
                
            
       
        if turn == "right" and (interval > 30 and check_if_attack_finished == True and attacked == False) and num_of_players == 2:
            icon_id = "p2"

            if key[pygame.K_1]:
                
                selected_character_right.basic_attack(armor_bar_left.width, hb_full_width)
                if selected_character_right == wizard:
                    attacked = True
                    wait_to_hurt = 27
                    hurt_who = "hurt_left"

                if selected_character_right == soldier:
                    attacked = True
                    wait_to_hurt = 15
                    hurt_who = "hurt_left"

                if selected_character_right == jonny:
                    jonnys_punch.flip()
                    jonnys_punch.changeCordinates(560, 320)
                    jonnys_punch.rate = 0.17
                    jonnys_punch.speed = -13
                    jonnys_punch.move()
                    check_if_attack_finished = False

                if selected_character_right == golem:
                    fireball_1.flip()
                    fireball_1.changeCordinates(620, 330)
                    fireball_1.rate = 0.17
                    fireball_1.speed = -12
                    fireball_1.move()
                    check_if_attack_finished = False


                turn = "left"
                interval = 0
                
                damage = selected_character_right.getDamageTotal()
                hb_damage = selected_character_right.getDamageHB()
                ab_damage = selected_character_right.getDamageAB()
                charge_u = selected_character_right.getChargeU()
                charge_su = selected_character_right.getChargeSU()
                damage_u = selected_character_right.getDamageU()
                damage_su = selected_character_right.getDamageSU()  
                print(damage, ab_damage, hb_damage)

            if key[pygame.K_2]: 
                
                
                selected_character_right.unique_attack(armor_bar_left.width, hb_full_width)
                if selected_character_right == wizard:
                    attacked = True
                    wait_to_hurt = 25
                    hurt_who = "hurt_left"

                if selected_character_right == jonny:
                    jonnys_punch.flip()
                    jonnys_punch.changeCordinates(570, 420)
                    jonnys_punch.rate = 0.17
                    jonnys_punch.speed = -13
                    jonnys_punch.move()
                    check_if_attack_finished = False

                if selected_character_right == golem:
                    fireball_2.flip()
                    fireball_2.changeCordinates(580, 320)
                    fireball_2.rate = 0.23
                    fireball_2.speed = -9
                    fireball_2.move()
                    check_if_attack_finished = False
                
                if selected_character_right == soldier:
                    
                    salvo_soldier = True
                    num_of_salvo_shots = 6
                    wait_to_hurt = 10
                    hurt_who = "hurt_left"


                turn = "left"
                interval = 0
                
                damage = selected_character_right.getDamageTotal()
                hb_damage = selected_character_right.getDamageHB()
                ab_damage = selected_character_right.getDamageAB()
                charge_u = selected_character_right.getChargeU()
                charge_su = selected_character_right.getChargeSU()
                damage_u = selected_character_right.getDamageU()
                damage_su = selected_character_right.getDamageSU()  
                print(damage, ab_damage, hb_damage)

            if key[pygame.K_3] and right_ulta_arc == 2.5*math.pi: 
                
                
                selected_character_right.ulta(armor_bar_left.width, hb_full_width)
                if selected_character_right == wizard:
                    wizards_arrow.changeCordinates(560, 440)
                    wizards_arrow.flip()
                    wizards_arrow.rate = 0.15
                    wizards_arrow.speed = -12
                    wizards_arrow.move()
                    damage = selected_character_right.getDamageTotal()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    right_ulta_arc += charge_u
                    charge_u = 0
                    check_if_attack_finished = False
                    interval = 0

                    

                if selected_character_right == jonny:
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU() 
                    chargeUpRight()
                    heal_armor = ab_full_width*(0.5+round(random.uniform(-0.1, 0.1), 4))
                    heal_health = hb_full_width*(0.1+round(random.uniform(-0.1, 0.1), 4))
                    armor_bar_right.width += heal_armor
                    health_bar_right.width += heal_health
                    armor_bar_right.x -= heal_armor
                    health_bar_right.x -= heal_health
                    right_ulta_active.visible = False
                    if health_bar_right.width >= hb_full_width:
                        health_bar_right.width = hb_full_width          
                    if armor_bar_right.width >= ab_full_width:
                        armor_bar_right.width = ab_full_width
                        armor_bar_right.x = ab_r_x
                    interval = -50
                        
                if selected_character_right == golem:
                    fireray.flip()
                    fireray.changeCordinates(-144, 362)
                    fireray.appear_while(20, 40)
                    damage = selected_character_right.getDamageTotal()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU()
                    attacked = True
                    wait_to_hurt = 35
                    hurt_who = "hurt_left"
                    skip_turn = True
                    interval = 0

                if selected_character_right == soldier:
                    damage = selected_character_right.getDamageTotal()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU()
                    chargeUpRight()
                    heal_armor = ab_full_width*(0.6+round(random.uniform(-0.15, 0.1), 4))
                    heal_health = hb_full_width*(0.05+round(random.uniform(-0.05, 0.05), 4))
                    armor_bar_right.width += heal_armor
                    health_bar_right.width += heal_health
                    armor_bar_right.x -= heal_armor
                    health_bar_right.x -= heal_health
                    right_ulta_active.visible = False
                    if health_bar_right.width >= hb_full_width:
                        health_bar_right.width = hb_full_width          
                    if armor_bar_right.width >= ab_full_width:
                        armor_bar_right.width = ab_full_width
                        armor_bar_right.x = ab_r_x
                    interval = -100
                    

                if skip_turn == False:
                    turn = "left"
                elif skip_turn == True:
                    turn = "right"
                    skip_turn = False
                    

                
                print(damage, ab_damage, hb_damage)

            if key[pygame.K_4] and right_super_ulta_arc == 2.5*math.pi:
                
                
                selected_character_right.super_ulta(armor_bar_left.width, hb_full_width)
                
                if selected_character_right == wizard:
                    wizards_sphere.changeCordinates(495, 387)
                    wizards_sphere.flip()
                    wizards_sphere.rate = 0.06
                    wizards_sphere.speed = -9
                    wizards_sphere.move()
                    armor_bar_right.width -= armor_bar_right.width
                    armor_bar_right.x += armor_bar_right.x
                    damage = selected_character_right.getDamageTotal()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU() 
                    right_super_ulta_arc += charge_su
                    charge_su = 0
                    check_if_attack_finished = False
                    interval = 0

                if selected_character_right == jonny:
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    chargeUpRight()
                    checkArcsLessZeroToRestoreInitial()
                    checkArcsFullToCalibrate()
                    interval = -30
                
                if selected_character_right == golem:
                    damage = selected_character_right.getDamageTotal()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU() 
                    attacked = True
                    wait_to_hurt = 12
                    hurt_who = "hurt_left"
                    interval = 0

                if selected_character_right == soldier:
                    explosion.changeCordinates(60, 330)
                    explosion.appear_while(22, 110)
                    damage = selected_character_right.getDamageTotal()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU()
                    chargeUpRight()
                    charge_u = 0
                    charge_su = 0

                    attacked = True
                    wait_to_hurt = 110
                    hurt_who = "hurt_left"
                    interval = 0

                    
                turn = "left"
                
                print(damage, ab_damage, hb_damage)
                
          
        elif turn == "right" and (interval > 30 and check_if_attack_finished == True and attacked == False) and num_of_players == 1:  

            if right_ulta_arc == 2.5*math.pi and appended_3 == False:
                attacks_list.append(3)
                appended_3 = True
            elif right_ulta_arc < 2.5*math.pi and appended_3 == True:
                attacks_list.remove(3)
                appended_3 = False
            if right_super_ulta_arc == 2.5*math.pi and appended_4 == False:
                attacks_list.append(4)
                appended_4 = True
            elif right_super_ulta_arc < 2.5*math.pi and appended_4 == True:
                attacks_list.remove(4)
                appended_4 = False
             
            choose_index = random.randint(0, len(attacks_list)-1)
            choose_attack = attacks_list[choose_index]
            
                

            if choose_attack == 1:
                
                selected_character_right.basic_attack(armor_bar_left.width, hb_full_width)
                if selected_character_right == wizard:
                    attacked = True
                    wait_to_hurt = 27
                    hurt_who = "hurt_left"
                
                if selected_character_right == soldier:
                    attacked = True
                    wait_to_hurt = 15
                    hurt_who = "hurt_left"

                if selected_character_right == jonny:
                    jonnys_punch.flip()
                    jonnys_punch.changeCordinates(560, 320)
                    jonnys_punch.rate = 0.17
                    jonnys_punch.speed = -13
                    jonnys_punch.move()
                    check_if_attack_finished = False
                
                if selected_character_right == golem:
                    fireball_1.flip()
                    fireball_1.changeCordinates(620, 330)
                    fireball_1.rate = 0.17
                    fireball_1.speed = -12
                    fireball_1.move()
                    check_if_attack_finished = False


                turn = "left"
                interval = 0
                
                damage = selected_character_right.getDamageTotal()
                hb_damage = selected_character_right.getDamageHB()
                ab_damage = selected_character_right.getDamageAB()
                charge_u = selected_character_right.getChargeU()
                charge_su = selected_character_right.getChargeSU()
                damage_u = selected_character_right.getDamageU()
                damage_su = selected_character_right.getDamageSU()  
                print(damage, ab_damage, hb_damage)
                         
            if choose_attack == 2:

                selected_character_right.unique_attack(armor_bar_left.width, hb_full_width)
                if selected_character_right == wizard:
                    attacked = True
                    wait_to_hurt = 25
                    hurt_who = "hurt_left"

                if selected_character_right == jonny:
                    jonnys_punch.flip()
                    jonnys_punch.changeCordinates(570, 420)
                    jonnys_punch.rate = 0.17
                    jonnys_punch.speed = -13
                    jonnys_punch.move()
                    check_if_attack_finished = False

                if selected_character_right == golem:
                    fireball_2.flip()
                    fireball_2.changeCordinates(580, 320)
                    fireball_2.rate = 0.23
                    fireball_2.speed = -9
                    fireball_2.move()
                    check_if_attack_finished = False

                if selected_character_right == soldier:
                    
                    salvo_soldier = True
                    num_of_salvo_shots = 6
                    wait_to_hurt = 10
                    hurt_who = "hurt_left"


                turn = "left"
                interval = 0
                
                damage = selected_character_right.getDamageTotal()
                hb_damage = selected_character_right.getDamageHB()
                ab_damage = selected_character_right.getDamageAB()
                charge_u = selected_character_right.getChargeU()
                charge_su = selected_character_right.getChargeSU()
                damage_u = selected_character_right.getDamageU()
                damage_su = selected_character_right.getDamageSU()  
                print(damage, ab_damage, hb_damage)            
            
            if choose_attack == 3:

                selected_character_right.ulta(armor_bar_left.width, hb_full_width)
                if selected_character_right == wizard:
                    wizards_arrow.changeCordinates(560, 440)
                    wizards_arrow.flip()
                    wizards_arrow.rate = 0.15
                    wizards_arrow.speed = -12
                    wizards_arrow.move()
                    damage = selected_character_right.getDamageTotal()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    right_ulta_arc += charge_u
                    charge_u = 0
                    check_if_attack_finished = False
                    interval = 0

                    

                if selected_character_right == jonny:
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU() 
                    chargeUpRight()
                    heal_armor = ab_full_width*(0.5+round(random.uniform(-0.1, 0.1), 4))
                    heal_health = hb_full_width*(0.1+round(random.uniform(-0.1, 0.1), 4))
                    armor_bar_right.width += heal_armor
                    health_bar_right.width += heal_health
                    armor_bar_right.x -= heal_armor
                    health_bar_right.x -= heal_health
                    right_ulta_active.visible = False
                    if health_bar_right.width >= hb_full_width:
                        health_bar_right.width = hb_full_width          
                    if armor_bar_right.width >= ab_full_width:
                        armor_bar_right.width = ab_full_width
                        armor_bar_right.x = ab_r_x
                    interval = -50
                    
                if selected_character_right == golem:
                    fireray.flip()
                    fireray.changeCordinates(-144, 362)
                    fireray.appear_while(20, 40)
                    damage = selected_character_right.getDamageTotal()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU()
                    attacked = True
                    wait_to_hurt = 35
                    hurt_who = "hurt_left"
                    skip_turn = True
                    interval = 0

                if selected_character_right == soldier:
                    damage = selected_character_right.getDamageTotal()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU()
                    chargeUpRight()
                    heal_armor = ab_full_width*(0.6+round(random.uniform(-0.15, 0.1), 4))
                    heal_health = hb_full_width*(0.05+round(random.uniform(-0.05, 0.05), 4))
                    armor_bar_right.width += heal_armor
                    health_bar_right.width += heal_health
                    armor_bar_right.x -= heal_armor
                    health_bar_right.x -= heal_health
                    right_ulta_active.visible = False
                    if health_bar_right.width >= hb_full_width:
                        health_bar_right.width = hb_full_width          
                    if armor_bar_right.width >= ab_full_width:
                        armor_bar_right.width = ab_full_width
                        armor_bar_right.x = ab_r_x
                    interval = -100

                if skip_turn == False:
                    turn = "left"
                elif skip_turn == True:
                    turn = "right"
                    skip_turn = False

                attacks_list.remove(3)
                appended_3 = False
                
                
                print(damage, ab_damage, hb_damage)
            
            if choose_attack == 4:

                selected_character_right.super_ulta(armor_bar_left.width, hb_full_width)
                
                if selected_character_right == wizard:
                    wizards_sphere.changeCordinates(495, 387)
                    wizards_sphere.flip()
                    wizards_sphere.rate = 0.06
                    wizards_sphere.speed = -9
                    wizards_sphere.move()
                    armor_bar_right.width -= armor_bar_right.width
                    armor_bar_right.x += armor_bar_right.x
                    damage = selected_character_right.getDamageTotal()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU() 
                    right_super_ulta_arc += charge_su
                    charge_su = 0
                    check_if_attack_finished = False
                    interval = 0

                if selected_character_right == jonny:
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    chargeUpRight()
                    checkArcsLessZeroToRestoreInitial()
                    checkArcsFullToCalibrate()
                    interval = -30
                
                if selected_character_right == golem:
                    damage = selected_character_right.getDamageTotal()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU() 
                    attacked = True
                    wait_to_hurt = 12
                    hurt_who = "hurt_left"
                    interval = 0
                
                if selected_character_right == soldier:
                    explosion.changeCordinates(60, 330)
                    explosion.appear_while(22, 110)
                    damage = selected_character_right.getDamageTotal()
                    hb_damage = selected_character_right.getDamageHB()
                    ab_damage = selected_character_right.getDamageAB()
                    charge_u = selected_character_right.getChargeU()
                    charge_su = selected_character_right.getChargeSU()
                    damage_u = selected_character_right.getDamageU()
                    damage_su = selected_character_right.getDamageSU()
                    chargeUpRight()
                    charge_u = 0
                    charge_su = 0

                    attacked = True
                    wait_to_hurt = 110
                    hurt_who = "hurt_left"
                    interval = 0

                    
                turn = "left"
                
                print(damage, ab_damage, hb_damage)

                attacks_list.remove(4)
                appended_4 = False
                
            
        if turn == "dead" and death_animation_played == False and interval>= 15:
            ko_title.visible = True
            if who_dead == "left_dead":
                selected_character_left.dead()
            elif who_dead == "right_dead":
                selected_character_right.dead()
            death_animation_played = True
            interval = 0
            turn = "end"

        if turn == "end" and interval > 180:
            selected_character_left.kill()
            selected_character_right.kill()
            wizards_arrow.kill()
            wizards_sphere.kill()
            jonnys_punch.kill()
            fireball_1.kill()
            fireball_2.kill()
            fireray.kill()
            explosion.kill()
            ko_title.kill()

            jonny = character.Fighter(0, 120, 1)
            wizard = character.Mage(0, 120, 1.2)
            golem = character.Golem(350, 350, 1)
            soldier = character.Soldier(350, 350, 1)
            wizards_sphere = object.DamagingObject(400, 385, pygame.image.load('assets/sphere.png').convert_alpha(), 1.2, 1.2)
            wizards_arrow = object.DamagingObject(385, 440, pygame.image.load('assets/arrow.png').convert_alpha(), 1.2, 1.2)
            jonnys_punch = object.DamagingObject(385, 440, pygame.image.load('assets/punchwave.png').convert_alpha(), 1.2, 1.2)
            fireball_1 = object.DamagingObject(0, 0, pygame.image.load('assets/fireball_2.png').convert_alpha(), 0.6, 0.6)
            fireball_2 = object.DamagingObject(0, 0, pygame.image.load('assets/fireball_1.png').convert_alpha(), 0.8, 0.8)
            fireray = object.AppearingDamagingObject(0, 0, pygame.image.load('assets/fireray_1.png').convert_alpha(), 1, 1)
            explosion = object.AppearingDamagingObject(0, 0, pygame.image.load('assets/explosion.png').convert_alpha(), 2, 2)
            ko_title = object.Object(350, 125, pygame.image.load('assets/ko_image.png').convert_alpha(), 1, 1)

            frame_lobby_wizard_left.deselect()
            frame_lobby_jonny_left.deselect()
            frame_lobby_jonny_right.deselect()
            frame_lobby_wizard_right.deselect()
            frame_lobby_golem_left.deselect()
            frame_lobby_golem_right.deselect()
            frame_lobby_soldier_left.deselect()
            frame_lobby_soldier_right.deselect()
            random_left.deselect()
            random_right.deselect()
            bg_hell_btn.deselect()
            bg_fountain_btn.deselect()
            bg_street_btn.deselect()
            bg_roof_btn.deselect()
            
            scene = "main_menu"
            cleared = True
            num_of_players = 0
            interval = 0
            selected_character_left = "noone"
            selected_character_right = "noone"
            characters_chosen = False
            left_ulta_arc = math.pi/2
            right_ulta_arc = math.pi/2
            left_super_ulta_arc = math.pi/2
            right_super_ulta_arc = math.pi/2
            turn = "left"
            key_pressed = False
            collision = False
            attacked = False
            setup_lobby = False
            p1_icon.visible = False
            p2_icon.visible = False
            icon_id = "none"
            choose_random_character = 0
            bg_image = bg_street_image
            selected_background = "none"
            code_skip = False
            salvo_soldier = False
            num_of_salvo_shots = 0
            characters_setup = False

            

            death_animation_played = False
            left_super_ulta_active.visible = False
            right_super_ulta_active.visible = False
            ko_title.visible = False
            left_ulta_active.visible = False
            right_ulta_active.visible = False

            attacks_list = [1, 2]
            appended_3 = False
            appended_4 = False
            bot_attacked = False
            check_if_attack_finished = True

            health_bar_left.width = hb_full_width
            armor_bar_left.width = ab_full_width

            health_bar_right.width = hb_full_width
            armor_bar_right.width = ab_full_width
            health_bar_right.x = hb_r_x
            armor_bar_right.x = ab_r_x

            damage = 0
            damage_u = 0
            damage_su = 0
            charge_su = 0
            charge_u = 0
            damage_u = 0
            damage_su = 0


        if health_bar_right.width <= 0 and turn != "dead" and turn != "end":
            turn = "dead"
            who_dead = "right_dead"
            interval = 0

        
        if icon_id == "p1":
            p1_icon.visible = True
            p2_icon.visible = False
        elif icon_id == "p2":
            p1_icon.visible = False
            p2_icon.visible = True
        else:
            p1_icon.visible = False
            p2_icon.visible = False
            

    pygame.display.update()
    clock.tick(60)

pygame.quit()
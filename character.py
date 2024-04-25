import pygame
import time
import random
import math

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.deal_damage = 0
        self.hb_damage = 0
        self.ab_damage = 0
        self.charge_u = 0
        self.charge_su = 0
        self.damage_u = 0
        self.damage_su = 0
        self.sprites = []
        self.flipped = False
        self.death = False


    def flip(self):
        self.flipped = True
   
    def changeCordinates(self, pos_x, pos_y):
        self.rect.center = [pos_x, pos_y]
        
        
        
    def getDamageHB(self):
        return self.hb_damage
    
    def getDamageAB(self):
        return self.ab_damage
    
    def getDamageTotal(self):
        return self.deal_damage
    
    def resetDamage(self):
        self.deal_damage = 0
    
    def getChargeU(self):
        return self.charge_u 
    
    def getChargeSU(self):
        return self.charge_su 
    
    def getDamageU(self):
        return self.damage_u
    
    def getDamageSU(self):
        return self.damage_su
    

class Fighter(Character):
    def __init__(self, pos_x, pos_y, scale):
        super().__init__()
        self.rate = 0.035
        self.scale= scale
        #mask_image = pygame.image.load('assets/fighter_1_stand.png').convert_alpha()
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/fighter_1_stand.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/fighter_2_stand.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        
        #self.mask = pygame.mask.from_surface(mask_image)
        self.extra_damage = 1
        
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        
    

    
    #kick
    def basic_attack(self, ab, full_hb):
        #time.sleep(1)
        self.sprites =[]
        self.sprites.append(pygame.image.load('assets/fighter_kick_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_kick_2.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_kick_1.png').convert_alpha())
        
        self.rate = 0.05
        self.current_image = 0

        self.damage_u = 0
        self.damage_su = 0

        self.deal_damage = round(self.extra_damage*(full_hb*0.1 + random.randint(-int(full_hb*0.03),int(full_hb*0.03))))
        self.ab_damage = round(self.deal_damage*0.7 + random.randint(-int(self.deal_damage*0.1),int(self.deal_damage*0.1)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = (2*math.pi)*(0.3 + round(random.uniform(-0.1, 0.1), 4))
        self.charge_su = (2*math.pi)*(0.25 + round(random.uniform(-0.05, 0.05), 4))
        

    #double kick
    def double_kick(self, ab, full_hb):
        #time.sleep(1)
        self.sprites =[]
        self.sprites.append(pygame.image.load('assets/fighter_kick_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_kick_2.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_kick_1.png').convert_alpha())        
        self.sprites.append(pygame.image.load('assets/fighter_kick_3.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_kick_4.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_kick_5.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_kick_1.png').convert_alpha())
        
        self.rate = 0.096
        self.current_image = 0


        

    #uppercut
    def unique_attack(self, ab, full_hb):
        #time.sleep(1)
        self.sprites =[]
        self.sprites.append(pygame.image.load('assets/fighter_uppercut_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_uppercut_2.png').convert_alpha())      
        self.sprites.append(pygame.image.load('assets/fighter_uppercut_3.png').convert_alpha())  
        self.sprites.append(pygame.image.load('assets/fighter_uppercut_3.png').convert_alpha())     
        self.sprites.append(pygame.image.load('assets/fighter_uppercut_2.png').convert_alpha())
        
        self.rate = 0.1
        self.current_image = 0


        self.damage_u = 0
        self.damage_su = 0

        self.deal_damage = round(self.extra_damage*(full_hb*0.18 + random.randint(-int(full_hb*0.05),int(full_hb*0.05))))
        self.ab_damage = round(self.deal_damage*0.35 + random.randint(-int(self.deal_damage*0.05),int(self.deal_damage*0.05)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = (2*math.pi)*(0.18 + round(random.uniform(-0.07, 0.07), 4))
        self.charge_su = (2*math.pi)*(0.1 + round(random.uniform(-0.05, 0.05), 4))


    def hurt(self):
        #time.sleep(1)
        self.sprites =[]
    
        
        self.sprites.append(pygame.image.load('assets/fighter_hurt_1_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_hurt_2_1.png').convert_alpha())
        
        
        self.rate = 0.12
        self.current_image = 0

    def dead(self):
        #time.sleep(1)
        self.sprites =[]
        self.sprites.append(pygame.image.load('assets/fighter_dead_1_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_dead_2_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_dead_3.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_dead_3.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_dead_3.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_dead_3.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/fighter_dead_3.png').convert_alpha())
        
        
        self.rate = 0.12
        self.current_image = 0

        self.death = True
        

    #hypercharge
    def super_ulta(self, ab, full_hb):
        self.sprites =[]
        self.sprites.append(pygame.image.load('assets/fighter_charge.png').convert_alpha())
        
        
        self.rate = 0.015
        self.current_image = 0
        self.damage_u = 0
        self.damage_su = 0
        self.deal_damage =0
        self.hb_damage = 0
        self.ab_damage = 0
        self.charge_u = (2*math.pi)*(0.01 + round(random.uniform(-0.05, 0.05), 4))
        self.charge_su = -(2*math.pi)

        self.extra_damage += 0.6
        

    #shield
    def ulta(self, ab, full_hb):
        
        self.sprites =[]
        self.sprites.append(pygame.image.load('assets/fighter_shield_1.png').convert_alpha())
        
        
        self.rate = 0.015
        self.current_image = 0

        self.deal_damage = 0
        self.ab_damage = 0
        self.hb_damage = 0
        self.damage_u = 0
        self.damage_su = 0


        self.charge_u = -(2*math.pi)
        self.charge_su = (2*math.pi)*(0.05 + round(random.uniform(-0.1, 0.1), 4))
        

    def update(self):
         
        self.current_image += self.rate

        if self.death == False:
            if self.current_image >= len(self.sprites):
                self.sprites =[]
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/fighter_1_stand.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/fighter_2_stand.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.current_image = 0
                self.rate = 0.035
                #self.rect.topleft = [self.position_x, self.position_y]
        
        elif self.death == True:
            if self.current_image >= len(self.sprites)-1:
                self.rate = 0

        if self.flipped == False:
            self.image = self.sprites[int(self.current_image)]
        elif self.flipped == True:
            self.image = pygame.transform.flip(self.sprites[int(self.current_image)], True, False)
        
        
        
class Golem(Character):
    def __init__(self, pos_x, pos_y, scale):
        super().__init__()
        self.rate = 0.13
        self.scale= scale
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 0
        self.acceleration = 0
        self.speed_activate = False
        
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_5.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))

        
        
        
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        
    def super_ulta(self, ab, full_hb):

        self.sprites =[]
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_5.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_5.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_7.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_8.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_9.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_9.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_9.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_9.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_sprint_9.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        

        self.rate = 0.2
        self.current_image = 0
        
        self.acceleration = 1.8
        self.speed = 1



        self.damage_u = ((5/2)*math.pi)*(0.4 + round(random.uniform(-0.05, 0.05), 4))
        self.damage_su = 0

        self.deal_damage = round((full_hb*0.35 + random.randint(-int(full_hb*0.1),int(full_hb*0.1))))
        self.ab_damage = round(self.deal_damage*0.5 + random.randint(-int(self.deal_damage*0.1),int(self.deal_damage*0.1)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = (2*math.pi)*(0.1 + round(random.uniform(-0.1, 0.1), 4))
        self.charge_su = -(2*math.pi)
            
    def basic_attack(self, ab, full_hb):
        self.sprites =[]
        self.sprites.append(pygame.image.load('assets/golem_fire_punch_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fire_punch_2.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fire_punch_3.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fire_punch_4.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fire_punch_5.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fire_punch_4.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fire_punch_1.png').convert_alpha())
        
        self.rate = 0.1
        self.current_image = 0

        self.damage_u = 0
        self.damage_su = 0

        self.deal_damage = round((full_hb*0.1 + random.randint(-int(full_hb*0.05),int(full_hb*0.05))))
        self.ab_damage = round(self.deal_damage*0.75 + random.randint(-int(self.deal_damage*0.1),int(self.deal_damage*0.1)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = (2*math.pi)*(0.3 + round(random.uniform(-0.1, 0.1), 4))
        self.charge_su = (2*math.pi)*(0.2 + round(random.uniform(-0.05, 0.05), 4))
    
    def unique_attack(self, ab, full_hb):
        self.sprites =[]
        self.sprites.append(pygame.image.load('assets/golem_fireball_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fireball_2.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fireball_3.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fireball_4.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fireball_1.png').convert_alpha())
        
        self.rate = 0.085
        self.current_image = 0

        self.damage_u = 0
        self.damage_su = 0

        self.deal_damage = round((full_hb*0.18 + random.randint(-int(full_hb*0.07),int(full_hb*0.07))))
        self.ab_damage = round(self.deal_damage*0.65 + random.randint(-int(self.deal_damage*0.15),int(self.deal_damage*0.15)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = (2*math.pi)*(0.15 + round(random.uniform(-0.05, 0.05), 4))
        self.charge_su = (2*math.pi)*(0.1 + round(random.uniform(-0.01, 0.01), 4))

    def ulta(self, ab, full_hb):
        self.sprites =[]
        self.sprites.append(pygame.image.load('assets/golem_fireray_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fireray_2.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fireray_3.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fireray_4.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fireray_5.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fireray_6.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fireray_7.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_fireray_2.png').convert_alpha())
        
        self.rate = 0.12
        self.current_image = 0


        self.damage_u = 0
        self.damage_su = 0

        self.deal_damage = round((full_hb*0.05 + random.randint(-int(full_hb*0.05),int(full_hb*0.05))))
        self.ab_damage = round(self.deal_damage*0.75 + random.randint(-int(self.deal_damage*0.1),int(self.deal_damage*0.1)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = -(2*math.pi)
        self.charge_su = (2*math.pi)*(0.02 + round(random.uniform(-0.01, 0.01), 4))

    def hurt(self):
        self.sprites =[]
        self.sprites.append(pygame.image.load('assets/golem_hurt_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_hurt_2.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_hurt_3.png').convert_alpha())
        #self.sprites.append(pygame.image.load('assets/golem_hurt_4.png').convert_alpha())
       
        
        self.rate = 0.18
        self.current_image = 0

    def dead(self):
        self.sprites =[]
        self.sprites.append(pygame.image.load('assets/golem_dead_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_dead_2.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_dead_3.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_dead_4.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_dead_5.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_dead_6.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/golem_dead_7.png').convert_alpha())
        
        self.rate = 0.12
        self.current_image = 0

        self.death = True
    
    def changeCordinates(self, pos_x, pos_y):
        self.rect.center = [pos_x, pos_y]
        self.pos_x = pos_x
        self.pos_y = pos_y


    def update(self):
        self.current_image += self.rate
        
        if self.flipped == False:
            if self.rect.x >= 1100:
                self.rect.x = -200

            self.speed = self.speed*self.acceleration
            self.rect.x += self.speed

            if self.speed > 45:
                self.acceleration = 0.95
            if self.speed < 0.0005:
                self.acceleration = 0
                self.speed = 0

        elif self.flipped == True:
            if self.rect.x <= -200:
                self.rect.x = 1300

            self.speed = self.speed*self.acceleration
            self.rect.x += -self.speed

            if self.speed > 55:
                self.acceleration = 0.957
            if self.speed < 0.0005:
                self.acceleration = 0
                self.speed = 0
        
        if self.death == False:
            if self.current_image >= len(self.sprites):
            
                self.sprites =[]

                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_5.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/golem_idle_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                
                self.speed = 0
                self.acceleration =0
                self.rect.center = [self.pos_x, self.pos_y]
                self.current_image = 0
                self.rate = 0.13
            #self.rect.topleft = [self.position_x, self.position_y]
        
        elif self.death == True:
            if self.current_image >= len(self.sprites)-1:
                self.rate = 0
        
        
        if self.flipped == False:
            self.image = self.sprites[int(self.current_image)]
        elif self.flipped == True:
            self.image = pygame.transform.flip(self.sprites[int(self.current_image)], True, False)


class Mage(Character):
    def __init__(self, pos_x, pos_y, scale):
        super().__init__()
        self.scale = scale
        self.rate = 0.13
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_7.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_8.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        
    
        


    #impulse
    def unique_attack(self, ab, full_hb):
        
        self.sprites =[]
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_impulse_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_impulse_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_impulse_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_impulse_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_impulse_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_impulse_7.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        
        self.rate = 0.12
        self.current_image = 0


        self.damage_u = 0
        self.damage_su = 0

        self.deal_damage = round(full_hb*0.17 + random.randint(-int(full_hb*0.08),int(full_hb*0.08)))
        self.ab_damage = round(self.deal_damage*0.7 + random.randint(-int(self.deal_damage*0.05),int(self.deal_damage*0.05)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = (2*math.pi)*(0.4 + round(random.uniform(-0.01, 0.01), 4))
        self.charge_su = (2*math.pi)*(0.1 + round(random.uniform(-0.1, 0.1), 4))

    #zap
    def basic_attack(self, ab, full_hb):
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_5.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_7.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_8.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_8.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_zap_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))

        self.rate = 0.2
        self.current_image = 0

        self.deal_damage = round(full_hb*0.15 + random.randint(-int(full_hb*0.05),int(full_hb*0.05)))
        self.ab_damage = round(self.deal_damage*0.4 + random.randint(-int(self.deal_damage*0.1),int(self.deal_damage*0.1)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = (2*math.pi)*(0.2 + round(random.uniform(-0.15, 0.15), 4))
        self.charge_su = (2*math.pi)*(0.15 + round(random.uniform(-0.1, 0.1), 4))

        self.damage_u = 0
        self.damage_su = 0


    #shpere
    def super_ulta(self, ab, full_hb):
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_sphere_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_sphere_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_sphere_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_sphere_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_sphere_5.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_sphere_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_sphere_7.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_sphere_8.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        
        self.rate = 0.09
        self.current_image = 0  


        self.damage_u = 0
        self.damage_su = 0

        self.deal_damage = round(full_hb*0.45 + random.randint(-int(full_hb*0.02),int(full_hb*0.02)))
        self.ab_damage = round(self.deal_damage*0.1 + random.randint(-int(self.deal_damage*0.05),int(self.deal_damage*0.05)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = (2*math.pi)*(0.015 + round(random.uniform(-0.01, 0.01), 4))
        self.charge_su = -(2*math.pi)
        

    #arrow
    def ulta(self, ab, full_hb):
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_arrow_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_arrow_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_arrow_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_arrow_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_arrow_5.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_arrow_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_arrow_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_arrow_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_arrow_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        
        self.rate = 0.14
        self.current_image = 0

        self.deal_damage = round(full_hb*0.05 + random.randint(-int(full_hb*0.02),int(full_hb*0.02)))
        self.ab_damage = round(self.deal_damage*0.75 + random.uniform(-int(self.deal_damage*0.1),int(self.deal_damage*0.1)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = -(2*math.pi)
        self.charge_su = (2*math.pi)*(0.15 + round(random.uniform(-0.05, 0.05), 4))

        self.damage_u = ((5/2)*math.pi)*(0.7 + round(random.uniform(-0.05, 0.05), 4))
        self.damage_su = ((5/2)*math.pi)*(0.2 + round(random.uniform(-0.05, 0.05), 4))

        


    def hurt(self):
        self.sprites =[]
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_hurt_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_hurt_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))

        
        
        self.rate = 0.16
        self.current_image = 0

    def dead(self):
        #time.sleep(1)
        self.sprites =[]
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_dead_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_dead_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_dead_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_dead_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        
        self.death = True
        self.rate = 0.12
        self.current_image = 0
    

    def update(self):
         
        self.current_image += self.rate
        
        if self.death == False:
            if self.current_image >= len(self.sprites):
            
                self.sprites =[]

                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_7.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/mage_idle_8.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))

           
                self.current_image = 0
                self.rate = 0.13
            #self.rect.topleft = [self.position_x, self.position_y]
        
        elif self.death == True:
            if self.current_image >= len(self.sprites)-1:
                self.rate = 0
        
        
        if self.flipped == False:
            self.image = self.sprites[int(self.current_image)]
        elif self.flipped == True:
            self.image = pygame.transform.flip(self.sprites[int(self.current_image)], True, False)


class Soldier(Character):
    def __init__(self, pos_x, pos_y, scale):
        super().__init__()
        self.scale = scale
        self.rate = 0.13
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_7.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        
    
        


    #salvo
    def unique_attack(self, ab, full_hb):
        
        self.sprites =[]
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_salvo_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_salvo_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_salvo_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_salvo_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_salvo_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_salvo_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_salvo_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_salvo_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_salvo_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_salvo_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        

        self.rate = 0.12
        self.current_image = 0

        self.damage_u = 0
        self.damage_su = 0

        self.deal_damage = round(full_hb*0.025 + random.randint(-int(full_hb*0.005),int(full_hb*0.005)))
        self.ab_damage = round(self.deal_damage*0.6 + random.randint(-int(self.deal_damage*0.05),int(self.deal_damage*0.05)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = (2*math.pi)*(0.03 + round(random.uniform(-0.01, 0.01), 4))
        self.charge_su = (2*math.pi)*(0.02 + round(random.uniform(-0.01, 0.01), 4))


        
    #shot
    def basic_attack(self, ab, full_hb):
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_shot_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_shot_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_shot_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_shot_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        

        self.rate = 0.11
        self.current_image = 0

        self.damage_u = 0
        self.damage_su = 0

        self.deal_damage = round(full_hb*0.12 + random.randint(-int(full_hb*0.08),int(full_hb*0.08)))
        self.ab_damage = round(self.deal_damage*0.5 + random.randint(-int(self.deal_damage*0.05),int(self.deal_damage*0.05)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = (2*math.pi)*(0.3 + round(random.uniform(-0.01, 0.01), 4))
        self.charge_su = (2*math.pi)*(0.2 + round(random.uniform(-0.1, 0.1), 4))

       


    #grenade
    def super_ulta(self, ab, full_hb):
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_grenade_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_grenade_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_grenade_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_grenade_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_grenade_5.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_grenade_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_grenade_7.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_grenade_8.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_grenade_8.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_grenade_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        

        self.rate = 0.09
        self.current_image = 0  

        self.damage_u = 0
        self.damage_su = (2*math.pi)*(0.25 + round(random.uniform(-0.05, 0.1), 4))

        self.deal_damage = round(full_hb*0.3 + random.randint(-int(full_hb*0.02),int(full_hb*0.04)))
        self.ab_damage = round(self.deal_damage*0.7 + random.randint(-int(self.deal_damage*0.05),int(self.deal_damage*0.05)))
        if ab >= self.ab_damage:
            self.hb_damage = round(self.deal_damage - self.ab_damage)
        elif ab < self.ab_damage:
            self.ab_damage = round(ab)
            self.hb_damage = round(self.deal_damage - self.ab_damage)

        self.charge_u = (2*math.pi)*(0.15 + round(random.uniform(-0.05, 0.05), 4))
        self.charge_su = -(2*math.pi)

       
        

    #reload
    def ulta(self, ab, full_hb):
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_5.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_7.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_8.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_5.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_reload_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        
        self.rate = 0.13
        self.current_image = 0



        self.damage_u = 0
        self.damage_su = 0

        self.deal_damage = 0
        self.ab_damage = 0
        self.hb_damage = 0

        self.charge_u = -(2*math.pi)
        self.charge_su = (2*math.pi)*(0.8 + round(random.uniform(-0.05, 0.05), 4))

        

        


    def hurt(self):
        self.sprites =[]
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_hurt_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_hurt_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_hurt_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))

        
        
        self.rate = 0.16
        self.current_image = 0

    def dead(self):
        #time.sleep(1)
        self.sprites =[]
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_dead_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_dead_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_dead_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_dead_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        
        self.death = True
        self.rate = 0.1
        self.current_image = 0
    

    def update(self):
         
        self.current_image += self.rate
        
        if self.death == False:
            if self.current_image >= len(self.sprites):
            
                self.sprites =[]

                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_1.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_2.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_3.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_4.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_6.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
                self.sprites.append(pygame.transform.scale(pygame.image.load('assets/soldier_idle_7.png').convert_alpha(), (int(self.scale*400), int(self.scale*400))))
        
           
                self.current_image = 0
                self.rate = 0.13
            
        
        elif self.death == True:
            if self.current_image >= len(self.sprites)-1:
                self.rate = 0
        
        
        if self.flipped == False:
            self.image = self.sprites[int(self.current_image)]
        elif self.flipped == True:
            self.image = pygame.transform.flip(self.sprites[int(self.current_image)], True, False)
                
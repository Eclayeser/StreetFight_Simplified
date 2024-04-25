import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image, scale_x, scale_y):
        super().__init__()
        self.invisible_img = pygame.image.load('assets/empty.png').convert_alpha()
        self.visible = True
        self.width = image.get_width()
        self.height= image.get_height()
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.sprite_img = image
        self.flipped = False
        
        self.work_image = pygame.transform.scale(self.sprite_img, (int(self.width*scale_x), int(self.height*scale_y)))
        self.image = self.work_image
        
        
        self.mask = pygame.mask.from_surface(self.work_image)
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

       
    def flip(self):
        self.flipped = True
        #self.image = pygame.transform.flip(self.work_image, True, False)

    def changeCordinates(self, pos_x, pos_y):
        self.rect.topleft = [pos_x, pos_y]

    def scaleIt(self, width, height):
        self.work_image = pygame.transform.scale(self.work_image, (width, height))
    
  
    

    def update(self):
        if self.flipped == True and self.visible == True:
            self.image = pygame.transform.flip(self.work_image, True, False)
        elif self.flipped == False and self.visible == True: 
            self.image =  self.work_image
        elif (self.flipped == False and self.visible == False) or (self.flipped == True and self.visible == False):
            self.image = self.invisible_img
    
    


class DamagingObject(Object):
    def __init__(self, pos_x, pos_y, image, scale_x, scale_y):
        super().__init__(pos_x, pos_y, image, scale_x, scale_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.wait_before_action = 0
        self.wait = 0
        self.visible = False
        self.rate=0
        self.speed = 0
        self.collided = False
        
        

    def move(self):

        self.wait_before_action = self.rate

    
    
        

    def update(self, check_col):
        super().update()

        
        self.wait += self.wait_before_action

        if self.wait >= 5:
            self.visible = True
            self.rect.x = self.rect.x + self.speed

        if self.rect.x >= 1200 or self.rect.x <= -100 or check_col == True:
            self.visible = False
            self.image = self.invisible_img
            self.speed = 0
            self.wait_before_action = 0
            self.wait = 0
            self.rate = 0
            self.collided = False
            self.rect.topleft = [self.pos_x, self.pos_y]
       
class AppearingDamagingObject(DamagingObject):
    def __init__(self, pos_x, pos_y, image, scale_x, scale_y):
        super().__init__(pos_x, pos_y, image, scale_x, scale_y)
        self.wait_before_appear = 0
        self.duration = 0
        self.perform = False

    def appear_while(self, duration, when_start):
        self.wait_before_appear = when_start
        self.duration = duration
        self.perform = True

    def update(self):
        if self.perform == True:
            if self.wait_before_appear <= 0:
                self.wait_before_appear = 0 
                if self.duration > 0:
                    self.visible = True
                    self.duration -= 1
                else:
                    self.perform = False
                    self.duration = 0
            else:
                self.wait_before_appear -= 1    
            
        else:
            self.visible = False
        
        if self.flipped == True and self.visible == True:
            self.image = pygame.transform.flip(self.work_image, True, False)
        elif self.flipped == False and self.visible == True: 
            self.image =  self.work_image
        elif (self.flipped == False and self.visible == False) or (self.flipped == True and self.visible == False):
            self.image = self.invisible_img
from typing import Any
import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, image, image_highlight, pos_x, pos_y, scale):
        super().__init__()
        width = image.get_width()
        height= image.get_height()
        
        

        self.image_normal = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        
        self.image_highlight = pygame.transform.scale(image_highlight, (int(width*scale), int(height*scale)))
        
        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.clicked = False
        self.new_image = False
        self.selected = False
        self.already_pressed = False
        
        
        

    def check_clicked(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.new_image = True
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == False:
                self.clicked = False
                self.already_pressed = False
        if self.rect.collidepoint(pos) == False:
            self.new_image = False

        return action
    
    def select_deselect(self):

        if self.selected == False and self.already_pressed == False:
            self.selected = True
            self.already_pressed = True
        if self.selected == True and self.already_pressed == False:
            self.selected = False
            self.already_pressed = True

    def deselect(self):
        self.selected = False
        self.already_pressed = True
    def getSelected(self):
        return self.selected
    
    def changeCordinates(self, pos_x, pos_y):
        self.rect.topleft = [pos_x, pos_y]
    
    def scaling(self, scale):
        self.image_normal = pygame.transform.scale(self.image_normal, (400*scale, 400*scale))

    def flip(self):
        self.image_normal = pygame.transform.flip(self.image_normal, True, False)
        

    def update(self):
         if self.new_image == True or self.selected == True:
            self.image = self.image_highlight
         if self.new_image == False and self.selected == False:
            self.image = self.image_normal



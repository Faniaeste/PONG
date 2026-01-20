import pygame as pg

class Raqueta:
    def __init__(self, posx, posy, color = (255, 255, 255), w = 20, h = 120):
        self.pos_x = posx
        self.pos_y = posy
        self.color = color
        self.h = h
        self.w = w


    def dibujar(self, screen):
        pg.draw.rect( screen, self.color, (self.pos_x - (self.w),(self.pos_y - self.h // 2), self.w, self.h) )

#
class Pelota:
    def __init__(self,posx,posy,color = (255, 255, 255), radio = 20):
        self.pos_x = posx
        self.pos_y = posy
        self.color = color
        self.radio = radio
        
        
    def dibujar(self,screen):
        pg.draw.circle(screen, self.color,(self.pos_x,self.pos_y), self.radio)
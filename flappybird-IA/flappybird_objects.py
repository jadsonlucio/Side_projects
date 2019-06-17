import pygame
from pygame_api.pygame_objects import pygame_actor,pyrect

class Pybird(pygame_actor):

    def set_bird_paint(self):
        rect=pygame.Surface((100,100))
        pygame.draw.rect(rect,(255,40,0),pyrect(0,0,100,100),0)
        self.paint(rect,(0,0,100,100))

    def __init__(self,x_pos,y_pos,width,height):
        pygame_actor.__init__(self,x_pos,y_pos,width,height)
        self.set_bird_paint()

    def update(self):
        self.y_pos=self.y_pos+30
        self.set_pos(self.x_pos,self.y_pos)
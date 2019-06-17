import pygame
from pygame_api.physical.physical import world,particle

class Pygame_world(world):
    def __init__(self,size,gravity,particles):
        world.__init__(self,size,gravity,particles)

    def draw(self):
        pass


class Pygame_particle(particle):
    def __init__(self,x_pos,y_pos,width,height,weight,angle,elasticity):
        particle.__init__(self,x_pos,y_pos,weight,angle,elasticity)
        self.surface=pygame.Surface((width,height))


    def paint(self,surface,rect):
        self.surface.blit(surface,rect)

    def draw(self,surface):
        surface.blit(self.surface,self.pyrect)

class pygame_actor():
    def set_pos(self,x_pos,y_pos):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.pyrect=pyrect(x_pos,y_pos,self.width,self.height)

    def set_size(self,width,height,scale=True):
        self.width=width
        self.height=height
        self.pyrect(self.x_pos,self.y_pos,width,height)

        if(scale):
            self.surface=pygame.transform.scale(self.surface,(width,height))


    def __init__(self,x_pos,y_pos,width,height):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.width=width
        self.height=height

        self.surface=pygame.Surface((self.width,self.height))
        self.pyrect=pyrect(self.x_pos,self.y_pos,self.width,self.height)

    def update(self):
        pass



class pyimage():
    def __init__(self,url_image):
        self.surface=pygame.image.load(url_image)
        self.surface_rect=self.surface.get_rect()

    def resize(self,width,height):
        self.surface=pygame.transform.scale(self.surface,(width,height))
        self.surface_rect=self.surface.get_rect()

def pyrect(x_pos,y_pos,width,height):
    """
    Cria um objeto pygame do tipo retagulo

    Parameters
    ----------
    x_pos: int
         posição x do retangulo
    y_pos: int
         posição y do retangulo
    width: int
         largura do retangulo
    height: int
         altura do retengulo

    Returns
    -------
    pyrect: objeto pygame do tipo retangulo

    """

    return pygame.Rect(x_pos,y_pos,width,height)

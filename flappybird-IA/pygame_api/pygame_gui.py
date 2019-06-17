import pygame
from pygame_api import pygame_objects
from pygame_api.physical.physical import world


class Pygame_gui():
    # eventos janela
    def close_event(self, event):
        pass

    def mouse_motion(self, event):
        pass

    def mouse_press(self, event):
        pass

    def mouse_release(self, event):
        pass

    def key_press(self, event):
        pass

    def key_release(self, event):
        pass

    # Pega os eventos que estão ocorrendo na janela e chamas os seus respectivos metodos
    def set_events(self):
        dict_events = {
            12: self.close_event,

            4: self.mouse_motion,
            5: self.mouse_press,
            6: self.mouse_release,
        }

        events = self.get_events()

        for event in events:
            for key in dict_events.keys():
                if (event.type == key):
                    dict_events[key](event)
                    break

    def set_screen_size(self, size=None):
        """
        Define o tamanho da tela

        Parameters
        ----------
        size: tuple
            Tamanho da tela

        Returns
        -------
        Display pygame object

        """

        if(size!=None):
            self.screen_size = size
        self.surface = pygame.display.set_mode(tuple(self.screen_size))

    # pega todos os eventos de interação do usuario com a janela
    def get_events(self):
        return pygame.event.get()

    def __init__(self,title,world=world((1000,500),10),width=1280,FPS=120):
        """
        Inicia a janela do jogo.

        Parameters
        ----------
        screen_dimention : tuple
            tamanho da janela do jogo
            default=1280x678

        Returns
        -------
        None

        """


        pygame.init()
        self.surface=None
        self.pygame_actors=[]

        self.title = title
        self.world = world
        self.real_size = self.world.size
        self.screen_size = [width, int(width / (self.real_size[0] / self.real_size[1]))]
        self.real_size = self.world.size
        self.pixel_to_real_size = self.real_size[0] / self.screen_size[0]
        self.real_to_pixel_size = self.screen_size[0] / self.real_size[0]
        self.FPS = FPS
        self.set_screen_size()

        self.pygame_backgroud=Pygame_background(self.screen_size,"midia//imagens//background.png")

    # atualiza a tela
    def update_screen(self):
        pygame.display.flip()

    def update_actors(self):
        for pygame_actor in self.pygame_actors:
            pygame_actor.update()

    def draw(self):
        self.pygame_backgroud.draw(self.surface)
        for pygame_actor in self.pygame_actors:
            pygame_actor.draw(self.surface)


class Pygame_background():
    def __init__(self,screen_dimention,url_image):
        self.background= pygame_objects.pyimage(url_image)
        self.background.resize(screen_dimention[0],screen_dimention[1])

    def draw(self,surface):
        surface.blit(self.background.surface,self.background.surface_rect)


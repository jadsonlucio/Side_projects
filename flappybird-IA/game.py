from pygame_api.pygame_gui import Pygame_gui
from flappybird_objects import Pybird

class flappybird_game(Pygame_gui):
    def close_event(self, event):
        self.gaming_running=False

    def __init__(self):
        Pygame_gui.__init__(self,"flappy_IA")
        self.gaming_running=False
        self.pygame_actors.append(Pybird(100,0,100,100))

    def main_loop(self):
        while(self.gaming_running):
            self.set_events()
            self.draw()
            self.update_screen()
            self.update_actors()


    def run(self):
        self.gaming_running=True
        self.main_loop()


game=flappybird_game()
game.run()
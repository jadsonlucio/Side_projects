from GUI import Pygame_gui
from players import IA_player,human_player



class game(Pygame_gui):
    # eventos jogo
    def close_event(self,event):
        self.game_running=False

    def mouse_press(self,event):
        pos=self.pygame_board.get_pos(event.pos)
        house=self.pygame_board.get_house(pos)

        if(not house.is_empty()):
            self.pygame_board.set_play(house.piece,house)

    def mouse_release(self,event):
        pass


    def create_event_list(self,func_ativacao,funcao_disparo):
        self.events_list[func_ativacao]=funcao_disparo

    def __init__(self,players):
        """
        Inicia um novo jogo.

        Parameters
        ----------
        players_list: list or tuple
             lista 2d das peças do tabuleiro. Ver mais em constantes.py
             default: matriz default in get_default_tab of board_size
             
        Returns
        -------
        None

        """

        Pygame_gui.__init__(self)
        self.player_list=player_control(self,players)
        self.events_list={}
        self.game_running=False

    #loop principal de eventos do jogo
    def mainlopp(self):
        while(self.game_running):
            self.set_events()
            self.pygame_board.draw()
            self.update_screen()

    #inicia a janela do jogo
    def run(self):
        self.game_running=True
        self.mainlopp()

    #para o loop principal fechando o jogo
    def close_game(self):
        self.game_running=False

class player_control():
    def get_current_player(self):
        return self.players[self.index_current_player%len(self.players)]

    def set_current_player(self):
        player=self.get_current_player()
        if(player.complet_move==True):
            player.complet_move=False
            self.index_current_player=self.index_current_player+1
            if(self.index_current_player>len(self.players)-1):
                self.index_current_player=0

    def __init__(self,game,players):
        self.game=game
        self.players=players
        self.index_current_player=0


if __name__=="__main__":
    players=(human_player(0),human_player(1))
    app=game(players)
    app.run()
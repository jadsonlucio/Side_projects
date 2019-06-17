import pygame
from board import board,house,piece
from constantes import HOUSES_COLORS,PIECES_COLORS
from numpy_functions import operation_vectors,float_to_int



def get_default_tab(size):
    """
    Inicia um tabuleiro padrão.

    Parameters
    ----------
    size: tuple or list

    Returns
    -------
    list of default board pieces

    """
    matriz_board = []
    for cont_col in range(0, size[0]):
        column = []
        for cont_line in range(0, size[1]):
            if ((cont_col + cont_line) % 2 == 0):
                if (cont_line < 3):
                    house = Pygame_house(3, (cont_col, cont_line))
                    piece=Pygame_piece(1, 1, (cont_col, cont_line),house)
                    house.piece=piece

                    column.append(house)
                elif (cont_line > size[0] - 4):
                    house = Pygame_house(3, (cont_col, cont_line))
                    piece = Pygame_piece(0, 1, (cont_col, cont_line),house)
                    house.piece=piece

                    column.append(house)
                else:
                    house = Pygame_house(3, (cont_col, cont_line))
                    column.append(house)
            else:
                house = Pygame_house(4, (cont_col, cont_line))
                column.append(house)

        matriz_board.append(column)

    return matriz_board

class Pygame_gui():
    #eventos janela
    def close_event(self,event):
        pass

    def mouse_motion(self,event):
        pass

    def mouse_press(self,event):
        pass

    def mouse_release(self,event):
        pass

    def key_press(self,event):
        pass

    def key_release(self,event):
        pass


    #Pega os eventos que estão ocorrendo na janela e chamas os seus respectivos metodos
    def set_events(self):
        dict_events={
            12:self.close_event,

            4:self.mouse_motion,
            5:self.mouse_press,
            6:self.mouse_release,
        }

        events=self.get_events()

        for event in events:
            for key in dict_events.keys():
                if(event.type==key):
                    dict_events[key](event)
                    break


    def set_screen_size(self,dimention):
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
        self.board_dimention=dimention
        self.surface=pygame.display.set_mode(tuple(self.board_dimention))
        self.pygame_board.surface=self.surface

    #pega todos os eventos de interação do usuario com a janela
    def get_events(self):
        return pygame.event.get()


    def __init__(self,board_dimention=(600,570),board_size=(8,8)):
        """
        Inicia a janela do jogo.

        Parameters
        ----------
        board_dimention : tuple
            tamanho da janela do jogo 
            default=650x570
        board_size : tuple
            tamanho do tabuleiro do jogo 
            default=8x8
        colors_config : dict
            Cores das peças e das casas do tabuleiro. Ver mais em constantes.py
            default=DEFAULT_COLORS_CONFIG
        
        Returns
        -------
        None
        
        """

        pygame.init()
        self.surface=None
        self.board_size = board_size
        self.board_dimention=board_dimention
        self.pygame_board=Pygame_board(board_dimention,board_size,self.surface)

        self.set_screen_size(board_dimention)

#eventos jogo

    #atualiza a tela
    def update_screen(self):
        pygame.display.flip()

class Pygame_board(board):

    def get_house_size(self):
        width=self.board_dimention[0]/self.board_size[0]
        height=self.board_dimention[1]/self.board_size[1]
        return width,height

    def get_pos(self,pos_screen):
        house_size=self.get_house_size()
        pos_lin=int(pos_screen[1]/house_size[1])
        pos_col = int(pos_screen[0] / house_size[0])

        return pos_col,pos_lin

    def __init__(self,board_dimention,board_size,surface):
        board.__init__(self,board_size)
        self.surface = surface
        self.board_dimention=board_dimention
        self.matriz_houses=get_default_tab(board_size)

    def draw(self):
        houses=self.get_house_list()
        pieces=self.get_pieces_list()
        house_size=self.get_house_size()
        for Pygame_house in houses:
            Pygame_house.draw(self.surface,house_size)
        for Pygame_piece in pieces:
            Pygame_piece.draw(self.surface,house_size)

class Pygame_house(house):

    def __init__(self, type, pos,piece=None,houses_colors=HOUSES_COLORS):
        house.__init__(self,type,pos,piece)
        self.houses_colors=houses_colors

    def draw(self,surface,house_size):
        pos=operation_vectors(self.pos,house_size,"*")
        rect=pygame.Rect(pos,house_size)
        pygame.draw.rect(surface,self.houses_colors[(self.type,self.state)],rect,0)

class Pygame_piece(piece):

    CIRCLE_SIZE_POR=0.76

    def __init__(self,side,type,pos, house, pieces_colors=PIECES_COLORS):
        piece.__init__(self,side,type,pos,house)
        self.pieces_colors=pieces_colors

    def draw(self,surface,house_size):
        pos_x=int((self.pos[0]*house_size[0])+house_size[0]/2)
        pos_y=int((self.pos[1]*house_size[1])+house_size[1]/2)
        radios=int((house_size[0]*self.CIRCLE_SIZE_POR)/2)
        color=self.pieces_colors[(self.side,self.type)]
        pygame.draw.circle(surface,color,(pos_x,pos_y),radios,0)


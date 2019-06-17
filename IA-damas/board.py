
from numpy_functions import operation_vectors,numpy,get_sinal_vector

class board():
    def get_tuple(self,pos):
        return pos[0],pos[1]

    def get_house(self,pos):
        pos_lin,pos_col=self.get_tuple(pos)
        if(pos_lin>=0 and pos_lin<self.board_size[0] and
              pos_col>=0 and pos_col<self.board_size[1]):

            return self.matriz_houses[pos_lin][pos_col]
        else:
            return None

    def get_house_list(self):
        house_array=numpy.array(self.matriz_houses)

        return house_array.ravel()

    def get_pieces_list(self):
        piece_list=[]
        house_list=self.get_house_list()
        [piece_list.append(house.piece) for house in house_list if(not house.is_empty())]

        return piece_list

    def get_all_plays(self,piece):
        possible_moves=piece.get_possible_moves()
        max_houses=piece.get_max_moves()
        move_list=moves(piece)

        for moveY,moveX,normal_move in possible_moves:
            pos_piece=piece.pos
            cont_moves=0
            while(cont_moves!=max_houses):
                pos_piece=operation_vectors(pos_piece,[moveY,moveX],"+")
                house=self.get_house(pos_piece)
                next_house=self.get_house(operation_vectors(pos_piece,[moveY,moveX],"+"))
                if(house!=None):
                    if(house.is_empty() and normal_move):
                        move_list.append(1,house)
                    elif(not house.piece==piece and house.piece!=None and next_house!=None):
                        if(next_house.is_empty()):
                            move_list.append(0,house)
                        break
                    else:
                        break
                else:
                    break
                cont_moves=cont_moves+1

        return move_list


    def set_play(self,piece,house_destiny):
        moves=self.get_all_plays(piece)
        if(moves.is_valid(house_destiny)):
            pos=operation_vectors(house_destiny.pos,piece.pos,"-")
            pos=get_sinal_vector(pos)
            pos=operation_vectors(house_destiny.pos,pos,"-")

            previous_house=self.get_house(pos)

            if(previous_house.is_empty() or previous_house.piece==piece):
                piece.move(house_destiny)
            else:
                piece.move(house_destiny)
                previous_house.piece=None

        else:
            raise invalid_play_exception("Move of piece"+str(piece.pos)+" to house"+str(house_destiny.pos))

    def set_move(self,piece):
        self.reset_houses_state()
        moves=self.get_all_plays(piece)
        moves.show()

    def __init__(self, board_size=(8,8)):
        self.board_size = board_size
        self.matriz_houses = []

    def reset_houses_state(self):
        for house in self.get_house_list():
            house.state=None

class house():

    def set_state(self,state):
        self.state=state

    def set_piece(self,piece):
        self.piece=piece
        self.piece.pos=self.pos

    def __init__(self, type, pos, piece=None,state=None):
        self.type = type
        self.pos=pos
        self.state=state
        self.piece=piece

        if(piece!=None):
            piece.house=self

    def is_empty(self):
        if(self.piece==None):
            return True
        else:
            return False


class piece():
    POSSIBLE_MOVES={
        (1, 1):[[-1, -1, 0], [1, -1, 0], [-1, 1, 1], [1, 1, 1]],
        (0, 1):[[-1, -1, 1], [1, -1, 1], [-1, 1, 0], [1, 1, 0]],
        (1, 2):[[-1, -1, 1], [1, -1, 1], [-1, 1, 1], [1, 1, 1]],
        (0, 2):[[-1, -1, 1], [1, -1, 1], [-1, 1, 0], [1, 1, 0]],
    }

    def get_possible_moves(self):
        return self.POSSIBLE_MOVES[(self.side,self.type)]

    def get_max_moves(self):
        max_moves=0
        if(self.type==1):
            max_moves=1
        elif(self.type==2):
            max_moves=None

        return max_moves


    def __init__(self,side, type, pos, house):
        self.side = side
        self.type = type
        self.pos = pos
        self.house=house

    def move(self,house):
        self.house.piece=None
        self.house=house
        self.house.set_piece(self)

    def __eq__(self, other):
        if(isinstance(other,piece)):
            if(self.side==other.side):
                return True
            else:
                return False
        else:
            return False

class moves():

    def get_houses(self):
        house_list=[]
        for type,house in self.list:
            house_list.append(house)

        return house_list

    def __init__(self,piece):
        self.piece=piece
        self.list=[]

    def append(self,type,house):
        self.list.append((type,house))

    def show(self):
        for house in self.get_houses():
            house.set_state(5)

    def hide(self):
        for house in self.get_houses():
            house.set_state(None)


    def is_valid(self,house):
        for _house in self.get_houses():
            if(house==_house):
                return True

        return False

    def __iter__(self):
        return self.list

    def __str__(self):
        string=""
        for type,house in self.list:
            string=string+"move of piece "+str(self.piece.pos)+" to "+str(house.pos)+" type:"+str(type)+"\n"

        return string

#exceptions custom

class piece_not_found_exception(Exception):
    pass

class invalid_play_exception(Exception):
    pass
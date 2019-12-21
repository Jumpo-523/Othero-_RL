# -*- coding: utf-8 -*-
import numpy as np
import time

class couldNotChangeTrunException(Exception):
    pass

class Othero():
    
    def __init__(self, N=8):
        self.set_board()
        self.current_turn = -1
        self.length_board = N
        self.display()

    def set_board(self):
        board = np.zeros((8, 8), dtype=int)
        i = 3
        j = 4
        board[i,i] = board[j,j] = 1
        board[j,i] = board[i,j] = -1
        self.state = board

    def display(self):
        # for i, r_ in enumerate(self.state):
        #     print(str(i)+" | "+str(r_))
        print(self.state)
    
    def _change_state(self, new_stone_loc):
        """change state for each direction"""
        count_reverse = 0
        i, j = new_stone_loc
        opposite = -1* self.current_turn
        state = np.copy(self.state)
        for direction in ["row", "col", "diag", "anti-diag"]:
            for dir_ in [1, -1]:
                count_reverse = 0
                for d in range(self.length_board):
                    try:
                        dx, dy = self.set_direction(dir_*d,direction)
                        # 縦横斜めどう制御する？
                        if dx == 0 and dy == 0:
                            pass
                        elif state[i + dx, j + dy] == opposite:
                            count_reverse += 1
                        elif state[i + dx, j + dy] == 0:
                            count_reverse = 0
                            break
                        elif state[i + dx, j + dy] == self.current_turn:
                            break
                    except IndexError:
                        break
                if count_reverse > 0:
                    print("we can reverse", count_reverse, "piece(s)!")
                    state[i, j] = self.current_turn
                    for d in range(1, count_reverse+1):
                        dx, dy = self.set_direction(dir_*d, direction)
                        state[i + dx, j + dy] = self.current_turn 
        if (self.state - state).sum() == 0:
            raise couldNotChangeTrunException("You could not put a new stone at this cell")
        self.current_turn = -1*self.current_turn
        self.state = state
    
    def play(self):
        
        try:
            while True:
                # import pdb; pdb.set_trace()
                print(str(self.current_turn) + "'s" + " Turn")
                print("set a new stone like d,d")
                new_stone = input() #list(map(int, input().split(',')))
                try:
                    self._change_state(new_stone)
                except couldNotChangeTrunException:
                    print("You could not put a new stone at this cell")
                    pass
                self.display()
        except KeyboardInterrupt:
            print('interrupted!')


    def set_direction(self, d, direction):
        if direction == "row":
            dx = d
            dy = 0
        elif direction == "col":
            dx = 0
            dy = d
        elif direction == "diag":
            dx = -1*d
            dy = d     
        elif direction == "anti-diag":
            dx = d
            dy = -1*d
        return dx, dy 



if __name__ == "__main__":
    
    othero = Othero()
    # import pdb; pdb.set_trace()
    # othero._change_state((2,3))
    # othero.display()
    othero.play()


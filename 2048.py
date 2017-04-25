from random import randint

class TwentyFortyEight:

    #Initialization constructor
    def __init__(self, board_width):

        #Python assumes that anything indented after a method is created belongs to that method
        #Python uses lists, similar to Java linked lists. You can prepend and append in Python lists.
        #Python automatically determines the type when you create a variable
        self.__board = []
        self.__board_width = board_width
        self.__score = 0
        self.reset()


    def reset(self):
        """This function resets the board to all zeroes, resets the score to zero and places a random 2 on the board"""

        #for how many rows we need in the board:
        #   generate a list of 0's of length board_width (representing a row)
        self.__board = [[0] * self.__board_width for _ in range(self.__board_width)]
        self.__score = 0
        self.place_random()


    def place_random(self):
        """Attempt to place a 2 in a random tile on the board"""

        #Uses list comprehension
        #blanks = [(i, j) for i in range(self.__board_width) for j in range(self.__board_width) if self.__board[i][j] == 0]
        blanks = []

        #Keeps track of all (i,j) coordinates that contain a zero in the board
        for i in range(self.__board_width):
            for j in range(self.__board_width):

                if self.__board[i][j] == 0:

                    blanks.append((i,j))

        #If we found any blanks, set a random blank position to 2
        if len(blanks) != 0:

            i,j = blanks[randint(0, len(blanks)-1)]
            self.__board[i][j] = 2

    def get_score(self):

        return self.__score

    def move_to(self, from_row, from_col, to_row, to_col):

        #Subtract rows, subtract columns and take the absolute value of the differences.
        row_dist = abs(to_row-from_row)
        col_dist = abs(to_col-from_col)

        #Valid distances are[1, 0] or [0, 1]
        if not ((row_dist == 1 and col_dist == 0) or (row_dist == 0 and col_dist == 1)):

            return False

        #if the piece we're trying to move is empty, then do NOTHING EVERyTHING IS OVER
        if self.__board[from_row][from_col] == 0:

            return False

        #If the to cell is 0, shift the value in the from cell to the to cell and erase the from cell.
        elif self.__board[to_row][to_col] == 0:

            self.__board[to_row][to_col] = self.__board[from_row][from_col]
            self.__board[from_row][from_col] = 0

        #If the values in from and to are the same, add them, place the added value in to, and clear the from value.
        elif self.__board[from_row][from_col] == self.__board[to_row][to_col]:

            self.__board[to_row][to_col] += self.__board[from_row][from_col]
            self.__board[from_row][from_col] = 0

            self.__score = max(self.__board[to_row][to_col], self.__score)

        #If the cell values are not equal and greater than zero, return false. Above else if checks cover this.
        else:

            return False

        return True

    def move_up(self):

        made_move = False

        #from 0 to board-2
        for i in range(len(self.__board)-1):
            #from board-1, to 0 and steps backwards 1
            for j in range(len(self.__board)-1,-1,-1):

                if self.move_to(i+1, j, i, j):

                    made_move = True

        return made_move

    def move_down(self):

        made_move = False

        for i in range(len(self.__board)-1, 0,-1):
            for j in range(len(self.__board)-1,-1,-1):

                if self.move_to(i-1, j, i, j):

                    made_move = True

        return made_move

    def move_right(self):

        made_move = False

        for i in range(len(self.__board)):
            for j in range(len(self.__board)-1,0,-1):

                if self.move_to(i, j-1,i,j):

                    made_move = True

        return made_move

    def move_left(self):

        made_move = False

        for i in range(len(self.__board)):
            for j in range(len(self.__board)-1):

                if self.move_to(i,j+1,i,j):

                    made_move = True

        return made_move


    def get_board(self):

        return self.__board

    def set_board(self, new_board):

        self.__board = new_board

    def show_board(self):

        for row in self.__board:

            row_output = ['{:^5}'.format(x) for x in row] #space=seperate the values ('%5s')
            row_output = '|'.join(row_output)               #join the output by '\'
            print('[' + row_output + ']')                  #surround by brackets and print



#If this is being ran as the main program(e.g. Python 2048.py), run the code below
if __name__ == '__main__':

    tfe = TwentyFortyEight(4)

    best_score = 0
    reset_flag = False

    while True:

        print("Current score:", tfe.get_score(), " | Best score:", best_score)
        tfe.show_board()

        print("Enter up, down, left or right to move in that direction.")
        print("Enter reset to reset the game or quit to exit.")

        user_choice = input()

        if user_choice == "up":

            while tfe.move_up():

                #Python expects an executable line of code, pass = do nothing
                pass


        elif user_choice == "down":

            while tfe.move_down():

                pass


        elif user_choice == "left":

            while tfe.move_left():

                pass


        elif user_choice == "right":

            while tfe.move_right():

                pass

        elif user_choice == "reset":

            tfe.reset()
            reset_flag = True

        elif user_choice == "quit":

            exit()

        else:

            print("Invalid move, Please try again!!!!\n")
            continue

        best_score = max(best_score, tfe.get_score())

        if not reset_flag:

            tfe.place_random()
            reset_flag = False

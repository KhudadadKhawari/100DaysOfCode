from subprocess import call
import os


def clear_screen():
    _ = call('clear' if os.name == 'posix' else 'cls')


class Board:
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def display_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("___|___|___")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("___|___|___")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("   |   |   ")


class Game(Board):
    def __init__(self, pl1_name="Player 1", pl2_name="Player 2"):
        super().__init__()
        self.player1 = pl1_name
        self.player2 = pl2_name
        self.player1_mark = 'X'
        self.player2_mark = 'O'
        self.win = False  # if any of players win this will turn True and the program will terminate by the results
        self.winner_mark = None  # the mark that wins[X or O ]

    def end_of_game(self):  # Checks if the Game is ended or not by checking if there's any empty cell
        if self.board.count(self.player1_mark) + self.board.count(self.player2_mark) == 9:
            return True
        else:
            return False

    def check_status(self):  # If any player wins This will assign True to self.win and the Winner Mark to self.winner_mark
        winner_mark = None  # winner_mark is used for finding the winner
        # checking if someone wins the game
        if (self.board[0] == self.board[1] == self.board[2] or self.board[0] == self.board[3] == self.board[6] or self.board[0] == self.board[4] == self.board[8]) and (self.board[0] != ' '):
            self.win = True
            winner_mark = self.board[0]
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != ' ':
            self.win = True
            winner_mark = self.board[1]
        # elif self.board[2] == self.board[5] == self.board[8] or self.board[2] == self.board[4] == self.board[6] and self.board[2] != ' ':
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != ' ':
            self.win = True
            winner_mark = self.board[2]
        elif self.board[2] == self.board[4] == self.board[6] and self.board[2] != ' ':
            self.win = True
            winner_mark = self.board[2]
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != ' ':
            self.win = True
            winner_mark = self.board[3]
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != ' ':
            self.win = True
            winner_mark = self.board[6]

        self.winner_mark = winner_mark

    def results(self):  # This function will execute if any or none of the players win.
        if self.win:
            if self.winner_mark == self.player1_mark:
                print(f"{self.player1} Successfully WIN the Game. \n {self.player2} LOST")
            else:
                print(f"{self.player2} Successfully WIN the Game. \n {self.player1} LOST")
        else:
            print("No one won the Game, IT's a Draw")


print("WELCOME TO TIC TAC TOE GAME by SeferYak")
player1 = input("PLayer 1 Please Enter Your Name: ")
player2 = input("Player 2 Please Enter Your Name: ")

game = Game(pl1_name=player1, pl2_name=player2)  # Creates the Game Object


def choose_location():
    available_locations = []
    for i in range(len(game.board)):
        if game.board[i] == " ":
            available_locations.append(i + 1)
    print(f"Available locations to put Your mark: \n{available_locations}")
    user_choice = int(input("Input The Location Number: "))
    return user_choice


while True:
    clear_screen()
    print(f"{game.player1}: [{game.player1_mark}] | {game.player2}: [{game.player2_mark}]")
    loc_count = game.board.count(' ')
    game.display_board()
    try:
        if loc_count % 2 == 0:
            print(f"it's {game.player2} Turn to Play")
            mark_loc = choose_location()-1
            if game.board[mark_loc] == ' ':
                game.board[mark_loc] = game.player2_mark
        else:
            print(f"it's {game.player1} Turn to Play")
            mark_loc = choose_location()-1
            if game.board[mark_loc] == ' ':
                game.board[mark_loc] = game.player1_mark
    except IndexError:
        pass
    except ValueError:
        pass

    game.check_status()
    if game.end_of_game() or game.win:
        game.display_board()
        game.results()
        break

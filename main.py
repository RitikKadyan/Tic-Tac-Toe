class Sudoku:  # This is the sudoku class
    # This method runs when an instance of this class is created
    def __init__(self):
        #  This is the board(Multi-List)
        self.board = ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']

    # This method will print the formatted version of the board
    def print_board(self):
        # This outer loop will print the seperator between the rows
        for i in range(1, len(self.board) + 1):
            # This inner loop will print the rows of the board and the seperator in between the values
            for j in range(1, len(self.board) + 1):
                # If the loop is on the last column(3) then it will not print the seperator else it will
                if j % 3 != 0:
                    # Got the ┃ symbol from https://www.lennyfacecopypaste.com/text-symbols/line.html
                    print(f'{self.board[i - 1][j - 1]} ┃', end=' ')
                else:
                    print(self.board[i - 1][j - 1])
            if i % 3 != 0:
                # Got the ━ symbol from https://www.lennyfacecopypaste.com/text-symbols/line.html
                print('━━━━━━━━━')

    # This method will get called after each turn and check for a winner
    def check_winner(self):
        pass

    # This method will assign X or O to a spot on the board
    def assign_spot(self, i, j):
        pass

    # This method will announce the winner
    def announce_winner(self):
        pass


def main():
    # This will create an object s of the Sudoku class
    s = Sudoku()
    # This variable to keep track if a winner has been found
    winner_found = False

    # This loop will stop when a winner has been found
    while not winner_found:
        pass


# This will run if the program starts directly instead of being imported
if __name__ == '__main__':
    main()

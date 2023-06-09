import random


class Puissance4:
    def __init__(self) -> None:
        '''
        Constructor for the Puissance4 class. Initializes the game grid to an empty list.
        '''
        self.grid = []

    def __str__(self) -> str:
        '''
        Special method of the Puissance4 class to convert the current state of the grid to 
        a formatted string for display. Returns a string representing the game grid.
        '''
        if self.grid == []:
            return []
        res = "\n\n\n\n"
        for i in range(6):
            for j in range(7):
                res += "|J" if self.grid[i][j] == 1 else ("|R" if self.grid[i][j] == 2 else "|*")
            res += '|\n'
        return res + ' 1 2 3 4 5 6 7'

    def start(self) -> None:
        '''
        Main method of the Puissance4 class to start the game. Initializes the game grid, 
        manages player turns, and checks if either player has won. Displays the end-of-game 
        message with the winner.
        '''
        self.grid = [[0 for i in range(7)] for j in range(6)]
        self.end = False
        playerRound = 0
        while not self.end:
            self.pawnPlacement(playerRound%2)
            self.end = self.check_win(playerRound%2+1)
            playerRound += 1
        print(self.__str__())
        print(f"Player {playerRound%2} win!")
    
    def playerPlay(self, color: int) -> int:
        '''
        Method of the Puissance4 class to allow a player to play a pawn. Asks the player 
        to input the desired location for the pawn placement and returns this value as an integer.
        '''
        print(self.__str__())
        playerInput = -1
        while playerInput > 6 or playerInput < 0:
            playerInput = int(input(f"{color} ->")) - 1
            #playerInput = random.randint(0,6)
        return playerInput
    
    def pawnPlacement(self, color: int) -> None:
        '''
        Method of the Puissance4 class to place a pawn on the grid. Checks if the location is 
        valid and places the pawn in the first empty space from the bottom.
        '''
        validLocation = False
        while not validLocation:
            location = self.playerPlay(color)
            if self.grid[0][location] == 0:
                validLocation = True
                for i in range(6):
                    if self.grid[5-i][location] == 0:
                        self.grid[5-i][location] = color + 1
                        break
    
    def check_win(self, color: int) -> bool:
        '''
        Method of the Puissance4 class to check if a player has won. Iterates over the grid to 
        detect if four pawns of the same player are aligned horizontally, vertically, or diagonally. 
        Returns True if a player has won, False otherwise.
        '''
        # Vérification horizontale
        for row in self.grid:
            for i in range(len(row)-3):
                if row[i:i+4] == [color]*4:
                    return True

        # Vérification verticale
        for col in range(len(self.grid[0])):
            column = [self.grid[row][col] for row in range(len(self.grid))]
            for i in range(len(column)-3):
                if column[i:i+4] == [color]*4:
                    return True

        # Vérification diagonale
        for i in range(len(self.grid)-3):
            for j in range(len(self.grid[0])-3):
                if self.grid[i][j] == color and self.grid[i+1][j+1] == color and self.grid[i+2][j+2] == color and self.grid[i+3][j+3] == color:
                    return True
                if self.grid[i][j+3] == color and self.grid[i+1][j+2] == color and self.grid[i+2][j+1] == color and self.grid[i+3][j] == color:
                    return True

        return False



a = Puissance4()
a.start()
import random
import cowsay


class Grid():
    def __init__(self, height=15, width=16, symbol="#"):
        self.height = height
        self.width = width
        self.symbol = symbol
        self.grid = self.makeGrid()
        self.board = self.clearBoard()
            
    def makeGrid(self):
        return [[self.symbol]*self.width for _ in range(self.height)] 
        
    def clearBoard(self):
        board = self.grid
        for hpos in range(1,self.height-1):
            for wpos in range(1,self.width-1):
                board[hpos][wpos] = " "
    
        return board
    
    def add_Vertical(self, height, width, len, symbol="_"):
        for item in range(self.width):
            if item >= width and item < width+len:
                self.board[height][item] = symbol
 
        
    def add_Horizontal(self, startVert, horPos, len, symbol ="|"):
        for row in range(startVert, startVert+len):
            self.board[row][horPos] = symbol


    def addX(self, cellInput):

        modCell = cellInput%3
        if modCell == 0:
            modCell = 3
        
        if cellInput <=3:
            self.board[2][2+modCell*5-5] = "\\"
            self.board[2][3+modCell*5-5] = "/"
            self.board[3][2+modCell*5-5] = "/"
            self.board[3][3+modCell*5-5] = "\\"

        elif cellInput <= 6:
            self.board[2+5][2+modCell*5-5] = "\\"
            self.board[2+5][3+modCell*5-5] = "/"
            self.board[3+5][2+modCell*5-5] = "/"
            self.board[3+5][3+modCell*5-5] = "\\"
            
        elif cellInput <=9:
            self.board[2+10][2+modCell*5-5] = "\\"
            self.board[2+10][3+modCell*5-5] = "/"
            self.board[3+10][2+modCell*5-5] = "/"
            self.board[3+10][3+modCell*5-5] = "\\"
        

    def addO(self, cellInput):
        modCell = cellInput%3
        if modCell == 0:
            modCell = 3
        if cellInput <= 3:
            self.board[2][3+modCell*5-5] = ")"
            self.board[2][2+modCell*5-5] = "("
        elif cellInput <= 6:
            self.board[2+5][3+modCell*5-5] = ")"
            self.board[2+5][2+modCell*5-5] = "("
        elif cellInput <=9:
            self.board[2+10][3+modCell*5-5] = ")"
            self.board[2+10][2+modCell*5-5] = "("
        
    def __str__(self) -> str:
        output = ""          
        for row in self.board:
            for item in row:
                output += item+" "
            output += "\n"
        return output

class TicTacToe(Grid):
    def __init__(self, *players, random=False):
        super().__init__()
        self.player1 = players[0]
        self.random = random
        if random:
            self.choices = [1,2,3,4,5,6,7,8,9]
        else:    
            self.player2 = players[1]
        self.tictactoe()
        self.game = [
            1,1,1,
            1,1,1,
            1,1,1
            ]   
        self.results = []
        
    def tictactoe(self):
        # Draw number labels
        anchors = [4, 9, 14]
        number = 0
        rowcon = 0
        for _ in range(3):
            for anchor in anchors:
                number += 1
                self.add_Vertical(max(rowcon,1), anchor, 1, symbol=str(number))
            rowcon += 5        
        # Draw grid
        self.add_Vertical(4, 1, 14)
        self.add_Vertical(9, 1, 14)
        self.add_Horizontal(1, 10, 13)
        self.add_Horizontal(1, 5, 13)
        # Print game table
        print(self)
    
    def checkVictory(self):
        # add sum of rows columns and diagonals to result
        self.results.append(sum([x for x in self.game[::3]]))
        self.results.append(sum([x for x in self.game[1::3]]))
        self.results.append(sum([x for x in self.game[2::3]]))
        self.results.append(sum([x for x in self.game[::4]]))
        self.results.append(sum([x for x in self.game[2:7:2]]))
        self.results.append(sum([x for x in self.game[:3:]]))
        self.results.append(sum([x for x in self.game[3:6:]]))
        self.results.append(sum([x for x in self.game[6:9:]]))
        
        # Check which player wins
        if 0 in self.results:
            cowsay.dragon(f"{self.player1} wins")
            return True
        elif 6 in self.results:
            if self.random:
                self.player2 = "Computer"
            cowsay.trex(f"{self.player2} wins")
            return True
        else:
            return False
        
        
    def playGame(self):
        counter = 0
        alreadyPlayed = []
        while True:
            # Draw if counter larger than 5
            counter += 1
            
            # Player 1 turn
            while True:
                try:
                    play = int(input(f"{self.player1} choose a number: "))
                except ValueError:
                    print("please input integer between 1 and 9")
                    continue
                if play < 1 or play > 9 or play in alreadyPlayed:
                    print("invalid move")
                    continue
                if self.random:
                    self.choices.remove(play)
                alreadyPlayed.append(play)
                
                break
            self.addX(play)
            self.game[play-1] -= 1    
            print(self)
            
            # Check win condition
            if self.checkVictory():
                return           
            if counter == 5:
                print("Draw")
                return
            
            # Play with the computer if selected
            if self.random:
                
                if  sum([x for x in self.game[::3]]) == 5:
                    plays = [1,4,7]
                    play = plays[self.game[::3].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                         

                elif sum([x for x in self.game[1::3]]) == 5:
                    plays = [2,5,8]
                    play = plays[self.game[1::3].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)           
                                        
                elif sum([x for x in self.game[2::3]]) == 5:
                    plays = [3,6,9]
                    play = plays[self.game[2::3].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                   
                elif sum([x for x in self.game[::4]]) == 5:
                    plays = [1,5,9]
                    play = plays[self.game[::4].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                    
                elif sum([x for x in self.game[2:7:2]]) == 5:
                    plays = [3,5,7]
                    play = plays[self.game[2:7:2].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                    
                elif sum([x for x in self.game[:3:]]) == 5:
                    plays = [1,2,3]
                    play = plays[self.game[:3:].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                    
                elif sum([x for x in self.game[3:6:]]) == 5:
                    plays = [4,5,6]
                    play = plays[self.game[3:6:].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                    
                elif sum([x for x in self.game[6:9:]]) == 5:
                    plays = [7,8,9]
                    play = plays[self.game[6:9:].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                    
                elif  sum([x for x in self.game[::3]]) == 1:
                    plays = [1,4,7]
                    play = plays[self.game[::3].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                            
                elif sum([x for x in self.game[1::3]]) == 1:
                    plays = [2,5,8]
                    play = plays[self.game[1::3].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)           

                elif sum([x for x in self.game[1::3]]) == 1:
                    plays = [2,5,8]
                    play = plays[self.game[1::3].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)           
                                        
                elif sum([x for x in self.game[2::3]]) == 1:
                    plays = [3,6,9]
                    play = plays[self.game[2::3].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                   
                elif sum([x for x in self.game[::4]]) == 1:
                    plays = [1,5,9]
                    play = plays[self.game[::4].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                    
                elif sum([x for x in self.game[2:7:2]]) == 1:
                    plays = [3,5,7]
                    play = plays[self.game[2:7:2].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                    
                elif sum([x for x in self.game[:3:]]) == 1:
                    plays = [1,2,3]
                    play = plays[self.game[:3:].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                    
                elif sum([x for x in self.game[3:6:]]) == 1:
                    plays = [4,5,6]
                    play = plays[self.game[3:6:].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                    
                elif sum([x for x in self.game[6:9:]]) == 1:
                    plays = [7,8,9]
                    play = plays[self.game[6:9:].index(1)]
                    print(play)
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                    
                    
                elif not 5 in alreadyPlayed:
                    play = 5
                    self.choices.remove(play)
                    alreadyPlayed.append(play)
                    
                elif sorted(alreadyPlayed) == [1,5,9] or sorted(alreadyPlayed) == [3,5,7]:
                    # check who has 5
                    if self.game[4] == 0:
                        possiblePlays = [1, 3, 7, 9]
                    elif self.game[4] == 2:
                        possiblePlays = [2, 4, 6, 8]
                    plays = []
                    for item in possiblePlays:
                        if not item in alreadyPlayed:
                            plays.append(item)
                    if plays:
                        play = random.choice(plays)                     
                        self.choices.remove(play)
                        alreadyPlayed.append(play)
                        plays = []
                                                                   
                else:
                    
                    possiblePlays = [1, 3, 7, 9]
                    plays = []
                    for item in possiblePlays:
                        if not item in alreadyPlayed:
                            plays.append(item)
                    if plays:
                        play = random.choice(plays)                     
                        self.choices.remove(play)
                        alreadyPlayed.append(play)
                        plays = []
                    else:
                        play = random.choice(self.choices) 
                        self.choices.remove(play)
                    
               
            else:
                # Player 2 turn
                while True:
                    try:
                        play = int(input(f"{self.player2} choose a number: "))
                    except ValueError:
                        print("please input integer between 1 and 9")
                        continue
                    if play < 1 or play > 9 or play in alreadyPlayed:
                        print("invalid move")
                        continue
                    alreadyPlayed.append(play)
                    break 
            self.addO(play)
            self.game[play-1] += 1    
            print(self)
            
            # Check win condition
            if self.checkVictory():
                return           
            

def main():

    pcgame = TicTacToe("tom", random=True)
    pcgame.playGame()

    
if __name__ == "__main__":        
    main()

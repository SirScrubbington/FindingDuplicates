import random

class Board:
    n = 0
    myList = [[]]
    checked=[]

    def __init__(self, n):
        self.n = n
        self.myList = [[] for i in range(n)]
        for y in range(n):
            for x in range(n):
                self.myList[y].append(random.randint(1,10))

    def checkduplicate(self,p):
        self.checked.append(p)

    def printduplicates(self):
        print(self.checked)

    def print_board(self):
        for y in range(self.n):
            print (y,": ",self.myList[y])

    def getval(self,p):
        n = self.myList[p.getX()][p.getY()]
        return n


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        str=("(",self.x,",",self.y,")")
        return str

    def getX(self):
        return self.x

    def getY(self):
        return self.y

## Game Data
n = 0
B = Board(n)


gameover = False
gameStarted = False

print("Welcome to Find Duplicates!")
print("Type 'Help' to view instructions and controls.")

while gameover == False:
    if gameStarted == False:
        n = input ("Please enter a board size: > ")
        B = Board(int(n))
        gameStarted = True

    command = input("> ").lower()
    if command == "help":
        print("The goal of the game is to check all of the spaces on the board which have a duplicate number")
        print("Until there are no more duplicates left. However, checked spaces cannot be directly left, right")
        print("Or diagonal to each other. That's it, good luck!")
        print("Controls:")
        print("'Help' displays the instructions and rules.")
        print("'Check' prompts you to provide the X and Y values of a space to be checked.")
        print("'Checked' prints all of the positions which have been checked.")
        print("'Print' prints the board state")
        print("'Exit' closes the program.")

    elif command == "check":
        x = int(input("X Coordinate: >"))
        y = int(input("Y Coordinate: >"))
        p = Point(x,y)
        B.checkduplicate(p)

    elif command == "checked":
        B.printduplicates()

    elif command == "print":
        B.print_board()

    elif command == "exit":
        gameover=True

    else:
        print("Command not recognised. Type 'help' for a list of valid commands.")


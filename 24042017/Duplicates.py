import random
import sys
#from collections import defaultdict


class Board:
    def __init__(self,size,r):
        self.solved=False
        self.n = size
        self.r=r
        self.myList = [[]]
        self.userChecked = []
        self.checked = []
        self.duplicates = {}
        self.valuecovers = {}
        self.values = {}

        self.myList = [[] for i in range(n)]
        for y in range(n):
            for x in range(n):
                self.myList[y].append(random.randint(1,r))

        for x in range(len(self.myList)):
            for y in range(len(self.myList)):
                ## Increment the number of times this value has been seen
                temp = self.myList[x][y]
                if temp in self.values:
                    self.values[temp]+=1
                else:
                    self.values[temp]=1
                pass

        for x in range(len(self.myList)):
            for y in range(len(self.myList)):
                temp = Point(x,y)
                if  self.values[self.myList[x][y]] > 1:
                    self.duplicates[temp]=self.myList[x][y]

    def print_values(self):
        print(self.values)

    def user_check(self,P):
        act=False
        #p = Point(P[0], P[1])
        for k in self.duplicates:
            if k == P:
                if k in self.userChecked:
                    print("Index unchecked.")
                    self.userChecked.remove(k)
                    self.updatecovers(k,-1)
                    act = True
                    pass
                else:
                    print("Index checked.")
                    self.userChecked.append(P)
                    self.updatecovers(k, 1)
                    act = True
                    pass
        if act == False:
            print("Index is not a duplicate.")

    def updatecovers(self,value,increment):
        if value in self.valuecovers:
            self.values[value]+=increment

    def check_duplicate(self,P):
        #p = Point(P[0],P[1])
        for k in self.duplicates:
            if k == P:
                if k in self.checked:
                    #print("Duplicate removed.")
                    self.checked.remove(k)
                    pass
                else:
                    if k in self.userChecked:
                        #print("Duplicate removed.")
                        pass
                    else:
                        self.checked.append(P)
                        pass

    def print_duplicates(self):
        print(self.duplicates)

    def print_covered(self):
        print(self.userChecked)
        print(self.checked)

    def cover_random(self):
        coverno = random.randint(0,len(self.duplicates))
        for i in range(coverno):
            P = Point(random.randint(0,self.n),random.randint(0,self.n))
            self.user_check(P)

    def print_board(self):
        #strlen=0
        for y in range(self.n):
            for x in range(self.n):
                sys.stdout.write(str(self.myList[x][y])+" ")
            sys.stdout.write("\n")

    def getval(self,p):
        n = self.myList[p.getX()][p.getY()]
        return n

    def has_adjacent(self,x,y):
        solved=True

        #If the algorithm has flagged an adjacent space as a duplicate
        if Point(x,y) in self.checked:
            solved=True
            if x > 0:
                if Point(x-1,y) in self.checked:
                    #print("Adjacent covers")
                    solved=False
                    pass
            if y > 0:
                if Point(x,y-1) in self.checked:
                    #print("Adjacent covers")
                    solved=False
                    pass
            if x < n:
                if Point(x+1,y) in self.checked:
                    #print("Adjacent covers")
                    solved=False
                    pass
            if y < n:
                if Point(x,y+1) in self.checked:
                    #print("Adjacent covers")
                    solved=False
                    pass

        # If user has flagged an adjacent space as a duplicate
        if Point(x,y) in self.userChecked:
             if x > 0:
                if Point(x-1,y) in self.userChecked:
                    #print("Adjacent covers")
                    solved=False
                    pass
             if y > 0:
                if Point(x,y-1) in self.userChecked:
                    #print("Adjacent covers")
                    solved=False
                    pass
             if x < n:
                if Point(x+1,y) in self.userChecked:
                    #print("Adjacent covers")
                    solved=False
                    pass
             if y < n:
                if Point(x,y+1) in self.userChecked:
                    #print("Adjacent covers")
                    solved=False
                    pass
                pass
        return solved

    def check_solution(self):
        solved=True
        adj=True

        for k,v in self.duplicates.items():
            if self.values.get(k) != v+1:
                #print("All duplicates not covered.")
                solved=False

        for x in range(self.n):
            for y in range(self.n):
                adj = self.has_adjacent(x,y)
                if adj == False:
                    solved = False
        return solved
        pass

    def find_solution(self,dup):
        for k,v in self.duplicates.items():
            pass
        pass

    def solve(self,index):
        if index == -1:
            return False
        else:
            valueat=self.duplicates.get(index)
            if self.values.get(valueat) != valueat+1:
                '''
            for k,v in self.duplicates.items():
                if self.values.get(k) != v+1:
                    #print("All duplicates not covered.")
                    solved=False
                return False
                '''
            pass
        pass

    def savedata(self,fname):
        outfile = open(str("./" + fname + "/values.txt"))
        for x in range(n):
            for y in range(n):
                outfile.write()
        pass
        outfile.close()
        outfile = open(str("./"+fname+"/extdata.txt"))
        outfile.write(self.solved)
        outfile.write(self.size)
        outfile.write(self.r)
        outfile.write(self.userChecked)
        outfile.write(self.checked)
        outfile.write(self.duplicates)
        outfile.write(self.valuecovers)
        outfile.write(self.values)

    def readdata(self,name):
        pass

class Point:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __hash__(self):
        return hash((self.x,self.y))

    def __str__(self):
        out = str("(" + str(self.x) + "," + str(self.y) + ")")
        return out

    def __repr__(self):
        out = str("(" + str(self.x) + "," + str(self.y) + ")")
        return out

    def __eq__(self,other):
        if isinstance(other,self.__class__):
            return (self.x == other.x and self.y == other.y)
        else:
            return False

    def __ne__(self,other):
        return not self.__eq__(other)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

## Game Data
n = 9
d = ""
r = 50
#B = Board(n,100)

## Debugging Code
#B.print_board()
#B.print_duplicates()
#B.cover_random()
#B.print_covered()
#print(B.check_solution())

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


gameover = False
gameStarted = False
s = Stack()
undone = False
print("Welcome to Find Duplicates!")
print("Type 'Help' to view instructions and controls.")

while gameover == False:
    if gameStarted == False:
        print("Please enter a grid size: ")
        n = int(input("> "))
        print("Please enter a difficulty (Easy, Normal, Hard): ")
        d = (input("> "))

        if d.lower() == "easy":
            r = 100
        elif d.lower() == "normal":
            r = 50
        elif d.lower() == "hard":
            r = 25
        else:
            r = 50
        B = Board(n,r)
        gameStarted = True

    command = input("> ").lower()

    if "check" in command:
        s.push(command)

    if command == "undo":
        if s.is_empty() != True:
            print(s.peek())
            command = s.pop()
            undone = True
        else:
            print("Nothing to undo.")
        #print(command)

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

    elif "check" in command:
        cmd = command.split()
        if len(cmd) > 1:
            p = Point(cmd[1],cmd[2])
            print(p)
            B.user_check(p)


    elif command == "solve":
        solved = B.solve()
        if solved == True:
            print("Solution state reached!")
        else:
            print("No solution found.")

    elif command == "print":
        B.print_board()
        B.print_covered()
        #B.print_duplicates()

    elif command == "exit":
        gameover=True

    elif command == "test":
        state=B.check_solution()
        if state == True:
            print("Goal state reached.")
        else:
            print("Goal state not found.")

    elif command == "restart":
        gameStarted = False

    elif command == "save":
        print("Name to save as:")
        fname = input("> ")
        B.savedata(fname)


    elif command == "load":
        print("Name of file to load:")
        fname = input("> ")
        if ".sav" in fname:
            pass
        else:
            fname = fname + ".sav"
            pass
        pass

    elif undone == False:
        print("Command not recognised. Type 'help' for a list of valid commands.")

    elif undone == True:
        undone = False

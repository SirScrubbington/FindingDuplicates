import random
import sys
import copy
#from collections import defaultdict


class Board:

    def updatecovers(self,value,increment):
        if value in self.valuecovers:
            self.valuecovers[value]+=increment
        else:
            self.valuecovers[value]=increment

    def __init__(self,size,r):
        self.backtrackingsolved=False
        self.n = size
        self.r=r
        self.myList = [[]]
        self.userChecked = []
        self.checked = []
        self.duplicates = {}
        self.valuecovers = {}
        self.values = {}
        self.indexes = []
        self.groups = {}


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
                self.updatecovers(self.myList[x][y], 0)
                if  self.values[self.myList[x][y]] > 1:
                    self.duplicates[temp]=self.myList[x][y]
                    self.indexes.append(temp)

    def print_values(self):
        print(self.values)

    def user_check(self,P):
        act=False
        for k,v in self.duplicates.items():
            if k == P:
                if k in self.userChecked:
                    print("Index unchecked.")
                    self.userChecked.remove(k)
                    self.updatecovers(v,-1)
                    act = True
                    pass
                else:
                    print("Index checked.")
                    self.userChecked.append(P)
                    self.updatecovers(v, 1)
                    act = True
                    pass
        if act == False:
            print("Index is not a duplicate.")

    def check_duplicate(self,P):
        #p = Point(P[0],P[1])
        for k,v in self.duplicates.items():
            if k == P:
                if k in self.checked:
                    #print("Duplicate removed.")
                    self.checked.remove(k)
                    self.updatecovers(v, -1)
                    pass
                else:
                    if k in self.userChecked:
                        #print("Duplicate removed.")
                        pass
                    else:
                        self.checked.append(P)
                        self.updatecovers(v, +1)
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

    def no_adjacent(self,x,y):
        backtrackingsolved=True

        #If the algorithm has flagged an adjacent space as a duplicate
        if Point(x,y) in self.checked:
        #if True:
            #backtrackingsolved=True
            if x > 0:
                if Point(x-1,y) in self.checked:
                    #print("Adjacent covers")
                    backtrackingsolved=False
                    pass
            if y > 0:
                if Point(x,y-1) in self.checked:
                    #print("Adjacent covers")
                    backtrackingsolved=False
                    pass
            if x < n:
                if Point(x+1,y) in self.checked:
                    #print("Adjacent covers")
                    backtrackingsolved=False
                    pass
            if y < n:
                if Point(x,y+1) in self.checked:
                    #print("Adjacent covers")
                    backtrackingsolved=False
                    pass

        # If user has flagged an adjacent space as a duplicate
        if Point(x,y) in self.userChecked:
        #if True:
             if x > 0:
                if Point(x-1,y) in self.userChecked:
                    #print("Adjacent covers")
                    backtrackingsolved=False
                    pass
             if y > 0:
                if Point(x,y-1) in self.userChecked:
                    #print("Adjacent covers")
                    backtrackingsolved=False
                    pass
             if x < n:
                if Point(x+1,y) in self.userChecked:
                    #print("Adjacent covers")
                    backtrackingsolved=False
                    pass
             if y < n:
                if Point(x,y+1) in self.userChecked:
                    #print("Adjacent covers")
                    backtrackingsolved=False
                    pass
                pass
        return backtrackingsolved

    def check_solution(self):

        backtrackingsolved=True
        adj=True

        #print(self.values)
        #print(self.valuecovers)

        for k,v in self.valuecovers.items():
            #print(k,v)
            if self.values.get(k) != v+1:
                if backtrackingsolved == True:
                    #print("All duplicates not covered.")
                    pass
                backtrackingsolved=False

        for x in range(self.n):
            for y in range(self.n):
                adj = self.no_adjacent(x,y)
                if adj == False:
                    backtrackingsolved = False
        return backtrackingsolved

        pass

    def find_solution(self,dup):
        for k,v in self.duplicates.items():
            pass
        pass

    def bruteforce(self):
        state = []
        solved = False
        changed = False
        loops = 0
        P = Point(0,0)

        while solved == False:
            for i in self.indexes:

                P.x = i.getX()
                P.y = i.getY()

                if self.no_adjacent(P.getX(),P.getY()):
                   val = self.myList[i.getX()][i.getY()]
                   if self.values.get(val) != self.valuecovers[val]+1:
                       if i not in self.checked:
                           self.check_duplicate(i)
                           changed = True
                   for i in state:
                       if i == self.checked:
                           return False
                   state.append(copy.deepcopy(self.checked))
                   loops = loops + 1
                   if changed==False:
                       print(loops)
                       return False
                print(self.checked)
            solved = self.check_solution()
        return True

    def backtrackingsolve(self,index):

        if self.no_adjacent(index.getX(),index.getY()):
            val = self.myList[i.getX()][i.getY()]
            if self.values.get(val) != self.valuecovers[val] + 1:
                if i not in self.checked:
                    self.check_duplicate(i)


        pass

    def print_indexes(self):
        print(self.indexes)

    def savedata(self,fname):
        outfile = open(str("./" + fname + "/values.txt"))
        for x in range(n):
            for y in range(n):
                outfile.write()
        pass
        outfile.close()
        outfile = open(str("./"+fname+"/extdata.txt"))
        outfile.write(self.backtrackingsolved)
        outfile.write(self.size)
        outfile.write(self.r)
        outfile.write(self.userChecked)
        outfile.write(self.checked)
        outfile.write(self.duplicates)
        outfile.write(self.valuecovers)
        outfile.write(self.values)

    def readdata(self,name):
        pass

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

succ = 0

for i in range(5):
    B = Board(n,100)
    if(B.bruteforce()):
        succ+=1
print (succ * 100.0)
#Debugging Code
#B.print_board()
#B.print_indexes()
#print(B.backtrackingsolve(0))


# Game State
gameover = True
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
        solved = B.backtrackingsolve(0)
        if solved == True:
            print("Solution state reached!")
        else:
            print("No solution found.")

    elif command == "bsolve":
        solved = B.bruteforce()
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

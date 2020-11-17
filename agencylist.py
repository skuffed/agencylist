# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:16:18 2019

@author: Alex
"""

class adjacencyList:
    
    nVert = 0

    def loadFile(self):
        self.fileName = input("Enter file name: ")

    def printVert(self, n, list):
        if n > nVert:
            print("Error")
            return
        print(n , ": " , list[n-1])  
        
    def readFile(self, file):
        f = open(file)
        global nVert 
        nVert = int(f.readline())
        list1 = [list() for i in range(nVert)]

        for line in f:
            vertNum = int(line.split(None, 1)[0]) - 1
            vertCon = int(line.split(None, 1)[1])
            list1[vertNum].append(vertCon)

        return list1


    def showMenu(self):
        print("")
        print("")
        print("")
        print("Menu")
        print("")
        print("1. Vertices connected to")
        print("")
        print("2. Print graph")
        print("")
        print("3. Add Connection")
        print("")   
        print("4. Store to file")
        print("")        
        print("5. Exit ")
        print("")        
        print("6. DFS ")
        print("")        
        print("7. BFS ")
        print("")
        choice = input("Enter option: ")
       
        if choice == "1":
            return(1)
        elif choice == "2":
            return(2)
        elif choice == "3":
            return(3)
        elif choice == "4":
            return(4)
        elif choice == "5":
            return(5)
        elif choice == "6":
            return(6)
        elif choice == "7":
            return(7) 

    def printGraph(self, list):
        for i in range(len(list)):
            num = i+1
            print(num, " : ", list[i])

    def addConnection(self, list):
        connection = input("Enter the new arch:" )
        edge = int(connection.split(None, 1)[0])
        con = int(connection.split(None, 1)[1])
        if edge > nVert or con > nVert:
            print("Error vertex doesn't exist")
        else:    
            list[edge-1].append(con)
            print(list)
                
    def storeFile(self, list):
        file = input("Enter file name to write:" )
        fi = open(file, "w")
        strVert = str(nVert)
        fi.write(strVert + "\n")
        for i in range(len(list)):
                for j in range(len(list[i])):
                    fi.write(str(i+1) + " " + str(list[i][j]) + "\n")


    
    def dfs(self, value):
        l1 = [list([0,1,0,0,1])]
        l1.append([1,0,1,1,0])
        l1.append([0,1,0,0,0])
        l1.append([0,1,0,0,0])
        l1.append([1,0,0,0,0])
        seen = list()
        #seen.append(value)
        stack = list()
        stack.append(value)
        while len(stack) > 0:
            value = stack[0]
            print(value)
            print("st1ack1",stack)
            seen.append(value)
            print("se2en2",seen)
            for i in range(len(l1[value])):
                if l1[value][i] == 1:
                    if i not in seen and i not in stack:
                        if i != value:
                            stack.append(i)
            del stack[0]
            print("sta2ck",stack) 
            print("se2en",seen)  

    def bfs(self, value):
        l1 = [list([0,1,0,0,1])]
        l1.append([1,0,1,1,0])
        l1.append([0,1,0,0,0])
        l1.append([0,1,0,0,0])
        l1.append([1,0,0,0,0])
        seen = list()
        #seen.append(value)
        stack = list()
        stack.append(value)
        while len(stack) > 0:
            value = stack[0]
            print(value)
            print("st1ack1",stack)
            seen.append(value)
            print("se2en2",seen)
            for i in range(len(l1[value])):
                if l1[value][i] == 1:
                    if i not in seen and i not in stack:
                        if i != value:
                            stack.append(i)
            del stack[0]
            print("sta2ck",stack) 
            print("se2en",seen)  
    


graph1 = adjacencyList()
graph1.loadFile()
print(graph1.fileName)
graphlist = graph1.readFile(graph1.fileName)
graph1.printGraph(graphlist)
answer = graph1.showMenu()
while answer != 5:
    if answer == 1:
        numVert = int(input("Please enter a vertice:"))
        graph1.printVert(numVert, graphlist)
    if answer == 2:
        graph1.printGraph(graphlist)
    if answer == 3:
        graph1.addConnection(graphlist)
    if answer == 4:
        graph1.storeFile(graphlist)
    if answer == 6:
        graph1.dfs(0)
    if answer == 7:
        graph1.bfs(0)
    answer = graph1.showMenu()
exit




# Find shortest path with dijkstra algorithm

# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm


import sys
import math
import time
import numpy as np
import matplotlib.pyplot as plt


class shortest_path:
    
    def __init__(self):
        #=== Read data from files ===
        
        self.data_coord = np.loadtxt('xy.txt') # Coordinate file
        self.data_node = np.loadtxt('node.txt') # Node file
        
        self.ID = self.data_coord[:][:,0] # Point ID of coordinates
        self.x  = self.data_coord[:][:,1] # X coordinates
        self.y  = self.data_coord[:][:,2] # Y coordinates
        self.m = self.y.shape[0]

        self.node_1 = self.data_node[:][:,0] # Nodes 1
        self.node_2 = self.data_node[:][:,1] # Nodes 2

        # All lines are bidirectional
        self.node1 = np.append(self.node_1,self.node_2)
        self.node2 = np.append(self.node_2,self.node_1)
        self.n = self.node1.shape[0]

        self.visited = []
        self.previous = {}
        self.distance_ = {}
        self.graph_ = self.graphData()
 

    def inputs(self):
        #=== Get start and end points from user ===

        print('\nChoose start and end point in list belown\n\n',
                [int(i) for i in self.ID], end = '\n\n')
        self.start = int(input('Enter initial point number:'))
        self.end = int(input('Enter end point number:'))
        
        assert self.start in self.ID, "Couldn't find start point"
        assert self.end in self.ID, "Couldn't find end point"
        
        return self.start
    
    
    def plotData(self, sh):
        #=== Plot the data ===

        self.figg = plt.figure(figsize = (10,10))
        plt.scatter(self.y, self.x, c = 'r', s = 8)
        
        # Plot ID of points
        for i,x,y in zip([*range(self.m)], self.x, self.y):
            plt.annotate(int(self.ID[i]), 
                    xy = (y, x),
                    textcoords="offset points",#how to position the text
                    xytext=(0,5),# distance from text to points
                    ha='left')# horizontal alignment
        
        # Draw line between points
        for i,j in zip(self.node1, self.node2):
            
            x1 = self.x[np.where(self.ID == i)]
            y1 = self.y[np.where(self.ID == i)]
            
            x2 = self.x[np.where(self.ID == j)]
            y2 = self.y[np.where(self.ID == j)]
            
            plt.plot((y1,y2), 
                    (x1,x2),
                    color='black',
                    marker = 'o', mfc = 'r',
                    linewidth = 1)
        plt.title("Dijkstra's shortest path algorithm")
        plotX = []
        plotY = []
        
        for i in sh:
            plotX.append(self.x[np.where(self.ID == i)])
            plotY.append(self.y[np.where(self.ID == i)])

        plt.plot(plotY, plotX,'r', lw=4)
        plt.show()


    
    def __length(self):
        #=== Find length between nodes ===
        
        self.distance = []
        
        for k in range(self.n):
            for i in range(self.m):
                if int(self.ID[i]) == int(self.node1[k]):
                    for j in range(self.m):
                        if int(self.ID[j])==int(self.node2[k]):
                            self.delta_x = float(self.x[i]) - float(self.x[j])
                            self.delta_y = float(self.y[i]) - float(self.y[j])
                            length  = math.sqrt((self.delta_x)**2 + (self.delta_y)**2)
                            self.distance.append(round(length,4))

        return self.distance



    def graphData(self):
        #=== Create graph data ===

        self.graph = {}

        # Check if node1 in dict
        def graph(node1,node2,length):
            if node1 not in self.graph:
                self.graph[node1] = {}
                self.graph[node1][node2] = length
            else:
                self.graph[node1].update({node2:length})
        
        for i in range(self.n):
            graph(int(self.node1[i]), int(self.node2[i]), self.__length()[i])
        
        return self.graph




    def dijkstra(self, start):
        #=== Dijkstra's algorithm ===
        
        self.start_ = start
        if (self.start_ != self.end):
            if not self.visited:
                self.distance_[self.start_] = 0

            for i in self.graph_[self.start_]:
                if (i not in self.visited):
                    node_dist = self.distance_[self.start_] + self.graph_[self.start_][i]
                    if (node_dist < self.distance_.get(i, sys.maxsize)):
                        self.distance_[i] = node_dist
                        self.previous[i] = self.start_
            
            self.visited.append(self.start_)
            unvisited = {}

            for i in self.graph_:
                if (i not in self.visited):
                    unvisited[i] = self.distance_.get(i, sys.maxsize)

            # Minimum distance for next node
            self.min = min(unvisited, key=unvisited.get)
            
            # Recursion
            self.dijkstra(self.min)

        else:
            self.sh_path = []
            self.prev = self.end
            
            while (self.prev != None): 
                self.sh_path.append(self.prev)
                self.prev = self.previous.get(self.prev,None)
            self.sh_path = self.sh_path[::-1]
            print('\nshortest path ---> ',self.sh_path, end = '\n\n')
        
            self.plotData(self.sh_path)


if __name__ == '__main__':
    driver_code = shortest_path()
    start_point = driver_code.inputs()
    driver_code.dijkstra(start_point)



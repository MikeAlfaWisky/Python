# -*- coding: utf-8 -*-
"""
Mark Webb
Cecs545
Project 3
09/13/19
Program will solve TSP using greedy heuristic
"""

import matplotlib.pyplot as plt #for plotting the graph
import random #used for randomly selecting starting city

              
         #calculates distance
def distance(x1, y1, x2, y2):
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 #distance formula
    return d

        #extracts x coordinates
def getX(cities):
    x = []                 #creates empty list to store x coordinates
    for city in cities:    #loops through all lines in cities
        row = city.split() #splits each number on a line into a new list
        x.append(row[1])   #adds x coordinate to list 'x'
    return x
         
        #extracts y coordinates   
def getY(cities):
    y = []                 #creates empty list to store y coordinates
    for city in cities:    #loops through all lines in cities
        row = city.split() #splits each number on a line into a new list
        y.append(row[2])   #adds y coordinate to list 'y'
    return y

        #determines shortest route
def findPath(cities, x, y):
    numCities = len(cities) #gets number of cities by taking lenght of list 'cities'
    print("\nNumber of Cities: " + str(numCities))
        
        
    citiesHelper = []          #used for storing "name" of cities still to be visited, i.e.(1,2,3,4...)
    for i in range(numCities): #populates citiesHelper based on total number of cities
        citiesHelper.append(i + 1)
        
    start = random.choice(citiesHelper) #randomly determines starting city
    print("start is:")
    print(start) #prints starting city
    citiesHelper.remove(start) #removes the starting city from citiesHelper
    
    cPath = [start] #adds start to current path
    cCity = start #sets current city to start
    cost = 0 #initializes cost of path to 0
    for i in range(len(cities) - 1): 
        sDistance = 0 #sets the shortest distance between two cities to 0
        for j in range(len(citiesHelper)):
                    #caclulates distance from the current city to each city in remaining in citiesHelper
            cDistance = distance(float(x[cCity - 1]), float(y[cCity - 1]), float(x[citiesHelper[j] - 1]), float(y[citiesHelper[j] - 1]))

            if sDistance == 0: #stores first calculated city as shortest
                sDistance = cDistance
                nextCity = citiesHelper[j]

            elif cDistance < sDistance:
                sDistance = cDistance #if last calculated distance is shortes, stores in sDistance
                nextCity = citiesHelper[j] #stores the current shortes city in nextCity

        cost = cost + sDistance #adds distance to total distance
        cPath.append(nextCity) #adds the next closest city to the current path
        cCity = nextCity #updates the current city traveling from
        citiesHelper.remove(nextCity) #removes last city added to path from list of cities remaining to visit
    cost = cost + distance(float(x[cCity - 1]), float(y[cCity - 1]), float(x[start - 1]), float(y[start - 1])) #adds distance of traveling from final city back to start city
    cPath.append(start) #adds the start city to the end of the route
    
    print("Calculated path is: ")
    print(cPath) #prints the route
    print("With a cost of: " + str(cost)) #prints the total distance of the route
    
    return cPath
  
    
        #plots the path on a graph
def plot_path(x, y, cSR): #plots route into a graph
    plt.plot([float(x[i-1]) for i in cSR], [float(y[i-1]) for i in cSR], 'bo-')
    plt.show()
    
    

def main():
    
    print("Please enter file path for text file")
    file = input()
    #open file with open(), 'with' is used to close file afterwords
    with open(file) as file_object:
        cities = file_object.readlines() #stores each line of file in a list
       
    for _ in range(7): #for loop deletes non coordinates lines from list
        cities.pop(0)
     
    print("     Cities:")
    for line in cities:
        print(line.rstrip())
        
    x = getX(cities)
    y = getY(cities)
    cShortRoute = findPath(cities, x, y)
    plot_path(x,y,cShortRoute)
    
        
       
if __name__ == "__main__":
    main()
    
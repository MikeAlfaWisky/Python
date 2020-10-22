# -*- coding: utf-8 -*-
"""
Mark Webb
Cecs545
Project 1
08/30/19
Program will brute force solve traveling salesperson problem.
"""

import matplotlib.pyplot as plt #for plotting the graph

        
def permute(cities):
    res = []
    permuteHelper(cities, 0, res)
    return res

def permuteHelper(cities, start, res):
    if start >= len(cities):      #determines if permuatation is complete
        res.append(cities[:]) #adds completed permutation to list
        #print(cities)
    else:
        for i in range(start, len(cities)):
            cities[i], cities[start] = cities[start], cities[i] #swaps numbers in list 'nums[]' based on current values of 'i' and 'start'
            permuteHelper(cities, start +1, res)      #recalls function until permutation is complete (start = length of numbers)
            cities[start], cities[i] = cities[i], cities[start]
         
         
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
        
        #unused code for testing
    #print("\nx coordinates")
    #print(x)
    #print("\ny coordinates")
   # print(y)
        #end for testing
        
    citiesHelper = []          #used for storing "name" of cities, i.e.(1,2,3,4...)
    for i in range(numCities): #populates citiesHelper based on total number of cities
        citiesHelper.append(i + 1)
        
    #print("citiesHelper: " + str(citiesHelper)) #unused print for testing
    
    print("Calculating Shortest Route...")
    
    permutations = permute(citiesHelper)    #calculates each permutation and stores them in a list
    cShortDistance = 0                      #initializes current shortest distance to 0
    cShortRoute = permutations[0]           #initializes current shortest route to first route in permutations
    
    for i in range(len(permutations)):
        cRoute = permutations[i]
        totalDistance = 0
        cRoute.append(cRoute[0]) #makes sure route ends at the start
        for j in range(len(cRoute) - 1):
                #calculates distance from one city to another
            cDistance = distance(float(x[cRoute[j]-1]), float(y[cRoute[j]-1]), float(x[cRoute[j+1]-1]), float(y[cRoute[j+1]-1]))
            totalDistance = totalDistance + cDistance #adds distance to running total of distance travelled
        if cShortDistance == 0:              #checks to see if this is the first calculated route
            cShortDistance = totalDistance  #sets current shortest distance to the first calculated distacne
        else:
            if totalDistance < cShortDistance:  #checks to see if the last computed distance/route is the shortest
                cShortDistance = totalDistance  #sets variables for current shortest distacne/route if new route is shorter
                cShortRoute = cRoute
    print("the shortest route is: ")            
    print(cShortRoute)
    print("with a total distance traveled of: ")
    print(cShortDistance)
    
    return cShortRoute
    
        #plots the path on a graph
def plot_path(x, y, cSR): #plots route into a graph
    plt.plot([float(x[i-1]) for i in cSR], [float(y[i-1]) for i in cSR], 'bo-')
    plt.show()
    
    

def main():
    
    print("Please enter path for text file")
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
    

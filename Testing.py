import math

import numpy as np
import scipy
import matplotlib as mp
import matplotlib.pyplot as plt

# CHALLENGE 1

TIMESTEP = 1

def chal1ProjPath(u, theta, g, h, step):

    theta = math.radians(theta)
    time = 0
    
    particleX = 0
    particleY = h
    
    XArray = []
    YArray = []
    
    velocityX = u*math.cos(theta)
    velocityY = u*math.sin(theta)
    
    while particleY > 0:
        particleX = velocityX * time
        particleY = h + velocityY * time - 0.5 * g * time**2
        
        XArray.append(particleX)
        YArray.append(particleY)
        
        time += step
    
    print(XArray)
    print(YArray)
    plt.plot(XArray, YArray)
    plt.show()
    
#chal1projPath(20, 0.7854, 9.81, 2, 0.02)


# CHALLENGE 2

def chal2ProjPath(u, theta, g, h, step):    
    theta = math.radians(theta)
    
    projRange = ((u**2)/g) * (math.sin(theta) * math.cos(theta) + math.cos(theta) * math.sqrt((math.sin(theta))** 2 + (2*g*h)/u**2))
    
    XArray = []
    noPoints = int(1/step)
    for i in range(noPoints):
        XArray.append(projRange*(i/noPoints))
        
    YArray = []
    
    XatYHighest = u**2/(2*g)
    YHighest = h + (XatYHighest * math.tan(theta)) - ((g / (2 * u**2)) * (1 + math.tan(theta)**2) * XatYHighest**2)
    
    
    for i in XArray:
        YArray.append(h + (i * math.tan(theta)) - ((g / (2 * u**2)) * (1 + math.tan(theta)**2) * i**2))
    

    print(XatYHighest)
    print(YHighest)
    
    plt.plot(XatYHighest, YHighest, 'ro') 
    plt.plot(XArray, YArray)
    plt.show()


#chal2ProjPath(10, 42, 9.81, 1, 0.02)


# CHALLENGE 3

def chal3ProjPath(u, g, h, step, X, Y):    
    
    
    # mingraph
    minu = math.sqrt(g) * math.sqrt(Y + math.sqrt(X**2 + Y **2))
    theta = math.atan((Y + math.sqrt(X**2 + Y**2))/X)
    
    XArray = []
    noPoints = int(1/step)
    for i in range(noPoints):
        XArray.append(X*(i/noPoints))
        
    YArray = []
    for i in XArray:
        YArray.append(h + (i * math.tan(theta)) - ((g / (2 * minu**2)) * (1 + math.tan(theta)**2) * i**2))
    
    
    plt.plot(XArray, YArray, color="grey")
    
    # max and min bounding graphs
    a = g / (2 * u**2) * X**2
    b = -X
    c = Y - h + ((g * X**2) / (2 * u**2))
    
    thetaMax = math.atan((-b + math.sqrt(b**2 - 4*a*c))/(2*a))
    thetaMin = math.atan((-b - math.sqrt(b**2 - 4*a*c))/(2*a))
    
    print(thetaMax)
    print(thetaMin)
    
    # max display
    XArray = []
    noPoints = int(1/step)
    for i in range(noPoints):
        XArray.append(X*(i/noPoints))
        
    YArray = []
    for i in XArray:
        YArray.append(h + (i * math.tan(thetaMax)) - ((g / (2 * u**2)) * (1 + math.tan(thetaMax)**2) * i**2))
    
    
    plt.plot(XArray, YArray, color="blue")
    
    # min display
    XArray = []
    noPoints = int(1/step)
    for i in range(noPoints):
        XArray.append(X*(i/noPoints))
        
    YArray = []
    for i in XArray:
        YArray.append(h + (i * math.tan(thetaMin)) - ((g / (2 * u**2)) * (1 + math.tan(thetaMin)**2) * i**2))
    
    
    plt.plot(XArray, YArray, color="orange")
    plt.plot(X, Y, 'yo') 
    plt.show()
    
    


#chal3ProjPath(150, 9.81, 0, 0.01, 1000, 300)
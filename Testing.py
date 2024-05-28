import math
import numpy as np
import scipy
import matplotlib as mp
import matplotlib.pyplot as plt

# PLOT LINE

def plot(x, y, colour, x_label, y_label, title, start_at_origin):
    plt.plot(x, y, color=colour)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    if start_at_origin:
        plt.xlim(xmin=0)
        plt.ylim(ymin=0)
    plt.show()


# CHALLENGE 1: Simple model of drag-free projectile motion

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
    
    plot(XArray, YArray, "blue", "x /m", "y /m", "Challenge 1: Projectile motion model", True)
    
# chal1ProjPath(20, 45, 9.81, 2, 0.02)


# CHALLENGE 2: More sophisticated exact ('analytic') model

def chal2ProjPath(u, theta, g, h, step):    
    theta = math.radians(theta)
    projRange = ((u**2)/g) * (math.sin(theta) * math.cos(theta) + math.cos(theta) * math.sqrt((math.sin(theta))** 2 + (2*g*h)/u**2))
    
    XArray = []
    noPoints = int(1/step)
    for i in range(noPoints):
        XArray.append(projRange*(i/noPoints))
        
    XatYHighest = u**2/(2*g)
    YHighest = h + (XatYHighest * math.tan(theta)) - ((g / (2 * u**2)) * (1 + math.tan(theta)**2) * XatYHighest**2)
    
    YArray = []
    for i in XArray:
        YArray.append(h + (i * math.tan(theta)) - ((g / (2 * u**2)) * (1 + math.tan(theta)**2) * i**2))
    
    plt.plot(XatYHighest, YHighest, "ro")
    plt.text(XatYHighest, YHighest, "apogee")
    plot(XArray, YArray, "blue", "x /m", "y /m", "Challenge 2: Projectile motion model", True)

# chal2ProjPath(10, 42, 9.81, 1, 0.02)


# CHALLENGE 3: Minimum launch speed, low ball trajectory, and high ball trajectory passing through a fixed point

def chal3ProjPath(u, g, h, step, X, Y):    
    
    # min graph
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
    
    plt.plot(X, Y, "yo")
    plt.text(X, Y, "target")
    plot(XArray, YArray, "orange", "x /m", "y /m", "Challenge 3: Projectile to hit X,Y", True)
    
# chal3ProjPath(150, 9.81, 0, 0.01, 1000, 300)

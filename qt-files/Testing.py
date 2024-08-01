import math
import numpy as np
import scipy
import matplotlib as mp
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator

# PLOT LINE

def plot(plotFrame, x, y, colour, x_label, y_label, title, start_at_origin, graphLabel = None):
    plotFrame.plot(x, y, color=colour, label = graphLabel)
    
    plotFrame.axes.set_xlabel(x_label)
    plotFrame.axes.set_ylabel(y_label)
    plotFrame.set_title(title)
    
    if graphLabel:
        return
        #plotFrame.legend()

    if start_at_origin:
        return
        #plotFrame.xlim(xmin=0)
        #plotFrame.ylim(ymin=0)
        
    #plt.show(block=False)



# CHALLENGE 1: Simple model of drag-free projectile motion

TIMESTEP = 1

def chal1ProjPath(plotFrame, u, theta, g, h, step):

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
    
    plot(plotFrame, XArray, YArray, "blue", "x /m", "y /m", "Challenge 1: Projectile motion model", True)
    
# chal1ProjPath(20, 45, 9.81, 2, 0.02)



# CHALLENGE 2: More sophisticated exact ('analytic') model

def chal2ProjPath(plotFrame, u, theta, g, h, step):    
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
    plot(plotFrame, XArray, YArray, "blue", "x /m", "y /m", "Challenge 2: Projectile motion model", True)

# chal2ProjPath(10, 42, 9.81, 1, 0.02)



# CHALLENGE 3: Minimum launch speed, low ball trajectory, and high ball trajectory passing through a fixed point

def chal3ProjPath(plotFrame, u, g, h, step, X, Y):    
    
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
    plot(plotFrame, XArray, YArray, "orange", "x /m", "y /m", "Challenge 3: Projectile to hit X,Y", True)
    
# chal3ProjPath(150, 9.81, 0, 0.01, 1000, 300)



# CHALLENGE 4: Comparing trajectory to trajectory maximising range given same launch height and launch speed
def chal4ProjPath(plotFrame, u, h, g, theta):
    
    theta = math.radians(theta)
    # max_r = (u**2 / g) * math.sqrt(1 + ((2 * g * h) / u**2))
    max_theta = math.asin(1 / math.sqrt(2 + 2 * ((g * h) / u**2)))
    
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
        
        time += 0.01
    
    plt.plot(XArray, YArray, "b")
    
    #Run 2
    time = 0
    particleX = 0
    particleY = h
    
    XArray = []
    YArray = []
    
    velocityX = u*math.cos(max_theta)
    velocityY = u*math.sin(max_theta)
    
    while particleY >= 0:
        particleX = velocityX * time
        particleY = h + velocityY * time - 0.5 * g * time**2
        
        XArray.append(particleX)
        YArray.append(particleY)
        
        time += 0.01
    plot(plotFrame, XArray, YArray, "r", "x /m", "y /m", "Challenge 4: Trajectory compared with maximised horizontal range", True)   

# chal4ProjPath(10, 2, 9.81, 60)



# CHALLENGE 5: Bounding parabola
def chal5ProjPath(u, g, h, X, Y):
    # Min u graph
    minu = math.sqrt(g) * math.sqrt(Y + math.sqrt(X**2 + Y **2))
    theta = math.atan((Y + math.sqrt(X**2 + Y**2))/X)
    max_theta = math.asin(1 / math.sqrt(2 + 2 * ((g * h) / u**2)))
    
    time = 0 
    
    particleX = 0
    particleY = h
    
    XArray = []
    YArray = []
    
    velocityX = u*math.cos(theta)
    velocityY = u*math.sin(theta)
    
    while particleY >= 0:
        particleX = velocityX * time
        particleY = h + (particleX * math.tan(theta)) - ((g / (2 * minu**2)) * (1 + math.tan(theta)**2) * particleX**2)
        
        XArray.append(particleX)
        YArray.append(particleY)
        
        time += 0.01  
    
    plt.plot(XArray, YArray, color="grey")
    
    # High and low graphs
    a = g / (2 * u**2) * X**2
    b = -X
    c = Y - h + ((g * X**2) / (2 * u**2))
    
    thetaMax = math.atan((-b + math.sqrt(b**2 - 4*a*c))/(2*a))
    thetaMin = math.atan((-b - math.sqrt(b**2 - 4*a*c))/(2*a))
    
    # Display max
    time = 0
    particleX = 0
    particleY = h
    
    XArray = []
    YArray = []
    
    velocityX = u*math.cos(theta)
    velocityY = u*math.sin(theta)
    
    while particleY >= 0:
        particleX = velocityX * time
        particleY = h + (particleX * math.tan(thetaMax)) - ((g / (2 * u**2)) * (1 + math.tan(thetaMax)**2) * particleX**2)
        
        XArray.append(particleX)
        YArray.append(particleY)
        
        time += 0.01  
    
    plt.plot(XArray, YArray, color="blue")
    
    # Max range
    time = 0
    particleX = 0
    particleY = h
    
    XArray = []
    YArray = []
    
    velocityX = u*math.cos(max_theta)
    velocityY = u*math.sin(max_theta)
    
    while particleY >= 0:
        particleX = velocityX * time
        particleY = h + velocityY * time - 0.5 * g * time**2
        
        XArray.append(particleX)
        YArray.append(particleY)
        
        time += 0.01
    plt.plot(XArray, YArray, color="red")  
    
    # Bounding parabola
    time = 0
    particleX = 0
    particleY = h
    
    XArray = []
    YArray = []
    
    while particleY >= 0:
        particleX = velocityX * time
        particleY = (u**2)/(2*g) - ((g)/(2 * (u ** 2)))*(particleX**2)
        
        XArray.append(particleX)
        YArray.append(particleY)
        
        time += 0.01
    plt.plot(XArray, YArray, color="pink")
    

    # Display low
    time = 0
    particleX = 0
    particleY = h
    
    XArray = []
    YArray = []
    
    velocityX = u*math.cos(theta)
    velocityY = u*math.sin(theta)
    
    while particleY >= 0:
        particleX = velocityX * time
        particleY = h + (particleX * math.tan(thetaMin)) - ((g / (2 * u**2)) * (1 + math.tan(thetaMin)**2) * particleX**2)
        
        XArray.append(particleX)
        YArray.append(particleY)
        
        time += 0.01  

    plt.plot(X, Y, "ro")
    
    plot(XArray, YArray, "orange", "x /m", "y /m", "Challenge 5: Bounding parabola", True)

# chal5ProjPath(1.3063*115, 9.81, 0, 1000, 300)



# CHALLENGE 6: Distance travelled by projectile

# Calculate distance
def chal6CalcDist(u, h, g, theta):
    higher_bound_int = 0.5*math.log(math.sqrt(1 + math.tan(theta)**2) + math.tan(theta)) + 0.5 * math.tan(theta) * math.sqrt(1 + math.tan(theta) ** 2)
    
    projRange = ((u**2)/g) * (math.sin(theta) * math.cos(theta) + math.cos(theta) * math.sqrt((math.sin(theta))** 2 + (2*g*h)/u**2))
    
    intpart2 = (math.tan(theta) - ((g * projRange)/(u**2))*(1 + math.tan(theta)**2))
    lower_bound_int = 0.5*math.log(math.sqrt(1 + intpart2**2) + intpart2) + 0.5 * intpart2 * math.sqrt(1 + intpart2 ** 2)

    s = (u**2)/(g * (1 + math.tan(theta)**2)) * (higher_bound_int - lower_bound_int)
    return s

def chal6ProjPath(u, h, g, theta):
    theta = math.radians(theta)
    max_theta = math.asin(1 / math.sqrt(2 + 2 * ((g * h) / u**2)))
    
    s = chal6CalcDist(u, h, g, theta)
    s_max = chal6CalcDist(u, h, g, max_theta)
    
    # Calculate s
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
        
        time += 0.01
    
    plt.plot(XArray, YArray, "b", label = "s: " + str(round(s, 2)))
    
    # Calculate s_max
    time = 0
    particleX = 0
    particleY = h
    
    XArray = []
    YArray = []
    
    velocityX = u*math.cos(max_theta)
    velocityY = u*math.sin(max_theta)
    
    while particleY >= 0:
        particleX = velocityX * time
        particleY = h + velocityY * time - 0.5 * g * time**2
        
        XArray.append(particleX)
        YArray.append(particleY)
        
        time += 0.01

    plt.plot(XArray, YArray, "r")

    plot(XArray, YArray, "r", "x /m", "y /m", "Challenge 6: Distance travelled by projectile", True, "s_max: " + str(round(s_max, 2)))

#chal6ProjPath(10, 2, 9.81, 60)



# CHALLENGE 7: Local maxima and minima data

def chal7ProjPath(u, g):
    # Right graph
    thetas = [30, 45, 60, 70.5, 78, 85]
    colours = ["blue", "green", "red", "cyan", "purple", "yellow"]
    ranges = []
    
    for thetaID in range(len(thetas)):
        theta = math.radians(thetas[thetaID])
        projRange = ((u**2)/g) * (math.sin(theta) * math.cos(theta) + math.cos(theta) * math.sqrt((math.sin(theta))** 2 + (2*g*5)/u**2))
        ranges.append(projRange)
    
    
    
    for thetaID in range(len(thetas)):

        theta = math.radians(thetas[thetaID])
        colour = colours[thetaID]
        time = 0
        
        particleX = 0
        particleY = 0
        
        XArray = []
        YArray = []
        
        velocityX = u*math.cos(theta)
        velocityY = u*math.sin(theta)
        
        while particleY >= -5:
            particleX = velocityX * time
            particleY = 0 + velocityY * time - 0.5 * g * time**2
            
            XArray.append(particleX)
            YArray.append(particleY)
            
            time += 0.01

        plt.subplot(1, 2, 1)
        plt.title("Challenge 7: y against x for different θ")
        plt.plot(XArray, YArray, color = colour)
        
        if theta >= math.radians(70.5):
            if theta == math.radians(70.5):
                T = ((u/g)) * math.sqrt(2)
                X = u * math.cos(theta) * T
                Y = 0 + (X * math.tan(theta)) - ((g / (2 * u**2)) * (1 + math.tan(theta)**2) * X**2)
                plt.plot(X, Y, "ro")
            else:
                T = ((3 * u)/(2 * g)) * (math.sin(theta) + math.sqrt(math.sin(theta)**2 - (8/9)))
                X = u * math.cos(theta) * T
                Y = 0 + (X * math.tan(theta)) - ((g / (2 * u**2)) * (1 + math.tan(theta)**2) * X**2)
                plt.plot(X, Y, "ro")
                
                T = ((3 * u)/(2 * g))*(math.sin(theta)-math.sqrt(math.sin(theta)**2 - (8/9)))
                X = u * math.cos(theta) * T
                Y = 0 + (X * math.tan(theta)) - ((g / (2 * u**2)) * (1 + math.tan(theta)**2) * X**2)
                plt.plot(X, Y, "go")
    
    # Left graph
    for thetaID in range(len(thetas)):
        theta = math.radians(thetas[thetaID])
        colour = colours[thetaID]
        
        particleX = 0
        particleY = 0
        
        XArray = []
        YArray = []
        
        while particleX <= 2.5:
            particleY = math.sqrt(u**2 * particleX**2 - g * particleX**3 * u * math.sin(theta) + 0.25 * g**2 * particleX ** 4)
            
            XArray.append(particleX)
            YArray.append(particleY)
            particleX += 0.01
        
        plt.subplot(1, 2, 2)
        plt.title("Challenge 7: range against time for different θ")
        plt.plot(XArray, YArray, colour)
        
        if theta >= math.radians(70.5):
            if theta == math.radians(70.5):
                X = ((u/g)) * math.sqrt(2)
                Y = math.sqrt(u**2 * X**2 - g * X**3 * u * math.sin(theta) + 0.25 * g**2 * X ** 4)
                plt.plot(X, Y, "ro")
            else:
                X = ((3 * u)/(2 * g)) * (math.sin(theta) + math.sqrt(math.sin(theta)**2 - (8/9)))
                Y = math.sqrt(u**2 * X**2 - g * X**3 * u * math.sin(theta) + 0.25 * g**2 * X ** 4)
                plt.plot(X, Y, "ro")
                
                X = ((3 * u)/(2 * g))*(math.sin(theta)-math.sqrt(math.sin(theta)**2 - (8/9)))
                Y = math.sqrt(u**2 * X**2 - g * X**3 * u * math.sin(theta) + 0.25 * g**2 * X ** 4)
                plt.plot(X, Y, "go")
    plt.show()
#chal7ProjPath(10, 10)


# CHALLENGE 8 - Bouncing ball
def chal8ProjPath(u, C, theta, h, g, maxBounces, timeStep):
    theta = math.radians(theta)
    YVelocity = u * math.sin(theta)
    XVelocity = u * math.cos(theta)
    
    XArray = []
    YArray = []
    
    bounceCount = 0
    currentIndex = 0 
    
    XArray.append(0)
    YArray.append(h)
    
    while bounceCount <= maxBounces:
        XAcceleration = 0 
        YAcceleration = -g
        XArray.append(XArray[currentIndex] + XVelocity * timeStep + 0.5 * XAcceleration * timeStep**2)
        YArray.append(YArray[currentIndex] + YVelocity * timeStep + 0.5 * YAcceleration * timeStep**2)
        
        YVelocity = YVelocity + (YAcceleration) * timeStep
        
        if YArray[currentIndex + 1] < 0:
            YArray[currentIndex + 1] = 0
            YVelocity = -C * YVelocity
            bounceCount += 1
            
        
        plot(XArray, YArray, "red", "x /m", "y /m", "Challenge 8: Bounding parabola", True)
        
        plt.close()
        currentIndex += 1
    
#chal8ProjPath(5, 0.7, 45, 10, 9.81, 6, 0.02)

# Challenge 9 - drag-free model 

def chal9ProjPath(theta, u, h, g, D, CSA, dA, M, timeStep):
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
        
        time += timeStep
        
    plt.plot(XArray, YArray, color = "blue")
    
    
    particleX = 0
    particleY = h
    
    XArray = []
    YArray = []
    
    velocityX = u*math.cos(theta)
    velocityY = u*math.sin(theta)
    
    k = 10* (0.5 * D * dA * CSA) / M
    print(k)
    
    while particleY > 0:
        
        AccelerationX = -(velocityX) * k * (math.sqrt(velocityX**2 + velocityY **2)) 
        AccelerationY = -(velocityY) * k * (math.sqrt(velocityX**2 + velocityY **2)) - g
        
        particleX += velocityX * timeStep + 0.5 * AccelerationX * timeStep**2
        particleY += velocityY * timeStep + 0.5 * AccelerationY * timeStep**2
        
        velocityX += AccelerationX * timeStep
        velocityY += AccelerationY * timeStep
        
        XArray.append(particleX)
        YArray.append(particleY)
    
    plt.plot(XArray, YArray, color = "red")
    plt.show()
    
    
#chal9ProjPath(30, 20, 2, 9.81, 0.3, 0.007854, 1, 0.1, 0.01)

def plt_sphere():
    ax = fig.add_subplot(projection='3d')
    
    # draw sphere
    theta, phi = np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi, 40)
    THETA, PHI = np.meshgrid(theta, phi)
    R = 6371000
    X = R * np.sin(THETA) * np.cos(PHI)
    Y = R * np.sin(THETA) * np.sin(PHI)
    Z = R * np.cos(THETA)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),linewidth=0, antialiased=False, alpha=0.5)
    
    #Start of calculations
    
    time = 0
    timestep = 150
    
    u = 5110
    orbitTime = 5000
    orbitSpeed = (6371000 * 2 * math.pi)/orbitTime
    orbitDistance = 6371000 * 2 * math.pi
    turningSpeed = (timestep/(orbitDistance/orbitSpeed)) * 2 * math.pi
    
    theta = math.pi/2
    phi = math.pi/2
    XArray = []
    YArray = []
    ZArray = []
    timeArray = []
    
    h = 6371000
    mass = 5
    
    while time < 30000:
        AccelerationH = -((6.67*(10**-11)*5.972*(10**24))/(h**2))/mass
        h += u * timestep + 0.5 * AccelerationH * timestep**2
        u += AccelerationH * timestep
        
        turningSpeed = (timestep/((h * 2 * math.pi)/orbitSpeed)) * 2 * math.pi
        theta += turningSpeed
    
        if h < 6371000:
            print("bang")
            break
        
        XArray.append(h * math.sin(theta) * math.cos(phi))
        YArray.append(h * math.sin(theta) * math.sin(phi))
        ZArray.append(h * math.cos(theta))
        
        timeArray.append(time)
        time += 0.5
    ax.scatter3D(XArray, YArray, ZArray, c = (timeArray), cmap = "Greens")
    plt.show()
fig = plt.figure()
#plt_sphere() 

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Plot the graph
def plot(plotFrame, x, y, colour, x_label, y_label, title, graphLabel = None, xlim = 0, ylim = 0):
    plotFrame.plot(x, y, color=colour, label = graphLabel)
    plotFrame.axes.set_xlabel(x_label)
    plotFrame.axes.set_ylabel(y_label)
    plotFrame.axes.spines['top'].set_visible(False)
    plotFrame.axes.spines['right'].set_visible(False)
    plotFrame.axes.grid(True)
    plotFrame.set_title(title)
    plotFrame.axes.set_xlim(left=xlim)
    plotFrame.axes.set_ylim(bottom=ylim)
        

# Challenge 1
def challenge1Path(plotFrame, u, theta, g, h, step):
    theta = math.radians(theta)
    time = 0
    particleX = 0
    particleY = h
    landed = False
    first_run_through = True
    
    XArray = []
    YArray = []
    
    velocityX = u*math.cos(theta)
    velocityY = u*math.sin(theta)
    
    while not landed:
        particleX = velocityX * time
        particleY = h + (velocityY * time) - (0.5 * g * time**2)
        XArray.append(particleX)
        YArray.append(particleY)
        time += (step / 1000)

        if particleY <= 0 and not first_run_through:
            landed = True

        first_run_through = False
    
    plot(plotFrame, XArray, YArray, "blue", "x /m", "y /m", "Simple Model of Projectile Motion\n", True)


# Challenge 2
def challenge2Path(plotFrame, u, theta, g, h, step):    
    try:
        theta = math.radians(theta)
        step /= 1000
        projRange = ((u**2)/g) * (math.sin(theta) * math.cos(theta) + math.cos(theta) * math.sqrt((math.sin(theta)) ** 2 + (2 * g * h)/u ** 2))
        
        XArray = []
        noPoints = int(1/step)
        for i in range(noPoints):
            XArray.append(projRange*(i/noPoints))
            
        XatYHighest = (u ** 2 / g) * math.sin(theta) * math.cos(theta)
        YHighest = h + ((u ** 2) / (2 * g)) * (math.sin(theta)) ** 2
        
        YArray = []
        for i in XArray:
            YArray.append(h + (i * math.tan(theta)) - ((g / (2 * u**2)) * (1 + math.tan(theta)**2) * i**2))
        
        flight_time = projRange / (u * math.cos(theta))
        
        try:
            plotFrame.plot(XatYHighest, YHighest, "ro", label="Apogee")
            plotFrame.legend()
            plot(plotFrame, XArray, YArray, "blue", "x /m", "y /m", "Analytic Model of Projectile Motion\n", True)
        except:
            return [projRange, XatYHighest, YHighest, flight_time]

    except:
        plot(plotFrame, [0], [0], "blue", "x /m", "y /m", "Analytic Model of Projectile Motion\n", True)


# Challenge 3
def challenge3Path(plotFrame, u, g, h, step, X, Y):    
    try:
        # min graph
        step /= 1000
        minu = math.sqrt(g) * math.sqrt((Y-h) + math.sqrt(X**2 + (Y-h) **2))
        theta = math.atan(((Y-h) + math.sqrt(X**2 + (Y-h)**2))/X)
        
        MinGraphXArray = []
        noPoints = int(1/step)
        for i in range(noPoints):
            MinGraphXArray.append(X*(i/noPoints))
            
        MinGraphYArray = []
        for i in MinGraphXArray:
            MinGraphYArray.append(h + (i * math.tan(theta)) - ((g / (2 * minu**2)) * (1 + (math.tan(theta))**2) * i**2))
        
        # max and min bounding graphs
        a = g / (2 * u**2) * X**2
        b = -X
        c = Y - h + ((g * X**2) / (2 * u**2))
        
        thetaMax = math.atan((-b + math.sqrt(b**2 - 4*a*c))/(2*a))
        thetaMin = math.atan((-b - math.sqrt(b**2 - 4*a*c))/(2*a))
        
        # max display
        MaxXArray = []
        noPoints = int(1/step)
        for i in range(noPoints):
            MaxXArray.append(X*(i/noPoints))
            
        MaxYArray = []
        for i in MaxXArray:
            MaxYArray.append(h + (i * math.tan(thetaMax)) - ((g / (2 * u**2)) * (1 + math.tan(thetaMax)**2) * i**2))
        
        # min display
        XArray = []
        noPoints = int(1/step)
        for i in range(noPoints):
            XArray.append(X*(i/noPoints))
            
        YArray = []
        for i in XArray:
            YArray.append(h + (i * math.tan(thetaMin)) - ((g / (2 * u**2)) * (1 + math.tan(thetaMin)**2) * i**2))
        
        minuFlightTime = X / (u * math.cos(theta))
        maxFlightTime = X / (u * math.cos(thetaMax))
        minFlightTime = X / (u * math.cos(thetaMin))
        
        try:
            plotFrame.plot(MaxXArray, MaxYArray, color="blue", label="High Ball")
            plotFrame.plot(XArray, YArray, color="orangered", label="Low Ball")
            plotFrame.plot(MinGraphXArray, MinGraphYArray, color="grey", label="Min. Launch Speed")
            plotFrame.plot(X, Y, "go", label="Target")
            plotFrame.legend()
            plot(plotFrame, [0], [0], "orangered", "x /m", "y /m", "High Ball, Low Ball, and Minimum Launch Speed Trajectories to Target (X,Y)\n", True)
        except Exception as error:
            return [minu, theta, theta * (180/math.pi), minuFlightTime, thetaMax, thetaMax * (180/math.pi), maxFlightTime, thetaMin, thetaMin * (180/math.pi), minFlightTime]
    except Exception as error:
        plot(plotFrame, [0], [0], "orangered", "x /m", "y /m", "High Ball, Low Ball, and Minimum Launch Speed Trajectories to Target (X,Y)\n", True)


# Challenge 4
def challenge4Path(plotFrame, u, theta, g, h, step):
    step /= 1000
    theta = math.radians(theta)
    max_theta = math.asin(1 / math.sqrt(2 + 2 * ((g * h) / u**2)))

    time = 0

    particleX = 0
    particleY = h

    RegularXArray = []
    RegularYArray = []

    velocityX = u*math.cos(theta)
    velocityY = u*math.sin(theta)

    while particleY > 0:
        particleX = velocityX * time
        particleY = h + velocityY * time - 0.5 * g * time**2

        RegularXArray.append(particleX)
        RegularYArray.append(particleY)

        time += step
    try:
        plt.plot(XArray, YArray, "b")
    except:
        pass

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

        time += step
    
    regular_range = (u**2 / g) * (math.sin(theta) * math.cos(theta) + math.cos(theta) * math.sqrt((math.sin(theta)**2 + (2 * g * h)/u ** 2)))
    regular_apogee_x = (u ** 2) / g * math.sin(theta) * math.cos(theta)
    regular_apogee_y = h + ((u**2) / (2 * g) * (math.sin(theta) ** 2))
    regular_flight_time = regular_range / (u * math.cos(theta)) 
    maximised_horizontal_range = (u**2 / g) * (math.sin(max_theta) * math.cos(max_theta) + math.cos(max_theta) * math.sqrt((math.sin(max_theta)**2 + (2 * g * h)/u ** 2)))
    maximised_horzontal_apogee_x = (u ** 2) / g * math.sin(max_theta) * math.cos(max_theta)
    maximised_horizontal_apogee_y = h + ((u**2) / (2 * g) * (math.sin(max_theta) ** 2))
    maximised_horizontal_flight_time = regular_range / (u * math.cos(max_theta)) 

    try:
        plotFrame.plot(RegularXArray, RegularYArray, "b", label="Regular")
        plotFrame.plot(XArray, YArray, "r", label="Max Horizontal Range")
        plotFrame.plot(regular_apogee_x, regular_apogee_y, "bo", label="Regular Apogee")
        plotFrame.plot(maximised_horzontal_apogee_x, maximised_horizontal_apogee_y, "ro", label="Max Hori. Range Apogee")
        plotFrame.legend()
        plot(plotFrame, [0], [0], "r", "x /m", "y /m", "Regular Trajectory and Trajectory Maximising Horizontal Range\nwith Same Launch Speed and Launch Height", True)   
    except:
        return [regular_range,
                regular_apogee_x,
                regular_apogee_y,
                regular_flight_time,
                maximised_horizontal_range,
                maximised_horzontal_apogee_x,
                maximised_horizontal_apogee_y,
                maximised_horizontal_flight_time]
    

# Challenge 5
def challenge5Path(plotFrame, u, g, h, step, X, Y):
    step /= 1000

    # Min u graph
    minu = math.sqrt(g) * math.sqrt(Y + math.sqrt(X**2 + Y **2))
    theta = math.atan((Y + math.sqrt(X**2 + Y**2))/X)
    max_theta = math.asin(1 / math.sqrt(2 + 2 * ((g * h) / u**2)))

    time = 0 

    particleX = 0
    particleY = h

    XArray_minu = []
    YArray_minu = []

    velocityX = u*math.cos(theta)
    velocityY = u*math.sin(theta)

    while particleY >= 0:
        particleX = velocityX * time
        particleY = h + (particleX * math.tan(theta)) - ((g / (2 * minu**2)) * (1 + math.tan(theta)**2) * particleX**2)

        XArray_minu.append(particleX)
        YArray_minu.append(particleY)

        time += step 

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

    XArray_max = []
    YArray_max = []

    velocityX = u*math.cos(theta)
    velocityY = u*math.sin(theta)

    while particleY >= 0:
        particleX = velocityX * time
        particleY = h + (particleX * math.tan(thetaMax)) - ((g / (2 * u**2)) * (1 + math.tan(thetaMax)**2) * particleX**2)

        XArray_max.append(particleX)
        YArray_max.append(particleY)

        time += step

    # Max range
    time = 0
    particleX = 0
    particleY = h

    XArray_maxrange = []
    YArray_maxrange = []

    velocityX = u*math.cos(max_theta)
    velocityY = u*math.sin(max_theta)

    while particleY >= 0:
        particleX = velocityX * time
        particleY = h + velocityY * time - 0.5 * g * time**2

        XArray_maxrange.append(particleX)
        YArray_maxrange.append(particleY)

        time += step 

    # Bounding parabola
    time = 0
    particleX = 0
    particleY = h

    XArray_bounding = []
    YArray_bounding = []

    while particleY >= 0:
        particleX = velocityX * time
        particleY = h + (u**2)/(2*g) - ((g)/(2 * (u ** 2)))*(particleX**2)

        XArray_bounding.append(particleX)
        YArray_bounding.append(particleY)

        time += step

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

        time += step
    try:
        plotFrame.plot(XArray_minu, YArray_minu, color="grey", label="Min. Launch Speed")
        plotFrame.plot(XArray_max, YArray_max, color="blue", label="High")
        plotFrame.plot(XArray, YArray, color="orange", label="Low")
        plotFrame.plot(XArray_bounding, YArray_bounding, color="pink", label="Bounding")
        plotFrame.plot(XArray_maxrange, YArray_maxrange, color="red", label="Max Hori. Range")
        plotFrame.plot(X, Y, "ro", label="Fixed Point")
        plotFrame.legend()
        plot(plotFrame, [0], [0], "orange", "x /m", "y /m", "Trajectory Through (X,Y) with Bounding Parabola", True)
    except:
        pass


# Challenge 6

# Calculate distance
def chal6CalcDist(u, h, g, theta):
    higher_bound_int = 0.5*math.log(math.sqrt(1 + math.tan(theta)**2) + math.tan(theta)) + 0.5 * math.tan(theta) * math.sqrt(1 + math.tan(theta) ** 2)
    
    projRange = ((u**2)/g) * (math.sin(theta) * math.cos(theta) + math.cos(theta) * math.sqrt((math.sin(theta))** 2 + (2*g*h)/u**2))
    
    intpart2 = (math.tan(theta) - ((g * projRange)/(u**2))*(1 + math.tan(theta)**2))
    lower_bound_int = 0.5*math.log(math.sqrt(1 + intpart2**2) + intpart2) + 0.5 * intpart2 * math.sqrt(1 + intpart2 ** 2)

    s = (u**2)/(g * (1 + math.tan(theta)**2)) * (higher_bound_int - lower_bound_int)
    return s


# Path
def challenge6Path(plotFrame, u, theta, g, h, step):
    step /= 1000
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
        
        time += step
    
    # Calculate s_max
    time = 0
    particleX = 0
    particleY = h
    
    XArray_smax = []
    YArray_smax = []
    
    velocityX = u*math.cos(max_theta)
    velocityY = u*math.sin(max_theta)
    
    while particleY >= 0:
        particleX = velocityX * time
        particleY = h + velocityY * time - 0.5 * g * time**2
        
        XArray_smax.append(particleX)
        YArray_smax.append(particleY)
        
        time += step
    
    regular_range = (u**2 / g) * (math.sin(theta) * math.cos(theta) + math.cos(theta) * math.sqrt((math.sin(theta)**2 + (2 * g * h)/u ** 2)))
    regular_apogee_x = (u ** 2) / g * math.sin(theta) * math.cos(theta)
    regular_apogee_y = h + ((u**2) / (2 * g) * (math.sin(theta) ** 2))
    regular_flight_time = regular_range / (u * math.cos(theta)) 
    maximised_horizontal_range = (u**2 / g) * (math.sin(max_theta) * math.cos(max_theta) + math.cos(max_theta) * math.sqrt((math.sin(max_theta)**2 + (2 * g * h)/u ** 2)))
    maximised_horzontal_apogee_x = (u ** 2) / g * math.sin(max_theta) * math.cos(max_theta)
    maximised_horizontal_apogee_y = h + ((u**2) / (2 * g) * (math.sin(max_theta) ** 2))
    maximised_horizontal_flight_time = regular_range / (u * math.cos(max_theta)) 

    try:
        plotFrame.plot(XArray, YArray, "b", label="Regular")
        plotFrame.plot(XArray_smax, YArray_smax, "r", label="Max Horizontal Range")
        plotFrame.plot(regular_apogee_x, regular_apogee_y, "bo", label="Regular Apogee")
        plotFrame.plot(maximised_horzontal_apogee_x, maximised_horizontal_apogee_y, "ro", label="Max Hori. Range Apogee")
        plotFrame.legend()
        plot(plotFrame, [0], [0], "r", "x /m", "y /m", "Regular Trajectory and Trajectory Maximising Horizontal Range\nwith Same Launch Speed and Launch Height", True)   
    except:
        return [regular_range,
                regular_apogee_x,
                regular_apogee_y,
                regular_flight_time,
                maximised_horizontal_range,
                maximised_horzontal_apogee_x,
                maximised_horizontal_apogee_y,
                maximised_horizontal_flight_time,
                s,
                s_max]


# Challenge 7
def challenge7PathLeft(plotFrame, u, g, step):
    step /= 1000
    
    # Right graph
    thetas = [30, 45, 60, 70.5, 78, 85]
    colours = ["blue", "green", "red", "cyan", "purple", "gold"]
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
            
            time += step

        plotFrame.plot(XArray, YArray, color = colour)

        if theta >= math.radians(math.asin((2 * math.sqrt(2))/3)):
            try:
                if theta == math.radians(70.5):
                    T = ((u/g)) * math.sqrt(2)
                    X = u * math.cos(theta) * T
                    Y = 0 + (X * math.tan(theta)) - ((g / (2 * u**2)) * (1 + math.tan(theta)**2) * X**2)
                    plotFrame.plot(X, Y, "ro")

                else:
                    T = ((3 * u)/(2 * g)) * (math.sin(theta) + math.sqrt((math.sin(theta))**2 - (8/9)))
                    X = u * math.cos(theta) * T
                    Y = 0 + (X * math.tan(theta)) - ((g / (2 * u**2)) * (1 + math.tan(theta)**2) * X**2)
                    plotFrame.plot(X, Y, "ro")
                    
                    T = ((3 * u)/(2 * g))*(math.sin(theta)-math.sqrt(math.sin(theta)**2 - (8/9)))
                    X = u * math.cos(theta) * T
                    Y = 0 + (X * math.tan(theta)) - ((g / (2 * u**2)) * (1 + math.tan(theta)**2) * X**2)
                    plotFrame.plot(X, Y, "go")
            except Exception as error:
                # print(error)
                pass

        legend = [Line2D([0], [0], linestyle="-", color="blue", label="θ = 30°"),
            Line2D([0], [0], linestyle="-", color="green", label="θ = 45°"),
            Line2D([0], [0], linestyle="-", color="red", label="θ = 60°"),
            Line2D([0], [0], linestyle="-", color="cyan", label="θ = 70.5°"),
            Line2D([0], [0], linestyle="-", color="purple", label="θ = 78°"),
            Line2D([0], [0], linestyle="-", color="gold", label="θ = 85°"),
            Line2D([0], [0], linestyle="None", marker="o", color="red", label="Minimum in r vs t"),
            Line2D([0], [0], linestyle="None", marker="o", color="green", label="Maximum in r vs t")] # r is the distance of the particle from the origin
        plotFrame.legend(fontsize="small", handles=legend)

        plotFrame.autoscale()
        plot(plotFrame, [0], [0], "r", "x /m", "y /m", "Comparing Different Launch Angles for Projectiles\n", True, ylim=(-5))  


def challenge7PathRight(plotFrame, u, g, step):
    step /= 1000

    # Left graph
    thetas = [30, 45, 60, 70.5, 78, 85]
    colours = ["blue", "green", "red", "cyan", "purple", "gold"]
    ranges = []

    for thetaID in range(len(thetas)):
        theta = math.radians(thetas[thetaID])
        projRange = ((u**2)/g) * (math.sin(theta) * math.cos(theta) + math.cos(theta) * math.sqrt((math.sin(theta))** 2 + (2*g*5)/u**2))
        ranges.append(projRange)

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
            particleX += step
        
        plotFrame.plot(XArray, YArray, colour)
        
        if theta >= math.radians(70.5):
            if theta == math.radians(70.5):
                X = ((u/g)) * math.sqrt(2)
                Y = math.sqrt(u**2 * X**2 - g * X**3 * u * math.sin(theta) + 0.25 * g**2 * X ** 4)
                plotFrame.plot(X, Y, "ro")
            else:
                X = ((3 * u)/(2 * g)) * (math.sin(theta) + math.sqrt(math.sin(theta)**2 - (8/9)))
                Y = math.sqrt(u**2 * X**2 - g * X**3 * u * math.sin(theta) + 0.25 * g**2 * X ** 4)
                plotFrame.plot(X, Y, "ro")
                
                X = ((3 * u)/(2 * g))*(math.sin(theta)-math.sqrt(math.sin(theta)**2 - (8/9)))
                Y = math.sqrt(u**2 * X**2 - g * X**3 * u * math.sin(theta) + 0.25 * g**2 * X ** 4)
                plotFrame.plot(X, Y, "go")
        
        legend = [Line2D([0], [0], linestyle="-", color="blue", label="θ = 30°"),
            Line2D([0], [0], linestyle="-", color="green", label="θ = 45°"),
            Line2D([0], [0], linestyle="-", color="red", label="θ = 60°"),
            Line2D([0], [0], linestyle="-", color="cyan", label="θ = 70.5°"),
            Line2D([0], [0], linestyle="-", color="purple", label="θ = 78°"),
            Line2D([0], [0], linestyle="-", color="gold", label="θ = 85°"),
            Line2D([0], [0], linestyle="None", marker="o", color="red", label="Minimum in r vs t"),
            Line2D([0], [0], linestyle="None", marker="o", color="green", label="Maximum in r vs t")] # r is the distance of the particle from the origin
        plotFrame.legend(fontsize="small", handles=legend)

        plot(plotFrame, [0], [0], "r", "range /m", "time /s", "Comparing Different Launch Angles for Projectiles", True)  


# Challenge 8
def challenge8Path(plotFrame, u, C, theta, g, h, maxBounces, step):
    allowed_to_continue = True
    try:
        step /= 1000

        # check if invalid
        test = 100/step

        theta = math.radians(theta)
        YVelocity = u * math.sin(theta)
        XVelocity = u * math.cos(theta)

        XArray = []
        YArray = []

        bounceCount = 0
        currentIndex = 0
        time = 0

        XArray.append(0)
        YArray.append(h)

        while bounceCount <= maxBounces:
            XAcceleration = 0 
            YAcceleration = -g

            XArray.append(XArray[currentIndex] + XVelocity * step + 0.5 * XAcceleration * step**2)
            YArray.append(YArray[currentIndex] + YVelocity * step + 0.5 * YAcceleration * step**2)

            YVelocity = YVelocity + (YAcceleration) * step

            if YArray[currentIndex + 1] < 0:
                YArray[currentIndex + 1] = 0
                YVelocity = -C * YVelocity
                bounceCount += 1

            currentIndex += 1
            time += step
    except:
        allowed_to_continue = False
        plot(plotFrame, [0], [0], "red", "x /m", "y /m", "Trajectory with Bounces Assuming Constant Acceleration\n", True)

    if allowed_to_continue:
        try:
            plot(plotFrame, XArray, YArray, "red", "x /m", "y /m", "Trajectory with Bounces, Assuming Constant Acceleration\n", True)
        except:
            return time
        

# Challenge 9
def challenge9Path(plotFrame, u, theta, g, h, step, D, CSA, dA, M):
    try:
        # test if valid inputs
        test = 1 / step

        step /= 1000
        CSA /= 10**4

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


        particleX = 0
        particleY = h

        DragXArray = []
        DragYArray = []

        velocityX = u*math.cos(theta)
        velocityY = u*math.sin(theta)

        k = 10* (0.5 * D * dA * CSA) / M
        drag_apogee_x, drag_apogee_y = 0, 0

        while particleY > 0:
            
            AccelerationX = -(velocityX) * k * (math.sqrt(velocityX**2 + velocityY **2)) 
            AccelerationY = -(velocityY) * k * (math.sqrt(velocityX**2 + velocityY **2)) - g

            particleX += velocityX * step + 0.5 * AccelerationX * step**2
            particleY += velocityY * step + 0.5 * AccelerationY * step**2

            velocityX += AccelerationX * step
            velocityY += AccelerationY * step

            DragXArray.append(particleX)
            DragYArray.append(particleY)

            if particleY > drag_apogee_y:
                drag_apogee_x, drag_apogee_y = particleX, particleY

        proj_range = ((u**2)/g) * (math.sin(theta) * math.cos(theta) + math.cos(theta) * math.sqrt((math.sin(theta))** 2 + (2*g*5)/u**2))
        drag_proj_range = XArray[-1]
        regular_apogee_x = (u ** 2) / g * math.sin(theta) * math.cos(theta)
        regular_apogee_y = h + ((u**2) / (2 * g) * (math.sin(theta) ** 2))
        regular_flight_time = proj_range / (u * math.cos(theta))
        drag_flight_time = drag_proj_range / (u * math.cos(theta))
        
        try:
            plotFrame.plot(XArray, YArray, color="blue", label="No Air Resistance")
            plotFrame.plot(DragXArray, DragYArray, color="red", label="Air Resistance")
            plotFrame.plot(regular_apogee_x, regular_apogee_y, "bo", label="No Air Resistance: Apogee")
            plotFrame.plot(drag_apogee_x, drag_apogee_y, "ro", label="Air Resistance: Apogee")
            plotFrame.legend()
            plot(plotFrame, [0], [0], "red", "x /m", "y /m", "Drag and Non-Drag Projectile Trajectory Models\n")
        except:
            return [proj_range, regular_apogee_x, regular_apogee_y, regular_flight_time, drag_proj_range, drag_apogee_x, drag_apogee_y, drag_flight_time, k]
        
    except:
        plot(plotFrame, [0], [0], "red", "x /m", "y /m", "Drag and Non-Drag Projectile Trajectory Models\n")
    

# Extension
def extensionPath(plotFrame, u, orbitTime, orbitRadius, planetMass, planetRadius, step, simulationLength):
    try:
        u /= 3.6                # convert from km/h to m/s
        orbitTime *= 60         # convert from mins to s
        orbitRadius *= 1000     # convert from km to m
        planetMass *= (10**21)  # convert from standard form
        planetRadius *= 1000    # convert from km to m
        
        # draw sphere
        theta, phi = np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi, 40)
        THETA, PHI = np.meshgrid(theta, phi)
        X = planetRadius * np.sin(THETA) * np.cos(PHI)
        Y = planetRadius * np.sin(THETA) * np.sin(PHI)
        Z = planetRadius * np.cos(THETA)
        
        # start of calculations
        time = 0
        orbitDistance = orbitRadius * 2 * math.pi
        orbitSpeed = orbitDistance/orbitTime
        turningSpeed = (step/(orbitDistance/orbitSpeed)) * 2 * math.pi
        
        theta = math.pi/2
        phi = math.pi/2
        XArray = []
        YArray = []
        ZArray = []
        timeArray = []
        
        h = orbitRadius
        crashed = False
        
        while time < simulationLength: 
            G = 6.67430 * (10 ** -11)
            AccelerationH = -1 * ((G * planetMass) / (h**2))       # For simplicity, we assume that the mass of the satellite is 1 kg.
            h += u * step + 0.5 * AccelerationH * step**2
            u += AccelerationH * step
            
            turningSpeed = (step/((h * 2 * math.pi)/orbitSpeed)) * 2 * math.pi
            theta += turningSpeed
        
            if h < planetRadius:   # satellite crashed into Earth
                crashed = True
                break
            
            XArray.append(h * math.sin(theta) * math.cos(phi))
            YArray.append(h * math.sin(theta) * math.sin(phi))
            ZArray.append(h * math.cos(theta))
            
            timeArray.append(time)
            time += step

        if XArray == []:
            raise ValueError

        try:
            # earth = image.imread("nasa_blue_marble_earth.jpeg")

            # display
            ax = plotFrame.add_subplot(projection='3d')
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('gist_earth'), linewidth=0, antialiased=False, alpha=0.5)
            ax.set_xlim([-orbitRadius*1.5, orbitRadius*1.5])
            ax.set_ylim([-orbitRadius*1.5, orbitRadius*1.5])
            ax.set_zlim([-orbitRadius*1.5, orbitRadius*1.5])
            ax.set_box_aspect([1, 1, 1])
            ax.scatter3D(XArray, YArray, ZArray, c = (timeArray), cmap = "cool")
            ax.plot3D(XArray, YArray, ZArray)
            ax.set_xlabel("X /m")
            ax.set_ylabel("Y /m")
            ax.set_ylabel("Z /m")
            if crashed:
                return True
            return False
        except:
            if crashed:
                return [True, time]
            return [False]
            
    except Exception as error:
        # print(error)
        pass
# fig = plt.figure()
#plt_sphere() 

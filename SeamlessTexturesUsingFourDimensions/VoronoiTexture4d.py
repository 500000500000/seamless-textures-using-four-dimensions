import sys # for max float
import random

#--------------------------------------------------------------------------------------------

# Four-dimensional space is partitioned into Voronoi regions based on randomly chosen points. 
# Each region has a random color.
# F returns the color of a given point.

# The number of points.
pointCount = 15

#--------------------------------------------------------------------------------------------
def getRandomColor():
    rgb = [0,0,0]
    rgb[0] = random.randint(0, 255)
    rgb[1] = random.randint(0, 255)
    rgb[2] = random.randint(0, 255)
    return rgb
#--------------------------------------------------------------------------------------------
# Create the points and region colors.
points = [0, 0, 0, 0] * pointCount
colors = [0, 0, 0] * pointCount
for i in range(pointCount):
    points[i] = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]
    colors[i] = getRandomColor()
    pass
# -------------------------------------------------------------------------------------------
def F(w,x,y,z):
    # Loop through the points.
    bestIndex = 0
    bestDistanceSquared = sys.float_info.max
    for i in range(pointCount):
        c = points[i]
        testDistanceSquared = (w-c[0])**2 + (x-c[1])**2 + (y-c[2])**2 + (z-c[3])**2
        if bestDistanceSquared > testDistanceSquared:
            bestDistanceSquared = testDistanceSquared
            bestIndex = i
    return colors[bestIndex]
#--------------------------------------------------------------------------------------------
import math # for sqrt
import random

#--------------------------------------------------------------------------------------------

# In four-dimensional space,
# Light rays with random colors emanate from randomly chosen points with falling intensity.
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
# Given a chosen hue, adjust color according to intensity within 0...100
# return:
# black for intensity 0
# original color for intensity 50
# white for intensity 100
def adjustForIntensity(color, intensity):
    rgb = [0,0,0]
    if intensity <= 50:
        for i in range(3):
            rgb[i] = round( (intensity/50)*color[i] )
        return rgb
    else:
        for i in range(3):
            rgb[i] = round(  ( (100-intensity)*color[i] + (intensity-50)*255 ) / 50  )
        return rgb
#--------------------------------------------------------------------------------------------
# Create the points and ray colors.
points = [0, 0, 0, 0] * pointCount
colors = [0, 0, 0] * pointCount
for i in range(pointCount):
    points[i] = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]
    colors[i] = getRandomColor()
    pass
#--------------------------------------------------------------------------------------------
def F(w,x,y,z):
    # Loop through the points.
    # Add the contribution of light from each point to a maximum of [255,255,255].
    rgb = [0,0,0]
    for i in range(pointCount):
        c = points[i]
        col = colors[i]
        distanceSquared = (w-c[0])**2 + (x-c[1])**2 + (y-c[2])**2 + (z-c[3])**2
        distance = math.sqrt(distanceSquared)
        # Falloff calculation.
        if distanceSquared > 0:
            intensity = 5/distance
        else:
            intensity = 100
        # Color of the current ray adjusted for intensity.
        intensitycol = adjustForIntensity(col, intensity)
        # Add to total color.
        for i in range(3):
            rgb[i] += intensitycol[i]
    # Cap at [255,255,255].
    for i in range(3):
        if(rgb[i] > 255):
            rgb[i] = 255
    # Return total color.
    return rgb
#--------------------------------------------------------------------------------------------
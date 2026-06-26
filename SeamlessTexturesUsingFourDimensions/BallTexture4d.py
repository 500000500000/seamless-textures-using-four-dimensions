import random

#--------------------------------------------------------------------------

# A set of hyperballs in four-dimensional space
# have the same radius, random centers and random colors.
# When hyperballs intersect, the colors add to a maximum of [255,255,255].
# A point not contained in any hyperball has the default color.
# F returns the color of a given point.

# The number of hyperballs
ballCount = 20

# The common radius
radius = 1

# The default color
defaultColor = [255,255,255]

#---------------------------------------------------------------------------
def getRandomColor():
    rgb = [0,0,0]
    rgb[0] = random.randint(0, 255)
    rgb[1] = random.randint(0, 255)
    rgb[2] = random.randint(0, 255)
    return rgb
#---------------------------------------------------------------------------
# Create 4-dimensional balls.
radiusSquared = radius * radius
centers = [0, 0, 0, 0] * ballCount
colors = [0, 0, 0] * ballCount
# F will only be called on [-1,1] x [-1,1] x [-1,1] x [-1,1] so chose random centers accordingly.
for i in range(ballCount):
    centers[i] = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]
    colors[i] = getRandomColor()
    pass
#----------------------------------------------------------------------------------
def F(w, x, y, z):
    # Color of 4-dimensional point to return.
    rgb = [0, 0, 0]
    # Loop through the 4-dimensional balls.
    for i in range(ballCount):
        # Get the center and the color.
        c = centers[i]
        col = colors[i]
        # See if the point is in the ball.
        distFromCenterSquared = (w-c[0])**2 + (x-c[1])**2 + (y-c[2])**2 + (z-c[3])**2
        if(distFromCenterSquared < radiusSquared):
            # Add the color of the ball to the output color, but cap at 255.
            for j in range(3):
                rgb[j] += col[j]
                if(rgb[j] > 255):
                    rgb[j] = 255
    # Default color if not set above.
    if rgb == [0, 0, 0]:
        rgb = defaultColor
    # Return the color of the 4-dimensional point.
    return rgb
#------------------------------------------------------------------------------------
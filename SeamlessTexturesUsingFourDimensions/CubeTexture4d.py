import random

#----------------------------------------------------------------------------------

# Four-dimensional space is partitioned into regular hypercubes with random colors.
# F returns the color of a given point.

# The hypercubes need only cover the main hypercube [-1,1] x [-1,1] x [-1,1] x [-1,1]
# Let n be the number of small hypercubes per side.
# This also determines the number of colors needed.
n = 3

#----------------------------------------------------------------------------------
def getRandomColor():
    rgb = [0,0,0]
    rgb[0] = random.randint(0, 255)
    rgb[1] = random.randint(0, 255)
    rgb[2] = random.randint(0, 255)
    return rgb
#----------------------------------------------------------------------------------
# Create the n by n by n by n color array.
colorArray = [[ [  [ [0,0,0] for i in range(n)] for j in range(n) ]  for k in range(n)]  for l in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                colorArray[i][j][k][l] = getRandomColor()
#----------------------------------------------------------------------------------
# F: [-1,1] x [-1,1] x [-1,1] x [-1,1] -> color
def F(w, x, y, z):
    i = round((n-1)*(w+1)/2)
    j = round((n-1)*(x+1)/2)
    k = round((n-1)*(y+1)/2)
    l = round((n-1)*(z+1)/2)
    return colorArray[i][j][k][l]
#----------------------------------------------------------------------------------
import math # for pi
import numpy as np
import matplotlib.pyplot as plt

# MAIN FILE

# Width and height in pixels of texture to be created.
size = 200

# Let F be a 4-dimensional texture,
# that is, a function that maps R4 to color.
# In particular it must be defined on [-1,1] x [-1,1] x [-1,1] x [-1,1].
def CreateSeamlessTextureFrom(F):
    # The function H(U,V) is 1-periodic in both U and V
    # so it gives a 2-dimensional tileable texture.
    # (U,V) -> [-1,1] x [-1,1] x [-1,1] x [-1,1] -> color
    # See https://www.cmdigitex.com/seamless-textures
    def H(U, V):
        twoPI = 2*math.pi
        return F(math.sin(twoPI*U), math.cos(twoPI*U), math.sin(twoPI*V), math.cos(twoPI*V))

    # Create the 2-dimensional texture.
    texture = [ [ [0,0,0] for i in range(size)] for j in range(size) ]
    for i in range(size):
        for j in range(size):
            U = i / size
            V = j / size
            texture[i][j] = H(U, V)

    # Show the texture.
    plt.imshow(texture)
    plt.show()

    # Tile.
    tiled = np.tile(texture, (3,4,1))

    # Show the tiling.
    plt.imshow(tiled)
    plt.show()

    pass

#------------------------------------------------------------------------------------------------
# Test the process on different 4-dimensional textures.

from CubeTexture4d import F as F1
from BallTexture4d import F as F2
from VoronoiTexture4d import F as F3
from RayTexture4d import F as F4

CreateSeamlessTextureFrom(F1)
CreateSeamlessTextureFrom(F2)
CreateSeamlessTextureFrom(F3)
CreateSeamlessTextureFrom(F4)

pass
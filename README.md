# Seamless Textures Using Four Dimensions

Let F be any function that maps four-dimensional space to colors.

rgb = F(w,x,y,z)

Then the function

H(U,V) = F[sin(2πU),cos(2πU),sin(2πV),cos(2πV)]

creates a seamless texture. 

https://www.cmdigitex.com/seamless-textures

The files CubeTexture4d.py, BallTexture4d.py, VoronoiTexture4d.py and RayTexture4d.py provide random example functions F of different types.

The main file SeamlessTexturesUsingFourDimensions.py creates the corresponding seamless textures. 

## Limitations

Each random example function F is defined on import.
Calling for example CreateSeamlessTextureFrom(F1) twice would produce the same random texture both times.

#! /usr/bin/env python3

#Dylan Creaven
#Calculate the square root of a number

def sqrt(x):
    """
    Calculate the sqaure root of argument x
    """
    #initial guess for the square root 
    z=x/2.0

    #Continously imporve the guess/
    #Adapted from https://tour.golang.org/flowcontrol/8
    while abs(x-(z*z))>0.00000011:
      z =z- (((z*z)-x)/(2*z))
    return z
    
myval=63.0
print("the square root of ",myval," is ",sqrt(myval))

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 17:42:12 2022

@author: LODKe

"""

"""#Signature
Print("Started making it,")
Print("Had a breakdown")
Print("Bon Appétit")
"""

#Import neccessary modules
import math as m
import numpy as np
import matplotlib.pyplot as plt

#Used All caps for constants, and snake_case for variables 

#Set up initiual values
EMISSION_RATE = 100                 #Set up  Emmision rate
DIFFUSIVITY_COEFFICIENT_X = 1       #Diffusivity co-effiecent in x
DIFFUSIVITY_COEFFICIENT_Y = 1       #Diffusivity co-effiecent in y
DIFFUSIVITY_COEFFICIENT_Z = 1       #Diffusivity co-effiecent in z
WIND_SPEED = 5                      #Windspeed in direction of x-axis

TIME_STEP = 1                       #How many seconds in each time step
SECOND = 1
HOUR = 60 * 60 * SECOND
DAY = 24 * HOUR
WEEK = 7 * DAY

NUM_TIME_STEPS = 5 * HOUR           #The number of steps we model for

X_DOMAIN = 200                      #Set up domain for x
Y_DOMAIN = 30                       #Set up domain for y
Z_DOMAIN = 30                       #Set up domain for z

#Setting the steps equal to the domains to simplify our equations
X_STEPS = X_DOMAIN
Y_STEPS = Y_DOMAIN
Z_STEPS = Z_DOMAIN

Dx = X_DOMAIN/X_STEPS
Dy = Y_DOMAIN/Y_STEPS
Dz = Z_DOMAIN/Z_STEPS

Mid_point_y = int(Y_DOMAIN / 2)     #Find a place for the chimney in y
CHIMNEY_HEIGHT = 5                  #Set a height for the chimney


#Create an array for concentration
C = np.zeros((NUM_TIME_STEPS+1, X_DOMAIN+1, Y_DOMAIN+1))

# Our Equation for working out diffusion/advection for x,y
for n in range(1,NUM_TIME_STEPS):
    #loop for 1=<t
    EMISSION_CHANGE = EMISSION_RATE * m.sin((n*m.pi)/(NUM_TIME_STEPS))
    for i in range(X_DOMAIN):
        #loop for 0=<x
        for j in range(Y_DOMAIN):
            #loop for 0=<y
            #print("C[",n,",",i,",",j,"]=",C[n,i,j]) #reads our array element by element 
            
                #Set boundary "condition" for source of pollution
                C[n,0,Mid_point_y] = EMISSION_RATE
                # C[n,0,Mid_point_y] = EMISSION_CHANGE
                
                #Just diffusion in y
                #C[n+1,i,j] = C[n,i,j] + TIME_STEP * DIFFUSIVITY_COEFFICIENT_Y * ((C[n-1,i,j+1]-2*C[n-1,i,j]+C[n-1,i,j-1])/(Y_DOMAIN**2))
                
                #Input our equation for advection/diffusion
                C[n+1,i,j] = (C[n,i,j] + 2 * TIME_STEP * ((DIFFUSIVITY_COEFFICIENT_Y * ((C[n-1,i,j+1]-2*C[n-1,i,j]+C[n-1,i,j-1])/(Y_DOMAIN**2))) - WIND_SPEED*((C[n,i+1,j]-C[n,i-1,j])/(X_DOMAIN*2))))

"""# Our Equation for working out diffusion/advection for x,z
for n in range(1,NUM_TIME_STEPS):
    #loop for 1=<t
    EMISSION_CHANGE = EMISSION_RATE * m.sin((2*n*m.pi)/(NUM_TIME_STEPS))
    for i in range(X_DOMAIN):
        #loop for 0=<x
        for j in range(Z_DOMAIN):
            #loop for 0=<y
            #print("C[",n,",",i,",",j,"]=",C[n,i,j]) #reads our array element by element 
            
                #Set boundary "condition" for source of pollution
                C[n,0,CHIMNEY_HEIGHT] = EMISSION_RATE
                #C[n,0,CHIMNEY_HEIGHT] = EMISSION_CHANGE
                
                #Just diffusion in z
                #C[n+1,i,j] = C[n,i,j] + TIME_STEP * DIFFUSIVITY_COEFFICIENT_Z * ((C[n-1,i,j+1]-2*C[n-1,i,j]+C[n-1,i,j-1])/(Z_DOMAIN**2))
                
                #Input our equation for advection/diffusion
                C[n+1,i,j] = (C[n,i,j] + 2 * TIME_STEP * ((DIFFUSIVITY_COEFFICIENT_Z * ((C[n-1,i,j+1]-2*C[n-1,i,j]+C[n-1,i,j-1])/(Z_DOMAIN**2))) - WIND_SPEED*((C[n,i+1,j]-C[n,i-1,j])/(X_DOMAIN*2))))
"""

"""# Our Equation for working out diffusion/advection for x,z with x diffusion
for n in range(1,NUM_TIME_STEPS):
    #loop for 1=<t
    EMISSION_CHANGE = EMISSION_RATE * m.sin((2*n*m.pi)/(NUM_TIME_STEPS))
    for i in range(X_DOMAIN):
        #loop for 0=<x
        for j in range(Z_DOMAIN):
            #loop for 0=<y
            #print("C[",n,",",i,",",j,"]=",C[n,i,j]) #reads our array element by element 
            
                #Set boundary "condition" for source of pollution
                C[n,0,CHIMNEY_HEIGHT] = EMISSION_RATE
                #C[n,0,CHIMNEY_HEIGHT] = EMISSION_CHANGE
                
                #Just diffusion in z
                #C[n+1,i,j] = C[n,i,j] + TIME_STEP * DIFFUSIVITY_COEFFICIENT_Z * ((C[n-1,i,j+1]-2*C[n-1,i,j]+C[n-1,i,j-1])/(Z_DOMAIN**2))
                
                #Input our equation for advection/diffusion
                C[n+1,i,j] = (C[n,i,j] + 2 * TIME_STEP * ((DIFFUSIVITY_COEFFICIENT_Z * ((C[n-1,i,j+1]-2*C[n-1,i,j]+C[n-1,i,j-1])/(Z_DOMAIN**2))) + (DIFFUSIVITY_COEFFICIENT_X * ((C[n-1,i,j+1]-2*C[n-1,i,j]+C[n-1,i,j-1])/(X_DOMAIN**2))) - WIND_SPEED*((C[n,i+1,j]-C[n,i-1,j])/(X_DOMAIN*2))))
"""



C_copy = C.clip(min=0)              #This eliminates any posible negative values in our array which makes graphing easier


"""#Scatter Graph Function
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for x in range(X_DOMAIN):
    for y in range(Y_DOMAIN):
        for t in range(NUM_TIME_STEPS):
           ax.scatter(x,t,y, s=C_copy[t,x,y])
           ax.set_xlabel("Variation in x")
           ax.set_ylabel("Time")
           ax.set_zlabel("Variation in y")
           ax.set_title("Concentration of pollutant")
plt.show()
"""

"""#Contour graph funciton
time_steps = [0,1800,HOUR,5 * HOUR]

fig, axes = plt.subplots(2,2,figsize=(10,10))
v = np.linspace(0, 100, 25)

for idx, ax in enumerate(axes.ravel()):

    cont = ax.contourf(C_copy[time_steps[idx],:,:], v, extend="max")
    plt.colorbar(cont, ax=ax,label="Concentration")
    ax.set_xlabel("x")
    ax.set_ylabel("z")
    ax.set_title(f"Time step = {time_steps[idx]}")

plt.show()

#plot.plot(C[15,0,:],z,'b-o',)
#for i in time_steps:
#    print(C[i,:,:])
"""
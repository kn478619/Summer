import numpy as np
import random as rand
L = 10 # size of the box
N = 50
cut_off = 2.0 
x = np.empty(N, dtype = object) # creates an empty array of N dimension with zeros
y = np.empty(N, dtype = object) 
z = np.empty(N, dtype = object)


outfile = open("POSCAR", 'w')
print("created on June 1 by Kishor", file = outfile)
print("10.00000000", file = outfile)
print("     1.00000000   0.00000000    0.00000000 ",file=outfile)
print("     0.00000000   1.00000000    0.00000000 ",file=outfile)
print("     0.00000000   0.00000000    1.00000000 ",file=outfile)
print("  Na ",file=outfile)
print("  50",file=outfile)
print("Direct",file=outfile)

number = 0
while number < N:# loop that creates continuous values for the N particle coordinates
    x_coord = rand.uniform(0,L)
    y_coord = rand.uniform(0,L)
    z_coord = rand.uniform(0,L)
    iteration = 0 
    # loop to check if the coordinates satisfies the condition for minimum distance between the particles.
    while iteration < number:
        length_x = abs(x_coord - x[iteration])
        if (length_x > 5.0):
            length_x = L - length_x
        else: length_x = length_x
        
       
        length_y = abs(y_coord - y[iteration])
        if (length_y > 5.0): 
            length_y = L - length_y
        else: length_y = length_y
        
        
        length_z = abs(z_coord - z[iteration])
        if (length_z > 5.0): 
            length_z = L - length_z
        else: length_z = length_z
        #print(length_x, length_y, length_z)
        
        
        if (length_x**2 + length_y**2 + length_z**2 < cut_off**2): # distance
         #   if (length_y < 2): # how to optimize a single condition for these, need to work
         #      if (length_z < 2): #(if none of these are satisfied by the values of x, y, z, 
                                   # loop should repeat to genereate new coordinates)
            x_coord = rand.uniform(0,L)
            y_coord = rand.uniform(0,L)
            z_coord = rand.uniform(0,L)
            iteration = 0
        else: 
            iteration = iteration + 1 # need to insert the boundary condition somewhere here.. How???
    x[number] = x_coord
    y[number] = y_coord
    z[number] = z_coord
    number = number + 1
    print("%10.8f"%(x_coord/L), "%10.8f"%(y_coord/L), "%10.8f"%(z_coord/L), file = outfile) # divided to make length of the box as a scaling parameter.




  

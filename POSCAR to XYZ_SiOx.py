#this program was initially to create for SiOx, x = 0.8

import numpy as np

inputfile = open("CONTCAR",'r') # CONTCAR or POSCAR (in VASP format) you want to change. This file and CONCAR should be in same directory
line_to_skip = 8
for i in np.arange(line_to_skip):
    inputfile.readline()     #skips unwanted 8 line from VASP format 
outfile= open("xyz_format", "w")
print ("216" ,file =outfile)
print("Comment : XYZ_format",file=outfile)
N_Si = 120
N_total = 216
coordinates = []
for i in np.arange(0,N_Si):
    coordinate = inputfile.readline().split()
    coordinates.append(coordinate)
    print( "Si" , "%10.6f"%(float(coordinate[0])),"%10.6f"%(float(coordinate[1])), "%10.6f"%(float(coordinate[2])), file = outfile)
for j in np.arange(N_Si, N_total):
    coordinate = inputfile.readline().split()
    coordinates.append(coordinate)
    print("O" , "%10.6f"%(float(coordinate[0])),"%10.6f"%(float(coordinate[1])), "%10.6f"%(float(coordinate[2])), file = outfile)
inputfile.close()
#print(coordinates, file = outfile)
print (len(coordinates))

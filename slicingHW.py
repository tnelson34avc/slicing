
# -*- coding: utf-8 -*-
"""
Created on thur 8 20:05:32 2022

@author: ya boy

hw assignment: slicing

9/24/2022 (september)
"""

import numpy as np

'''
Use numpy.array to define a 3-by-7 array, A.  In array location (i,j), row i, column j,  put the number i*j

Use slicing to produce and print:
'''
A = np.zeros(shape = (3,7))# creats an array of 3 rows by 7 columns

for i in range(3):#row
  for j in range(7):#column
    A[i,j] = i * j     #thank god its like java

print(f"row 2 of A: {A[2,:]}") # : = all the columsn in the row


'''1)  row 2 of A'''
print(f"row 2 of A: {A[2,:]}") # : = all the columsn in the row

'''2) row 2 of A in reverse order'''
print(f"row 2 of A , reverse order: {A[2,::-1]}") # ::-1 = reverse the order

'''3) the sub-matrix consisting or the bottom right 2x2 sub-array '''
print(f"sub matrix bottom right 2x2:\n {A[1:,5:]}")# number: = all the rest of the row or column

'''4) the sub-array consisting of the bottom left 2x2 sub-array'''
print(f"sub matrix bottom left 2x2:\n {A[1:,:2]}") # :number = all the number before that row or column

'''5) the 3x3 sub-array in the middle of A'''
print(f"sub matrix middle of array 3x3:\n {A[:,2:5]}")# number:number = all the numbers between those two rows or columns 
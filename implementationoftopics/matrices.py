import numpy 
  
# initializing matrices
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])
  
# using add() to add matrices
print ("The element wise addition of matrix is : ")
print (numpy.add(x,y))
  
# using subtract() to subtract matrices
print ("The element wise subtraction of matrix is : ")
print (numpy.subtract(x,y))
  
# using divide() to divide matrices
print ("The element wise division of matrix is : ")
print (numpy.divide(x,y))

# using sqrt() to print the square root of matrix
print ("The element wise square root is : ")
print (numpy.sqrt(x))
  
# using sum() to print summation of all elements of matrix
print ("The summation of all matrix element is : ")
print (numpy.sum(y))
  
# using sum(axis=0) to print summation of all columns of matrix
print ("The column wise summation of all matrix  is : ")
print (numpy.sum(y,axis=0))
  
# using sum(axis=1) to print summation of all columns of matrix
print ("The row wise summation of all matrix  is : ")
print (numpy.sum(y,axis=1))
  
# using "T" to transpose the matrix
print ("The transpose of given matrix is : ")
print (x.T)

#using dot to print matrix multiplication
print("Matrix multiplication of x and y matrix:")
print( numpy.dot(x,y))

#printing the the inverse of the matrix
print(numpy.linalg.inv(x))
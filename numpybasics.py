import numpy as np

#1d array
a = np.array([0,1, 2, 3,4,5])
print a
print a.ndim  #dimension is 1 
print a.shape #(6,) is 6 rows
print a.dtype #type of the array


#For 2d array
b = a.reshape((3,2)) # 3 rows and 2 columns
print b
print b.ndim  #2 dimensional 
print b.shape #Shape of the array

#Here b and a refers same object ,to have independent objects use .copy()
c = a.reshape((3,2)).copy()

#Operations on numpy array
d = np.array([1,2,3,4,5])
print d * 2
print d ** 2

#To filter the data with some conditions
print a > 4
print a[a > 4]

#To trim outliers of any data
a[a > 4] = 5
print a

print a.clip(0, 4)  #To clip the values at both ends of an interval


#Non existing values
k = np.array([1, 2, np.NAN, 3, 4])
print k
print np.isnan(k)   #Array that results True for Nan
print k[~np.isnan(k)] #Array results only valid numbers
print np.mean(k[~np.isnan(k)])   #Find the mean of all valid numbers


#For different datatypes in np array
print np.array([1, "Test"]).dtype
print np.array([1, "Test", set([1,2,3])]).dtype

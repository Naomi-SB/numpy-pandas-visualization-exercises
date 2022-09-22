

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#How many negative numbers are there?
len(a[a < 0])

#How many positive numbers are there?
len(a[a > 0])

#How many even positive numbers are there?
na = a[a>0]
na
na[na % 2 == 0]
len(na[na % 2 == 0])

#If you were to add 3 to each data point, how many positive numbers would there be?
a + 3
ap3 = a+3
ap3
len(ap3[ap3 > 0])

#If you squared each number, what would the new mean
new_a = a ** 2
new_a.mean()


# new standard deviation after sqaring
new_a.std()

#Center the data set.
a_mean = a.mean()
a - a_mean

#check centering:
center = a - a_mean
center.mean()

#Calculate the z-score for each data point.







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
a.std()
a_std = a.std()
deviation = (center / a_std)
deviation 

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
sum_of_a

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
min_of_a
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
max_of_a
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
[n ** 2 for n in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
[n for n in a if n % 2 != 0]
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
[n for n in a if n % 2 ==0]


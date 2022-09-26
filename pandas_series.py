# checking the type:
#type(variable name)
#.head limits it to the first 5
# comparing a series against a list of values: 
import numpy as np
import pandas as pd
 
 #make a series from this list:    ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
fruit_series = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
fruit_series 

#1. Determine the number of fruits in the series
len(fruit_series)

#2. Output only the index from fruits.
fruit_series.index

#3. Output only the values from fruits.
fruit_series.values

#4. Confirm the data type of the values in fruits.
fruit_series.dtype
 
#5.a first five
fruit_series.head()
#5.b
fruit_series.tail(3)
#5.c
fruit_series.sample(2)

#6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruit_series.describe()

#7. unique strings
fruit_series.unique()

#8. Determine how many times each unique string value occurs in fruits.
fruit_series.value_counts()

# 9.Determine the string value that occurs most frequently in fruits.
fruit_series.value_counts().idxmax()

#10. Determine the string value that occurs least frequently in fruits.
fruit_series.value_counts().idxmin()

###################################################   EXERCISES PART 2      ###################################################

# 1. Capitalize all the string values in fruits.
fruit_series.str.upper()

# 2. Count the letter "a" in all the string values (use string vectorization).
fruit_series.str.count('a')

# 3. Output the number of vowels in each and every string value.
fruit_series.str.count('[aeiou]')

# 4. Write the code to get the longest string value from fruits.
    #to identify the length of the longest string:
fruit_series.str.len().max()
    # to output the name of the fruit with the longest string value:
fruit_series[fruit_series.str.len().idmax()]

# 5. Write the code to get the string values with 5 or more letters in the name.
fruit_series[fruit_series.str.len() >= 5]

#6. Find the fruit(s) containing the letter "o" two or more times.
fruit_series.str.count('o') >= 2 

#7. Write the code to get only the string values containing the substring "berry".
fruit_series[fruit_series.str.contains('berry')]

#8. Write the code to get only the string values containing the substring "apple".
fruit_series[fruit_series.str.contains('apple')]

#9. Which string value contains the most vowels?
fruit_series.str.count('[aeiou]').max()



# Python Programming

### 1. Write a program to demonstrate different number data types in Python

```py
'''Aim: Write a program to demonstrate different number data types in Python.'''

a = 10  # Integer DataType
b = 11.5  # Float DataType
c = 2.05j # Complex Number

print("a is Type of", type(a))  # prints type of variable a
print("b is Type of", type(b))  # prints type of vairiable b
print("c is Type of", type(c))  # prints type of variable c
```

__Output:__
```s
a is Type of <class 'int'>
b is Type of <class 'float'>
c is Type of <class 'complex'>
```

### 2. Write a program to perform different Arithmetic Operations on numbers in Python.

```py
'''Aim: Write a program to perform different Arithmetic Operations on numbers in Python.'''

a = int(input("Enter a value: "))  # input() takes data from console at runtime as string.
b = int(input("Enter b value: "))  # type cast the input string to int 

print("Addition of a and b", a + b)
print("Subtraction of a and b", a - b)
print("Multiplication of a and b", a * b)
print("Division of a and b", a / b)
print("Remainder of a and b", a % b)
print("Exponent of a and b", a ** b)  # exponent operator (a ^ b)
print("Floor division of a and b", a // b)  # integer division
```

__Output:__

```s
Enter a value: 3
Enter b value: 2
Addition  of a and b 5
Subtraction of a and b 1
Multiplication of a and b 6
Division of a and b 1.5
Remainder of a and b 1
Exponent of a and b 9
Floar division of a and b 1
```


### 3. Write a program to create, concatinate and print a string and accessing sub-string from a given string

```py
'''Aim: write a program to create, concatenate and print a string and accessing sub-string from a given string'''

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print("First string is:", s1)
print("Second string is:", s2)
print("Concatenation of two strings:", s1 + s2)
print("Substring of given string:", s1[1:4])
```

__Output:__

```s
Enter first string: COMPUTER-
Enter second string: SCIENCE
First string is: COMPUTER-
Second string is: SCIENCE
Concatenation of two string: COMPUTER-SCIENCE
Substring of given string: OMP
```


### 4. Write a python script to print the current date in the following format -> "Sun May 29 02:26:23 IST 2017"

```py
'''Aim: Write a python script to print the current date in the following format "Sun May 29 02:26:23 IST 2017'''

import time

ltime = time.localtime()

print(time.strftime("%a %b %d %H:%M:%S %Z %Y", ltime))  # print formatted time

'''
%a : Abbreviated weekday name.
%b : Abbreviated month name.
%d : Day of the month as a decimal number [01, 31]
%H : Hour (24-hour clock) as a decimal number [00, 23]
%M : Minute as a decimal number [00, 59]
%S : Second as a decimal number [00, 59]
%Z : Time zone name (no characters if no time zone exists)
%Y : Year with century as a decimal number.'''
```


### 24. Python Program to find area of a Circle

> Hint: $Area$ = $\pi$ * $r^2$  \
where r is the radius of circle


```py
# Python program to find Area of a circle
def findArea(r):
    PI = 3.142
    return PI * r * r

r = int(input("Enter radius: "))
print("Area of circle is", findArea(r))
```

__Output:__

```
Enter radius: 5
Area of circle is 15.71
```


### 25. Python Program for Compound Interest

```py
# Python program to find compound interest for given values

def compound_interest(principle, rate, time):
    amount = principle * pow(1 + rate / 100, time)
    ci = amount - principle
    return ci

print("Compound Interest", compound_interest(10000, 10.25, 5))
```

__Ouput:__

```
Compound Interest 6288.94627
```


### 26. Python program to print positive numbers in a list

```py
# Python program to print positive number in a list

# list of numbers
arr = [11, -21, 0, 45, 66, -93]

# iterating each number in list
for num in arr:
    # check if num is positive
    if num >= 0:
        print(num, end=" ")
```

__Output:__

```
11 0 45 66
```

### 27. Remove multiple elements from a list in Python

```py
# Python program to remove multiple elements from a list

# list of numbers
arr = [11, 5, 17, 18, 23, 50]

# iterate each element in list
for num in arr:
    if num % 2 == 0:
        arr.remove(num)

# print modified list
print("New list after removing all even numbers:", arr)
```

__Output:__

```
New list after removing all even numbers: [11, 5, 17, 23]
```
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

**Output:**

```sh
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

**Output:**

```sh
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

**Output:**

```sh
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

### 5. Write a program to create, append and remove item from a list.

**Creating a list**

```py
# empty list
list1 = []

# list of integers
list2 = [1, 2, 3, 4, 5]

# list with mixed data type
list3 = ['a', 1, 2.0, True]
```

**Add item to list and extend list**

```py
# append and extend lists in Python

my_list = [1, 2, 3, 4, 5]
print("Initial list:", my_list)

# append an item
my_list.append(6)
print("After append", my_list)

# extend a list
my_list.extend([7, 8, 9])
print("After extend", my_list)
```

**Output:**

```sh
Initial list: [1, 2, 3, 4, 5]
After append [1, 2, 3, 4, 5, 6]
After extend [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Delete/Remove item from list**

```py
my_list = [1, 2, 3, 4, 5]

# delete one item
del my_list[2]
print("After delete", my_list)

# delete multiple items
del my_list[1:3]
print("After delete", my_list)

# delete all items
del my_list[:]
print("After delete", my_list)
```

**Output:**

```sh
After delete [1, 2, 4, 5]
After delete [1, 4, 5]
After delete []
```

### 6. Write a program to demonstrate the use of tuples in Python.

> A tuple can have any number of items, and they are immutable and may be of different types(integer, float, string, boolean, etc.)

```py
# Different types of tuples

# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# tuples having integers
tuple_with_integers = (1, 2, 3, 4, 5)
print("Tuple with integers:", tuple_with_integers)

# tuples having mixed data types
tuple_with_mixed_data_types = (1, "Hello", 2.0, True)
print("Tuple with mixed data types:", tuple_with_mixed_data_types)

# nested tuples
tuple_with_nested_tuples = (1, 2, ("Hello", "World"))
print("Tuple with nested tuples:", tuple_with_nested_tuples)
```

**Output:**

```sh
Empty tuple: ()
Tuple with integers: (1, 2, 3, 4, 5)
Tuple with mixed data types: (1, 'Hello', 2.0, True)
Tuple with nested tuples: (1, 2, ('Hello', 'World'))
```

> A tuple can also be created without using parentheses. This is known as tuple packing.

```py
my_tuple = 1, 2, 3, 4, 5
print("Tuple created without using parentheses:", my_tuple)

# tuple unpacking
a, b, c, d, e = my_tuple

print("Tuple unpacked:", a, b, c, d, e)
```

**Output:**

```sh
Tuple created without using parentheses: (1, 2, 3, 4, 5)
Tuple unpacked: 1 2 3 4 5
```

> Having one element within a parenthesis is not enough. We will need a trailing comma to indicate that it is, in fact, a tuple.

```py
my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

# Parenthesis is optional
my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'>
```

**Output:**

```sh
<class 'str'>
<class 'tuple'>
<class 'tuple'>
```

### 7. Write a program to demonstrate working with dictionaries in Python.

```py
# empty dictionary
my_dict = {}
print("Empty dictionary:", my_dict)

# dictionary with integer keys
my_dict = {1: "One", 2: "Two", 3: "Three"}
print("Dictionary with integer keys:", my_dict)

# dictionary with mixed keys
my_dict = {1: "One", "Two": 2, "Three": 3.0, True: False}
print("Dictionary with mixed keys:", my_dict)

# from sequence having each item as a pair
my_dict = dict([(1, "One"), (2, "Two"), (3, "Three")])
```

**Output:**

```sh
Empty dictionary: {}
Dictionary with integer keys: {1: 'One', 2: 'Two', 3: 'Three'}
Dictionary with mixed keys: {1: 'One', 'Two': 2, 'Three': 3.0, True: False}
Dictionary with mixed keys: {1: 'One', 2: 'Two', 3: 'Three'}
```

#### Accessing Elements from Dictionary

While indexing is used with other data types to access values a dictionary uses `keys`. Keys can be used either inside square brackets `[]` or with `get()` method.

If we use the square brackets `[]`, `KeyError` is raised in case a key is not found in the dictionary. On the other hand, the `get()` method returns `None` in case a key is not found.

```py
# get vs [] for retrieving values from dictionary
my_dict = {1: "One", 2: "Two", 3: "Three"}

# Output: One
print(my_dict[1])

# Output: Three
print(my_dict.get(3))

# Try to access key which is not present in the dictionary
# Output: None
print(my_dict.get(4))

# KeyError
print(my_dict[4])  # 4 is not in the dictionary
```

**Output:**

```sh
One
Three
None
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
KeyError: 4
```

### 8. Write a program to find largest of three integers.

```py
# largest of three integers

num1 = 10
num2 = 20
num3 = 30

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number between", num1, num2, num3, "is", largest)
```

**Output:**

```sh
The largest number between 10 20 30 is 30
```

### 9. Write a Python Program to convert temperatures to and from Celsius, Fahrenheit.

> Hint: $C$ = 5/9 \* ($F$ - 32)

```py
# temperature conversion

temp = float(input("Enter temperature: "))
unit = input("Enter unit of temperature(C for celsius and F for Fahrenheit): ")

if unit == "C" or unit == "c":
    new_temp = 9 / 5 * temp + 32
    print("Temperature in Fahrenheit:", new_temp)
elif unit == "F" or unit == "f":
    new_temp = (temp - 32) * 5 / 9
    print("Temperature in Celsius:", new_temp)
else:
    print("Invalid unit of temperature")
```

**Output:**

```sh
Enter temperature: 100
Enter unit of temperature(C for celsius and F for Fahrenheit): C
Temperature in Fahrenheit: 212.0
```

### 10. Write a Python program to construct the following pattern using nested for loops.

```
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
```

**Program:**

```py
n = 5
for i in range(n):
    for j in range(i):
        print("* ", end="")
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()
```

**Output:**

```sh
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
```

### 11. Write a Python script that prints prime numbers less than 20.

```py
# prime numbers
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(2, 20):
    if is_prime(i):
        print(i, end=" ")
```

**Output:**

```sh
2 3 5 7 11 13 17 19
```

### 12. Write a python program to find the factorial of a number using recursion.

```py
# factorial
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Driver code
num = 5
print("The factorial of", num, "is", factorial(num))
```

**Output:**

```sh
The factorial of 5 is 120
```

### 13. Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides).

```py
# right triangle
a = int(input("Enter the length of side a(base): "))
b = int(input("Enter the length of side b(height): "))
c = int(input("Enter the length of side c(hypotenuse): "))

def is_right_triangle(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False

if is_right_triangle(a, b, c):
    print("The triangle is a right triangle")
else:
    print("The triangle is not a right triangle")
```

**Output:**

```sh
Enter the length of side a(base): 5
Enter the length of side b(height): 5
Enter the length of side c(hypotenuse): 5
The triangle is a right triangle
```

### 14. Write a python program to define a module to find Fibonacci Numbers and import the module to another program.

```py
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

# driver code
n = int(input("Enter the number of terms: "))
fib(n)
```

**Output:**

```sh
Enter the number of terms: 10
1 1 2 3 5 8 13 21 34
```

### 15. Write a python program to define a module and import a specific function in that to another program.

### 19. Write a Python function to implement pow(x, n)

```py
# pow(x, n)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

# Driver code
x = float(input("Enter the base number: "))
n = int(input("Enter the power number: "))
print("The result is:", power(x, n))
```

**Output:**

```sh
Enter the base number: 5
Enter the power number: 2
The result is: 25
```

### 20. Write a Python class to reverse a string word by word.

```py
# reverse string word by word
def reverse_word(word):
    word_list = word.split()
    word_list.reverse()
    return " ".join(word_list)

# driver code
word = "Hello World"
print("The reversed word is:", reverse_word(word))
```

**Output:**

```sh
The reversed word is: World Hello
```

### 21. Python Program for finding remainder of array multiplication divided by n

```py
def remainder(arr, n):
    mul = 1

    for i in arr:
        mul  = mul * (i % n)

    return mul % n

# driver code
arr = [1, 2, 3, 4, 5]
n = 5
print("The remainder is:", remainder(arr, n))
```

**Output:**

```sh
The remainder is: 1
```

### 22. Python Program for cube sum of first n natural numbers

Print the sum of series 1 <sup>3</sup> + 2 <sup>3</sup> + 3 <sup>3</sup> + ... + n <sup>3</sup> till nth term

```py
# cube sum of first n natural numbers
def cube_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i ** 3

    return sum

# driver code
n = 5
print("The sum is:", cube_sum(n))
```

**Output:**

```sh
The sum is: 1395
```

### 23. Python program to check whether a number is Prime of not

```py
# check whether a number is Prime of not
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# driver code
num = 5
print("The number is:", num, "is", end=" ")
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")
```

**Output:**

```sh
The number is: 5 is Prime
```

### 24. Python Program to find area of a Circle

> Hint: Area = &pi; \* r <sup>2</sup> \
> where r is the radius of circle

```py
# Python program to find Area of a circle
def findArea(r):
    PI = 3.142
    return PI * r * r

r = int(input("Enter radius: "))
print("Area of circle is", findArea(r))
```

**Output:**

```sh
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

**Ouput:**

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

**Output:**

```sh
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

**Output:**

```sh
New list after removing all even numbers: [11, 5, 17, 23]
```

### 28. Python program to interchange first and last elements in a list

```py
# Python program to swap first and last elements of a list

# swap function
def swap(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

    return arr

# Driver code
arr = [11, 5, 17, 18, 23, 50]
print("Original list:", arr)
arr = swap(arr)
print("New list after swapping:", arr)
```

**Output:**

```sh
Original list: [11, 5, 17, 18, 23, 50]
New list after swapping: [50, 5, 17, 18, 23, 11]
```

### 29. Program to accept the strings which contains all vowels

```py
# Python program to accept the strings which contains all vowels

# function to check string
def check(string):
    # list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # iterate each vowel
    for volwel in vowels:
        # check if vowel is present in string
        if not volwel in string:
            return False
    return True

# Driver Code
if __name__ == '__main__':
    string = input("Enter string: ")
    if check(string):
        print("Accepted")
    else:
        print("Not Accepted")
```

**Output:**

```sh
Enter string: aa
Not Accepted
```

### 30. Convert Snake case to Pascal case

```py
# convert snake case to pascal case
# using title() + replace()

# initial string
string = "this_is_snake_case"

print("Original string:", string)

# Conver to pascal case
res = string.title().replace("_", "")

# print result
print("Pascal case:", res)
```

### 31. Conver a list of Tuples into Dictionary

```py
# Python code to conver a list of tuples into dictionary

def convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di

# Driver code
tup = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
di = {}
print(convert(tup, di))
```

**Output:**

```sh
{'a': [1], 'c': [3], 'b': [2], 'd': [4]}
```

### 32. Python program to sort a list of tuples by second item

```py
# Python program to sort a list of tuples by second item

# function to sort list of tuples
def sort_tuple(tup):

    # get length of list
    length = len(tup)
    for i in range(length):
        for j in range(0, length - i - 1):
            if tup[j][1] > tup[j + 1][1]:
                tup[j], tup[j + 1] = tup[j + 1], tup[j]

    return tup

# Driver code
tup = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print("Sorted list:", sort_tuple(tup))
```

**Output:**

```sh
Sorted list: [('a', 1), ('b', 2), ('d', 4), ('c', 3)]
```

### 33. Python program to check if a string is pallindrom or not

```py
# function to check if a string is pallindrom or not

def isPallindrome(string):
    return string == string[::-1]

# Driver code
string = "malayalam"
if isPallindrome(string):
    print("String is pallindrome")
else:
    print("String is not pallindrome")
```

**Output:**

```sh
String is pallindrome
```

### 34. Python program for sum of squares of first n natural numbers

```py
# Python program to sum of squares of first n natural numbers

def square_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum

# Driver code
n = 5
print("Sum of squares of first", n, "natural numbers is", square_sum(n))
```

**Output:**

```sh
Sum of squares of first 5 natural numbers is 55
```

# Exercise: Functions in python
1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
def calculate(base, height):
    area = (1/2)*base*height
    return area

2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
def calculate(base, height, shape):
    area = (1/2)*base*height
    if shape == "rectangle":
        area=length*width
     elif shape == "triangle"
        area = (1/2)*base*height
     return area
         
         
    
If no shape is supplied then it should take triangle as a default shape

3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
```
def print_pattern(input):
    for i in range(input):
        print((i+1) * "*")
*
**
***
```
if input is 4 then it should print
```
*
**
***
****
```
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

[Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/10_functions/10_functions_exercise.py)

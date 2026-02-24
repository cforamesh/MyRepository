
num = int(input("Enter a number : "))

# defining a function to compute factorial using recursion
"""
Recursion is a process in which a function calls itself till a certain condition is not met
Factorial of n => n * (n-1) * (n-2) * .... 2 * 1
n!
4! = 4 * 3 * 2 * 1 = 24

n! => n * (n-1) * (n-2) * ..... * 2 * 1
    => n * (n-1)!
    => n * (n-1) * (n-2)! ........

There are 2 parts to any recursive function
1. Base/terminal condition
2. Recursive condition
"""

def fact(num):

    if num < 0:
        return " not defined, being negative number"
    elif num == 0 or num == 1:
        return 1
    else:
        return num*fact(num-1)
# print(help(fact)) this statement can be used to provide help on how the function is going to calculate values


print(f"Factorial of Number {num} is {fact(num)}")

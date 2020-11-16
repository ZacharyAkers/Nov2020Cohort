# 1. Write a function called power which accepts a base and an exponent.
# The function should return the power of the base to the exponent.
# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent -1)
# result = power(2, 6)
# print(result)

# 2. Write a function factorial which accepts a number and returns
# the factorial of that number.  A factorial is the product of an
# interger and all the integers below it; eg. , factorial four( 4!) is
# equal to 24, because 4 * 3 * 2 * 1 equals 24.  factorial zero (0!) is always 1.
# def factorial(n):
#     if n == 1:
#         return n
#     return n*factorial(n-1)
# result = factorial(5)
# print(result)

# 3. Write a function called recursiveRange which accepts a number and adds up all
# the numbers from 0 to the number passed to the function
# def recursiveRange(n):
#     if n == 0:
#         return n
#     return n + recursiveRange(n-1)
# result = recursiveRange(4)
# print(result)

# 4. Write a recursive function called reverse which accepts
# a string and returns a new string in reverse
# def reverseString(string):
#     if len(string) == 0 :
#         return string
#     return reverseString(string[1:])+string[0]
# a = "hello"
# print(reverseString(a))

# 5. Write a recursive function called isPalindrome which returns
# true if the string passed to it is a palindrome (reads the same forward and backward).
# Otherwise returns false.
# def isPalindrome(word):
#     if len(word) <2:
#         return True
#     if word[0] !=word[-1]:
#         return False
#     return isPalindrome(word[1:-1])
# result= input("enter a word : ")
# print(isPalindrome(result))

# isPalindrome('awesome') // false
# isPalindrome('foobar') // false
# isPalindrome('tacocat') // true
# isPalindrome('amanaplanacanalpanama') // true
# isPalindrome('amanaplanacanalpandemonium') // false


# 6. Write  function called product ofArray which takes in
# an array of numbers and returns the product of them all
# productlist = [5,3,6,8,2]
# def ofArray(productlist):
#     if len(productlist)==1:
#         return productlist[0]
#     return ofArray([productlist[0]]) * ofArray(productlist[1:])
# print(ofArray(productlist))

# 7. Write a recursive function called fib which accepts a number and
# returns the nth number in teh Fibonacci Sequence. Recall that the
# Fibonacci Sequence is the Sequence of whole numbers 1, 1, 2, 3, 5, 8, ... which
# starts with 1 and 1, and where ever number
# thereafter is equal to the sum of the previous two numbers.
# def fib(n):
#     arr = [0, 1]
#     for i in range(2, n+1):
#         a = arr[i -1]
#         b = arr[i -2]
#         arr.append(a+b)
#     return arr[n]
# result = fib(5)
# print(result)

# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
# result = fib(5)
# print(result)
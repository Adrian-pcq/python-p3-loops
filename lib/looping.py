#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 10
    while num >0:
        print(num)
        num -= 1
        if num == 0:
            print ("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    square_ints = [int * int for int in int_list]
    return square_ints

def fizzbuzz():
    # code goes here!
    num = 1
    while num <= 100:
        if num % 3 == 0 and num %5 ==0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        
        else:print(num)
        num += 1           

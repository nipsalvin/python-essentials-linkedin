#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def function(n): #Defines function
    print(n) #

function(47) #Calls function

#Second function
def function2(n = 1): #assigns value 1 to variable n
    print(n)

function2() #prints n(1) is no arguments is declared
function2(60) #prints 60 because argument is declared

#third function
def function(n):
    print(n)
    return n * 2 #without this the program returns none

x = function(47)
print(x)

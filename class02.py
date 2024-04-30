#!/usr/bin/python3


def my_function(my_list = ["a", "b", "c"]):
    print(my_list)

#Loop through the argument list
def my_function(my_list = ["a", "b", "c"]):
    for element in my_list:
    print(element)

#Using the library datetime, print out current date and time
import datetime

#from datetime import date 

#print out the current time
import time
now = time.time()
print(now)

today = datetime.date.today()
print(today)


if __name__== "__main__":
    my_variable = [1, 2, 3, 4, 5]
    my_function(my_variable)
    my_function()
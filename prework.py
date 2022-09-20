#Question 1
# Write a funstion to print "Hello_USERNAME!" USERNAME is the input of the function. The first line of code has been defined as below. 
import numbers
from urllib.parse import MAX_CACHE_SIZE


def hello_name(user_name):
    print("Hello, " + user_name.title()+ "!")
hello_name('Kamaree')
 

#Question 2:
# Write a pthon function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    print(list(range(1,101,2)))
first_odds()


#Question 3:
# Please write a pthon function, max_num_in_list to return the max number of a given list. 
def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num
print(max_num_in_list([1,5,7,9,23]))

#Question 4:
#Write a function to return if the given year is a leap year a function returns the max number in a given list
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')

#question 5:
#Write a function to check ifall numbers in a list are consecutive
def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)
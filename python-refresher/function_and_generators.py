# coding=utf-8

# FUNCTIONS
# Example function 1: return the sum of two numbers.
def sum_redo(a, b):
    return a + b


# Example function 2: return the size of list, and modify the list to now be sorted.
def list_sort(my_list):
    my_list.sort()
    return len(my_list), my_list


# GENERATORS
# A generator becomes very useful when dealing with very large collections of data that you don’t want
# to store in memory all at once. It’s also very useful for dealing with extremely large or even infinite series.

# Below is an example of how to use a generator to print even numbers.
# Printing all even numbers at once would take an infinite amount of time,
# but the generator allows the process to pause, and go back to creating even numbers when needed.
# To create the next successive even number simply call next() on the generator object,
# and it will yield the next iteration. After yield is called,
# everything in the state of the generator function freezes, and the value is returned.
# When the generator is called again with next(), it picks back up right where it stopped at yield from before.

# Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2


my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

# Now go back to generating more even numbers.
for i in range(100):
    print(next(my_gen))


# The example above is showing the advantage of
# using a generator to be able to pause the process and be able to do other things.

# FUNCTION AND GENERATOR PRACTICE
# Exercise 1

# In the following exercise, you will create a generator fact_gen() that generates factorials.
# For a number n, n factorial is denoted by n!, and it is the product of all positive integers
# less than or equal to n. For example,

# 5! = 5 * 4 * 3 * 2 * 1 = 120

# In this exercise, you will define prod(a, b) which returns the product of numbers a and b.
# You will also define fact_gen() which yields the next factorial number.

def prod(a, b):
    # TODO change output to the product of a and b
    return a * b


def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        i += 1
        n = output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120

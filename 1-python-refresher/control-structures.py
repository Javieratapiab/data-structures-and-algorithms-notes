# ITERATION WITH LOOPS

# Examples of iteration with for loops.
my_list = [0, 1, 2, 3, 4, 5]

# Print each value in my_list. Note you can use the "in" keyword to iterate over a list.
for item in my_list:
    print('The value of item is: ' + str(item))

# Print each index and value pair
for i, value in enumerate(my_list):
    print('The index value is: ' + str(i) + '. The value at i is: ' + str(value))

# Print each number from 0 to 9 using a while loop.
i = 0
while i < 10:
    print(i)
    i += 1

# Print each key and dictionary value. Note that you can use the "in" keyword
# to iterate over dictionary keys.
my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
for key in my_dict:
    print(key + ', ' + my_dict[key])

# Remember that Python requires correct indentation for code blocks to be interpreted correctly.
# Indentation for a block is usually four spaces, or one tab length.

# What would be the output of the following code?
my_dict = {
    'a': [0, 1, 2, 3],
    'b': [0, 1, 2, 3],
    'c': [0, 1, 2, 3],
    'd': [0, 1, 2, 3]
}

i = 0
output = []
for key in my_dict:
    output.append(my_dict[key][i])
    i += 1
print(output)

# => [0, 1, 2, 3]

# CONDITIONAL STATEMENTS
num = 5
if num < 5:
    print('The number is smaller than 5.')
elif num == 5:
    print('The number is equals 5.')
else:
    print('The number is greater than 5.')


# => The number is equals 5.

# CONTROL STRUCTURE PRACTICE
# Exercise 1.
def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_pos = None
    for num in in_list:
        if num > 0:
            # Note: we use a logical "or" in this solution to form
            # the conditional statement, although this was
            # not introduced above.
            if smallest_pos is None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos


# Test cases
print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None

# Exercise 2. Now let's assume you are planning on taking some additional courses at your local educational
# institution, and you have acquired some data about the available courses and when they will be offered. In the
# following exercise, you will write control structures to process the data and return the semesters when a given
# course is offered. You will need to complete the function when_offered(courses, course). This function accepts a
# "courses" data structure and a "course" string. The function should return a list of strings representing the
# semesters when the input course is offered. See the two test cases below for examples of correct results. Since the
# when_offered function accepts a dictionary data structure, you will find the:

# for <key> in <dictionary>:
#    <block>

# This exercise uses a data structure that stores Udacity course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

courses = {
    'spring2020': {'cs101': {'name': 'Building a Search Engine',
                             'teacher': 'Dave',
                             'assistant': 'Peter C.'},
                   'cs373': {'name': 'Programming a Robotic Car',
                             'teacher': 'Sebastian',
                             'assistant': 'Andy'}},
    'fall2020': {'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                             'teacher': 'Dorina'},
                   'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                             'teacher': 'Jasper'},
                   }
}


def when_offered(courses, course):
    semesters = []
    # TODO: Fill out the function here.
    for semester in courses:
        if course in courses[semester]:
            semesters.append(semester)
    # TODO: Return list of semesters here.
    return semesters


print(when_offered(courses, 'cs101'))
# Correct result:
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result:
# []

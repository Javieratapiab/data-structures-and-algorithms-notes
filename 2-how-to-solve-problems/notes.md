# How to solve a problem? 📚

Avoid thinking about that particular problem, think in a general solution.

![alt Problem](resources/problem.png "Problem sentence")

Steps:

### 1. Understand the (computation) problem.

Problem is defined by possible inputs, and the relationship of them with the desired outputs.

### 2. Recognize the inputs (What are the inputs?).
In the `daysBetweenDate.ipynb` file:

- Inputs: two dates.
- Inputs representation: `daysBetweenDates(year1, month1, day1, year2, month2, day2):`

What is the set of valid inputs?
- Second date must not be before first date (Use defensive programming).
- Gregorian calendar (15 Oct 1582).

### 3. What are the outputs?.

> "Given your birthday and the current date, calculate your age in days"

Meaning: return a number giving the number of days between the first date, and the second date.


### 4. Work through some examples by hand.

We can work out some examples (test cases) to check if our program is correct.

In this case, we can start looking at the calendar and check the number of days.

> Hard example: Leap years

Sample:
```
    daysBetweenDate(2013,1,24,2013,6,9):
    Jan 24 - Jan 31     =  7
    + Feb               =  28
    + March             =  31
    + April             =  30
    + May               =  31
    + June 1-29         =  29
                          ----
                           156     
    # days in years
    2013                = 365
    2014
    ...
    2024                = 366  (leap year)
```

* #### Algorithm "pseudocode".

```
    days = # of days in month1 - day1
    month1 += 1
    while month1 < month2:`
        days += # of days in month1
        month1 += 1
    days += day2
    while year1 < year2:
        days += days in year 1
```

* #### Should we implement this algorithm?.

No, we should find a simpler way, AND it doesn't address all cases

**doesn't handle:**

    1. Inputs dates in same month.
    2. month2 < month1 if year2 > year1-
    3. Counting days in leap year.

Let's think the simpler way:

### 5. Simple mechanical algorithm (different approach).
```
    days = 0
    while date1 is before date2:
        date1 = advance to next day
        days += 1
```

![alt Quiz](resources/quiz-computation-time.png "Quiz computation time")

Maybe that is good enough. looks pretty fast initially.

### 6. Don't optimize prematurely! Simple and correct.

**What should we write first?**

Still, we want to break it down into simpler parts and make progress.

`nextDay(year,month,day) to get next day for a simple case.`

Define a procedure `nextDay(year,month,day)` that takes as input
a valid date in the Gregorian calendar encoded as the year, month,
and day as numbers, and returns the next day as a **year, month, day.**

> Assume: all months have 30 days!

```python
def nextDay(year, month, day):
    """Warning: this version incorrectly
    assumes all months have 30 days!"""
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
```

Using the Python console, we can start invoking some test cases
and check our results.

**What should we do next?**

[] refine `nextDay` to work correctly for real months.\
[X] define `daysBetweenDates` to give approximate answers using our `nextDay` procedure.\
[] go to beach and celebrate.

> Hint: start by defining a helper procedure

**Pseudocode**

```
    days = 0
    while date1 is before date2:
        date1 = advance to next day # We have this!
        days += 1
    return days
```

**Solution in Three Parts**

Well done for getting this far! The solution to this problem is broken down into three parts:

1) Step One Pseudocode
2) Step Two Helper Function
3) Step Three daysBetweenDates

It makes sense to have a helper procedure as follows:

```python
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
    year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False
```

According to that, we can replace this code in our pseudocode:

```
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
```

Now, we should try to make use of the **defensive programming**
to start using it when the inputs are invalid.

> Add an assertion to `daysBetweenDates` to give an assertion
> failure when the inputs are invalid: `assert<Expresion> False => fail`

```python
# Credit goes to Websten from forums
#
# Program defensively:
#
# What do you do if your input is invalid? For example what should
# happen when date 1 is not before date 2?
#
# Add an assertion to the code for daysBetweenDates to give
# an assertion failure when the inputs are invalid. This should
# occur when the first date is not before the second date.
#

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert(dateIsBefore(year1, month1, day1, year2, month2, day2) == True)

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result == answer and answer != "AssertionError":
                print("Test case passed!")
            else:
                print("Test with data:", args, "failed")

        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))
test()
```

### Real world problem

We are not getting the right answer, not all the months have 30 days. Let's see what should be the most
appropriate strategy to handle the rest of the problem:

[X] write stub `daysInMonth(year, month)` that always return 30.\
[X] modify `nextDay(year, month, day)` to use daysInMonth(year, month).\
[X] test `nextDay(year, month, day)` using stub daysInMonth.\
[X] modify `daysInMonth(year, month)` to be correct except for leap years.\
[X] test (again) `nextDay(year, month, day)` using stub daysInMonth.\
[X] write `isLeapYear(year)`.\
[X] test `isLeapYear(year)`.\
[X] test `daysBetweenDates(...)` for all test cases.

The order can change and still make sense. The property that they should have
(all the correct answers) is that you're writing small bits of code that you
can test independently as you go. You don't want to be writing a lot of code
and not being able to test it. **That's one of the most important things to learn
as a developer** is to think of ways to structure a code, to organize the way you build code,
so you're able to do meaningful tests as you go and see the code incrementally get closer to the solution
that you need for that.

**In conclusion: test as you go.**


# Efficiency

We said earlier that this Nanodegree program is about how to write code to solve problems and to do so **efficiently.**
In the last section, we looked at some basic aspects of solving problems—, but we didn't really think too much about whether our solutions were efficient.

## Space and time

When we refer to the efficiency of a program, we aren't just thinking about its speed—we're considering both the **time**
it will take to run the program, and the amount of **space** the program will require in the computer's memory.
Often there will be a trade-off between the two, where you can design a program that runs faster by selecting a
data structure that takes up more space—or vice versa.

**Notes**

- Efficiency also called **complexity** is how well you're using your computer's resources
to get a particular job done.
- **Space and time**. How long does your code take to run, and how much storage space do you need?

## Algorithms

> An algorithm is essentially a series of steps for solving a problem. Usually,
> an algorithm takes some kind of input (such as an unsorted list) and then produces the desired output
> (such as a sorted list).

For any given problem, there are usually many different algorithms that will get you to exactly the same end result.
But some will be much more efficient than others. To be an effective problem solver, you'll need to develop the ability
to look at a problem and identify different algorithms that could be used—and then contrast those algorithms to consider
which will be more or less efficient. But computers are so fast!

Sometimes it seems like computers run programs so quickly that efficiency shouldn't really matter. And in some cases,
this is true—one version of a program may take 10 times longer than another, but they both still run so quickly that it
has no real impact.

But in other cases, a small difference in how your code is written—, or a tiny change in the type of data structure you
use—can mean the difference between a program that runs in a fraction of a millisecond, and a program that takes hours
(or even years!) to run.

### Quantifying efficiency

It's fine to say "this algorithm is more efficient than that algorithm", but can we be more specific than that?
Can we quantify things and say how much more efficient the algorithm is?

Let's look at a simple example, so that we have something specific to consider.

**Question 1 of 3**

Here is a short (and rather silly) function written in Python:

```python
def some_function(n):
    for i in range(2):
        n += 100
    return n
```

What does it do? Adds 200 to the given input.

**Question 2 of 3**

Now how about this one?

```python
def other_function(n):
    for i in range(100):
        n += 2
    return n
```

What does it do?  Adds 200 to the given input.

**Question 3 of 3**

So these functions have exactly the same end result. But can you guess which one is more efficient?

Here they are next to each other for comparison:

```python
def some_function(n):
    for i in range(2):
        n += 100
    return n

def other_function(n):
    for i in range(100):
        n += 2
    return n
```

* `some_function` is more efficient.

Although the two functions have the exact same end result, one of them iterates many times to get to that result,
while the other iterates only a couple of times.

This was admittedly a rather impractical example (you could skip the for loop altogether and just add 200 to the input),
but it nevertheless demonstrates one way in which efficiency can come up.


### Counting lines

With the above examples, what we basically did was count the number of lines of code that were executed.
Let's look again at the first function:

```python
def some_function(n):
    for i in range(2):
        n += 100
    return n
```

There are four lines in total, but the line inside the for a loop will get run twice.
So running this code will involve running 5 lines.

Now let's look at the second example:

```python
def other_function(n):
    for i in range(100):
        n += 2
    return n
```

In this case, the code inside the loop runs 100 times. So running this code will involve running 103 lines!

Counting lines of code is not a perfect way to quantify efficiency, and we'll see that there's a lot more to it as we
go through the program. But in this case, it's an easy way for us to approximate the difference in efficiency
between the two solutions. We can see that if Python has to perform an addition operation 100 times, this will certainly
take longer than if it only has to perform an addition operation twice!

### Input Size and Efficiency

**Question 1 of 6**

Here's one of our functions from the last page:

```python
def some_function(n):
    for i in range(2):
        n += 100
    return n
```

Suppose we call this function and give it the value 1, like this:

`some_function(1)`

And then we call it again, but give it the input 1000:

some_function(1000)`

Will this change the number of lines of code that get run?

>No — the same number of lines will run in both cases.


**Question 2 of 6**

Now, here's a new function:

```python
def say_hello(n):
    for i in range(n):
        print("Hello!")
```

Suppose we call it like this:

`say_hello(3)`

And then we call it like this:

`say_hello(1000)`

Will this change the number of lines of code that get run?

> Yes — say_hello(1000) will involve running more lines of code.

This highlights a key idea:

> As the input to an algorithm increases, the time required to run the algorithm may also increase.

Notice that we said may increase. As we saw with the above examples,
input size sometimes affects the run-time of the program and sometimes doesn't—it depends on the program.

### The rate of increase

**Question 3 of 6**

Let's look again at this function from above:

```python
def say_hello(n):
    for i in range(n):
        print("Hello!")
```

Below are some different function calls. Match each one with the number of lines of code that will get run.

| Function call | How many lines get run? |
| ------------- |:-------------:|
| `say_hello(1)`    | 3 |
| `say_hello(2)`    | 4 |
| `say_hello(3)`    | 5 |
| `say_hello(4)`    | 6 |

**Question 4 of 6**

Here's another question about that same function (from the above exercise).
When we increase the size of the input n by 1, how many more lines of code get run?

> When n goes up by 1, the number of lines run also goes up by 1.

So here's one thing that we know about this function: As the input increases,
the number of lines executed also increases.

But we can go further than that! We can also say that as the input increases, the number of lines executed increases by
a proportional amount. Increasing the input by 1 will cause 1 more line to get run. Increasing the input by 10 will
cause 10 more lines to get run. Any change in the input is tied to a consistent, proportional change in the number of
lines executed. This type of relationship is called a linear relationship, and we can see why if we graph it:

![alt Linear graph](resources/linear-graph.png "Linear graph")

- The horizontal axis, n, represents the size of the input (in this case, the number of times we want to print `"Hello!"`).
- The vertical axis, N, represents the number of operations that will be performed. In this case, we're thinking of an
  "operation" as a single line of Python code (which is not the most accurate, but it will do for now).

We can see that if we give the function a larger input, this will result in more operations.
And we can see the rate at which this increase happens—the rate of increase is linear. Another way of saying this is
that the number of operations increases at a constant rate.

If that doesn't quite seem clear yet, it may help to contrast it with an alternative possibility—a function where the
operations increase at a rate that is not constant.

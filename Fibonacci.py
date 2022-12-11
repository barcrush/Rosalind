""" Fibonacci concept """
import timeit

def fib(num):
    """ Basic number series calculation """
    f0, f1 = 0, 1
    for i in range(num):
        f0, f1 = f1, f0 + f1
    print(f0, end="\n")

fib(10)

def fibonacci_loop_pythonic(number):
    old, new = 1, 1
    for itr in range(number - 1):
        tmpval = new
        new, old = old, old + tmpval
    print(new)
    return new

fibonacci_loop_pythonic(94)

def fib_rabbits_counts(month=int, rabbit=int):
    """ function that calculates the total number of rabbits in a
    given month based on their reproductive cycle"""
    parent, child = [1, 1]
    for idx in range(month - 1):
        child, parent = parent, parent + (child * rabbit)
    print(child)
    return child

fib_rabbits_counts(29, 4)

#run for n months, rabbits die after m months.
def mortal_rabbit_fib(i, j):   # i = running months till, j = months after rabbits die
    count = 2
    generations = [1, 1]
    # Seed the sequence with the 1 pair, then in their reproductive month.
    start = timeit.timeit()

    while (count < i):
        if count < j:
            generations.append(generations[-2] + generations[-1])
            # using the basic recurrence relation Fn = Fn-2 + Fn-1
        elif count == i or count == j:
            generations.append((generations[-2] + generations[-1]) - 1)
            # print("in base cases for newborns (1st+2nd gen. deaths)")
            # base cases for removing rabbits death in each generation (1 death in first two death gens)
        else:
            generations.append((generations[-2] + generations[-1]) - generations[-(j + 1)])
            # recurrence relation here, (Fn = Fn-2 + Fn-1) - Fn-(j+1)
        count += 1
    end = timeit.timeit()
    # total = start - end

    return generations[-1]


print(mortal_rabbit_fib(94, 10))

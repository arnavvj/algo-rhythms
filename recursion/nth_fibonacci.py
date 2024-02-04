# use dict/map to avoid duplicate recursion
fib_dict = {}

def getNthFib(n):
    # Write your code here.
    if n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        try:
            n_1 = fib_dict[n-1]
        except KeyError:
            n_1 = getNthFib(n-1)

        try:
            n_2 = fib_dict[n-2]
        except KeyError:
            n_2 = getNthFib(n-2)
            
        return  n_1 + n_2
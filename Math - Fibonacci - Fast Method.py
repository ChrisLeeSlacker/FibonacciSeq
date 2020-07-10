import timing

"""
Memoized recursion for efficiency: It can be memoized to improve speed. 
This example takes advantage of the fact that a default keyword 
argument is the same object every time the function is called, but normally you wouldn't use a 
mutable default argument for exactly this reason
"""


def mem_fib(n, _cache={}):
    """efficiently memoized recursive function, returns a Fibonacci number"""
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, mem_fib(n - 1) + mem_fib(n - 2))
    return n


for i in range(41):
    print(i, mem_fib(i))

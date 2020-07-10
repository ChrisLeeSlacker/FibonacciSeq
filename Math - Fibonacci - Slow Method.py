"""
Fibonacci Sequence: recursively
F(n) = F(n-1) + F(n-2)
F(0) = 0 and F(1) = 1
"""
import timing
"""
this exact representation of the mathematical definition is incredibly inefficient for 
numbers much greater than 30, because each number being calculated must also 
calculate for every number below it.
"""
def fibRec(num):
    if num > 1:
        return fibRec(num - 1) + fibRec(num - 2)
    return num

for i in range(41):
    print(i, fibRec(i))
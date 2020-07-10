"""
Getting the Nth number in the Fibonacci Sequence
The caching feature reduces the normal way of calculating Fibonacci series from
O(2^n) to O(n) by eliminating the repeats in the recursive tree of Fibonacci series.
"""
import sys

table = [0] * 1000


def Fib(n):
    if n <= 1:
        return n
    else:
        if table[n - 1] == 0:
            table[n - 1] = Fib(n - 1)
        if table[n - 2] == 0:
            table[n - 2] = Fib(n - 2)
        table[n] = table[n - 1] + table[n - 2]
        return table[n]


def main():
    while True:
        try:
            line = '=' * 20
            print(line)
            print('Enter a number : ')
            num = int(sys.stdin.readline())
            len_fib = str(Fib(num))
            print(34 * '=' + len(len_fib) * '=')
            print(f'= The {num}th Fibonacci number is: {len_fib} =')
            print(34 * '=' + len(len_fib) * '=')
        except ValueError:
            print('Only accepts integers!')
        except TypeError:
            print('Only accepts integers!')
        finally:
            choice = input('Want to do it for another number?:\n<Any Key> Yes | <X> Exit\n')
            if choice.lower() in {'x'}:
                break
            else:
                continue


"""The module is being run standalone by the user and we can do corresponding appropriate actions"""
if __name__ == '__main__':
    main()

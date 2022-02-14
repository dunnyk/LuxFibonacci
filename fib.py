
from pydoc import doc

from matplotlib import docstring


def checkFib(n):
    """A function that checks if a number is fibonacci

    Args:
        n (_type_): takes a variable and check if number is fibonacci
    """

    n=int(input("Enter the number: "))
    c=0
    a=1
    b=1
    if n==0 or n==1:
        print(f'Yes {n} is a fibonacci number')
    else:
        while c<n:
            c=a+b
            b=a
            a=c
        if c==n:
            print(f'Yes {n} is a fibonacci number')
        else:
            print(f'No {n} is not a fibonacci number')
checkFib('n')

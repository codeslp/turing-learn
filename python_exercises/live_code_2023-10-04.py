"""
calculate_factorial

Accepts positve integer

Returns factorial product of the integer- the product of all positive integers <= integer multiplied

Consider edge cases such as 0! which is 1 an only accept positive integers

iterate through range of int

save to a list

multiply all list elements together
"""

def calculate_factorial(n: int) -> int:
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError('Value must be positive.')
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return(factorial)
    
n = 5

print(calculate_factorial(n))

def recursive_factorial(m: int) -> int:
    if m == 0:
        return 1
    elif m < 0:
        raise ValueError('Value must be positive.')
    else: 
        return m * recursive_factorial(m-1)

m = 5
print(recursive_factorial(m))

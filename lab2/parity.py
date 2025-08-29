"""Module for checking if a number is even or odd."""


def parity(x):
    """
    Determine if a number is even or odd.
    
    Args:
        x (int): The number to check
        
    Returns:
        str: 'Partall' if even, 'Oddetall' if odd
    """
    if x % 2 == 1:
        return 'Oddetall'
    return 'Partall'


print('Tester parity... ', end='')
assert 'Partall' == parity(0)   # False
assert 'Oddetall' == parity(1)
assert 'Partall' == parity(42)
assert 'Oddetall' == parity(99)
print('OK')

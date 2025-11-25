def function1(x: int, div: int = 2) -> int:
    '''
    The function determines a natural user number is prime or not prime.
    If the number is prime, the function return 1, otherwise return 0.

    Args:
        x: User number
        
    Returns:
        int: 1 if user number is prime, otherwise 0
    '''
    if x == 1:
        return 0
    
    if x == div:
        return 1
    
    if x % div == 0:
        return 0
    
    return function1(x, div + 1)
    

if __name__ == '__main__':
    num = int(input('Введите число: '))
    print(function1(num))

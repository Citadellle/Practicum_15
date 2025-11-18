def degree5(n: int) -> int:
    '''
    Check if number is power of 5 and return the exponent.
    
    Args:
        n: Number
        
    Returns:
        int: Exponent if n is power of 5, otherwise -1
    '''
    if n == 1:
        return 0
    
    if n % 5 != 0 or n <= 0:
        return -1
    
    return 1 + degree5(n // 5)


if __name__ == '__main__':
    num = int(input('Введите натуральное число: '))
    print(degree5(num))
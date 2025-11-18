def ten_to_n(x: int, n: int) -> str:
    '''
    The function converts a natural number from decimal to n-th using recursion.
    
    Args:
        x: Decimal number
        
    Returns:
        str: n-th number as a string
    '''
    digits = '0123456789ABCDEF'
    
    if x == 0:
        return ''
    elif x < n:
        return digits[x]
    
    return ten_to_n(x // n, n) + digits[x % n]


if __name__ == '__main__':
    num = int(input('Введите число для перевода из ' \
                    'десятичной системы счисления в n-ричную: '))
    n = int(input('Введите систему счисления, в которую нужно ' \
                  'перевести число (от 2 до 16): '))
    print(ten_to_n(num, n))
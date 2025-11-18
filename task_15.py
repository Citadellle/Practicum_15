def ten_to_bin(x: int) -> str:
    '''
    The function converts a natural number from decimal to binary using recursion.
    
    Args:
        x: Decimal number
        
    Returns:
        str: Binary number as a string
    '''
    if x == 1:
        return '1'
    if x == 0:
        return ''   
    
    return ten_to_bin(x // 2) + str(x % 2)


if __name__ == '__main__':
    num = int(input('Введите число для перевода из десятичной ' \
                    'системы счисления в двоичную: '))
    print(ten_to_bin(num))
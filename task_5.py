def mod_number(a: int, b: int) -> int:
    '''
    The function find remainder of division of natural numbers using recursion.
    
    Args:
        a: Divisible
        b: Divider
        
    Returns:
        int: Remainder of a divided by b
    '''
    if a < b:
        return a
    
    return mod_number(a - b, b)


if __name__ == '__main__':
    divisible = int(input('Введите делимое - натуральное число: '))
    divider = int(input('Введите делитель - натуральное число: '))
    print(f'Остаток от деления числа {divisible} на число {divider}:',
          f'{mod_number(divisible, divider)}')
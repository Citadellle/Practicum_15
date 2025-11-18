def node(a: int, b: int) -> int:
    '''
    The function calculate largest common divisor for a and b using recursion.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        int: Largest common divisor of a and b
    '''
    if b == 0:
        return a
    
    return node(b, a % b)


if __name__ == '__main__':
    first_el = int(input('Введите первое натуральное число: '))
    second_el = int(input('Введите второе натуральное число: '))
    print(node(first_el, second_el))
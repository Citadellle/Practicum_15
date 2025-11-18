def count(a: int, b: int) -> int:
    '''
    The function counts the number of squares that can be cut off
    from the rectangle, each time cutting off the largest square.
    
    Args:
        a: First side rectangle
        b: Second side rectangle
        
    Returns:
        int: Number of squares
    '''
    if a == b:
        return 1
    
    if a > b:
        return 1 + count(a - b, b)
    else:
        return 1 + count(a, b - a)


if __name__ == '__main__':
    first_side = int(input('Введите длину первой стороны: '))
    second_side = int(input('Введите длину второй стороны: '))
    print(count(first_side, second_side))
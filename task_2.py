def count(n: int) -> int:
    '''
    The function calculate quantity of digits in natural number using recursion.
    
    Args:
        n: Number
        
    Returns:
        int: Quantity of digits in the number
    '''
    if n < 10:
        return 1
    
    return 1 + count(n // 10)


if __name__ == '__main__':
    print(count(int(input('Введите натуральное число: '))))
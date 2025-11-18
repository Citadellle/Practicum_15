def progress(a_1: float, r: float, n: int) -> float:
    '''
    The function find n-th term of arithmetic progression using recursion.
    
    Args:
        a1: First term of progression
        r: Difference of progression
        n: Number term to find
        
    Returns:
        float: n-th term of arithmetic progression
    '''
    if n == 1:
        return a_1
    
    return r + progress(a_1, r, n - 1)


if __name__ == '__main__':
    a_1 = float(input('Введите первый член арифметической прогрессии: '))
    r = float(input('Введите разность арифметической прогрессии: '))
    n = int(input('Введите номер искомого члена последовательности: '))
    print(progress(a_1, r, n))
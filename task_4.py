def sum_progress(a_1: float, r: float, n: int) -> float:
    '''
    The function find sum of first n terms of arithmetic progression using recursion.
    
    Args:
        a1: First term of progression
        r: Difference of progression
        n: Number of terms to sum
        
    Returns:
        float: Sum of first n terms of arithmetic progression
    '''
    if n == 1:
        return a_1
    
    return a_1 + sum_progress(a_1 + r, r, n - 1)

if __name__ == '__main__':
    a_1 = float(input('Введите первый член арифметической прогрессии: '))
    r = float(input('Введите разность арифметической прогрессии: '))
    n = int(input('Введите номер n-го члена последовательности: '))
    print(sum_progress(a_1, r, n))
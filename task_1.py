def pownum(a: float, n: int) -> float:
    '''
    The function calculate power of real number using recursion.
    
    Args:
        a: User number
        n: Power of number
        
    Returns:
        float: Result of exponentiation of n
    '''
    if n == 0:
        return 1
    
    return a * pownum(a, n - 1)


if __name__ == '__main__':
    num = float(input('Введите вещественное число: '))
    power = int(input('Введите степень числа (натуральное число): '))
    print(pownum(num, power))
def numbers(x: int) -> None:
    '''
    The function prints the digits of a natural number 
    line by line in reverse order using recursion.
    
    Args:
        x: Number to process
    '''
    if x < 10:
        print(x)
        return
    
    print(x % 10)

    numbers(x // 10)

if __name__ == '__main__':
    num = int(input('Введите число: '))
    numbers(num)
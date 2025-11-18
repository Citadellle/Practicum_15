def fib(k: int) -> int:
    '''
    The function calculate k-th term of Fibonacci sequence using recursion.
    
    Args:
        k: The index of a term in Fibonacci sequence
        
    Returns:
        int: k-th term of Fibonacci sequence
    '''
    if k in (0, 1):
        return k
    
    return fib(k - 1) + fib(k - 2)


if __name__ == '__main__':
    print(fib(int(input('Введите номер члена последовательности Фибоначи: '))))
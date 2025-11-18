def combin(n: int, k: int) -> int:
    '''
    The function calculate combinatorial combination C(n, k) using recursion.

    An n-by-k combinatorial combination is the number of ways to select k different 
    elements from a set of n elements, regardless of the order of the elements.
    
    Args:
        n: Total number of elements
        k: Number of elements of select
        
    Returns:
        int: Combinatorial combination C(n, k)
    '''
    if k == 0 or k == n:
        return 1
    
    # The second identity of combinations or Pascal's identity.
    return combin(n - 1, k - 1) + combin(n - 1, k)


if __name__ == '__main__':
    n = int(input('Сколько всего элементов: '))
    k = int(input(f'Сколько элементов необходимо выбрать из {n}: '))
    print(combin(n, k))
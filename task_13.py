def get_user_list() -> list:
    '''
    The function generates a list of integers entered in 
    one line separated by a space.
    
    Returns:
        list: List of numbers entered by the user
    '''
    user_list = [int(i) for i in input('Введите целочисленные ' \
    'элементы списка через пробел: ').split(' ')]

    return user_list


def odd_list(a: list, n: int = None) -> list:
    '''
    The function return list of odd numbers from original list using recursion.
    
    Args:
        a: List of numbers
        n: Length of list
        
    Returns:
        list: List of odd numbers
    '''
    if n == 0:
        return []
    
    other = odd_list(a[1:], n - 1)
    
    if a[0] % 2 == 0:
        return [a[0]] + other
    else:
        return other


if __name__ == '__main__':
    user_list = get_user_list()
    n = int(input('Сколько элементов в списке: '))

    print(odd_list(user_list, n))

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


def maxlist(a: list) -> int:
    '''
    The function find maximum element in list of integers using recursion.
    
    Args:
        a: List of numbers
        
    Returns:
        int: Maximum element in the list
    '''
    if len(a) == 1:
        return a[0]
    
    if a[0] > maxlist(a[1:]):
        return a[0]
    else:
        return maxlist(a[1:])


if __name__ == '__main__':
    user_list = get_user_list()
    print(maxlist(user_list))

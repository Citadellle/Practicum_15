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

    
def ind_maxlist(a):
    '''
    The function find maximum element in list of integers using recursion.
    
    Args:
        a: List of numbers
        
    Returns:
        int: Index of max element
    '''
    if len(a) == 1:
        return 0
    
    # Add 1, since each iteration we go deeper into the list by 1
    max_index_rest = ind_maxlist(a[1:]) + 1
    
    if a[0] > a[max_index_rest]:
        return 0
    else:
        return max_index_rest


if __name__ == '__main__':
    user_list = get_user_list()
    print(ind_maxlist(user_list))

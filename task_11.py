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


def ind_maxlist(a: list, 
                index: int = 0, 
                max_val = None, 
                max_index = None) -> int:
    '''
    The function find index of max element in user list using recursion.
    
    Args:
        a: List of numbers
        index: Index that the check starts from
        max_val: Max element in list
        max_index: Index of max element in list
        
    Returns:
        int: Index of max element
    '''
    if len(a) == 1:
        return index
    
    if index == len(a):
        return max_index

    if max_val is None or a[index] > max_val:
        max_val = a[index]
        max_index = index

    return ind_maxlist(a, index + 1, max_val, max_index)


if __name__ == '__main__':
    user_list = get_user_list()
    print(ind_maxlist(user_list))
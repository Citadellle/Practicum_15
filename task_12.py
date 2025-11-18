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

def search(a: list, x: int) -> int:
    '''
    The function search the number in user list using recursion.
    
    Args:
        a: List of numbers
        x: Number to search
        
    Returns:
        int: 1 if number found, 0 otherwise
    '''
    if a[0] == x:
        return 1
    
    return search(a[1:], x)


if __name__ == '__main__':
    user_list = get_user_list
    num_for_seacrh = int(input('Введите искомое число: '))
    print(search(user_list, num_for_seacrh))
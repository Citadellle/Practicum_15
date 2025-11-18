def simmetr(s: str, i: int, j: int) -> bool:
    '''
    The function determines whether the part of the string s is symmetrical, 
    starting with the i-th character and ending with the j-th.
    
    Args:
        s: User string
        i: Start index
        j: End index
        
    Returns:
        bool: True if symmetric, False if not symmetric
    '''
    if i >= j:
        return True
    
    if s[i] == s[j]:
        return simmetr(s, i + 1, j - 1)
    else:
        return False


if __name__ == '__main__':
    string = input('Введите строку: ')
    start_range = int(input('Введите индекс начала проверяемой подстроки: '))
    end_range = int(input('Введите индекс конца проверяемой подстроки: '))
    print(simmetr(string, start_range, end_range))
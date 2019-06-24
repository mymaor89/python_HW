def main():
    print(binary_search(4, [2, 3, 6, 100]))  # => False
    print(binary_search(4, [4, 6, 100]))  # => True
    print(binary_search(4, []))  # => False

def binary_search(num,a_list):
    """
    :param num: number to search in list
    :param a_list: list that we want to search num in
    :return: true if number is in list otherwise false
    """
    length = len(a_list)
    middle = length//2
    if length == 0:
        return False
    if num==a_list[middle]:
        return True
    elif num>a_list[middle]:
        return binary_search(num,a_list[middle+1:])
    else:
        return binary_search(num,a_list[0:middle])
    
main()

def main():
    print(is_balanced('(()()()())'))  # => True
    print(is_balanced('(((())))'))  # => True
    print(is_balanced('(()((())()))'))  # => True
    print(is_balanced('((((((())'))  # => False
    print(is_balanced('((())'))  # => False
    print(is_balanced('(())())))'))  # => False


def is_balanced(input):
    """
    :param input: string of parentheses
    :return: true if the string if the string is balanced otherwise false
    """

    if len(input)== 0:
        return True
    elif input[0] is ')':
        return False
    else:
        for i in range(1,len(input)):
            if input[i] is ')':
                return is_balanced(input[1:i]+input[i+1:])
        return False


main()

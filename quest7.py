def main():
    print(gcd(45, 54)) # => 9
    print(gcd(51, 100))  # => 1
    print(gcd(1071, 1029))  # => 21

def gcd(num1,num2):
    """
    :param num1: first number
    :param num2: second number
    :return: the greatest common divisor
    """
    if num2==0:
        return num1
    else:
        return gcd(num2,num1%num2)
main()

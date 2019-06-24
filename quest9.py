def main():
    print(babylonian(2))  # =>  1.414213562373095
    print(babylonian(101))  # =>  10.04987562112089
    print(babylonian(11))  # =>  3.3166247903554
    print(babylonian(100))  # =>  10


def babylonian(number):
    """
    :param number: number to find it's square root
    :return: the square root of the input number
    """
    guess=1
    for i in range (10):
        guess= (guess+number/guess)/2
    return guess
main()

def main():
    print(approx_pi(5))  # => 3.3396825396825403
    print(approx_pi(623)) # => 3.143197788992502


def approx_pi(iters):
    """
    :param iters: number of iterations
    :return: approximate value of Pi using the Leibniz formula for π
    """
    pi=0
    for i in range(iters):
        pi += ((-1)** i) / ((2 * i) + 1)
    return pi*4

main()

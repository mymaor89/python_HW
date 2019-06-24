def main():
    print(to_roman(1))
    print(to_roman(51))
    print(to_roman(199))
    print(to_roman(4123))


def to_roman(num):
    """
    :param num: Arabic number to convert to roman number
    :return: roman number
    """
    units = 'I'  # up to 3
    five = "V"
    tens = "X"  # up to 30
    fifty = "L"
    hundred = "C"  # up to 300
    fiveHundred = "D"
    thousand = "M"  # up to 4000
    num_of_thousands = num // 1000
    num_of_hundreds = (num // 100) % 10
    num_of_tens = (num // 10) % 10
    num_of_units = num % 10
    roman = ""
    for i in range(num_of_thousands):
        roman += thousand

    def add_to_string(output, ones_inner, five_inner, tens_inner, num_inner):
        if num_inner < 4:
            for i in range(num_inner):
                output += ones_inner
        elif num_inner == 9:
            output += ones_inner + tens_inner
        elif num_inner == 4:
            output += ones_inner + five_inner
        elif num_inner > 4:
            output += five_inner
            num_inner -= 5
            for i in range(num_inner):
                output += ones_inner
        return output

    roman = add_to_string(roman, hundred, fiveHundred, thousand, num_of_hundreds)
    roman = add_to_string(roman, tens, fifty, hundred, num_of_tens)
    roman = add_to_string(roman, units, five, tens, num_of_units)
    return roman


main()

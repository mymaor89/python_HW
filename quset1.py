def main():
    message = "THOSE WHO DARE TO FAIL MISERABLY CAN ACHIEVE GREATLY"
    shift = 7
    enc_message = encrypt(message, shift)
    print("encrypted: ", enc_message)
    print("original message: ", encrypt(enc_message, -shift))


def encrypt(msg, shift):
    """
    
    :param msg: String to encrypt with caesar's cypher
    :param shift: Number of shifts of new alphabet
    :return: encrypted string using caesar's cypher
    """
    msg_as_list = list(msg)

    for i in range(len(msg)):
        char_as_int = ord(msg_as_list[i])
        if char_as_int is not 32:
            char_after_shift = char_as_int + shift
            char_as_int_modulo = (char_after_shift - 65) % 26 + 65
            char_complete = chr(char_as_int_modulo)
            msg_as_list[i] = char_complete

    msg = "".join(msg_as_list)
    return msg
main()

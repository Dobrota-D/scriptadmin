def get_user_input():
    """
    Function that ask the User for a string
    :return: to the separation of each character
    """
    user_input = input("Entrez des caractères à convertir base64: ")
    seperate_char(user_input)


def seperate_char(user_input):
    """
    Function that separate all character in an array
    :param userInput: String from the user
    :return: to modification of each character to an ascii
    """
    char_list = []
    for x in user_input:
        char_list.append(x)
    char_to_ascii(char_list)


def char_to_ascii(char_list):
    """
    Function that modify each character element in the array to an ascii element
    :param char_list: Array of character
    :return: to modification of each ascii element to a binary element
    """
    index = 0
    while index < len(char_list):
        char_list[index] = ord(char_list[index])
        index += 1;
    ascii_to_binary(char_list)


def ascii_to_binary(ascii_list):
    """
    Function that modify each ascii element in the array to a binary element
    :param ascii_list: Array of ascii element
    :return: to modification of each binary element to a binary element on 8 Bits
    """
    index = 0
    while index < len(ascii_list):
        ascii_list[index] = str(int(bin(ascii_list[index])[2:]))
        index += 1
    binaryTo8Bits(charList)


def binary_to_8bits(binaryChar):
    """
    Function that convert binary list in 8bits list
    :param binaryList: Array of binary 8bits element
    :return: Array of 8bits list
    """
    binaryList2 = []
    for bnr in binaryList:
        x = bnr[::-1]  # this reverses an array
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        binaryList2.append(bnr)
    print(binaryList2)
    groupBinaries(binaryList2)


def group_binaries(binaryList):
    """
    take all binary 8bit and concatenate in one string
    :param binaryList: Array of 8bits elements
    :return: One String of all 8bits
    """
    binary_string = ""
    for binary in binary_list:
        binary_string += binary
    separateGroupBinariesIn6Bits(binary_string)
    


def separate_group_binaries_in6bits(binariesString):
    """

    :param binariesString:
    :return:
    """
    return True


def all_element_in_6bits(binaries6BitsList):
    """

    :param binaries6BitsList:
    :return:
    """
    return True


def six_bits_to_decimal(binary_6bits_char):
    """
    Transform each binary element of the array into its decimal value

    :param binary_6bits_char: array of 6bits binary elements
    :return: array of decimal values
    """

    for index, value in enumerate(binary_6bits_char):
        binary_6bits_char[index] = int(value, 2)

    decimal_to_base64(binary_6bits_char)


def decimal_to_base64(decimal_char):
    """
    Transform each decimal number by its value in base 64

    :param decimal_char: array of decimal values
    :return: array of base 64 elements
    """

    base64_table = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', '0', '1', '2', '3',
        '4', '5', '6', '7', '8', '9', '+', '/',
    ]

    for index, value in enumerate(decimal_char):
        decimal_char[index] = base64_table[(int(value))]

    base64_list_to_string(decimal_char)


def base64_list_to_string(base64_list):
    """
    Convert the base64List to a string

    :param base64_list: array of base64 elements
    :return: string
    """

    base64_string = ''.join(base64_list)
    complete_base64_string_to8(base64_string)


def complete_base64_string_to8(base64_string):
    """
    Complete the string with '=' to reach the nearest multiple of 8

    :param base64_string: string
    :return: base64 encoded string
    """
    nearest_multiple = ((len(base64_string) + 7) & (-8))

    for i in range(nearest_multiple - len(base64_string)):
        base64_string += '='

    print(base64_string)


get_user_input()

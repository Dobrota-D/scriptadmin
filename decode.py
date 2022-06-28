from os import sep

def get_user_input():
    """
    Function that ask the User for a string
    :return: to the separation of each character
    """
    user_input = input("Entrez des caractères en Base64 à décoder: ")
    delete_neutral_char(user_input)

def decode_base64(source, _output):
  delete_neutral_char(source)
    
def delete_neutral_char(user_input):
    """
    Delete all the '=' to get the orignal string base64
    :param user_input: string
    :return: Base64 encoded without '=' string
    """
    base64_string = user_input.replace("=",'')
    seperate_char(base64_string)
    
def seperate_char(base64_string):
    """
    Function that separate all character in an array
    :param base64_string: String 
    :return: an array with all character in the base64 string
    """
    base64_list = []
    for x in base64_string:
        base64_list.append(x)
    base64_to_decimal(base64_list)
    
def base64_to_decimal(base64_list):
    """
    Transform each base64 character by it's value in 

    :param base64_list: array of base64 elements
    :return: array of decimal elements
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


    for index, value in enumerate(base64_list):
       for base64_index, base64_value in enumerate(base64_table):
           if value == base64_value :
               base64_list[index] = base64_index

    decimal_to_6bits(base64_list)
    
def decimal_to_6bits(decimal_list):
    """
    Transform each decimal value of the array into its binary element

    :param decimal_list: sarray of decimal values
    :return: array of 6bits binary element
    """
    for index, value in enumerate(decimal_list):
        decimal_list[index] = str(int(bin(value)[2:]))

    all_element_in_6bits(decimal_list)
    
def all_element_in_6bits(binaries_6bits_list):
    """
    Add for the last 6bits in the array and complete by adding 0
    :param binaries_6bits_list: list of 6bits
    :return: array of complete 6bits list
    """
    for index, value in enumerate(binaries_6bits_list):
        length = len(value)
        value = value[::-1]
        while length < 6:
            value += '0'
            length +=1
        binaries_6bits_list[index] = value[::-1]

    group_binaries(binaries_6bits_list)

def group_binaries(binary_list):
    """
    take all binary 6bit and concatenate in one string
    :param binaryList: Array of 6bits elements
    :return: One String of all 6bits
    """
    binary_string = ''.join(binary_list)
    separate_group_binaries_in8bits(binary_string)
    
def separate_group_binaries_in8bits(binaries_string):
    """
    Take the string and convert it in list of 8bits
    :param binariesString: string of 6bits
    :return: array of 8bits string
    """
    x = 8
    binaries_8bits_list = [binaries_string[i: i + x] for i in range(0, len(binaries_string), x)]
    eigth_bits_to_binary(binaries_8bits_list)
    
def eigth_bits_to_binary(eigth_bits_list):
    """
    Function that convert binary list in 8bits list
    :param binaryList: Array of binary 8bits element
    :return: Array of 8bits list
    """
    if len(eigth_bits_list[len(eigth_bits_list)-1]) < 8:
        eigth_bits_list.pop(len(eigth_bits_list)-1)
    binary_to_ascii(eigth_bits_list)
    
def binary_to_ascii(binary_list):
    """
    Function that modify each binary element in the array to an ascii element
    :param ascii_list: Array of binary element
    :return: array of ascii element 
    """
    for index, value in enumerate(binary_list):
        binary_list[index] = int(value, 2)
        
    ascii_to_char(binary_list)

def ascii_to_char(ascii_list):
    """
    Function that modify each ascii element in the array to a char element
    :param char_list: Array of ascii element
    :return: Array of char element
    """
    for index, value in enumerate(ascii_list):
        ascii_list[index] = chr(value)
        
    char_list_to_string(ascii_list)
    
def char_list_to_string(char_list):
    """
    Convert the char array to a string
    :param char_list: array of char 
    :return: string
    """

    char_string = ''.join(char_list)
    print(char_string)
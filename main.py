

def getUserInput():
    """
    Function that ask the User for a string
    :return: to the separation of each character
    """
    userInput = input("Entrez des caractères à convertir base64: ")
    seperateChar(userInput)

def seperateChar(userInput):
    """
    Function that separate all character in an array
    :param userInput: String from the user
    :return: to modification of each character to an ascii
    """
    charList = []
    for x in userInput:
        charList.append(x)
    charToAscii(charList)

def charToAscii(charList):
    """
    Function that modify each character element in the array to an ascii element
    :param charList: Array of character
    :return: to modification of each ascii element to a binary element
    """
    index = 0
    while index < len(charList):
        charList[index] = ord(charList[index])
        index += 1;
    asciiToBinary(charList)

def asciiToBinary(charList):
    """
    Function that modify each ascii element in the array to a binary element
    :param charList: Array of ascii element
    :return: to modification of each binary element to a binary element on 8 Bits
    """
    index = 0
    while index < len(charList):
        charList[index] = str(int(bin(charList[index])[2:]))
        index += 1;
    binaryTo8Bits(charList)

def binaryTo8Bits(binaryList):
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

def groupBinaries(binaryList):
    """
    take all binary 8bit and concatenate in one string
    :param binaryList: Array of 8bits elements
    :return:
    """
    return True;

def separateGroupBinariesIn6Bits(binariesString):
    """

    :param binariesString:
    :return:
    """
    return True;

def allElementIn6Bits(binaries6BitsList):
    """

    :param binaries6BitsList:
    :return:
    """
    return True;

def sixBitsToDecimal(binary6BitsChar):
    """
    Transform each binary element of the array into its decimal value

    :param binary6BitsChar: array of 6bits binary elements
    :return: array of decimal values
    """
    
    for index, value in enumerate(binary6BitsChar):
      binary6BitsChar[index] = int(value,2)
      
    decimalToBase64(binary6BitsChar)
      
def decimalToBase64(decimalChar):
    """
    Transform each decimal number by its value in base 64

    :param decimalChar: array of decimal values
    :return: array of base 64 elements
    """
    
    base64Table = [
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
      'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
      'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
      't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',
      '2', '3', '4', '5', '6', '7', '8', '9', '+',
      '/'
    ]
    
    for index, value in enumerate(decimalChar):
      decimalChar[index] = base64Table[(int(value))]
      
    base64ListToString(decimalChar)
    

def base64ListToString(base64List):
    """
    Convert the base64List to a string

    :param base64List: array of base64 elements
    :return: string
    """
    
    base64String = ''.join(base64List)
    completeBase64StringTo8(base64String)
    

def completeBase64StringTo8(base64String):
    """
    Complete the string with '=' to reach the nearest multiple of 8

    :param base64String: string
    :return: base64 encoded string
    """
    nearestMultiple = ((len(base64String) + 7) & (-8))
    
    for i in range(nearestMultiple - len(base64String)):
      base64String += '='
      
    print(base64String)

getUserInput()

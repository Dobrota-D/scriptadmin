
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
    print(charList)
    return True;

def binaryTo8Bits(binaryChar):
    """

    :param binaryChar:
    :return:
    """
    return true;

def groupBinaries(binaryList):
    """

    :param binaryList:
    :return:
    """
    return true;

def separateGroupBinariesIn6Bits(binariesString):
    """

    :param binariesString:
    :return:
    """
    return true;

def allElementIn6Bits(binaries6BitsList):
    """

    :param binaries6BitsList:
    :return:
    """
    return true;

def sixBitsToDecimal(binary6BitsChar):
    """

    :param binary6BitsChar:
    :return:
    """
    return true;

def decimalToBase64(decimalChar):
    """

    :param decimalChar:
    :return:
    """
    return true;

def base64ListToString(base64List):
    """

    :param base64List:
    :return:
    """
    return true;

def completeBase64StringTo8(base64String):
    """

    :param base64String:
    :return:
    """
    return true;

getUserInput()
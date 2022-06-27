# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def askYear():
    yearInput = input("Entrez une année à vérifier (ou X pour quitter): ");
    isLeapYear(yearInput)

def isLeapYear(year):
    if (year=="X"):
        print("Au revoir 👋")
        exit()
    year = int(year)
    if(year%4==0 and year%100!= 0 or year%400==0):
        print("C'est une année bissextile")
    else:
        print("Ce n'est pas une année bissextile")
    askYear()

askYear()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

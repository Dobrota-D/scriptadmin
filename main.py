# Une année est bissextile si elle respecte l'un des deux critaires suivants.
# L'année est divisible par 4 sans être divisible pas 100
# L'année est divisible par 400


def print_year():
    yearInput = int(input("Enter your year to know if is a leap year"));
    leapyear(yearInput)

def leapyear(year):
    if(year%4==0 and year%100!= 0 or year%400==0):
        print("is an leap year")
    else:
        print("is not and leap year")
    print_year()

print_year()


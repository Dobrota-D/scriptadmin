def is_leap_year(year):
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    return True
  return False
  
def script_loop():
  quit = False
  while quit != True:
    year = input('\nEntrer une année (q pour quitter) : ')

    if (year == 'q'): quit = True
    elif (year.isdigit() == False): print(f"'{year}' n'est pas une entrée correcte")
    elif is_leap_year(int(year)): print(f'{year} est une année bissextile')
    else: print(f'{year} n\'est pas une année bissextile')
    
script_loop()
import os
os.system('cls')

import datetime 
_now = datetime.datetime.now()
current_year = _now.year
# print(current_year)

# age calculator
birth_year = int(input("Enter Your Birth Year : "))
print(f"Your Age is : {current_year - birth_year}")
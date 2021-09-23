print("""

#                                                                                                                         
#   .oPYo.                                                  8   .oPYo.                                    o               
#   8    8                                                  8   8    8                                    8               
#  o8YooP' .oPYo. .oPYo. .oPYo. o   o   o .oPYo. oPYo. .oPYo8   8      .oPYo. odYo. .oPYo. oPYo. .oPYo.  o8P .oPYo. oPYo. 
#   8      .oooo8 Yb..   Yb..   Y. .P. .P 8    8 8  `' 8    8   8   oo 8oooo8 8' `8 8oooo8 8  `' .oooo8   8  8    8 8  `' 
#   8      8    8   'Yb.   'Yb. `b.d'b.d' 8    8 8     8    8   8    8 8.     8   8 8.     8     8    8   8  8    8 8     
#   8      `YooP8 `YooP' `YooP'  `Y' `Y'  `YooP' 8     `YooP'   `YooP8 `Yooo' 8   8 `Yooo' 8     `YooP8   8  `YooP' 8     
#  :..::::::.....::.....::.....:::..::..:::.....:..:::::.....::::....8 :.....:..::..:.....:..:::::.....:::..::.....:..::::
#  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::8 :::::::::::::::::::::::::::::::::::::::::::::::::::
#  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..:::::::::::::::::::::::::::::::::::::::::::::::::::
""")

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for _ in range(nr_letters):
    password.append(random.choice(letters))
for _ in range(nr_symbols):
    password.append(random.choice(symbols))
for _ in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
generated_password = ""
for a in password:
    generated_password += a

print(f"Generated Password: {generated_password}")
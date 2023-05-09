import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_input = int(input("How many letters would like in your password? "))
print(letters_input)
symbols_input = int(input("How many Symbols would you like? "))
print(symbols_input)
numbers_input = int(input("How many numbers would you like? "))
print(numbers_input)

password_list = []

for char in range(1, letters_input + 1):
    randnon_char = random.choice(letters)
    password_list += randnon_char
    

for sym in range(1, symbols_input + 1):
    password_ran = random.choice(symbols)
    password_list += password_ran
    

for num in range(1, numbers_input + 1):
    random_num = random.choice(numbers)
    password_list += random_num



   
random.shuffle(password_list)    


password_string = ""

for str in password_list:
    password_string += str








print(f"Here is your password {password_string}")


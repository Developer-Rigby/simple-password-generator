
class password_criteria:
    def __init__(self, char_length, caps, symbols, numbers):
        self.char_length = char_length
        self.caps = caps
        self.symbols = symbols
        self.numbers = numbers

def criteria():
    char_length = input("How many characters will your password be: ")
    
    caps = input("Do you want your password to have caps? y/n: ")
    if caps == "y":
        bool_caps = 1
    elif caps == 'n':
        bool_caps = 0
    else:
        print("Invalid. Please try again.")
    
    symbols = input("Do you want your password to contain symbols? y/n: ")
    if symbols == 'y':
        bool_symbols = 1
    elif symbols == 'n':
        bool_symbols = 0
    else:
        print("invalid. Please try again.")

    numbers = input("Do you want your password to contain numbers? y/n: ")
    if numbers ==  'y':
        bool_numbers = 1
    elif numbers == 'n':
        bool_numbers = 0
    else:
        print("Invalid. Please try again.")

    user_criteria = password_criteria(char_length, bool_caps, bool_symbols, bool_numbers)
    return user_criteria


test = criteria() 
print(test.char_length, test.caps, test.symbols, test.numbers)
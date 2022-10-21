import random
#Defining the password criteria class. Used to bundle the data for the specifics of the password.

class password_criteria:
    def __init__(self, char_length, caps, symbols, numbers):
        self.char_length = char_length
        self.caps = caps
        self.symbols = symbols
        self.numbers = numbers

    def criteria():
        char_length = input("How many characters will your password be: ")
        
        bool_caps = None
        while bool_caps == None:
            caps = input("Do you want your password to have caps? y/n: ")
            if caps == "y":
                bool_caps = True
            elif caps == 'n':
                bool_caps = False
            else:
                print("Invalid. Please try again.")
        
        bool_symbols = None
        while bool_symbols == None:
            symbols = input("Do you want your password to contain symbols? y/n: ")
            if symbols == 'y':
                bool_symbols = True
            elif symbols == 'n':
                bool_symbols = False
            else:
                print("invalid. Please try again.")

        bool_numbers = None
        while bool_numbers == None:
            numbers = input("Do you want your password to contain numbers? y/n: ")
            if numbers ==  'y':
                bool_numbers = True
            elif numbers == 'n':
                bool_numbers = False
            else:
                print("Invalid. Please try again.")

        user_criteria = password_criteria(char_length, bool_caps, bool_symbols, bool_numbers)
        return user_criteria

#I honestly have no idea if this is good practise but I'm only really differentiating it this way
class characters:
    characters = {
        "caps" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "lowercase" : "abcdefghijklmnopqrstuvwxyz",
        "symbols" : "!@#$%^&*()",
        "numbers" : "1234567890"
        }

    def caps_true():
        capsString = ""
        capsString = capsString + characters.characters["caps"]
        return capsString

    def symbol_true():
        symbolString = ""
        symbolString = symbolString + characters.characters["symbols"]
        return symbolString
    
    def numbers_true():
        numbersString = ""
        numbersString = numbersString + characters.characters["numbers"]
        return numbersString

def create_password():
    choose_criteria = password_criteria.criteria() #This allows the user to select the criteria for their password.
    if choose_criteria.caps == True:
        caps_string = characters.caps_true()
    else:
        caps_string = ""
    #These are seperate as they're different conditions
    if choose_criteria.numbers == True:
        numbers_string = characters.numbers_true()
    else:
        numbers_string = ""
    #These are seperate as they're different conditions
    if choose_criteria.symbols == True:
        symbols_string = characters.symbol_true()
    else:
        symbols_string = ""

    non_randomised_string = caps_string + numbers_string + symbols_string

    non_randomised_list = list(non_randomised_string)

    randomised_list = random.shuffle(non_randomised_list)
    return randomised_list
    

foo = create_password()
print(foo)

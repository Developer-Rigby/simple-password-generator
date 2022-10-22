import random
#Defining the password criteria class. Used to bundle the data for the specifics of the password.
class password_criteria:
    def __init__(self, char_length, caps, symbols, numbers):
        self.char_length = char_length
        self.caps = caps
        self.symbols = symbols
        self.numbers = numbers

    def criteria():
        char_length = None
        while isinstance(char_length, int) != True:
            try: #DAMN. This worked? Seems like a weird way to do it but im proud of it.
                char_length = int(input("How many characters will your password be: "))
            except ValueError:
                print("Value not an integer. Try again.")
        
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

    #Some code to handle shuffling 
    non_randomised_string = caps_string + numbers_string + symbols_string
    shufflelist = list(non_randomised_string)
    #random.shuffle shuffles in place which is confusing as hell. It's why we reuse the indentifier.
    random.shuffle(shufflelist)
    randomised_list = shufflelist

    #randomised_string = ''.join(randomised_list)

    #Now we're going to quickly use the char_length we asked for before:
    character_length = int(choose_criteria.char_length)
    randomised_list_result = randomised_list[0:character_length]

    result = ''.join(randomised_list_result)

    return result

def main():
    #splash screen
    print("                                     _                 ")
    print("  _ __  __ _ _______ __ _____ _ _ __| |  __ _ ___ _ _  ")
    print(" | '_ \/ _` (_-<_-< V  V / _ \ '_/ _` | / _` / -_) ' \ ")
    print(" | .__/\__,_/__/__/\_/\_/\___/_| \__,_| \__, \___|_||_|")
    print(" |_|                                    |___/          ")

    #options to create password or exit
    print("1. Generate a password.")
    print("2. Exit...")
    option = input("Please select an option: ")
    match option:
        case '1':
            password = create_password()
            print("Generating Password...")
            print("Password: " + password)
        case '2':
            print("Hope you enjoyed this little project :)")
            exit()

main()
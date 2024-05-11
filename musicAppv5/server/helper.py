# module contains miscellaneous functions

class helper():
    # function parses a string and converts to appropriate type
    @staticmethod
    def convert(value):
        types = [int,float,str] # order needs to be this way
        if value == '':
            return None
        for t in types:
            try:
                return t(value)
            except:
                pass

    # function reads file path to clean up data file
    @staticmethod
    def data_cleaner(path):
        with open(path,"r",encoding="utf-8") as f:
            data = f.readlines()

        data = [i.strip().split(",") for i in data]
        data_cleaned = []
        for row in data[:]:
            row = [helper.convert(i) for i in row]
            data_cleaned.append(tuple(row))
        return data_cleaned

    # function checks for user input given a list of choices
    @staticmethod
    def get_choice(lst):
        choice = input("Enter: ")
        while choice.isdigit() == False:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")

        while int(choice) not in lst:
            print("Incorrect option. ")
            choice = input("Try again: ")
        return int(choice)



    #adding a method to make just the song is in the dataBase
    @staticmethod
    def get_choiceName(songs):
        choice = input("")
        choice = choice.lower()
        while choice not in songs:
            print("Incorrect option Try again")
            choice = input("Enter your choice: ")
            choice = choice.strip()
        return choice

    # function prints a list of strings nicely
    @staticmethod
    def pretty_print(lst):
        print("Results..\n")
        for i in lst:
            print(i)
        print("")

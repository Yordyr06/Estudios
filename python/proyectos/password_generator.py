import random
import string


def password_gen():
    upper = (string.ascii_uppercase)
    lower = (string.ascii_lowercase)
    digits = (string.digits)
    symbols = (string.punctuation)
    caracters = upper + lower + digits + symbols
    password = []
    
    for i in range(16):
        choising = random.choice(caracters)
        password.append(choising) 
    password = "".join(password)
    return password
        

def run ():
    input("This is a password generator"
        " press Enter to continue")
    password = password_gen()
    input("Your new password is:   " + password + "   press Enter to continue")
    answers = input("""
        Do you want another password?:
        Type Y for yes
        Type N for No
        Answer: """)

    while answers != "y" or "n":
        if answers == "y":
            password = password_gen()
            input("Your new password is:   " + password + "   press Enter to continue")
            answers = input("""
            Do you want another password?:
            Type Y for yes
            Type N for No
            Answer: """)

        elif answers == "n":
            input("See you latter")
            break
        else:
            answers = input("Invalid answer, plis type a correct answer: ")
    

if __name__ == "__main__":
    run()
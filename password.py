import string
import random

logo = """
______                                          _                                         _               
| ___ \                                        | |                                       | |              
| |_/ /__ _  ___  ___ __      __ ___   _ __  __| |   __ _   ___  _ __    ___  _ __  __ _ | |_  ___   _ __ 
|  __// _` |/ __|/ __|\ \ /\ / // _ \ | '__|/ _` |  / _` | / _ \| '_ \  / _ \| '__|/ _` || __|/ _ \ | '__|
| |  | (_| |\__ \\__ \ \ V  V /| (_) || |  | (_| | | (_| ||  __/| | | ||  __/| |  | (_| || |_| (_) || |   
\_|   \__,_||___/|___/  \_/\_/  \___/ |_|   \__,_|  \__, | \___||_| |_| \___||_|   \__,_| \__|\___/ |_|   
                                                     __/ |                                                
                                                    |___/                                                 
"""

def passwordgenerator(n,s,d):
    res = [] 
    alpha = string.ascii_letters
    num = string.digits
    special = string.punctuation

    if s+d <= n:
        for i in range(s):
            res.append(random.choice(special))
        for i in range(d):
            res.append(random.choice(num))
        for i in range(n-s-d):
            res.append(random.choice(alpha))
        random.shuffle(res)
        print(''.join(res))
    else:
        print("Invalid length is given ")



if __name__=="__main__":
    print(logo)
    while True:

        print("\n1.generate a password")
        print("2.Exit")
        choice = input("enter your choice : ")
        if choice == "1":
            n=int(input("Enter the length of the password :  "))
            s=int(input("enter the number of special characters : "))
            d=int(input("enter number of digits : "))
            print()
            passwordgenerator(n,s,d)
        elif choice == "2":
            print("\nEXITING .......\n")
            break
        else:
            print("Invalid Choice. please select valid option ..\n")










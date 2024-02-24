logo='''
   _____        _               _         _               
  / ____|      | |             | |       | |              
 | |      __ _ | |  ___  _   _ | |  __ _ | |_  ___   _ __ 
 | |     / _` || | / __|| | | || | / _` || __|/ _ \ | '__|
 | |____| (_| || || (__ | |_| || || (_| || |_| (_) || |   
  \_____|\__,_||_| \___| \__,_||_| \__,_| \__|\___/ |_|   
                                                          
                                                          
'''


def calculator(expression):
    try:
        result = eval(expression)
        return result
    
    except Exception as e:
        return "invalid expression is given\n\n"




if __name__=="__main__":
    print(logo)

    while True:
        print("\n1. Evaluate the expression")
        print("2. Exit\n\n")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            expression = input("Enter an expression to evaluate:  ")
            print("Result: ", calculator(expression),"\n\n")

        elif choice == '2':
            print("EXITING.........\n\n")
            break
        else:
            print("invalid choice. Please select the correct option..")
        


# a. fatima chatbot
print("Welcome to the Elite 101 Prototype Chatbot")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Welcome " + name + ", " + "how can I help you today?\n")

def menu(name, age):
    option = 0
    while option != 4:
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Exit ")
        option = int(input("Please select an option (1, 2, 3, 4): "))
        
        # check which option the user selected
        if option == 1:
            print("Option #1 under development\m")
        elif option == 2:
            print("Option #2 under development\n")
        elif option == 3:
            print("Option #3 under development\n")
        elif option == 4:
            print("Conversation has ended. Goodbye, " + name)
        else:
            print("Invalid Input. Try again\n")

    '''
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit ")
    option = int(input("Please select an option (1, 2, 3, 4): "))
    
    # check which option the user selected
    if (option == 1):
        print("Option #1 under development")
    elif (option == 2):
        print("Option #2 under development")
    elif (option == 3):
        print("Option #3 under development")
    elif (option == 4):
        print("Conversation has ended. Goodbye, " + name)
   
    else:
        print("Invalid Input. Try again")
'''
# display menu 
menu(name, age)


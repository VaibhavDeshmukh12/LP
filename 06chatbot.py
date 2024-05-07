print("Hello Customer, I am Ann")
print("You may ask your queries to me about our product")
print("And I shall answer your questions :)\n")

input("Enter your registered mobile number to verify and access me:")

while True:
    print("\nWELCOME!!\nPlease tell me how shall I assist you\n1.Complaint about product\n2.Feedback on a product\n3.Connect to a customer executive")

    query = int(input())
    
    if query == 1:
        print("1.Shoes\n2.Shirts\n3.Pants\n4.Watches")
        pro = input("Please choose which category of product you are referring to: ")
        
        if pro == "1":
            pro = "Shoes"
        elif pro == "2":
            pro = "Shirts"
        elif pro == "3":
            pro = "Pants"
        elif pro == "4":
            pro = "Watches"
            
        mod = input("Please enter the model number (if possible): ")
        comp = input(f"Tell us your complaint about {mod} {pro}: ")
        
        print(f"Thank You, We have successfully received your complaint about {mod} {pro}")
        print("We will take action on your complaint ASAP")

    elif query == 2:
        print("1.Shoes\n2.Shirts\n3.Pants\n4.Watches")
        pro = input("Please choose which category of product you are referring to: ")
        
        if pro == "1":
            pro = "Shoes"
        elif pro == "2":
            pro = "Shirts"
        elif pro == "3":
            pro = "Pants"
        elif pro == "4":
            pro = "Watches"
            
        mod = input("Please enter the model number (if possible): ")
        rev = int(input(f"How much will you rate for the {mod} {pro}? (1-5): "))
        
        if rev > 0 and rev < 3:
            ch = input("Well, That's some poor rating, would you like to tell us what we should improve? (Y/N): ")
            if ch.lower() == 'y':
                print("Thanks, that's a much appreciated response. Please register your complaint in the Complaint section.")
            else:
                print("Nevermind.")
        elif rev >= 3 and rev <= 5:
            print("We are glad you like our product. Thanks for your support.")

    elif query == 3:
        print("Connecting to an available executive")

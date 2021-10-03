correctness = False
  
while True:
  
    a = input("Is Weezer bad? (yes/no): ")
    
    if a == "no":
        
        print("Well, your opinion is wrong. Please try again.")
        
        while True:
            
            a = input("Is Weezer bad? (type yes): ")
            
            if a == "yes":
                
                correctness = True
                print("Correct")
                break
                
            elif a == "no":
                
                print("Wrong")
                continue
            
            else:
                
                print("That's not one of the options")
                continue
            
        if correctness == True:
            
            break
            
    elif a == "yes":
        
        print("You have impeccable taste.")
        break
        
    else:
        
        print("That's not one of the options. Try again.")
    
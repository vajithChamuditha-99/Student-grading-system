passmark=0 # declaring variables
defer=0
fail=0
all=0
def all():
        try: #this won't let strings to pass
            while True: 
                passmark=int(input("Enter the Pass mark   :")) # getting the user's passmark
                if passmark == 0 or passmark == 20 or passmark == 40 or passmark == 60 or passmark == 80 or passmark == 100 or passmark == 120:
                    while True:
                        defer=int(input("Enter the Defer mark  :")) # getting the user's defermark
                        if defer == 0 or defer == 20 or defer == 40 or defer == 60 or defer == 80 or defer == 100 or defer == 120:

                            while True:
                                fail=int(input("Enter the fail mark   :")) # getting the user's failmark
                                if fail == 0 or fail == 20 or fail == 40 or fail == 60 or fail == 80 or fail == 100 or fail == 120:
                                    tot = passmark + defer + fail
                                    if tot == 120:  # checking whether total of enterted marks are equal to 120
                                        if passmark ==120:
                                            print ("progress")       #printing outputs
                                        elif passmark==100:
                                            print ("Progress-module treiler\n")
                                        elif fail >= 80:
                                            print("Exclude")
                                        else:
                                            print("Do not progress-module retriever\n")
                                    else:
                                        print("Total Incorrect")   #printing errors
                                        all()
                                else:
                                    print("Range error\n")
                                    all()
                                break
                        else:                                      
                            print("Range error\n")      
                            all()
                        break
                else:
                    print("Range error\n")
                    all()
                break
        except ValueError: #checking integer errors
            print("Integer error")
            all()
all()    
    

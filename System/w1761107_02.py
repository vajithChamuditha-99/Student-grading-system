passmark=0 # declaring variables 
defer=0
fail=0

def rotate(): #printing horizontal histogram
    rotate=str(input("press Q to exit Press any key to continue:-"))
    if rotate == "Q" or rotate == "q":
        print("Progress",prog, ":",("* "*prog))
        print("Trailing",treil, ":",("*"*treil))
        print("Retriver",dont, ":",("*"*dont))
        print("Excluded",exclude, ":",("*"*exclude))
        print(prog + dont + treil + exclude ,"Outcomes in total\n\n")
    else:
        all()
prog=0
dont=0
treil=0
exclude=0        
def all():
    global prog
    global dont
    global treil
    global exclude
    try:  # This won't let strings to pass 
        while True:  # the loop which runs inifinte time while the condition comes true
            passmark=int(input("Enter the Pass mark   :")) #getting the marks from the user
            if passmark == 0 or passmark == 20 or passmark == 40 or passmark == 60 or passmark == 80 or passmark == 100 or passmark == 120:
                while True:
                    defer=int(input("Enter the Defer mark  :"))
                    if defer == 0 or defer == 20 or defer == 40 or defer == 60 or defer == 80 or defer == 100 or defer == 120:
                        while True:
                            fail=int(input("Enter the fail mark   :"))
                            if fail == 0 or fail == 20 or fail == 40 or fail == 60 or fail == 80 or fail == 100 or fail == 120:
                                tot = passmark + defer + fail
                                if tot == 120:# checking whether enterted marks are equal to 120 
                                    if passmark ==120:
                                        print ("progress\n\n")
                                        prog += 1
                                        rotate ()
                                    elif passmark==100:
                                        print ("Progress-module treiler\n\n")    #printing outputs
                                        treil += 1
                                        rotate()
                                    elif fail >= 80:
                                        print("Exclude")
                                        exclude += 1
                                        rotate()
                                    else:
                                        print("Do not progress-module retriver\n\n")
                                        dont += 1
                                        rotate()
                                else:
                                    print("Total Incorrect")
                                    all()
                            else:
                                print("Do not progress module retriver\n\n")
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
        print("Integers required\n")
        all()
all()

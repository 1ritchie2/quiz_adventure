# Our quiz!
score = 0

def quiz():
    global score

    score = 0
    
    question1()
    question2()
    finalscore()
    




def question1():
    global score
    
    print("Who is the best Presidential candidate?")
    print(",") 
    print("Hillary Clinton")
    print(",")
    print("Jill Stein")
    print(",") 
    print("Bernie Sanders")
    print(",") 
    print("Donald Trump")
    answer = input("Enter one of the above: ")
    if answer == "Donald Trump":
        score = score + 1000000
        print("You my friend have sense and for that, you will recieve... A SMALL LOAN OF  1000000 POINTS!")

    if answer == "Hillary Clinton":
        score = score - 1000000
        print("WHY?!?!?!?! You help Hillary pay off her fines for federal crimes and pay 1000000!")        
     
    if answer == "Bernie Sanders":
        print("No response...") 

    if answer == "Jill Stein":
        print("?")

    if answer == ",":
          print("Ha,very smart answer properly next time...")
    elif answer == " ":
          print("Thats not an answer!!!")




def question2():
    global score
    
    print("What is Donald Trumps slogan?")
    print("A. Make America great again")
    print("B. Feed the poor support the needy")
    print("C. I will build the wall!")
    answer = input("A, B or C? Enter one here: ")

    if answer == ("A"):
        score = score + 1000
        print("Correctamondo! +1000 points!")

    else:
        print("WRONGGG!!")





def finalscore():
    global score
    print("This is your final score!", score)
    

  

        

    

       
        


   





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()

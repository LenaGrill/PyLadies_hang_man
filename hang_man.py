def word_generator(a, b, c):
    """ This function will randomly return one out of three words"""
    from random import randrange

    word_nr = randrange(3) # random numbers between 1 and 3 will be generated
    if word_nr == 0:    # random numbers will be allocated to three different words
        word = a
    elif word_nr == 1:
        word = b
    elif word_nr == 2:
        word = c
    return word

def evaluate_position(chosen_letter, word):
    """ this for loop returns a list res with the positions of the chosen_letter """
    res = []
    for i in range(0, len(word)): 
        #print(i)
        if word[i] == chosen_letter:
            res = res + [i + 1]     
    return res  

def evaluate_letter(status, res, chosen_letter):
    """ This function evaluates, if the chosen_letter is contained in the given word 
    and replaces underline by the chosen_letter"""
    if res == []: # if list res is empty, the chosen letter is not contained in the word
        print("Wrong letter!")
        # print(status)         
    else: # if res is not empty, the chosen letter is contained
        print("Strike!")
        status2 = ""
        for position in range(0, len(status)):
            letter_position = position + 1
            if letter_position in res:
                status2 = status2 + status[position].replace("_", chosen_letter)
            else:
                status2 = status2 + status[position]
        status = status2
    return status
                          
def evaluate_status(status):
    if "_" in status:
        move_on = True
    else:
        print("You won!")
        move_on = False
    return move_on 

def hang_man():
    word = word_generator("lalalala", "lelelele", "lililili") # calls the word generator to randomly choose one of these words
    status = "_" * len(word) # a status with the length of the chosen word will be generated
    print(status)
    move_on = True
    while move_on == True:
        chosen_letter = str(input("Please select a letter: "))
        # print(chosen_letter)
        if len(chosen_letter) == 1: # in case input is a single letter, continue:
            res = evaluate_position(chosen_letter, word)   
            # print(res)
            status = evaluate_letter(status, res, chosen_letter)
            print(status)
            move_on = evaluate_status(status)   
       
        else:
            print("Please enter a single letter!")
            move_on = True

hang_man()
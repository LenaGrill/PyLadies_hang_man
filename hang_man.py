def word_generator(a, b, c):
    """ This function randomly returns one out of three words"""
    from random import randrange

    word_nr = randrange(3) # random numbers between 1 and 3 are generated
    if word_nr == 0:    # random numbers are allocated to three different words
        word = a
    elif word_nr == 1:
        word = b
    elif word_nr == 2:
        word = c
    return word

def evaluate_position(chosen_letter, word):
    """ this for loop returns a list result with the positions of the chosen_letter """
    result = []
    for i in range(0, len(word)): 
        #print(i)
        if word[i] == chosen_letter:
            result = result + [i + 1]     
    return result  

def evaluate_letter(status, result, chosen_letter):
    """ This function evaluates, if the chosen_letter is contained in the given word 
    and replaces underscore by chosen_letter"""
    
    if result == []: # if list res is empty, the chosen letter is not contained in the word
        print("Wrong letter!")
        # print(status)
        unsuccessful_try = True        
    else: # if res is not empty, the chosen letter is contained
        print("Strike!")
        status2 = ""
        for position in range(0, len(status)):
            letter_position = position + 1
            if letter_position in result:
                status2 = status2 + chosen_letter # status[position].replace("_", chosen_letter)
            else:
                status2 = status2 + status[position]
        status = status2
        unsuccessful_try = False
            
    return (status, unsuccessful_try)
                          
def evaluate_status(status):
    """This function evaluates the status of the replaced underscores and returns,
    if the game is finished or is still on"""
    if "_" in status:
        move_on = True
    else:
        print("You win!")
        move_on = False
    return move_on 

# def move_count(word, status, move_on):
#     """ This function counts all the moves and returns the evaluation status"""
#     for move in range(9):
#         chosen_letter = str(input("Please select a letter: "))
#         # print(chosen_letter)
#         if len(chosen_letter) == 1: # in case input is a single letter, continue:
#             result = evaluate_position(chosen_letter, word)   
#             # print(result)
#             status = evaluate_letter(status, result, chosen_letter)
#             print(status)
#             print("This was move number: ", move + 1)
#         else:
#             print("Please enter a single letter!")
#             print("This was move number: ", move + 1)
#         move_on = evaluate_status(status)
#         if move_on == False:
#             break
    
def make_move(word, status, move_on):
    """ This function asks for an input letter, calls positional and letter evaluation, 
    only counts unsuccessful tries, evaluates the status and returns move_on """
    miss_count = 0
    while miss_count < 9:
        chosen_letter = str(input("Please select a letter: "))
        chosen_letter = chosen_letter.lower()
        # print(chosen_letter)
        if len(chosen_letter) == 1: # in case input is a single letter, continue:
            result = evaluate_position(chosen_letter, word)   
            # print(result)
            status, unsuccessfull_try = evaluate_letter(status, result, chosen_letter)
            print(status)
            if unsuccessfull_try == True:
                miss_count = miss_count + 1
                print("This was unsuccessful try number: ", miss_count)
            # else:
                # miss_count = miss_count
        else:
            print("Please enter a single letter!")
        move_on = evaluate_status(status)
        if move_on == False:
            break
    return move_on


def hang_man():
    """ This is the function for the actual hang_man using and calling all the functions above. 
    """
    word = word_generator("lalinea", "pyladies", "awesome") # calls the word generator to randomly choose one of these words
    status = "_" * len(word) # generates a status with the length of the chosen word
    print(status)
            
    move_on = True
    while move_on == True:
        move_on = make_move(word, status, move_on)   # move_count(word, status, move_on)
        # print(move_on)
        if move_on == False:
            break
        else:
            print("You loose!")
            break
    
hang_man()


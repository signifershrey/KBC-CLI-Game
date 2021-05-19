from questions import QUESTIONS


def isAnswerCorrect(question, ans):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    if(question["answer"] == ans):
        return True
    return False


def lifeLine(ques):


    # :param ques: The question for which the lifeline is asked for. (Type JSON)
    # :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    
    print("BE CAREFUL ------ 50-50 lifeline will  provided to with two options in which one option is correct and another one is wrong!! \n")

    correctoption = ques["answer"]    
    option1ToDelete = 0
    option2ToDelete = 0
    

    if(correctoption == 1 or correctoption == 2):
        option1ToDelete = "option3"
        option2ToDelete = "option4"
        
    elif(correctoption ==3 or correctoption == 4):
        option1ToDelete = "option1"
        option2ToDelete = "option2"
                 
       
    del ques[option2ToDelete]
    del ques[option1ToDelete]

    return ques
    # 2 incorrect  options were  to be deleted 


def finalreward(i,finalprize):
    if(i>=11):
        finalprize=320000
    elif(i>=5):
        finalprize = 10000
    else:
        # finalprize =0
        msg = "You won total  prize money of : {} "
        print('-----------------------------------')
        print(msg.format(finalprize))
        print('-----------------------------------\n')
    


def kbc(minprize,lifeline):
    '''
        Rules to play KBC:
        # * The user will have 15 rounds
        # * In each round, user will get a question
        # * For each question, there are 4 choices out of which ONLY one is correct.
        # * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        # * Each correct answer get the user money corresponding to the question and displays the next question.
        # * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        # * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        # * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks


   
    totalprize = minprize
    
    for i in range(0,len(QUESTIONS)):
        print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

        while(ans not in ["1","2","3","4","lifeline","quit"]):
            print("Please Choose a correct option")
            ans = input('Your choice ( 1-4 ) : ')

        if(ans.lower() == "lifeline"):
            if(lifeline > 0):
                print(f'You have {lifeline}  Lifeline left\n')
                q = lifeLine(QUESTIONS[i])
                updateans1 = 0
                if((q["answer"] == 1) or (q["answer"] == 2)):
                    print(f'\tQuestion {i+1}: {q["name"]}' )
                    print(f'\t\tOptions:')
                    print(f'\t\t\tOption 1: {q["option1"]}')
                    print(f'\t\t\tOption 2: {q["option2"]}')
                    updateans1 = input('Your choice ( 1-2 ) : ')
                elif((q["answer"] == 3) or (q["answer"] == 4)):
                    print(f'\tQuestion {i+1}: {q["name"]}' )
                    print(f'\t\tOptions:')
                    print(f'\t\t\tOption 3: {q["option3"]}')
                    print(f'\t\t\tOption 4: {q["option4"]}')
                    updateans1 = input('Your choice ( 3-4 ) : ')
                lifeline = 0 
                ans = updateans1
            else:
                print("Sorry, You don't have any LIFELINE left :( \n" )
                print("Now , you can either guess the correct answer or quit the game :)")
                updatedans = input('What do you want to go with ?')
                ans = updatedans

       
        if(ans.lower()=="quit"):
            finalreward(i,totalprize)
            break
        
    
    # check for the input validations

        if isAnswerCorrect(QUESTIONS[i], int(ans)):
        # print the total money won.
        # See if the user has crossed a level, print that if yes
            print('\nCorrect !\n')
            if(i+1 ==5):
                print('---------------------------')
                print('You have crossed FIRST LEVEL .')
                print('---------------------------\n')
            elif(i+1 ==11):
                print('---------------------------\n')
                print('You have crossed SECOND LEVEL.\n') 
                print('---------------------------\n') 
            else:
                print('') 
            totalprize = minprize + QUESTIONS[i]["money"]
            msg = "Your Current prize money is : {} \n"
            print(msg.format(totalprize))

        else:
        # end the game now.
        # also print the correct answer
        
            print('\nIncorrect !\n')
            print(f'The correct answer is : {QUESTIONS[i]["answer"]}\n')
            # msg = "You won total  prize money of : {} \n"
            # print(msg.format(totalprize))
            finalreward(i,minprize)
            break

    # print the total money won in the end.


print("Welcome to Kaun Banega Crorepati! \n")
print("Toh Chaliye Suru karte hain --------\n")
minimumprize = 0 
lifeline = 1
kbc(minimumprize,lifeline)

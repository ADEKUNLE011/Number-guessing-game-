#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random
def number_guessing_game():
    while True:
        try:
            counter = 0
            print('Welcome to guessing game. LEVEL 1 ACTIVATED')
            print('\n')
            while True:
                play = int(input('play by entering a number within 1 to 15: '))
                number_generator = random.randint(1,15)
                print(f'Number generated is: {number_generator}')
                counter= counter + 1
                print(f'you have played the game {counter} times')
                if play == number_generator:
                    print(f'you won, the number you guessed is {play}')
                    print('you are done with level 1. Congratulations')
                    print('\n')
                    counter = 0
                    print('Welcome to guessing game. LEVEL 2 ACTIVATED')
                    while True:
                        play = int(input('play by entering a number within 1 to 40: '))
                        number_generator = random.randint(1,40)
                        print(f'Number generated is: {number_generator}')
                        counter= counter + 1
                        print(f'you have played the game {counter} times')
                        if play == number_generator:
                            print(f'you won, the number you guessed is {play}')
                            print('you are done with level 2. Congratulations')
                            print('\n')
                            counter = 0
                            print('Welcome to guessing game. LEVEL 3 ACTIVATED')
                            while True:
                                play = int(input('play by entering a number within 1 to 60: '))
                                number_generator = random.randint(1,60)
                                print(f'Number generated is: {number_generator}')
                                counter= counter + 1
                                print(f'you have played the game {counter} times')
                                if play == number_generator:
                                    print(f'you won, the number you guessed is {play}')
                                    print('you are done with level 3. Congratulations')
                                    print('\n')

                                    break
                                else:
                                    if counter ==2: 
                                        print('you have exceeded your trials')
                                        break
                                    else:
                                        print('you guessed a wrong number, try again')
                                        print('\n')
                                        continue
                                break
                        else:
                            if counter == 3: 
                                print('you have exceeded your trials')
                                print('\n')
                                break
                            else: 
                                print('you guessed a wrong number, try again')
                                print('\n')
                                continue
                        break
                else:
                    if counter == 4: 
                        print('you have exceeded your trials')
                        print('\n')
                        break
                    else:
                        print('you guessed a wrong number, try again')
                        print('\n')
                        continue
                break
        except ValueError: 
            print('enter only numbers without other characters')
            print('\n')


# In[ ]:


number_guessing_game()


# In[ ]:





import random
l = ['Rock','Paper', 'Scissor']
'''
 Rock vs paper > wins paper
 Rock vs scissor > wins Rock
 scissor vs paper > wins scissor 
'''
while True:
    Ccount =0
    ucount = 0
    uc = int(input('''
Game start....
1. yes.                   
2. No Exit.
                                                         
 '''))
    if uc==1:
        for a in range(1,6):
            userinput = int(input('''
1. Rock
                         
2. Scissor
                                 
3. Paper                                 
                        '''))
            
            if userinput == 1:
                uchoice ="Rock"
            elif userinput == 2:
                uchoice ="Scissor"
            elif userinput == 3:
                uchoice ="Paper" 
            Cchoice = random.choice(l)
            if Cchoice == uchoice:
                print("Computer value:",Cchoice)
                print("user value:",uchoice)
                print("Game draw:")  
                ucount = ucount + 1
                Ccount = Ccount + 1
            elif(uchoice == 'Rock' and Cchoice =='Scissor') or (uchoice =='paper' and Cchoice =='Rock' ) or (uchoice =='Scissor' and Cchoice =='Paper'): 
                print("Computer value:",Cchoice)
                print("user value",uchoice)
                print("you win")
                ucount = ucount + 1

            else:
                print("Computer value",Cchoice)
                print("user value",uchoice)
                print("Computer win")
                Ccount = Ccount + 1
                if ucount == Ccount :
                     print("Computer computer",Ccount)
                     print("user score",ucount)
                     print("Final game draw.......")

                elif ucount > Ccount:
                     print("Computer score",Ccount)
                     print("user value",ucount)
                     print("Final you win the game")     
                else:
                    print("Computer score",Ccount)
                    print("user value",ucount)
                    print("computer win the game") 

                  
        else:
           break



boat_side = "Right"
Missionaries_on_right = 3
Cannibals_on_right = 3
Missionaries_on_left = 0
Cannibals_on_left = 0   

print( 'M =',Missionaries_on_left,'🧑', 'C =',Cannibals_on_left,'👹', '|------🚤|', 'M =',Missionaries_on_right,'🧑',  'C =', Cannibals_on_right,'👹' ) 

#To make more interactive i added emojis insted of emojis we can use UNICODE also.
#Here are the UNICODE for emojis used in this project
#\U0001F9D1 → 🧑
#\U0001F479 → 👹
#\U0001F6A4 → 🚤

while True: # to play game in loop until user losse or Win ! 

    Missionaries = int(input("No Of Missionaries -🧑 or Enter 5 To Quit :"))

    if Missionaries == 5:
        print("You Quit. Game is Over")
        break
    Cannibals = int(input("No of Cannibals -👹:"))

    if (Missionaries + Cannibals) !=1 and (Missionaries + Cannibals) != 2:
           print(" Invalid Move")
           continue
    if boat_side == "Right":
        #if Missionaries_on_right < Missionaries or Cannibals_on_right < Cannibals :  - if we use this condition then user can enter negative value and it will show invalid move
        if Missionaries < 0 or Cannibals < 0 or Missionaries + Cannibals > 2:
            print(" Invalid Move")
         
        Missionaries_on_right = Missionaries_on_right - Missionaries 
        Cannibals_on_right = Cannibals_on_right - Cannibals

        Missionaries_on_left = Missionaries_on_left + Missionaries
        Cannibals_on_left = Cannibals_on_left + Cannibals

        print('M =', Missionaries_on_left,'🧑', 'C =',Cannibals_on_left,'👹', '|🚤-----|', 'M =', Missionaries_on_right,'🧑','C =', Cannibals_on_right,'👹')
       
        boat_side = 'Left'

    else:         
        if Missionaries_on_left < Missionaries or Cannibals_on_left < Cannibals :
            print ("invalid Move ")
            continue
        
        Missionaries_on_left = Missionaries_on_left - Missionaries
        Cannibals_on_left = Cannibals_on_left - Cannibals

        Missionaries_on_right = Missionaries_on_right + Missionaries
        Cannibals_on_right = Cannibals_on_right + Cannibals

        print('M=', Missionaries_on_left,'🧑', 'C =', Cannibals_on_left,'👹', '|-----🚤|', 'M =', Missionaries_on_right,'🧑', 'C =', Cannibals_on_right,'👹')
        boat_side = 'Right'

    if (Missionaries_on_right < Cannibals_on_right and Missionaries_on_right > 0 ) or (Missionaries_on_left < Cannibals_on_left and Missionaries_on_left > 0):
        print("You Loose The Game")
        break  #if user losse the game loop will break and user will have to start again 
        
        #Winning Condition
    if (Missionaries_on_left == 3 and Cannibals_on_left == 3):
         print("You Win The Game")
         break  #if user win the game loop will break and user will have to start again
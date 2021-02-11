# Game: SOLITARIE
# Group #1
# Date:Feb/15/2021
# Students:
#  Gabriel A. Roman Tapia COE #85157
#  NAME #student ID
#  NAME #student ID


from graphics      import *
from Card_Movement import *

def main():
  #DECLARATION VARIABLE AREA  
  CM = Card_Movement()
  Undo = Undo_Botton(CM.getWindow())
  G="Game"
  Power="On"
  TUIC=0
  while Power == "On":
   #---graphic user interface menu here----
   #      CODE HERE
   #-------------------------------

  
   #---user interface menu here----
   
   
   # 
   #  Options Start Game      (Starts the game  press # or insert the desired input)
   #  high scores             (optional I think press # or insert the desired input )
   #  Description of the game ( do in a README file and read it there. This also will be used to describe the gam
   #                           the profesor press # or insert the desired input)
   #  Quit game
      while TUIC == 0:#(THIS IS TO AVOID INSERTING A WRONG TECHNICAL INPUT that would crash our program, like a string instead of an integer)
       try:
          
         Input=Input=int(input("Insert your Option: "))
         TUIC=1
         
       except:
         print("Please enter a number not a word.")#This can be changed depending on what answer you want from the user.  
   # 
   #-------------------------------
   #if user selected start game from the GUI or the TUI "Text User Interface"
     while  G == "Game": #infinite loop for the game (indent this code completly when you start working with the conditions.) 
  
  
      CM.Card_Move(Undo)
  
      Over=CM.Window.checkKey()
    
      if Over == "":
        pass
      else:
        G="Over"

    
    CM.Window.close()
   #elif high scores:
   #elif game description:
   #elif quit game:
   #else: "sorry your answer is not correct" (This would be if you recieve a answer that is out of your scope of the options
   #                                          of this game.)


  


main()
    

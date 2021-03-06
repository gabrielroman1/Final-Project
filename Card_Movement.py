from graphics import *
from cards import *
from button import *

class Card_Movement(Cards):
  
  """This class is based on how the game will move the cards from
     all the GUI. It contains when the card can be moved, where can it stay,
     when it returns to the place it was before or accept the place the user
     put it in.
  """
  def __init__(self,win, center, width, height, types, number, color):
    
    super().__init__(win, center, width, height, types, number, color)
    self.MOVE=0
    self.condition=0

    self.Card_Mov=Point(0,0)
    

  def getpos(self):
      return self.pos
  def setCardMove(self,MOVE):
    self.Card_Mov=MOVE
  def setcondition(self):
    if self.condition == 0:
      self.condition=1
    else:
      self.condition=0
    
  def Cards_Move(self,FoundationPile,column,deck):
    
    """Movement of the card"""
    
    link=self.down_link
    if self.MOVE == 0 and link == 0:  
      self.rect.undraw()
      self.rect.setOutline("yellow")
      self.rect.setWidth(5)
      self.rect.draw(self.win)
      self.MOVE=1
    elif self.MOVE == 0 and link != 0:
      self.rect.undraw()
      self.rect.setOutline("yellow")
      self.rect.setWidth(5)
      self.rect.draw(self.win)
      register=self.getsavedown_register()
      while link != 0:
        
        deck[register].rect.undraw()
        deck[register].rect.setOutline("yellow")
        deck[register].rect.setWidth(5)
        deck[register].rect.draw(self.win)
        link=deck[register].getdown_link()
        register=self.getsavedown_register()
      self.MOVE=1
      
    elif self.MOVE == 1 and self.condition == 1 and self.down_link == 0: #If I select a place where I can move the card or cards
       
           self.rect.move((self.Card_Mov.getX()-self.rect.getCenter().getX()),((self.Card_Mov.getY()-self.rect.getCenter().getY())-20))
           self.frontCard.move((self.Card_Mov.getX()-self.frontCard.getAnchor().getX()),(self.Card_Mov.getY()-self.frontCard.getAnchor().getY()-20))
           self.frontCard.undraw()
           self.rect.undraw()
           self.rect.setOutline("black")
           self.rect.setWidth(1)
           self.rect.draw(self.win)
           self.frontCard.draw(self.win)
           self.condition=0
           self.MOVE=0
    elif self.MOVE == 1 and self.condition == 1 and self.down_link != 0: #If I select a place where I can move the card or cards   
           link=self.down_link
           self.rect.move((self.Card_Mov.getX()-self.rect.getCenter().getX()),((self.Card_Mov.getY()-self.rect.getCenter().getY())-20))
           self.frontCard.move((self.Card_Mov.getX()-self.frontCard.getAnchor().getX()),(self.Card_Mov.getY()-self.frontCard.getAnchor().getY()-20))
           self.frontCard.undraw()
           self.rect.undraw()
           self.rect.setOutline("black")
           self.rect.setWidth(1)
           self.rect.draw(self.win)
           self.frontCard.draw(self.win)
           inc=20
           register=self.getsavedown_register()
           while link != 0:
             deck[register].rect.move((self.rect.getCenter().getX()-deck[link].rect.getCenter().getX()),((self.rect.getCenter().getY()-deck[register].rect.getCenter().getY())-inc))
             deck[register].frontCard.move((self.rect.getCenter().getX()-deck[register].frontCard.getAnchor().getX()),(self.rect.getCenter().getY()-deck[register].frontCard.getAnchor().getY()-inc))
             deck[register].frontCard.undraw()
             deck[register].rect.undraw()
             deck[register].rect.setOutline("black")
             deck[register].rect.setWidth(1)
             deck[register].rect.draw(self.win)
             deck[register].frontCard.draw(self.win)
             link=deck[register].getdown_link()
             register=deck[register].getsavedown_register()
             #inc=inc+20
           self.condition=0
           self.MOVE=0
    else:
         if link == 0:
           self.rect.move(0,0)
           self.frontCard.move(0,0)
           self.rect.undraw()
           self.frontCard.undraw()
           self.rect.setOutline("black")
           self.rect.setWidth(1)
           self.rect.draw(self.win)
           self.frontCard.draw(self.win)
           self.MOVE=0
         else:
           self.rect.move(0,0)
           self.frontCard.move(0,0)
           self.rect.undraw()
           self.frontCard.undraw()
           self.rect.setOutline("black")
           self.rect.setWidth(1)
           self.rect.draw(self.win)
           self.frontCard.draw(self.win)
           register=self.getsavedown_register()
           while link != 0:
             deck[register].rect.move(0,0)
             deck[register].frontCard.move(0,0)
             deck[register].rect.undraw()
             deck[register].frontCard.undraw()
             deck[register].rect.setOutline("black")
             deck[register].rect.setWidth(1)
             deck[register].rect.draw(self.win)
             deck[register].frontCard.draw(self.win)
             link=deck[register].getdown_link()
             register=deck[register].getsavedown_register()
           self.MOVE=0
       

      
  def getWindow(self):
     """
         it returns the atribute window.
     """
     return self.Window



  def getMove(self):
    return self.MOVE
      
class Undo_Button(Button):

  
  def __init__ (self, win, center, width, height, label):
    super().__init__(win, center, width, height, label)
    self.moves_center_rectPA=[]
    self.moves_center_frontPA=[]
    self.moves_card_locP=[]
    self.moves_card2_locP=[]
    
    
    self.move_size=len(self.moves_card2_locP)

    
  def movement_store_past(self,card,A,window):
    
    
    if self.move_size == 10:
      

      del self.moves_center_rectPA[0]
      del self.moves_center_frontPA[0]
      del self.moves_card_locP[0]
      

      self.moves_center_rectPA.append(card.getCenter())
      self.moves_center_frontPA.append(card.getCenter())
      self.moves_card_locP.append(A)

    else:
      self.moves_center_rectPA.append(card.getCenter())
      self.moves_center_frontPA.append(card.getCenter())
      self.moves_card_locP.append(A)
      self.move_size=len(self.moves_card2_locP)
      self.Undo_set(window)
  def movement_store_present(self,B,window):
    
    
    if self.move_size == 10:
      

      del self.moves_card2_locP[0]
      


      self.moves_card2_locP.append(B)
      
    else:

      self.moves_card2_locP.append(B)
      self.move_size=len(self.moves_card2_locP)
      self.Undo_set(window)

  def Undo_Activate(self,Card,window):
    
      if self.move_size == 0:
        
        pass
      
      else:
          
        Card[self.moves_card_locP[(self.move_size-1)]].rect.move((self.moves_center_rectPA[(self.move_size-1)].getX()- Card[self.moves_card_locP[(self.move_size-1)]].getCenter().getX()),(self.moves_center_rectPA[(self.move_size-1)].getY()-Card[self.moves_card_locP[(self.move_size-1)]].getCenter().getY()))
        Card[self.moves_card_locP[(self.move_size-1)]].frontCard.move((self.moves_center_rectPA[(self.move_size-1)].getX()-Card[self.moves_card_locP[(self.move_size-1)]].frontCard.getAnchor().getX()),(self.moves_center_rectPA[(self.move_size-1)].getY()-Card[self.moves_card_locP[(self.move_size-1)]].frontCard.getAnchor().getY()))
        card_qeue="front"
        Card[self.moves_card2_locP[(self.move_size-1)]].setposition(card_qeue)
        del self.moves_card2_locP[(self.move_size-1)]
        del self.moves_center_rectPA[(self.move_size-1)]
        del self.moves_center_frontPA[(self.move_size-1)]
        del self.moves_card_locP[(self.move_size-1)]
        self.move_size=len(self.moves_card2_locP)
        self.Undo_set(window)


  
  def Undo_set(self,Window):
     
     
     if self.move_size == 0:
        
        self.deactivate()
        
     elif self.move_size > 0:
        
        self.activate()
        
     else:
       
        pass
      

if __name__ == "Game": 
  win = GraphWin("Solitaire", 1000, 900)    
  Test  = Card_Movement(win,Point(100,100), 100, 150, "H", 1, "R")
  Test2 = Undo_Button(win)
  x="on"
  while  x == "on":
  
  
    Test.Card_Move(Test2)
  
    off=Test.win.checkKey()
    if off == "":
      pass
    else:
      x="off"

    
  Test.win.close()

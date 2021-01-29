from graphics import *
from button import Button


def interface():
    win = GraphWin("Solitaire", 500, 300)
    win.setBackground("green")

    Quit = Button(win, Point(350, 100), 120, 50, "Quit Game")
    Quit.activate()

    Start = Button(win, Point(150, 100), 120, 50, "Start Game")
    Start.activate()
    q = win.getMouse()
    if Quit.clicked(q):
        win.close()
    elif Start.clicked(q):
        win.close()
        return main()


def main():
    win = GraphWin("Solitaire", 1400, 800)
    win.setBackground("green")

    Time = Button(win, Point(500, 30), 120, 50, "Time")
    Time.activate()

    Score = Button(win, Point(1200, 30), 120, 50, "Score")
    Score.activate()

    randomCards = Button(win, Point(100, 150), 100, 150, "random card")  # where the randomized deck is piled

    firstCol = Button(win, Point(250, 400), 100, 150, "1st column")  # add +150 pixel in the x value for all
    secondCol = Button(win, Point(400, 400), 100, 150, "2nd column")
    thirdCol = Button(win, Point(550, 400), 100, 150, "3rd column")
    fourthCol = Button(win, Point(700, 400), 100, 150, "4th column")
    fifthCol = Button(win, Point(850, 400), 100, 150, "5th column")
    sixthCol = Button(win, Point(1000, 400), 100, 150, "6th column")
    seventhCol = Button(win, Point(1150, 400), 100, 150, "7th column")

    randomCards.activate()
    firstCol.activate()
    secondCol.activate()
    thirdCol.activate()
    fourthCol.activate()
    fifthCol.activate()
    sixthCol.activate()
    seventhCol.activate()

    foundationPiles1 = Button(win, Point(700, 150), 100, 150, "Foundation")  # add +150 pixel in the x value for all
    foundationPiles1.activate()
    foundationPiles2 = Button(win, Point(850, 150), 100, 150, "Foundation")
    foundationPiles2.activate()
    foundationPiles3 = Button(win, Point(1000, 150), 100, 150, "Foundation")
    foundationPiles3.activate()
    foundationPiles4 = Button(win, Point(1150, 150), 100, 150, "Foundation")
    foundationPiles4.activate()

    QuitButton = Button(win, Point(1330, 750), 120, 50, "Quit")
    QuitButton.activate()

    UndoButton = Button(win, Point(1200, 750), 120, 50, "Undo")
    UndoButton.activate()

    while True:
        p = win.getMouse()
        if randomCards.clicked(p):
            print("Touching random cards ")
        elif firstCol.clicked(p):
            print("Touching first column ")
        elif secondCol.clicked(p):
            print("Touching second column ")
        elif thirdCol.clicked(p):
            print("Touching third column ")
        elif fourthCol.clicked(p):
            print("Touching fourth column ")
        elif fifthCol.clicked(p):
            print("Touching fifth column ")
        elif sixthCol.clicked(p):
            print("Touching sixth column ")
        elif seventhCol.clicked(p):
            print("Touching seventh column ")
        elif foundationPiles1.clicked(p):
            print("Touching first foundation pile ")
        elif foundationPiles2.clicked(p):
            print("Touching second foundation pile ")
        elif foundationPiles3.clicked(p):
            print("Touching third foundation pile ")
        elif foundationPiles4.clicked(p):
            print("Touching fourth foundation pile ")
        elif Time.clicked(p):
            print("Touching time section ")
        elif Score.clicked(p):
            print("Touching score section ")
        elif UndoButton.clicked(p):
            print("Touching Undo Button")
        elif QuitButton.clicked(p):
            win.close()


interface()
main()

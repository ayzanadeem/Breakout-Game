
from tkinter import *

#-----------------------------------    

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

#-----------------------------------    

class GameObject:
    
    def __init__(self, pos):
        self.position = Vector(pos[0], pos[1])
    
    def isCollidingWith(self, otherGameObject):  # Checks collosion between itself
        #############################            #   and another game object. Returns
        #   INSERT YOUR CODE HERE                #   True if they are colliding,
        pass                                     #   False otherwise.
        #############################
    
    def Draw(self):                    # This function MUST be overidden by all 
        raise                          #   sub-classes !!!
        

#-----------------------------------

class Background(GameObject):
    def __init__(self):
        #############################
        #   INSERT YOUR CODE HERE
        pass
        #############################
    
    def Draw(self):
        #############################
        #   INSERT YOUR CODE HERE
        pass
        #############################
        

#-----------------------------------
    
class Brick(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################


class NormalBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################

    
class MetalBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################

    
class ExplodingBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################


#-----------------------------------
    
class Ball(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################

    
#-----------------------------------

class Powerup(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################

    
class Life(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################

    
class FastPaddle(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################


class CrazyBall(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################


#-----------------------------------

class Player(GameObject):
    def __init__(self, game, pos, vel):
        #############################
        #   INSERT YOUR CODE HERE
        pass
        #############################


    def Draw(self):
        #############################
        #   INSERT YOUR CODE HERE
        pass
        #############################

        
    
#-----------------------------------

class Game:
    canvas = None
    def __init__(self, canvas):
        Game.canvas = canvas           # Save canvas for future use
        self.gameObjects = []          # A list of ALL game objects in the game
    
        #############################
        #   INSERT YOUR CODE HERE
        pass
        #############################

                
    def Draw(self):                    # This function draws ALL of the things
        Game.canvas.delete(ALL)        # First clear the screen
        for obj in self.gameObjects:   # Now the objects draw THEMSELVES one by one
            obj.Draw()            
       
            
    def LeftKeyPressed(self):        
        #############################
        #   INSERT YOUR CODE HERE
        print("Left key pressed")
        #############################

    
    def RightKeyPressed(self):        
        #############################
        #   INSERT YOUR CODE HERE
        print("Right key pressed")
        #############################

            
    def Update(self):                   # You can add all of your game logic here
        #############################   #   for example collision between game objects,
        #   INSERT YOUR CODE HERE       #   updating the state of the objects based
        pass                            #   on decisions or logic etc...
        #############################

        
            
#-----------------------------------


class GameWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Project 2 -- Breakout Game")
        self.root.geometry('640x480')

        self.canvas = Canvas(self.root, width = 640, height = 480)
        self.canvas.grid(column=0, row=0)
        self.canvas.after(1, self.OneSecTimer)
        self.canvas.bind("<Key>", self.KeyPressed)
        self.canvas.focus_set()
        
        self.game = Game(self.canvas)    
        self.root.after(1, self.GameLoop)
        self.root.mainloop()
    
    def KeyPressed(self, event):
        c = str(event.char)
        if c == 'a':
            self.game.LeftKeyPressed()
        if c == 'd':
            self.game.RightKeyPressed()

    
    def GameLoop(self):        
        self.game.Update()
        self.game.Draw()
        
        self.root.after(1000//60, self.GameLoop)

    def OneSecTimer(self):
        print("One second Tick")
        self.canvas.after(1000, self.OneSecTimer)
        
#-----------------------------------


game = GameWindow()


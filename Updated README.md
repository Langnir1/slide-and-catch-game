Slide and catch game pseudocode!

Setup
--------------
import simpleGE, pygame, and random

main():
* Create variable that gets class Game()
* start game using the start() function from simpleGE
call main through the:
  "If __name__ == "__main__"
method
---------
Class Game()
This class runs the game and calls variables 
* create function __init__ that runs self and will contain variables
* Add a background image using "setImage"
  * The image for the background is from NASA space photos
* add images for both the bubble and the player
* add a self.bubblePop that calls an external sound when the bubble collides
* create self.score that is equal to 0
* create self.labelScore that calls the class LabelScore()
* create self.timer that calls simpleGE.Timer()
* set self.timer to 10 using the totalTime from simpleGE
  * self.timer.totalTime = 10
* create self.labelTime that calls class LabelTime()
* call sprites including sword, bubble, score, and timer
  
  process function
  * checks to see if sword collidesWith bubble
     * When bubble pops, play the sound effect
     * When bubble pops, += 1 to score
     * Update score text with each pop, call the labelScore.text and assign (f"score = self.score")
     * When bubble pops, reset
       
   Update timer (inside the process function)
  * create a countdown using the getTimeLeft method from simpleGE
     * update time text to show self.timer.getTimeLeft() **Later addition, added :.2f at the end for decimal placements**
     * If statement that checks when self.timer.getTimeLeft() < 0
       * print a statement that shows the score in the console (makes sure that things are running)
       * stop game
---------
New Class for the player image
* set simple.GE and scene as parameter
* add the image (in this case, a sword from opengameart)
* setSize of image
* setPosition of image

  Process function
  This function lets the player image move left and right
  * if a key is pressed down, move left or right by 5 pixels
  * self.x will be the variable since we are controlling the x position
---------
New class for Bubble
 This class creates the image that the player wants to "pop"
 The bubble spawns at random postions along the x axis and travels downwards at a random speed.
* same thing as the previous class until the position.
*Create reset() (orginally called action())
  * reset() sets the bubbles y to 0, randomizes the x placement, and moves downwards
*Create check()
  * check() makes sure that the bubble resets after it is greater then screenheight
---------
New class for LabelScore
  This class creates a small text that will keep track of score
  * def init
  * super().__init__()
  * create variable called text that gives a base text of "Score = 0". (This is way, even if other things don't work, if this text appears it means that the code is running semi correctly)
  * create variable center to position the score somewhere on screen
---------
New class for LabelTime
*Same stuff as LabelScore but the position is different





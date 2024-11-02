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
* call sprites

Later additions:
* add a self.bubblePop that calls an external sound when the bubble collides

  process function
  * checks to see if sword collidesWith bubble
  * If the statement is true, bubble sound plays and bubble resets.
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




# Zuma 

This is a puzzle game built using Python and the Tkinter GUI package. It is based on the Popcap game [Zuma](http://www.popcap.com/zuma).

## Game Instructions

The game involves a trail of balls that circle around a center in a maze-like
structure. The user can fire a ball from the center by clicking their mouse
anywhere. The ball fires in that direction (all the way until it either
hits the edge of the screen or hits a moving ball). If the user fires a ball
and it hits one of the moving balls, it is inserted into the trail (by pushing 
all of balls forward). If the inserted balls hits a group of 2 or more same 
colored balls (need 3 colored balls in total), all of those balls get deleted
and the trailing/leading ends join back together.

You can press space to swap your ball with a saved ball. You can only save
one ball at a time.

The level is cleared if you get rid of all the balls. Once that happens,
the next level starts. The next level will have more balls and faster ball
movement. There are 20 levels. You officially win the game if you complete all 
20 levels.

Press enter to start the game.
You can press P to pause the game and R to restart the game at any time.


## Installation and Usage

Download the Git project onto your desktop and unzip the folder.

Download the newest version of Python 2.7 [here](https://www.python.org/downloads/).

To start the game, execute:

    $ python main.py


## Contributing

Bug reports and pull requests are welcome. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.
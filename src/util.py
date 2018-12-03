import sys
import inspect

#method borrowed from cs221 pacman assignment
def raiseNotDefined():
  print ("Method not implemented: %s" % inspect.stack()[1][3])
  sys.exit(1)

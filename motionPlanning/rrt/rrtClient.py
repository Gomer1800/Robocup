#!/usr/bin/python3
from rrt import *

myRRT = rrt( [ 1 , 1 ] ,
        [ 10 , 10 ],
        [ [ 5 , 5, 1 ] ],
        [ 0 , 11 ],
        1 )

myRRT.computeSolutionPath()
myRRT.traceFinalPath()

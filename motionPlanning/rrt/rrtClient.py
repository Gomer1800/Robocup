#!/usr/bin/python3
from rrt import *

myRRT = rrt( [ 1.0 , 1.0 ] ,
        [ 10.0 , 10.0 ] ,
        [ [ 5.0 , 5.0, 1.0 ] , [ 2.5, 7.5, 4.0] , [7.5, 2.5 , 5.0] ],
        [ 0.0 , 11.0 ] )

myRRT.computeSolutionPath()
myRRT.traceFinalPath()

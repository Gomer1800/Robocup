#!/usr/bin/python3
from rrt import *

constraints = [ 0.0 , 11.0 ]

myRRT = rrt( [ 1.0 , 1.0 ] ,
        [ 10.0 , 12.0 ] ,
        [ ( 5.0 , 5.0 , 2.0 ),
            ( random.uniform( constraints[0], constraints[1]), random.uniform( constraints[0], constraints[1] ), 1.0 ) ,
            ( random.uniform( constraints[0], constraints[1]), random.uniform( constraints[0], constraints[1] ), 1.5 ) ,
            ( random.uniform( constraints[0], constraints[1]), random.uniform( constraints[0], constraints[1]), 1 ) ],
        constraints )

myRRT.computeSolutionPath()
myRRT.traceFinalPath()

import matplotlib.pyplot as plt
import random
import math
 
# The rrt program 
# Algorithm BuildRRT from wikipedia
#  Input: Initial configuration qinit, number of vertices in RRT K, incremental distance Δq)
#    Output: RRT graph G
#
#      G.init(qinit)
#        for k = 1 to K
#            qrand ← RAND_CONF()
#                qnear ← NEAREST_VERTEX(qrand, G)
#                    qnew ← NEW_CONF(qnear, qrand, Δq)
#                        G.add_vertex(qnew)
#                            G.add_edge(qnear, qnew)
#                              return G

class rrt():

    def __init__(self, 
            start_Point, # coordinates of start Point
            goal_Point, # coordinates of goal Point
            obstacle_List, # List of obstacle Point objects 
            randomization_Constraints, # List of min/max constraints for random Point Sampling
            growth_Factor, # Amount by which a new branch will grow towards Sample Point
            goal_SampleRate = 1, # probability of sampling the Goal point
            max_Iterations = 1000) : # Maximum number of cycles of rrt growth

        self.start_Point = Point ( start_Point[0], start_Point[1] )
        self.goal_Point = Point ( goal_Point[0], start_Point[1] )
        self.min_Rand_Constraint = randomization_Constraints[0]
        self.max_Rand_Constraint = randomization_Constraints[1]
        self.growth_Factor = growth_Factor
        self.goal_SampleRate = goal_SampleRate
        self.max_Iterations = max_Iterations

        self.obstacle_List = obstacle_List

        def computeRRT (self) :
            # 1) Initialize PointList with start_Position
            point_List = [self.start_Point]
            # WHILE LOOP
            reached_Goal = False
            while ( reached_Goal == False ) :
                # 2) generateRandomSample (), returns random sample Point or biased Point
                sample_Point = generateRandomSamplePoint ()
                # 3) getClosestPointIndex( sample Point  ), returns index of Point in pointList closest to given sample point
                closest_Point_Index = getClosestPointIndex( sample_Point)
            # 4) growTree( new_Point , closest_Point_Index ) , creates new Point and grows tree
            # 5) collisionDetected ( nearby Point ), returns boolean based on check if nearby point collides with osbtacle
            # 5a) If 5 is true , restart loop
            # 5b) If 5 is false, proceed to 6
            # 6) add new_Point to point_List
            # 7) goalStatus( new_Point) , returns boolean based on check of distance from goal_Point to new_Point
            # 7a) If 7 is true, proceed to 8
            # 7b) if 7 is false, repeat cycle, return to 2
            # Trace backwards towards start Point
            # 8) traceFinalPath() , returns list of Point coordinate pairs from endPoint to startPoint 

        def getClosestPointIndex(self, sample_Point) :
           placeHolder = 1

        def generateRandomSamplePoint(self) : # generateRandomSample (), returns random sample Point or biased Point
            if random.randint(0,100) > goal_sampleRate :
                sample_Point = Point ( random.uniform( self.min_Rand_Constraint, self.max_Rand_Constraint) , random.uniform( self.min_Rand_Constraint, self.max_Rand_Constraint)) 

            else : sample_Point = Point ( self.goal_Point.x , self.goal_Point.y) # Biased Point

            return sample_Point


        def DrawGraph(self, rnd=None):
            plt.clf() # clears figure w/ all is axes, but leaves the window opened
            if rnd is not None:
                plt.plot(rnd[0], rnd[1], "r+") # displays cursor from random sampling
            for node in self.nodeList: # 
                if node.parent is not None:
                    plt.plot([node.x, self.nodeList[node.parent].x], [
                        node.y, self.nodeList[node.parent].y], "-g")

            for (ox, oy, size) in self.obstacleList:
                plt.plot(ox, oy, "ok", ms=30 * size)
                
                plt.plot(self.start.x, self.start.y, "xr")
                plt.plot(self.end.x, self.end.y, "xr")
                plt.axis([-2, 15, -2, 15])
                plt.grid(True)
                plt.pause(0.01)

class Point () :

    def __init__(self, x, y) :
        self.x_Position = x
        self.y_Position = y
        self.preceding_Point_Index = None 

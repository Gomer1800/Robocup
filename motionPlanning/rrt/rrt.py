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

        def computeSolutionPath (self) :
            # 1) Initialize PointList with start_Position
            point_List = [self.start_Point]
            # WHILE LOOP
            reached_Goal = False
            while ( reached_Goal == False ) :
                # 2) generateRandomSample (), returns random sample Point or biased Point
                sample_Point = generateRandomSamplePoint ()
                # 3) getClosestPointIndex( sample Point  ), returns index of Point in pointList closest to given sample point
                closest_Point_Index = getClosestPointIndex( point_List, sample_Point)
                # 4) growTree( new_Point , closest_Point_Index ) , creates new Point and grows tree at closes_Point_index in point_List
                new_Point = growTree( sample_Point, closest_Point_Index )
                # 5) collisionDetected ( nearby Point ), returns boolean based on check if nearby point collides with osbtacle
                # 5a) If 5 is true , next loop iteration 
                # 5b) If 5 is false, proceed to 6 
                if collisionDetected( new_Point) :
                    continue 
                
                # 6) add new_Point to point_List
                point_List.append( new_Point)
                # 7) goalStatus( new_Point) , returns boolean based on check of distance from goal_Point to new_Point
                # 7a) If 7 is true, break while loop
                # 7b) if 7 is false, next loop iteration
                if getGoalStatus( new_Point) == True :
                    reached_Goal = True

            # Trace backwards towards start Point for solution path
            # 8) traceFinalPath() , returns list of Point coordinate pairs from endPoint to startPoint
            solution_Path = traceFinalPath( point_List)
            return solution_Path

######## METHODS
        def traceFinalPath(self, point_List) :
            solution_Points = [point_List[-1]]
            solution_Coordinate_Pairs = [ [point_List[-1].x, point_List[-1].y] ]
            for this_Point.preceding_Point_Index in solution_Points is not None:
                solution_Points.append( point_List( this_Point.preceding_Point_Index))
                solution_Coordinate_Pairs.append( [ point_List(this_Point.preceding_Point_Index).x , point_List( this_Point.preceding_Point_Index).y ] )

            solution_Coordinate_Pairs.append( [ self.start_Point.x , self.start_Point.y ] )
            return solution_Coordinate_Pairs

        def getGoalStatus(self, new_Point) :
            if self.goal_Point.x == new_Point.x & self.goal_Point.y == new_Point.y :
                return True
            else : return False

        def collisionDetected(self, new_Point) :
            for (x , y, obstacle_Radius) in self.obstacle_List :
                dx = x - new_Point.x
                dy = y - new_Point.y
                distance_to_Obstacle = math.sqrt( dx**2, dy**2)
                if distance_to_Obstacle <= obstacle_Radius :
                    return True
                else : return False


        def growTree(self, sample_Point, closest_Point_Index ) :
            growth_Angle = math.atan2( (sample_Point.y - point_List(closest_Point_Index).y) , (sample_Point.x - point_List(closest_Point_Index).x))
            new_Point = Point ( self.growth_Factor * math.cos( growth_Angle), self.growth_Factor * math.sin( growth_Angle))
            newPoint.preceding_Point_Index = closest_Point_Index

            return newPoint


        def getClosestPointIndex(self, point_List, sample_Point) :
            distance_to_Sample = []
            for this_Point in point_List :
                distance_to_Sample.append( math.sqrt( (sample_Point.x - this_Point.x )**2 + (sample_Point.y - this_Point.y)**2 )) 

            index = distance_to_Sample.index( min(distance_to_Sample))
            return index

        def generateRandomSamplePoint(self) : # generateRandomSample (), returns random sample Point or biased Point
            if random.randint(0,100) > goal_sampleRate :
                sample_Point = Point ( random.uniform( self.min_Rand_Constraint, self.max_Rand_Constraint) , random.uniform( self.min_Rand_Constraint, self.max_Rand_Constraint)) 

            else : sample_Point = Point ( self.goal_Point.x , self.goal_Point.y) # Biased Point

            return sample_Point

class Point () :

    def __init__(self, x, y) :
        self.x_Position = x
        self.y_Position = y
        self.preceding_Point_Index = None 

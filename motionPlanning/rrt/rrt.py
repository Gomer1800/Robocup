#!/usr/bin/python3

import matplotlib.pyplot as plt
from matplotlib import collections as mc
import pylab as pl
import random
import math
import sys

class rrt():
    def __init__(self, 
            start_Point, # coordinates of start Point
            goal_Point, # coordinates of goal Point
            obstacle_List, # List of obstacle ( x, y, radius )
            randomization_Constraints, # List of min/max constraints for random Point Sampling
            growth_Factor = 1, # Amount by which a new branch will grow towards Sample Point
            goal_SampleRate = 2.5) : # probability of sampling the Goal point

        self.start_Point = Point ( start_Point[0], start_Point[1] )
        self.goal_Point = Point ( goal_Point[0], goal_Point[1] )
        self.min_Rand_Constraint = randomization_Constraints[0]
        self.max_Rand_Constraint = randomization_Constraints[1]
        self.growth_Factor = growth_Factor
        self.goal_SampleRate = goal_SampleRate
        self.obstacle_List = obstacle_List
        
    def computeSolutionPath(self) :
        # 1) Initialize PointList with start_Position
        point_List = [self.start_Point]
        # WHILE LOOP
        self.windowCount = 0
        self.reached_Goal = False
        while ( self.reached_Goal == False ) :
            # 2) generateRandomSample (), returns random sample Point or biased Point
            sample_Point = self.generateRandomSamplePoint()
            # 3) getClosestPointIndex( sample Point  ), returns index of Point in pointList closest to given sample point
            closest_Point_Index = self.getClosestPointIndex(point_List, sample_Point)
            # 4) growTree( new_Point , closest_Point_Index ) , creates new Point and grows tree at closes_Point_index in point_List
            new_Point = self.growTree(point_List, sample_Point, closest_Point_Index)
            # 4a) refresh RRT figure and draw new tree
            # 5) collisionDetected ( nearby Point ), returns boolean based on check if nearby point collides with osbtacle
            # 5a) If 5 is true , next loop iteration 
            # 5b) If 5 is false, proceed to 6 
            if self.collisionDetected(new_Point) :
                continue 
            # 6) add new_Point to point_List
            point_List.append(new_Point)
            # 7) goalStatus( new_Point) , returns boolean based on check of distance from goal_Point to new_Point
            # 7a) If 7 is true, break while loop & print rrt graph
            # 7b) if 7 is false, next loop iteration
            if self.getGoalStatus(new_Point) == True :
                self.reached_Goal = True
                self.drawRRT(point_List)
            # Trace backwards towards start Point for solution path
            # 8) traceFinalPath() , returns list of Point coordinate pairs from endPoint to startPoint
            # self.solution_Path = traceFinalPath( point_List)
    
    ######## METHODS
    def drawRRT(self, point_List) :
        ax = plt.cla()
        plt.clf()
        for point in point_List :
            if point.preceding_Point_Index is not None:
                plt.plot( [ point.x, point_List[point.preceding_Point_Index].x],
                        [point.y, point_List[point.preceding_Point_Index].y], "-r")

        fig = plt.gcf()
        ax = fig.gca()
        for ( obstacle_x, obstacle_y, radius ) in self.obstacle_List :
            ax.add_artist(plt.Circle( (obstacle_x, obstacle_y) , radius , color='b'))
            
        self.traceFinalPath(point_List)

        plt.plot( self.start_Point.x, self.start_Point.y, "-xb", label='START')
        plt.plot( self.goal_Point.x, self.goal_Point.y, "-xb", label='GOAL')
        plt.pause( .1 )
        plt.show()

    def traceFinalPath(self, point_List) : # work in progress
        solution_Points = [point_List[-1]]
        # solution_Coordinate_Pairs = [ [point_List[-1].x, point_List[-1].y] ]
        for this_Point in solution_Points :
            if this_Point.preceding_Point_Index != None :
                plt.plot( [ this_Point.x , point_List[this_Point.preceding_Point_Index].x ],
                        [ this_Point.y , point_List[this_Point.preceding_Point_Index].y ], "-b" )
                # plt.show()
                solution_Points.append( point_List[ this_Point.preceding_Point_Index])
        
    def getGoalStatus(self, new_Point) :
        dx = new_Point.x - self.goal_Point.x
        dy = new_Point.y - self.goal_Point.y
        distance =math.sqrt ( dx**2 + dy**2 )

        print("X :", new_Point.x)
        print("Y :", new_Point.y)

        if distance <= self.growth_Factor :
            print("True")
            return True
        else :
            print("False")
            return False

    def collisionDetected(self, new_Point) :
        for (x , y, obstacle_Radius) in self.obstacle_List :
            dx = x - new_Point.x
            dy = y - new_Point.y
            distance_to_Obstacle = math.sqrt( dx**2 + dy**2)
            if distance_to_Obstacle <= obstacle_Radius :
                return True
        return False

    def growTree(self, point_List, sample_Point, closest_Point_Index) :
        growth_Angle = math.atan2((sample_Point.y - point_List[closest_Point_Index].y) , (sample_Point.x - point_List[closest_Point_Index].x))
        new_Point = Point ( point_List[closest_Point_Index].x + self.growth_Factor * math.cos( growth_Angle), 
                point_List[closest_Point_Index].y + self.growth_Factor * math.sin( growth_Angle))
        new_Point.preceding_Point_Index = closest_Point_Index

        return new_Point

    def getClosestPointIndex(self, point_List, sample_Point) :
        distance_to_Sample = []
        for this_Point in point_List :
            distance_to_Sample.append(math.sqrt( (sample_Point.x - this_Point.x )**2 + (sample_Point.y - this_Point.y)**2 )) 

        index = distance_to_Sample.index( min(distance_to_Sample))
        return index

    def generateRandomSamplePoint(self) : # generateRandomSample (), returns random sample Point or biased Point
        if random.randint(0,100) > self.goal_SampleRate :
            sample_Point = Point ( random.uniform( self.min_Rand_Constraint, self.max_Rand_Constraint) , random.uniform( self.min_Rand_Constraint, self.max_Rand_Constraint)) 

        else : sample_Point = Point ( self.goal_Point.x , self.goal_Point.y) # Biased Point
        
        # print("X :", sample_Point.x)
        # print("Y :", sample_Point.y)
        return sample_Point

class Point () :

    def __init__(self, x, y) :
        self.x = x
        self.y = y
        self.preceding_Point_Index = None

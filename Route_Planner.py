import math
import heapq


#resources Used: looked up the math formula for distance between two points and how to use a tuple with heapq

def shortest_path(M,start,goal):
    print("shortest path called")
    if start == goal:
        return [start]
    #set up a heap with the initial start point
    #est total distance to end, The Paths taken so far, distance travelled on path so far
    pathList = [(distance(M.intersections[start], M.intersections[goal]), [start], 0)]
    #set a currentBest to save the best path so far and return an empty path if no path exists
    currentBest = ([], math.inf)
    
    #keep going untill all possible paths are exhausted
    while len(pathList) > 0:
        #pop the least estimated Distace to End which includes Distance so far and distance from intersection to goal
        #unpack the tuple into a currentPath, last Intersection, distanceSoFar, and estDistanceEnd
        pathTest = heapq.heappop(pathList)
        cPath = pathTest[1]
        lastIntersection = cPath[-1]
        distanceSoFar = pathTest[2]
        estDistanceEnd = pathTest[0]
        
        #if the estimated Distatnce to the End is greater than our currentBest than we have found the best alternative
        if estDistanceEnd > currentBest[1]:
            break
        
        #check all of the next intersections that we have not visited in this path and push them onto the heap
        for intersection in M.roads[lastIntersection]:
            if intersection not in cPath:
                path = cPath + [intersection]
                distanceToInt = distanceSoFar + distance(M.intersections[lastIntersection], M.intersections[intersection])
                estDistToEnd = distanceToInt

                if intersection == goal:
                    #if we have found the goal and it is better than our currentBest save it as currentBest
                    if estDistToEnd < currentBest[1]:
                        currentBest = (path, estDistToEnd)
                    continue
                else:
                    #estimate distance as distance so far + distance from intersection to the goal in straight line
                    estDistToEnd = estDistToEnd + distance(M.intersections[intersection], M.intersections[goal]) 

                #Only push onto the heap if the estDistance is less than our current Best
                if estDistToEnd<currentBest[1]:
                    pathTuple = (estDistToEnd, path, distanceToInt)
                    heapq.heappush(pathList, pathTuple)
    
    return currentBest[0]
    
#distance between two points helper function
def distance(start, end):
        return math.sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2)
"""
This module provides heuristic and approximation algorithms for travelling salesman problem solution(TSP).
It starts with the greedy algorithm, which is to find the next nearest neighbor.
Then the 2-opt (pairwise exchange) is applied for optimization.
More reference: https://en.wikipedia.org/wiki/Travelling_salesman_problem, 
https://github.com/evil-mad/stipplegen.
"""
import random


def get_TSP_greedy(pts):
    """calculate a simple, greedy route to connnet all the points

    parameter:
    ----------
        pts: a list of points(tuple)
    
    return:
    -------
        sorted key of the input points
    """
    greedy_route = list(range(len(pts)))

    for key_i in range(len(greedy_route)-1):
        dist_min = 99999999

        for key_j in range(key_i+1, len(greedy_route)):

            dist = (pts[greedy_route[key_j]][0] - pts[greedy_route[key_i]][0])**2 + \
            (pts[greedy_route[key_j]][1] - pts[greedy_route[key_i]][1])**2

            if dist < dist_min:
                dist_min = dist
                step_closest = key_j 

        temp = greedy_route[key_i+1]
        greedy_route[key_i+1] = greedy_route[step_closest]
        greedy_route[step_closest] = temp
    
    return greedy_route

def pairwise_exchange(pts, greedy_route, iteration):
    """running pairwise exchange algorithm (2-opt) to optimize TSP route

    parameter:
    ----------
        pts: a list of points(tuple)
        
        greedy_route: a list of keys of the points that generated from greedy algorithm
        
        iteration: an integer representing how many iterations the algorithm run.   
    
    return:
    -------
        sorted key of the input points
    """

    for _ in range(iteration):
        index_a = random.randrange(0, len(greedy_route)-1)
        index_b = random.randrange(0, len(greedy_route)-1)

        if abs(index_a - index_b) < 2:
            continue

        if index_b < index_a:
            index_a, index_b = index_b, index_a

        a0 = pts[greedy_route[index_a]]
        a1 = pts[greedy_route[index_a + 1]]
        b0 = pts[greedy_route[index_b]]
        b1 = pts[greedy_route[index_b + 1]]

        dist_original = (a1[0] - a0[0])**2 + (a1[1] - a0[1])**2 \
            + (b1[0] - b0[0])**2 + (b1[1] - b0[1])**2
        
        dist_test = (a0[0] - b0[0])**2 + (a0[1] - b0[1])**2 \
            + (a1[0] - b1[0])**2 + (a1[1] - b1[1])**2

        if dist_test < dist_original:
            index_high = index_b
            index_low = index_a + 1

            while index_high > index_low:
                greedy_route[index_low], greedy_route[index_high] =\
                    greedy_route[index_high], greedy_route[index_low]

                index_high -= 1
                index_low += 1

    return greedy_route
        

if __name__ == '__main__':
    import rhinoscriptsyntax as rs
    import random

    pts = []
    for i in range(200):
        x = random.randrange(0, 100)
        y = random.randrange(0, 100)
        pts.append((x, y))

    route = get_TSP_greedy(pts)
    route = pairwise_exchange(pts, route, 10000)

    rs.AddPolyline([pts[i] for i in route])



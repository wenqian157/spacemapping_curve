"""
This module provides heuristic and approximation algorithms for travelling salesman problem solution(TSP).
It starts with the greedy algorithm, which is to find the next nearest neighbor.
Then the 2-opt (pairwise exchange) is applied for optimization.
More reference: https://en.wikipedia.org/wiki/Travelling_salesman_problem, 
https://github.com/evil-mad/stipplegen.
"""

import random
import rhinoscriptsyntax as rs


def get_TSP_greedy(pts):
    greedy_route = list(range(len(pts)))

    for key_i in range(len(greedy_route)-1):
        # step_closest = 0
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


if __name__ == '__main__':
    pts = []
    for i in range(200):
        x = random.randrange(0, 100)
        y = random.randrange(0, 100)
        pts.append((x, y))

    route = get_TSP_greedy(pts)
    rs.AddPolyline([pts[i] for i in route])



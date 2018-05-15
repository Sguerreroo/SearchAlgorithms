# Search methods

from __future__ import print_function
from __future__ import print_function
import search

routes = []

ab = search.GPSProblem('A', 'B', search.romania)
tn = search.GPSProblem('T', 'N', search.romania)
zs = search.GPSProblem('Z', 'S', search.romania)

routes.append(ab)
routes.append(tn)
routes.append(zs)

for i in routes:
    print(search.branch_bound_graph_search(i).path())
    print(search.branch_bound_with_heuristic_graph_search(i).path())
    # print(search.depth_first_graph_search(i).path())
    # print(search.breadth_first_graph_search(i).path())
    print("-----------------------------------------------------------")

# print search.iterative_deepening_search(ab).path()
# print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

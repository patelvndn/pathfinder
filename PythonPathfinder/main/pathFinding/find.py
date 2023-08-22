from .algorithm import *
class PathFinder:
    def __init__(self, occupationArray):
        self.oa = occupationArray

    def find(self, root, algorithmName, start, end):
        problem = SearchProblem(root, start, end, self.oa)
        result = None 
        if algorithmName == "Dijkstras":
            pass
        elif algorithmName ==  "A*":
            root.after(500, astar, problem)
            result = astar(problem)
        elif algorithmName == "Depth First Search":
            result = dfs(problem)
        elif algorithmName == "Bredth First Search":
            result = bfs(problem) 
        else:
             pass
        return result

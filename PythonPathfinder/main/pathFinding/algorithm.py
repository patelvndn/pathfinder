import copy

class SearchProblem:
    def __init__(self, root, start, end, occupationGrid):
        self.start = start
        self.end = end
        self.grid = occupationGrid
        self.size = self.grid.shape
        self.root = root

    def _isValidState(self, state):
        pass 

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        if (state[0] == self.end[0] and state[1] == self.end[1]):
            return True
        return False

    def getSuccessors(self, state):
        possibleMoves = []
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            if(dx == 0 and dy == 0): continue
            newMove = (state[0] + dx, state[1] + dy)
            x = newMove[0]
            y = newMove[1]
            if (x < 0 or y < 0 or x >= self.size[0] or y >= self.size[1]): continue
            if (self.grid[x,y] == 1): continue
            possibleMoves.append( (newMove, dx, dy) )
        return possibleMoves

    def getCostOfActions(self, actions):
        return 0


'''
input is 'Search Problem'
output is path that is a solution
'''
def nullHeuristic(state, problem=None):
    return 0

def astar(problem, heuristic=nullHeuristic):
    pass

def ucs(problem):
    pass

def dfs(problem):
    stack = []

def bfs(problem):
    start = problem.getStartState()
    queue = [Path(start)]
    visited = []
    while len(queue) > 0:
        path = queue.pop()        
        node = path.get_node()

        if node in visited:
            continue
        visited.append(node)

        if(problem.isGoalState(node)):
            return path.get_path()

        children = problem.getSuccessors(node)
        for i in range(0, len(children)):
            child, dx, dy = children[i]
            if child not in visited:
                queue.insert(0, path.add(child, (dx, dy)))
    return []

class Path:
	def __init__(self, root, heuristic=0, useHeuristic=False):
		self.nodes = [root]
		self.actions = []
		self.cost = 0
		self.heur = 0
		self.useHeuristic = useHeuristic

	def __copy__(self):
		return copy.deepcopy(self)

	def __lt__(self, other):
		if self.useHeuristic:
			return self.cost + self.heuristic < other.cost + other.heuristic
		else:
			return self.cost < other.cost

	def __gt__(self, other):
		if self.useHeuristic:
			return self.cost + self.heuristic > other.cost + other.heuristic
		else:
			return self.cost > other.cost

	def add(self, child, action, cost=0, heuristic=0):
		# create copy
		path = self.__copy__()
		# append new items to path
		path.nodes.append(child)
		path.actions.append(action)
		path.cost += cost
		path.heuristic = heuristic

		return path

	def get_cost(self):
		return self.cost

	def get_node(self):
		return self.nodes[-1]

	def get_actions(self):
		return self.actions

	def get_path(self):
		return self.nodes

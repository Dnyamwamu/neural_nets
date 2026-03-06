# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).

  You do not need to change anything in this class, ever.
  """

  def getStartState(self):
     """
     Returns the start state for the search problem
     """
     util.raiseNotDefined()

  def isGoalState(self, state):
     """
       state: Search state

     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state

     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take

     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]

  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  from util import Stack

  stack = Stack()
  visited = set()

    # stack holds: (state, actions up to this state)
  start = problem.getStartState()
  stack.push((start, []))

  while not stack.isEmpty():
        state, actions = stack.pop()

        # Goal check
        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    stack.push((successor, actions + [action]))

  return []
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  from util import Queue

  queue = Queue()
  visited = set()

  start = problem.getStartState()
  queue.push((start, []))

  while not queue.isEmpty():
        state, actions = queue.pop()

        # Goal check
        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    queue.push((successor, actions + [action]))

  return []
  util.raiseNotDefined()

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  from util import PriorityQueue

  pq = PriorityQueue()
  visited = set()

  start = problem.getStartState()
  pq.push((start, [], 0), 0)   # (state, actions, cost), priority = cost

  while not pq.isEmpty():
        state, actions, cost = pq.pop()

        # If we already expanded this state, skip it
        if state in visited:
            continue

        visited.add(state)

        # Goal check
        if problem.isGoalState(state):
            return actions

        # Expand successors
        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                newActions = actions + [action]
                newCost = cost + stepCost
                pq.push((successor, newActions, newCost), newCost)

  return []
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  from util import PriorityQueue

  pq = PriorityQueue()
  visited = set()

  start = problem.getStartState()
  startCost = 0
  startHeuristic = heuristic(start, problem)

  pq.push((start, [], 0), startHeuristic)

  while not pq.isEmpty():
        state, actions, cost = pq.pop()

        # Skip if we've already expanded this state
        if state in visited:
            continue

        visited.add(state)

        # Goal check
        if problem.isGoalState(state):
            return actions

        # Successor expansion
        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                newCost = cost + stepCost     # g(n)
                h = heuristic(successor, problem)
                priority = newCost + h        # f(n) = g(n) + h(n)
                pq.push((successor, actions + [action], newCost), priority)

  return []
  util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

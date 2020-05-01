from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from heapq import heappush, heappop

T = TypeVar('T')

class Stack(Generic[T]):
  def __init__(self):
    self._container: List[T] = []

  @property
  def empty(self):
    return not self._container

  def push(self, item: T):
    self._container.append(item)

  def pop(self):
    return self._container.pop() # FILO

  def __repr__(self):
    return repr(self._container)

class Queue(Generic[T]):
  def __init__(self) -> None:
    self._container: Deque[T] = Deque()

  @property
  def empty(self) -> bool:
    return not self._container

  def push(self, item: T) -> None:
    self._container.append(item)

  def pop(self) -> T:
    return self._container.popleft()  # FIFO

  def __repr__(self) -> str:
    return repr(self._container)

class PriorityQueue(Generic[T]):
  def __init__(self):
    self._container: List[T] = []

  @property
  def empty(self):
    return not self._container  # not is true for empty container

  def push(self, item: T):
    heappush(self._container, item)  # in by priority

  def pop(self):
    return heappop(self._container)  # out by priority

  def __repr__(self):
    return repr(self._container)

class Node(Generic[T]):
  def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0):
    self.state: T = state
    self.parent: Optional[Node] = parent
    self.cost: float = cost
    self.heuristic: float = heuristic

  def __lt__(self, other: Node):
    return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def node_to_path(node: Node[T]) -> List[T]:
  path: List[T] = [node.state]
  # work backwards from end to front
  while node.parent is not None:
      node = node.parent
      path.append(node.state)
  path.reverse()
  return path
    
def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]):
  frontier: Stack[Node[T]] = Stack()
  frontier.push(Node(initial, None))

  explored: Set[T] = { initial }
  # keep searching while frontier is not empty
  while not frontier.empty:
    current_node: Node[T] = frontier.pop()
    current_state: T = current_node.state
    # if found the goal, return and finish
    if goal_test(current_state):
      return current_node
    # check where we can go, if it was not yet explored
    for child in successors(current_state):
      if child in explored:
        continue
      explored.add(child)
      frontier.push(Node(child, current_node))
  return None

def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]):
  frontier: Queue[Node[T]] = Queue()
  frontier.push(Node(initial, None))

  explored: Set[T] = { initial }
  # keep searching while frontier is not empty
  while not frontier.empty:
    current_node: Node[T] = frontier.pop()
    current_state: T = current_node.state
    # if found the goal, return and finish
    if goal_test(current_state):
      return current_node
    # check where we can go, if it was not yet explored
    for child in successors(current_state):
      if child in explored:
        continue
      explored.add(child)
      frontier.push(Node(child, current_node))
  return None

def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]], heuristic: Callable[[T], float]):
  # frontier is where we've yet to go
  frontier: PriorityQueue[Node[T]] = PriorityQueue()
  frontier.push(Node(initial, None, 0.0, heuristic(initial)))
  # explored is where we've been
  explored: Dict[T, float] = { initial: 0.0 }

  # keep going while there is more to explore
  while not frontier.empty:
    current_node: Node[T] = frontier.pop()
    current_state: T = current_node.state
    # if we found the goal, we're done
    if goal_test(current_state):
      return current_node
    # check where we can go next and haven't explored
    for child in successors(current_state):
      new_cost: float = current_node.cost + 1  # 1 assumes a grid, need a cost function for more sophisticated apps

      if child not in explored or explored[child] > new_cost:
        explored[child] = new_cost
        frontier.push(Node(child, current_node, new_cost, heuristic(child)))
  return None  # went through everything and never found goal


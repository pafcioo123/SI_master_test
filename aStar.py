from anytree import Node, RenderTree
import PriorityQueue
import constants

def forward(istate):
    state = istate.copy()
    way = state[2]
    if way == 0:
        state[0] = state[0] - 1
    if way == 1:
        state[1] = state[1] + 1
    if way == 2:
        state[0] = state[0] + 1
    if way == 3:
        state[1] = state[1] - 1
    state[3] = state[3] + 1
    state[5] = "FORWARD"
    if (constants.MAP_WIDTH > state[1] >= 0 and constants.MAP_HEIGHT > state[0] >= 0 and
            constants.REST[state[0]][state[1]] == 0):
        return state
    else:
        return None


def left(istate):
    state = istate.copy()
    if state[2] > 0:
        state[2] = state[2] - 1
    else:
        state[2] = 3
    state[3] = state[3] + 1
    state[5] = "LEFT"
    return state


def right(istate):
    state = istate.copy()
    if state[2] < 3:
        state[2] = state[2] + 1
    else:
        state[2] = 0
    state[3] = state[3] + 1
    state[5] = "RIGHT"
    return state


def succ(state):
    table = []
    result = []
    table.append(forward(state))
    table.append(left(state))
    table.append(right(state))
    for st in table:
        if not (st is None):
            result.append(st)
    return result


def manh(istate, fstate):
    return abs(istate[0] - fstate[0]) + abs(istate[1] - fstate[1])


class aStar:
    def __init__(self, istate, final):
        self.fringe = PriorityQueue.PriorityQueue()
        self.explored = []
        self.istate = istate
        self.final = final

    def astar(self):
        s = Node(self.istate)
        # print(self.istate)
        self.fringe.insert(s)
        while True:
            # print("petla")
            if self.fringe.isEmpty():
                # print("whoopsie")
                return None
            # print("b4pop fringe")
            # print(self.fringe)
            elem = self.fringe.delete()
            # print("pop fringe")
            if elem.name[0] == self.final[0] and elem.name[1] == self.final[1] and elem.name[2] == self.final[2]:
                # print("done?")
                return elem
            self.explored.append(elem)
            # print("elem")
            # print(elem)
            # print("succ")
            # print(succ(elem.name))
            for stan in succ(elem.name):
                x = Node(stan, elem)
                x.name[4] = x.name[3] + manh(x.name, self.final)
                infringe = any((st.name[0] == x.name[0] and
                                st.name[1] == x.name[1] and
                                st.name[2] == x.name[2]) for st in self.fringe.queue)
                inexplored = any((st.name[0] == x.name[0] and
                                  st.name[1] == x.name[1] and
                                  st.name[2] == x.name[2]) for st in self.explored)
                if not infringe and not inexplored:
                    self.fringe.insert(x)
                else:
                    if infringe:
                        i = next(self.fringe.queue.index(z) for z in self.fringe.queue if (z.name[0] == x.name[0] and
                                                                                           z.name[1] == x.name[1] and
                                                                                           z.name[2] == x.name[2]))
                        if x.name[4] < self.fringe.queue[i].name[4]:
                            self.fringe.queue[i] = x

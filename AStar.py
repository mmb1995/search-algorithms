''' Matthew Blumenschein mmb1995
Example that uses the AStar search algorithm and heuristics to solve the EightPuzzle game

Usage:
python3 Astar.py EightPuzzleWithHeuristics <heuristic>
'''

import sys
from PriorityQB import PriorityQB

if sys.argv == [''] or len(sys.argv) < 2:
    import EightPuzzleWithHeuristics as Problem
    # import TowersOfHanoi as Problem
    from Problem import h_manhattan as heuristic
else:
    import importlib

    Problem = importlib.import_module(sys.argv[1])

    # attempts to access the heuristic specified on the command line
    try:
        h = sys.argv[2]
        heuristics = { "h_manhattan": lambda s: s.h_manhattan(), "h_hamming": lambda s: s.h_hamming(),
                   "h_euclidean": lambda s: s.h_euclidean(), "h_custom": lambda s: s.h_custom()}
        heur = heuristics[h]
    except Exception:
        print("invalid heuristic. Please type in h_manhattan, h_hamming, h_euclidian, or h_custom")
        exit(1)

print("\nWelcome to ItrDFS")
COUNT = None
BACKLINKS = {}

gio
def runAStar():
    global Problem
    initial_state = Problem.CREATE_INITIAL_STATE()
    if not isSolvable(initial_state):
            print("There is no possible solution to this puzzle. Please choose a different initial state.")
            return
    print("Initial State:")
    print(initial_state)
    global COUNT, BACKLINKS, MAX_OPEN_LENGTH
    COUNT = 0
    BACKLINKS = {}
    MAX_OPEN_LENGTH = 0
    AStar(initial_state)
    print(str(COUNT) + " states expanded.")
    print('MAX_OPEN_LENGTH = ' + str(MAX_OPEN_LENGTH))

def isSolvable(S):
    '''This will check the initial state to determine if AStar can find a valid solution.
       This is needed because certain initial states of the EightPuzzle are unsolvable.
    '''
    coord = [(0,0), (0,1), (0, 2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    inv_count = 0
    for i in range(9):
        c = coord[i]
        num = S.b[c[0]][c[1]]
        if num != 0:
            for j in range(i+1, 9):
                v = coord[j]
                value = S.b[v[0]][v[1]]
                if num > value and value != 0:
                    inv_count += 1
    #print(inv_count)
    return inv_count % 2 == 0



def AStar(initial_state):
    global COUNT, BACKLINKS, MAX_OPEN_LENGTH

    # STEP 1. Put the start state on a list OPEN
    OPEN = PriorityQB()
    OPEN.insert(initial_state, heur(initial_state))
    x = OPEN.getpriority(initial_state)
    print(x)
    CLOSED = []
    BACKLINKS[initial_state] = None
    moves = {initial_state: 0}

    # STEP 2. If OPEN is empty, output “DONE” and stop.
    while len(OPEN) != 0:
        report(OPEN, CLOSED, COUNT)
        if len(OPEN) > MAX_OPEN_LENGTH: MAX_OPEN_LENGTH = len(OPEN)

        # STEP 3. Select the first state on OPEN and call it S.
        #         Delete S from OPEN.
        #         Put S on CLOSED.
        #         If S is a goal state, output its description
        S = OPEN.deletemin()
        S = S[0]
        CLOSED.append(S)

        if Problem.GOAL_TEST(S):
            print(Problem.GOAL_MESSAGE_FUNCTION(S))
            path = backtrace(S)
            print('Length of solution path found: ' + str(len(path) - 1) + ' edges')
            return
        COUNT += 1

        # STEP 4. Generate the list L of successors of S and delete
        #         from L those states already appearing on CLOSED.
        L = []
        for op in Problem.OPERATORS:
            if op.precond(S):
                new_state = op.state_transf(S)
                if not (new_state in CLOSED):
                    priority = getPriority(new_state, moves[S] + 1)
                    if new_state in OPEN and priority < OPEN.getpriority(new_state):
                        OPEN.remove(new_state)
                    if new_state not in OPEN:
                        BACKLINKS[new_state] = S
                        moves[new_state] = moves[S] + 1
                        OPEN.insert(new_state, priority)

        #OPEN.print_pq("OPEN", "H(S)")


# STEP 6. Go to Step 2.

def getPriority(S, moves):
    return moves + heur(S)


def print_state_list(name, lst):
    print(name + " is now: ", end='')
    for s in lst[:-1]:
        print(str(s), end=', ')
    print(str(lst[-1]))


def backtrace(S):
    '''Returns the path found by AStar'''
    global BACKLINKS
    path = []
    while S:
        path.append(S)
        S = BACKLINKS[S]
    path.reverse()
    print("Solution path: ")
    for s in path:
        print(s)
    return path


def report(open, closed, count):
    print("len(OPEN)=" + str(len(open)), end='; ')
    print("len(CLOSED)=" + str(len(closed)), end='; ')
    print("COUNT = " + str(count))


if __name__ == '__main__':
    runAStar()

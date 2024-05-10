from search import *

# Student(s): Patton Tang
# Course: CPSC-481
# Due Date: 2024-03-10

'''
The problem of crossing a river is represented by the letters F W G C and
a raft that may transport two persons/objects across the river at a time.
A state is represented by a set of letters in them. The goal represents the left bank.
F represents Farmer, W represents Wolf, G represents goat, C represents Cabbage.
'''
class WolfGoatCabbage(Problem):
    def __init__(self, initial=frozenset({'F', 'W', 'G', 'C'}), goal = frozenset()):
        super().__init__(initial, goal)

    def goal_test(self, state):
        if state == self.goal:
            return True
        return False

    def result(self, state, action):
        # Copy given state, then add letters if RtL or remove if LtR
        new_state = list(state)

        if 'F' in state: # Left to Right
            for letter in action:
                new_state.remove(letter)
        else: # Right to Left
            for letter in action:
                new_state.append(letter)
        return frozenset(new_state)

    def actions(self, state):
        # State represented by a set of characters crossing the river
        # possible_actions = [{'F'}, {'F', 'W'}, {'F', 'G'}, {'F', 'C'}]
        valid_acts = []

        if 'F' in state:
            # Cross River from Left to Right
            if 'W' in state and 'G' in state and 'C' in state:
                valid_acts.append({'F', 'G'})
            elif 'W' in state and 'G' in state:
                valid_acts.append({'F', 'W'})
                valid_acts.append({'F', 'G'})
            elif 'G' in state and 'C' in state:
                valid_acts.append({'F', 'G'})
                valid_acts.append({'F', 'C'})
            elif 'W' in state and 'C' in state:
                valid_acts.append({'F'})
                valid_acts.append({'F', 'W'})
                valid_acts.append({'F', 'C'})
            elif 'G' in state:
                valid_acts.append({'F', 'G'})
        elif 'F' not in state:
            # Cross River from Right to Left
            if 'W' in state and 'C' in state:
                valid_acts.append({'F'})
                valid_acts.append({'F', 'G'})
            else:
                if ('W') in state:
                    valid_acts.append({'F', 'G'})
                    valid_acts.append({'F', 'C'})
                elif ('G') in state:
                    valid_acts.append({'F'})
                    valid_acts.append({'F', 'W'})
                    valid_acts.append({'F', 'C'})
                elif ('C') in state:
                    valid_acts.append({'F', 'W'})
                    valid_acts.append({'F', 'G'})
        return valid_acts


# def main():
    # May set initial = FWGC, FWC, FG, WC
    '''wgc = WolfGoatCabbage(initial = ('F', 'W', 'G', 'C'), goal = ())
    solution = (depth_first_graph_search(wgc, h=None, display=True).solution())
    print(solution)
    solution = (breadth_first_graph_search(wgc, h=None, display=True).solution())
    print(solution)'''


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
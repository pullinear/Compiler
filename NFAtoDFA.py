# definition of DFA
#  delta = (state, input, result(state) )
#  start_state = "q0"
#  end_state = ["q3", "q4" ...]
#  string = [a, b]
#  state = ["q0", "q1" , "q2" , "q3"]


# definition of NFA
#  delta = (state, input, result(state) : list )
#  start_state = "q0"
#  end_state = ["q3", "q4" ...]
#  string = [a, b] + epsilon
#  state = ["q0", "q1" , "q2" , "q3"]

class DFA:
    states = []
    start_state = 0
    end_states = []
    strings = []
    delta = []

    def __init__(self, states:list, start_state: int, end_states: list, strings: list, delta: list):
        self.states = states
        self.start_state = start_state
        self.end_states = end_states
        self.strings = strings
        self.delta = delta
    


def DFA(states: list, start_state: int, end_states: list, string: list, delta: list):
    dfa = {}


def NFAtoDFA():
    pass


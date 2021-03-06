
class State:

    def __init__(self, is_initial_state = False, is_final_state = False, name = "q"):
        self.name             = name
        self.transitions      = {}
        self.is_initial_state = is_initial_state
        self.is_final_state   = is_final_state

    def add_transition(self, symbol, state):
        self.transitions[symbol] = state

    def validate_symbol(self, symbol):
        return self.transitions.get(symbol) != None

    def transition_state(self, symbol):
        if self.validate_symbol(symbol):
            return self.transitions.get(symbol)
        else:
            raise Exception("Invalid input!")

    def __repr__(self):
        return self.name


class Automata():

    def __init__(self):
        self.count         = 0
        self.current_state = None
        self.states        = [None]

    def has_any_initial(self):
        return any(st for st in self.states if st is not None and st.is_initial_state)

    def has_any_final(self):
        return any(st for st in self.states if st is not None and st.is_final_state)

    def add_state(self, state):
        state.name = state.name + str(self.count)
        self.states.append(state)
        self.count += 1
        if self.current_state == None:
            state.is_initial_state = True
            self.current_state     = state

    def remove_state(self, state):
        if state is not None:
                self.states.remove(state)

    def validate(self, input):
        for symbol in input:
            self.current_state = self.current_state.transition_state(symbol)
        if(self.current_state.is_final_state):
            validation_result = self.current_state.is_final_state
            self.current_state = self.states[1]
            return validation_result
        else:
            raise Exception("Invalid input!")

    def get_state(self, state):
        for st in self.states:
            if st != None:
                if st.name == str(state):
                    return st
        return None

    def make_initial_state(self, state):
        for st in self.states:
            if st != None:
                if str(st) != state:
                    st.is_initial_state = False
                else:
                    self.current_state = st
                    st.is_initial_state = True


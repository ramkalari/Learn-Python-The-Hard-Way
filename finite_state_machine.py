finite_state_machine = [states, actions, transition_function, start_state, accept_states]


def finite_state_machine(states, start_state):

	def next_state(current_state,action):
		

	def transition(action):
		next_state = self.current_state.next_state(action)
		self.current_state = next_state

	def start():
		self.current_state = start_state
		


def class State(object):

	def __init__(self, transitions, is_start_state = False, is_accept_state = False):
		self.transitions = transitions
		self.is_start_state = is_start_state
		self.is_accept_state = is_accept_state

	def next_state(self, action):

		if is_accept_state:
			return END_STATE

		else:
			next_state = self.transitions[action]	
			# handle the case where there is no next state for the action



def class Transition(object):
	
	def __init__(self, action, next_state):
		
		self.action = action
		self.next_state = next_state
   
	
	
def class Engine(object):

	def run():
		states = None # get list of states
		fsm_instance = fsm(states)
		fsm_instance.start() # puts this in the start state
		fsm_instance.transition(action)
	
	
				
	


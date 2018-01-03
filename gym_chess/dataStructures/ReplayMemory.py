import json

class ReplayMemory():
    "class to handle memory"
    def __init__(self):
        try:
            with open('data.json', 'r') as data_file:
                self.memory = json.load(data_file)
        except:
            self.memory = dict()
            squares = ['{}{}'.format(i, j) for i in 'abcdefgh' for j in range(1, 9)]
            for square_1 in squares:
                self.memory[square_1] = dict()
                for square_2 in squares:
                    self.memory[square_1][square_2] = dict()
            

    def push(self, origin_square, destination_square, state, action, next_state, q_value):
        """Saves a transition."""
        #create transition to store
        temp = dict()
        temp['action'] = action
        temp['next_state'] = next_state
        temp['q_value'] = q_value
        
        #if a transition with same characteristics exists, compare q_values
        try:
            old_state = self.memory[origin_square][destination_square][state]
            if q_value > old_state['q_value']:
                self.memory[origin_square][destination_square][state] = temp
        
        #otherwise create a new entry in the database
        except KeyError:
            self.memory[origin_square][destination_square][state] = temp
        
    def save(self):
        "load the database from memory"
        with open('data.json' 'w') as data_file:
            json.dump(self.memory, data_file, sort_keys=True, indent=4)

import time

class Genetic:
    def __init__(self):
        self.w1 = 1
        self.w2 = 1
        self.w3 = 1


    def eval(self, state):
        print(state)
        result = self.center_control(state) * self.w1
        result += self.winner(state) * self.w2
        # Implement genetic evaluation logic here
        print(result)
        state.value = result
        time.sleep(2)
        return state
    
    


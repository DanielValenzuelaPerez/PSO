class Particle:
    def __init__(self, x):
        self.x = x
        print("Hello! My position is at: " + str(self.x))
    
    def update(self):
        print("Swarm formation BEGIN! " + str(self.x))
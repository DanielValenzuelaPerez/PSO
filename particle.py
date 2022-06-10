from random import random

class Particle:
    global_best_fitness = None
    global_best_position = None
    def __init__(self):
        self.x = [random() * 5, random() * 5]
        self.v = [random(), random()]
        self.x = [self.x[0] + self.v[0], self.x[1] + self.v[1]] # Update position (pos + vel)

        self.w = 0.8
        self.r = [random(), random()]
        self.c = [0.1, 0.1]

        self.personal_best_fitness = None
        self.personal_best_position = self.x.copy()

        self.current_fitness = None
    
    def move(self):
        if Particle.global_best_fitness == None:
            return

        for i in range(len(self.v)):
            self.v[i] = self.w*self.v[i] + self.c[0]*self.r[0]*(self.personal_best_position[i] - self.x[i]) + self.c[1]*self.r[1]*(Particle.global_best_position[i] - self.x[i])
            self.x[i] = self.x[i] + self.v[i]
    
    def update_fitness(self, fitness):
        self.current_fitness = fitness

        if self.personal_best_fitness == None:
            self.personal_best_fitness = fitness
        if Particle.global_best_fitness == None:
            Particle.global_best_fitness = self.personal_best_fitness 
            Particle.global_best_position = self.personal_best_position.copy()
        
        if fitness < self.personal_best_fitness:
            self.personal_best_fitness = fitness
            self.personal_best_position = self.x.copy()

        if self.personal_best_fitness < Particle.global_best_fitness:
            Particle.global_best_fitness = self.personal_best_fitness
            Particle.global_best_position = self.personal_best_position.copy()
        
        self.printProgress()
    
    def printArray(self, array):
        msg = ""
        msg += "[{:.2f}".format(array[0]) + ", {:.2f}".format(array[1]) + "]\t"
        return msg
    
    def printProgress(self):
        msg = "(" + "{:.2f}".format(self.current_fitness) + ")"
        msg += self.printArray(self.x)
        msg += self.printArray(self.v)
        msg += "(" + "{:.2f}".format(self.personal_best_fitness) + ")"
        msg += self.printArray(self.personal_best_position)
        msg += "(" + "{:.2f}".format(Particle.global_best_fitness) + ")"
        msg += self.printArray(Particle.global_best_position)
        print(msg)
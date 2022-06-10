from math import sin
from particle import Particle

class Swarm:
    def __init__(self, number_of_particles):
        self.number_of_particles = number_of_particles
        print("Creating constructore with " + str(self.number_of_particles) + " particles.")
        self.particle = []
        for _ in range(self.number_of_particles):
            p = Particle()
            self.particle.append(p)
    
    def run_swarm_on_plane(self, plane, iterations):
        iteration = 0
        while iteration < iterations:
            print("--CURRENT FIT & POS-------VELOCITY---------PERSONAL BEST-----------GLOBAL BEST----@" + str(iteration))
            fitness = 0
            for particle in self.particle:
                particle.move();

                if plane == 1:
                    fitness = pow(particle.x[0], 2) + pow(particle.x[1], 2) # function x^2 + y^2 => (0) [0,0]
                elif plane == 2:
                    fitness = pow(particle.x[0], 3) + pow(particle.x[1], 3) - 12*particle.x[0]*particle.x[1] # x^3 + y^3 - 12xy => (-64) [4, 4]
                elif plane == 3:
                    fitness = pow(particle.x[0] - 3.14, 2) + pow(particle.x[1] - 2.72, 2) + sin(3*particle.x[0] + 1.41) + sin(4*particle.x[1] - 1.73)
                
                particle.update_fitness(fitness)
            iteration += 1

#        if(plane == 1):
 #           while iteration < iterations:
  #              print("--CURRENT FIT & POS-------VELOCITY---------PERSONAL BEST-----------GLOBAL BEST----@" + iteration)
   #             for i in range(self.number_of_particles):
    #                self.particle[i].move()
     #               fitness = pow(self.particle[i].x[0], 2) + pow(self.particle[i].x[1], 2) # function
      #              self.particle[i].update_fitness(fitness)
       #         iteration += 1

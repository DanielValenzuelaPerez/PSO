from particle import Particle
class Swarm:
    def __init__(self, number_of_particles):
        self.number_of_particles = number_of_particles
        print("Creating constructore with " + str(self.number_of_particles) + " particles.")
        self.particle = []
        for i in range(self.number_of_particles):
            p = Particle()
            self.particle.append(p)
    
    def run_swarm_on_plane(self, plane, iterations):
        iteration = 0
        if(plane == 1):
            while iteration < iterations:
                print("--CURRENT FIT & POS-------VELOCITY---------PERSONAL BEST-----------GLOBAL BEST----")
                for i in range(self.number_of_particles):
                    self.particle[i].move()
                    fitness = pow(self.particle[i].x[0], 2) + pow(self.particle[i].x[1], 2) # function
                    self.particle[i].update_fitness(fitness)
                iteration += 1

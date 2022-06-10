from particle import Particle
class Swarm:
    def __init__(self, number_of_particles):
        self.number_of_paritcles = number_of_particles
        print("Creating constructore with " + str(self.number_of_paritcles) + " particles.")
        self.particle = []
        for i in range(self.number_of_paritcles):
            p = Particle(i+1)
            self.particle.append(p)
    
    def run_swarm_on_plane(self, plane):
        if(plane == 1):
            for i in range(self.number_of_paritcles):
                self.particle[i].update()

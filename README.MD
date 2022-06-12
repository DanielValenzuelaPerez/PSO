# Particle Swarm Optimization
> Algorithm that finds the minima of a given function with an agent-based cooperation approach
## About

Particle Swarm Optimization is an algorithm that has a set of agents. Each agent searches for an optimal solution with the help of each other. As each agent can profit from the experience of all others.

[Image of the algorithm as it converges at one point]
Source: [gbhat](https://gbhat.com/machine_learning/pso_convex.html "gbhat post")

The way that cooperation works is by sharing a best global position among all the agents in the system, and updating their velocity according to its inertia, personal best position (**pbest**) and swarm's best position (**gbest**).

[function]

### Functions to optimize
Function 1 | Function 2 |  Function 3
-- | - | -
x^2 + y^2 | x^3 + y^3 - 12xy | (x - 3.14)^2 + (y - 2.72)^2 + sin(3x + 1.41) + sin(4y - 1.74)
image1 | image2 | image 3
Minimia: 0 | Minimia: -64  | Minimia: -1.81
Position: <0, 0> | Position: <4, 4> | Position: <3.18, 3.13>
### How to use

You can add as many 3D functions as you'd like. You would add them inside the function **run_swarm_on_plane** in the **swarm** class. The classes' structures are quite simple.

#### Master Class

    Swarm(number_of_particles)
        run_swarm_on_plane(plane, iterations)
    

#### Particle Class (*AKA Agent*)

    Particle()
        move()
        update_fitness()
        print_array()
        print_progress()

## Project based on

https://machinelearningmastery.com/a-gentle-introduction-to-particle-swarm-optimization/
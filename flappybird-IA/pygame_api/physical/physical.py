import math


class movement_vector():
    def __init__(self,angle,speed):
        self.angle=angle
        self.speed=speed


class world():
    def __init__(self,size,gravity,particles=None):
        self.size=size
        self.gravity=gravity
        if(particles==None):
            self.particles=[]
        else:
            self.particles=particles

    def add_particles(self,particles):
        if(not isinstance(particles,list) and not isinstance(particles,tuple)):
            self.particles.append(particles)
        else:
            for particle in particles:
                self.particles.append(particle)

    def move_particles(self,fps):
        for particle in self.particles:
            particle.move(fps)


class particle():
    def __init__(self,x,y,weight,angle,elasticity):
        self.x=x
        self.y=y
        self.weight=weight
        self.angle=angle
        self.elasticity=elasticity
        self.vectors_movement=[]

    def add_movement_vectors(self,movement_vector):
        self.vectors_movement.append(movement_vector)

    def move(self,fps):
        if(fps!=0):
            vector_final=self.vectors_movement[0]

            self.x += math.sin(vector_final.angle) * (vector_final.speed/fps)
            self.y -= math.cos(vector_final.angle) * (vector_final.speed/fps)



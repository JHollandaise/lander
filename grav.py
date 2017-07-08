import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 6.67428*(10**-11)
M = 6.42*(10**23)

# Time variants
t_max = 150000
dt = 10

# Starting values
pos_init = np.array([17031000,0,0])
vel_init = np.array([900,1000,0])


def Euler():

    # initialise pos and vel arrays
    pos_array = np.zeros(shape=(int(t_max/dt),3))
    vel_array = np.zeros(shape=(int(t_max/dt),3))

    # initialise fist pos and vel
    pos = pos_init
    vel = vel_init

    # integrate and populate arrays
    for i in range(np.shape(pos_array)[0]):

        # add latest value to array
        pos_array[i] = pos
        vel_array[i] = vel

        # calc next value

        # NOTE: not actually force, is f/m
        f = -(G*M)/(np.linalg.norm(pos)**3)*pos

        pos = pos + dt*vel
        vel = vel + dt*f

    # zip values from arrays
    pos_x, pos_y, pos_z = zip(*pos_array)


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(pos_x,pos_y,pos_z)

    plt.show()

def Verlet():
    # initialise pos and vel arrays
    pos_array = np.zeros(shape=(int(t_max/dt),3))
    vel_array = np.zeros(shape=(int(t_max/dt),3))

    # initialise fist pos and vel
    pos = pos_init
    vel = vel_init

    # set first and second array values
    pos_array[0] = pos
    pos_array[1] = pos = pos + dt*vel

    vel_array[0] = vel_array[1] = vel

    # integrate and populate arrays
    for i in range(2,np.shape(pos_array)[0]):

        # calc next
        f = -(G*M)/(np.linalg.norm(pos)**3)*pos

        pos = 2*pos - pos_array[i-2] + dt**2*f

        vel = (1/(2*dt))*(pos - pos_array[i-1])

        # add to array
        pos_array[i] = pos
        vel_array[i] = vel

    # zip values from arrays
    pos_x, pos_y, pos_z = zip(*pos_array)


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(pos_x,pos_y,pos_z)

    plt.show()

if __name__=="__main__":
    #Euler()
    Verlet()

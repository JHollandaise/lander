# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


# simulation time, timestep and time
t_max = 10
dt = 0.1
t_array = np.arange(0, t_max, dt)

def Euler():
    global t_array
    global dt
    # mass, spring constant, initial position and velocity
    m = 1
    k = 1
    x = 0
    v = 1

    # initialise empty lists to record trajectories
    x_list = []
    v_list = []

    # Euler integration
    for t in t_array:

        # append current state to trajectories
        x_list.append(x)
        v_list.append(v)

        # calculate new position and velocity
        a = -k * x / m
        x = x + dt * v
        v = v + dt * a

    # convert trajectory lists into arrays, so they can be indexed more easily
    x_array = np.array(x_list)
    v_array = np.array(v_list)

    # plot the position-time graph
    plt.figure(1)
    plt.clf()
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(t_array, x_array, label='x (m)')
    plt.plot(t_array, v_array, label='v (m/s)')
    plt.legend()
    plt.show()

def Verlet():
        global t_array
        global dt
        # mass, spring constant, initial position and velocity
        m = 1
        k = 1
        x = 0
        v = 1

        # initialise empty lists to record trajectories
        x_list = []
        v_list = []

        # adding first values of t-dt
        x_list.append(x + dt * v)

        # Integration
        for t in t_array:
            x_list.append(x)
            v_list.append(v)

            # find next values

            x = 2*x - x_list[-2] - dt**2*k*x/m
            v = 1/(2*dt)*(x-x_list[-2])

        del x_list[-1]
        # convert trajectory lists into arrays, so they can be indexed more easily
        x_array = np.array(x_list)
        v_array = np.array(v_list)

        # plot the position-time graph
        plt.figure(1)
        plt.clf()
        plt.xlabel('time (s)')
        plt.grid()
        plt.plot(t_array, x_array, label='x (m)')
        plt.plot(t_array, v_array, label='v (m/s)')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    Euler()
    Verlet()

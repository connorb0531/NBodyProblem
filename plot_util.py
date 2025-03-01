import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

FIG_SIZE = (5, 5)

def plot_solar_sys(history, N, attr):
    # Plot Trajectories (Full System View)
    fig = plt.figure(figsize=FIG_SIZE)
    ax = fig.add_subplot(111, projection='3d')
    
    for i in range(N):
        ax.plot(history[:, i, 0], history[:, i, 1], history[:, i, 2], 
        label=attr[0][i], color=attr[1][i])


    ax.scatter(history[-1, 0, 0], history[-1, 0, 1], history[-1, 0, 2], 
           color=attr[1][0], s=75)  # Large Sun marker

    # Axis Labels
    ax.set_xlabel("X Position (AU)")
    ax.set_ylabel("Y Position (AU)")
    ax.set_zlabel("Z Position (AU)")
    
    # Show Legend
    ax.legend()
    plt.ion()
    plt.show()

def plot_MS(history):
    # Plot Trajectories (Earth-Moon System View)
    fig = plt.figure(figsize=FIG_SIZE)
    ax = fig.add_subplot(111, projection='3d')
    
    # Normalize positions so Earth is at (0,0,0)
    moon_orbit = history[:, 2] - history[:, 1]  # Moon's motion relative to Earth
    
    # Plot Earth's motion at the center
    ax.scatter(0, 0, 0, color='blue', s=100, label="Earth")
    
    # Plot Moon's orbit around Earth
    ax.plot(moon_orbit[:, 0], moon_orbit[:, 1], moon_orbit[:, 2], 
            label="Moon's Orbit", color='gray')
    
    # Adjust limits for Earth-Moon distance (~384,000 km)
    ax.set_xlim([-5e8, 5e8])  # ±500,000 km
    ax.set_ylim([-5e8, 5e8])
    ax.set_zlim([-5e8, 5e8])
    
    # Set axis labels
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")
    ax.set_zlabel("Z Position (m)")
    ax.set_title("Moon's Orbit Around Earth")
    
    # Show Legend
    ax.legend()
    plt.show()

def plot_fig8(history):
    fig = plt.figure(figsize=FIG_SIZE)
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot trajectories of each body
    ax.plot(history[:, 0, 0], history[:, 0, 1], history[:, 0, 2], color='red')
    ax.plot(history[:, 1, 0], history[:, 1, 1], history[:, 1, 2], color='blue')
    ax.plot(history[:, 2, 0], history[:, 2, 1], history[:, 2, 2], color='green')

    # Mark final positions
    ax.scatter(history[-1, 0, 0], history[-1, 0, 1], history[-1, 0, 2], 
               color='red', s=100, marker='o', label="Body 1")
    ax.scatter(history[-1, 1, 0], history[-1, 1, 1], history[-1, 1, 2], 
               color='blue', s=100, marker='o', label="Body 2")
    ax.scatter(history[-1, 2, 0], history[-1, 2, 1], history[-1, 2, 2], 
               color='green', s=50, marker='o', label="Body 3")

    
    # Set labels
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")
    ax.set_zlabel("Z Position (m)")
    ax.set_title("Figure-8 Three-Body Orbit")

    ax.legend()
    plt.show()
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

FIG_SIZE = (5, 5)

def plot_EMS(history):
    plt.close('all')
    
    # Plot Trajectories (Full System View)
    fig = plt.figure(figsize=FIG_SIZE)
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the Sun's trajectory with an orange line
    ax.plot(history[:, 0, 0], history[:, 0, 1], history[:, 0, 2], 
            label="Sun", color='orange')  # Sun in orange
    
    # Plot Earth's trajectory in blue
    ax.plot(history[:, 1, 0], history[:, 1, 1], history[:, 1, 2], 
            label="Earth", color='blue')  # Earth in blue
    
    # Plot Moon's trajectory in grey
    ax.plot(history[:, 2, 0], history[:, 2, 1], history[:, 2, 2], 
            label="Moon", color='gray')  # Moon in grey
    
    # Scatter plot for the Sun (starting position) for visibility
    ax.scatter(history[-1, 0, 0], history[0, 0, 1], history[0, 0, 2], 
               color='orange', s=500)  # Large Sun marker
    
    # Axis Labels
    ax.set_xlabel("X Position (AU)")
    ax.set_ylabel("Y Position (AU)")
    ax.set_zlabel("Z Position (AU)")
    
    # Show Legend
    ax.legend()
    plt.ion()
    plt.show()
    
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
    plt.close('all')
    
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
               color='green', s=100, marker='o', label="Body 3")

    
    # Set labels
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")
    ax.set_zlabel("Z Position (m)")
    ax.set_title("Figure-8 Three-Body Orbit")

    ax.legend()
    plt.show()
import numpy as np

# ----------------------
# Solar System body data
# ----------------------

# Positions (X, Y, Z) in meters (m)
solar_sys_positions = np.array([
    [0, 0, 0],                 # Sun at origin
    [5.791e10, 0, 0],          # Mercury distance from Sun
    [1.082e11, 0, 0],          # Venus distance from Sun
    [1.496e11, 0, 0],          # Earth distance from Sun
    [2.279e11, 0, 0],          # Mars distance from Sun
    [7.786e11, 0, 0],          # Jupiter distance from Sun
    [1.433e12, 0, 0],          # Saturn distance from Sun
    [2.872e12, 0, 0],          # Uranus distance from Sun
    [4.495e12, 0, 0]           # Neptune distance from Sun
])

# Average velocities (Vx, Vy, Vz) in meters per second (m/s)
solar_sys_velocities = np.array([
    [0, 0, 1e2],                    # Sun stationary
    [0, 4.74e4, 0],               # Mercury orbits Sun
    [0, 3.50e4, 0],               # Venus orbits Sun
    [0, 2.978e4, 0],              # Earth orbits Sun
    [0, 2.4077e4, 0],             # Mars orbits Sun
    [0, 1.307e4, 0],              # Jupiter orbits Sun
    [0, 9.69e3, 0],               # Saturn orbits Sun
    [0, 6.81e3, 0],               # Uranus orbits Sun
    [0, 5.43e3, 0]                # Neptune orbits Sun
])

# Masses in kilograms (kg)
solar_sys_masses = np.array([
    1.989e30,    # Sun
    3.285e23,    # Mercury
    4.867e24,    # Venus
    5.972e24,    # Earth
    6.417e23,    # Mars
    1.898e27,    # Jupiter
    5.683e26,    # Saturn
    8.681e25,    # Uranus
    1.024e26     # Neptune
])

# Planet names and colors for visualization
solar_sys_attr = [
    ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],  # Names
    ["orange", "brown", "yellow", "blue", "red", "tan", "gold", "cyan", "darkblue"]         # Colors
]

# ---------------
# Figure-8 System
# ---------------
fig8_masses = np.array([1e30, 1e30, 1e30])

# Initial positions (meters) for fig8 bodies
fig8_positions = np.array([
    [-1.0, 0.0, 0.0],  
    [1.0, 0.0, 0.0],   
    [0.0, 0.0, 0.0]  
]) * 1e11  # Scale to astronomical distances

# Initial velocities (m/s) for fig8 mass bodies
fig8_velocities = np.array([
    [0.347111, 0.532728, 0.0],
    [0.347111, -0.532728, 0.0],
    [-0.694222, 0.0, 0.0]
]) * 1e4  # Scale to realistic speeds

# Planet names for Figure-8 system
fig8_planet_names = ["Body 1", "Body 2", "Body 3"]
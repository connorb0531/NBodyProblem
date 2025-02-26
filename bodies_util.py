import numpy as np

# Figure-8 System
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

# Earth-Moon-Sun (EMS) System

# Positions (X, Y, Z) in meters (m)
EMS_positions = np.array([
    [0, 0, 0],  # Sun at origin
    [1.5e11, 0, 0],            # Earth at 1 AU (~150 million km)
    [1.5e11 + 3.84e8, 0, 0]    # Moon 384,000 km from Earth
])

# Velocities (Vx, Vy, Vz) in meters per second (m/s)
EMS_velocities = np.array([
    [0, 0, -1],  # Sun stationary
    [0, 2.978e4, 0],              # Earth orbits Sun at ~29.78 km/s
    [0, 2.978e4 + 1.022e3, 0]     # Moon orbits Earth at ~1.022 km/s
])

# Masses in kilograms (kg)
EMS_masses = np.array([
    1.989e30,    # Sun (~1.989 × 10^30 kg)
    5.972e24,    # Earth (~5.972 × 10^24 kg)
    7.348e22     # Moon (~7.348 × 10^22 kg)
])

# Planet names for EMS system
EMS_names = ["Sun", "Earth", "Moon"]

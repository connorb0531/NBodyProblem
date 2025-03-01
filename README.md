# N-Body Problem Simulation

## Overview

This project simulates the motion of celestial bodies under the influence of gravity using numerical integration methods. The simulation implements both Euler's method and the fourth-order Runge-Kutta method (RK4) to solve the equations of motion.

## Features

- Supports an arbitrary number of bodies with customizable initial conditions.
- Implements Euler's method for basic integration.
- Implements the Runge-Kutta 4th-order method for higher accuracy.
- Visual representation of trajectories using Matplotlib.

## Prerequisites

- Python 3.x
- Jupyter Notebook
- Required libraries: NumPy, Matplotlib

## Installation

Clone the repository:

```bash
git clone https://github.com/your-repo/n-body-simulation.git
cd n-body-simulation
```

Install dependencies::
```bash
pip install numpy matplotlib
```

## Usage
Run the Jupyter Notebook:
```bash
jupyter notebook nbody_simulation.ipynb
```

## Performance Considerations
- Euler's method is faster but less accurate.
- RK4 provides better accuracy at the cost of additional computations.
- Performance can be improved using vectorized NumPy operations.

## Future Improvements
- Implement adaptive time-stepping.
- Add GPU acceleration for larger simulations using Numba or CuPy.
- Improve visualization with real-time animations using Matplotlib's FuncAnimation.

## Contact
For questions or contributions, contact connorbuckley144@gmail.com.

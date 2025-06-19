import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from scipy.interpolate import griddata

def plot_gradient_circle(points):
    # Extract coordinates and values
    x_coords, y_coords, values = zip(*points)
    
    # Normalize values for color mapping
    norm = mcolors.Normalize(min(values), max(values))
    cmap = cm.jet  # Use a colormap that has colors similar to the uploaded image
    
    # Create a grid to interpolate the values, ensuring it covers the entire circle
    grid_x, grid_y = np.mgrid[-radius:radius:200j, -radius:radius:200j]  # Create a finer grid for smoother interpolation
    grid_values = griddata((x_coords, y_coords), values, (grid_x, grid_y), method='cubic', fill_value=np.min(values))
    
    # Mask the grid values outside the circle to keep only the inside part
    mask = (grid_x**2 + grid_y**2) <= radius**2
    grid_values = np.where(mask, grid_values, np.nan)
    
    # Plot the filled gradient using the interpolated grid
    fig, ax = plt.subplots(figsize=(8, 8))
    im = ax.imshow(grid_values, extent=(-radius, radius, -radius, radius), origin='lower', cmap=cmap, norm=norm)
    
    # Plot the boundary of the circle
    circle = plt.Circle((0, 0), radius, color='black', fill=False, linewidth=2)
    ax.add_artist(circle)
    
    # Plot each point in the circle with colors matching the gradient
    ax.scatter(x_coords, y_coords, color=[cmap(norm(value)) for value in values], s=10, edgecolor='k')
    
    # Setting the aspect ratio to make sure it looks like a circle
    ax.set_aspect('equal')
    fig.colorbar(im, ax=ax, label='Value')
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Gradient Circle Plot")
    plt.show()
      

# Example usage:
num_points = 100
radius = 5
values = np.random.rand(num_points) * 100  # Random values between 0 and 100

# Calculate (x, y) positions of points randomly distributed within the circle
points = []
for _ in range(num_points):
    r = radius * np.sqrt(np.random.rand())  # Random radius within the circle
    angle = np.random.rand() * 2 * np.pi  # Random angle
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    value = np.random.rand() * 100
    points.append((x, y, value))

# Plot the gradient circle
plot_gradient_circle(points)

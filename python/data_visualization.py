import plotly.graph_objects as go
import numpy as np
import colorsys

def hsv_to_cartesian(hsv_values):
    """
    Convert HSV values to Cartesian coordinates for plotting.
    Hue is converted to angles, Saturation to radius (for point size), and Value directly maps to Z.
    """
    # Convert hue angle (0-360) to radians for X and Y calculations
    hues = np.radians([h * 360 for h, s, v in hsv_values])
    
    # Saturation will affect the size of the points
    saturations = [s * 100 for h, s, v in hsv_values]  # Example scale, adjust as needed
    
    # Value for Z-axis
    values = [v for h, s, v in hsv_values]
    
    # Calculate Cartesian coordinates for hue on a unit circle, ignoring saturation
    x = np.cos(hues)
    y = np.sin(hues)
    
    return x, y, values, saturations

def plot_hsv_values(hsv_values):
    """
    Plot a list of HSV values in 3D space using Plotly, with points colored according to their HSV values.
    """
    x, y, z, sizes = hsv_to_cartesian(hsv_values)

    # Prepare hover text
    hover_texts = []
    for h, s, v in hsv_values:
        # Convert to RGB
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        # Prepare RGB text
        rgb_text = f"RGB: ({int(r*255)}, {int(g*255)}, {int(b*255)})"
        # Prepare Saturation and Brightness text
        sat_text = f"Saturation: {int(s*100)}%"
        val_text = f"Brightness: {int(v*100)}%"
        # Combine into hover text for this point
        hover_text = f"{rgb_text}<br>{sat_text}<br>{val_text}"
        hover_texts.append(hover_text)
    
    # Convert HSV to RGB, then scale RGB to [0, 255] and format for Plotly
    rgb_colors = ['rgb({},{},{})'.format(int(r*255), int(g*255), int(b*255)) 
                  for h, s, v in hsv_values 
                  for r, g, b in [colorsys.hsv_to_rgb(h, s, v)]]

    fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=sizes,
            color=rgb_colors,  # Use the formatted RGB colors
            line=dict(width=0),
            opacity=1
        ),
        hoverinfo='text',
        text=hover_texts  # Use the prepared hover text
    )])
    
    # Update plot layout to make plots look like they are floating in empty space
    fig.update_layout(
        title='Image As 3D Color Wheel',
        scene=dict(
            xaxis=dict(showbackground=False, showticklabels=False, title=''),
            yaxis=dict(showbackground=False, showticklabels=False, title=''),
            zaxis=dict(showbackground=False, showticklabels=False, title=''),
            # You might also want to hide the grid and zero lines if needed
            xaxis_showgrid=False, yaxis_showgrid=False, zaxis_showgrid=False,
            xaxis_zeroline=False, yaxis_zeroline=False, zaxis_zeroline=False
        ),
        paper_bgcolor='rgba(0,0,0,0)', # Optional: Sets the background color of the plotting area to transparent
        plot_bgcolor='rgba(0,0,0,0)',  # Optional: Also set plot background to transparent
    )
    # Hide axis lines
    fig.update_scenes(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False)
    fig.show()

import tkinter as tk
from tkinter import filedialog
from PIL import Image
import numpy as np
import random
import colorsys

# Prompt the user to select an image file that is either a jpg, jpeg or png from
# their computer
def select_image_file():
    # Initialize the Tkinter root window
    root = tk.Tk()
    # Hide the root window
    root.withdraw()

    # Specify the file types to allow (JPG and PNG)
    filetypes = [
        ('Image files', '*.jpg *.jpeg *.png'),
        ('All files', '*.*')
    ]

    # Open the file dialog and allow the user to select an image file
    file_path = filedialog.askopenfilename(title='Select an Image File', filetypes=filetypes)

    # Return the selected file path
    return file_path


def extract_hsv_data(image_path):
    # Load the image
    img = Image.open(image_path)
    
    # Convert the image to RGB (if not already in RGB, e.g., if it's in palette mode)
    img = img.convert('RGB')
    
    # Convert the image to a NumPy array for easier access to pixels
    img_array = np.array(img)
    
    # Calculate a percentage of the pixels
    total_pixels = img_array.shape[0] * img_array.shape[1]
    sample_size = int(total_pixels * 0.001)
    
    # Generate random indices to sample pixels
    indices = random.sample(range(total_pixels), sample_size)
    
    # Flatten the image array to make indexing easier
    img_flat = img_array.reshape(-1, img_array.shape[-1])
    
    # Sample the pixels
    sampled_pixels = img_flat[indices]
    
    # Convert sampled pixels from RGB to HSV
    hsv_values = [colorsys.rgb_to_hsv(pixel[0]/255.0, pixel[1]/255.0, pixel[2]/255.0) for pixel in sampled_pixels]
    
    return hsv_values

def extract_hsv_data_from_all_pixels(image_path):
    # Load the image
    img = Image.open(image_path)
    
    # Convert the image to RGB (if not already in RGB, e.g., if it's in palette mode)
    img = img.convert('RGB')
    
    # Convert the image to a NumPy array for easier access to pixels
    img_array = np.array(img)
    
    # Reshape the image array to a 2D array where each row is a pixel
    img_flat = img_array.reshape(-1, img_array.shape[-1])
    
    # Convert all pixels from RGB to HSV
    hsv_values = [colorsys.rgb_to_hsv(pixel[0]/255.0, pixel[1]/255.0, pixel[2]/255.0) for pixel in img_flat]
    
    return hsv_values

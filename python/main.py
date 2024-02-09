# main.py
import image_selection
from image_selection import select_image_file, extract_hsv_data
from data_visualization import plot_hsv_values

def main():
    # user selects image from computer
    image_path = select_image_file()
    print("Selected image path:", image_path)

    if image_path:
        # Image data is converted into a list of Hue, Saturation, and Value (HSV) Data
        hsv_data = extract_hsv_data(image_path) #  using only a random selection of pixels
        plot_hsv_values(hsv_data)

    else:
        print("No Image Selected")

if __name__ == "__main__":
    main()

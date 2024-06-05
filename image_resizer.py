import os
from PIL import Image

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)

def resize_images_in_directory(directory, output_directory, size):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)
            resize_image(input_path, output_path, size)
            print(f"Resized {filename} and saved to {output_path}")

if __name__ == "__main__":
    input_directory = input("Enter the directory of images to resize: ")
    output_directory = input("Enter the output directory for resized images: ")
    width = int(input("Enter the width for resizing: "))
    height = int(input("Enter the height for resizing: "))
    size = (width, height)

    resize_images_in_directory(input_directory, output_directory, size)
    print("All images have been resized.")
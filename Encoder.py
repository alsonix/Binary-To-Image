from PIL import Image
import math
from alive_progress import alive_bar

data = input("Enter path to binary file: ")
xPixels = int(input("Enter X pixels (HORIZONTAL): "))
yPixels = int(input("Enter Y pixels (VERTICAL): "))

def encode_binary_to_image(binary_file, image_width, image_height):
    # Prepare data for encoding binary file
    with open(binary_file, 'rb') as f:
        data = f.read()
    data = [int(bit) for byte in data for bit in format(byte, '08b')]

    # Calculate the number of images needed to encode the binary file
    num_pixels_per_image = image_width * image_height
    num_images = math.ceil(len(data) / num_pixels_per_image)
    if num_images > 1:
        print()
        print("=====================================================@")
        print("Insuficient space in Image. Image is now multiplying.|")
        print("=====================================================@")

    # Encode data into images
    for i in range(num_images):
        # Create a new image with the desired dimensions
        image = Image.new('1', (image_width, image_height))  # '1' indicates binary mode (1 bit per pixel)

        # Get the data for this image
        start_index = i * num_pixels_per_image
        end_index = min(start_index + num_pixels_per_image, len(data))
        image_data = data[start_index:end_index]

        # Encode data into the image
        pixel_index = 0
        print()
        with alive_bar(len(image_data)) as bar:
            for bit in image_data:
                x = pixel_index % image_width
                y = pixel_index // image_width
                image.putpixel((x, y), bit)
                pixel_index += 1
                bar()

        # Save the encoded image
        if num_images == 1:
            filename = './DATA/rawdata.png'
        else:
            filename = f'./DATA/rawdata_part{i+1}.png'
    
            # Crop the image if it is the last one
            if i == num_images - 1:
                y_max = math.ceil(len(image_data) / image_width)
                image = image.crop((0, 0, image_width, y_max))
        
        image.save(filename)
        print(f"[AI]~# Binary encoded to: [{filename}]")

        
        # Display remaining bits
        remaining_bits = num_pixels_per_image - len(image_data)
        print(f"[AI]~# Remaining bits: [{remaining_bits}]")

# Use function to encode binary file into an image
encode_binary_to_image(data, xPixels, yPixels)

end = input()

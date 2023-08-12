from PIL import Image
import os
from alive_progress import alive_bar

def decode_binary_from_images(image_prefix, output_file):
    # Check if there is a single image file to decode
    if os.path.exists(f'{image_prefix}.png'):
        image_files = [f'{image_prefix}.png']
    else:
        # Get the list of image files to decode
        image_files = []
        i = 1
        while True:
            image_file = f'{image_prefix}_part{i}.png'
            if os.path.exists(image_file):
                image_files.append(image_file)
                i += 1
            else:
                break

    # Decode data from the images
    binary_data = bytearray()
    for image_file in image_files:
        # Open the image
        image = Image.open(image_file)

        # Get the dimensions of the image
        image_width, image_height = image.size

        # Decode data from the image
        data = []
        with alive_bar(image_width * image_height, title=f"Decoding {os.path.basename(image_file)}", bar='blocks') as bar:
            for y in range(image_height):
                for x in range(image_width):
                    pixel_value = image.getpixel((x, y))
                    data.append(pixel_value)
                    bar()

        print(f"[AI]~# File {os.path.basename(image_file)} has been successfully decoded.")
        print()

        # Decode data into binary
        binary_str = ""
        for pixel_value in data:
            # Convert pixel value to binary string
            binary_str += '1' if pixel_value > 127 else '0'

            # If we have reached 8 bits, convert them to a byte
            if len(binary_str) == 8:
                decimal_value = int(binary_str, 2)
                binary_data.append(decimal_value)
                binary_str = ""

    # Write decoded binary data to output file
    with open(output_file, 'wb') as f:
        f.write(binary_data)

# Use function to decode binary data from a single or multiple images
decode_binary_from_images("./DATA/rawdata", "raw.bin")
print("Image RAW data has been saved to >> [raw.bin].")

end = input()

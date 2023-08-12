# Binary-To-Image
How it works:

1. A file Encode.py takes the binary file that the user selects and then converts that binary file to binary data that is encoded into the PNG file.
   For example:
     1.1. Path: test.mp3 (For example, size is 145kB [1,160,000 bit])
     1.2. X_PIXELS: 1024
     1.3. Y_PIXELS: 1024
     1.4. So if you enter the output image size of 1024x1024, you get a total of the ability to encode up to 1,048,576 bits into one image.
          This would encode the image into the rawdata.png file. In our case, however, our file, which occupies 1,160,000 bits, cannot be
          written into this image because it does not fit into it, so there is a solution. So if our file takes up more space that is not
          normally possible to encode into this file, the output PNG file is divided into PARTs. In our case, it would be divided into
          files: rawdata_part1.png andrawdata_part2.png. This would store 1,048,576 bits in the rawdata_part1.png file and the remaining
          111,424 bits would be stored in the second rawdata_part2.png file.

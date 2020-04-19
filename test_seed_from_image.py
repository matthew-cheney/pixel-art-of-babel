from sys import argv

if len(argv) < 3:
    print(f'USAGE: {argv[0]} <path_to_image> <destination_file>')
    exit(1)

image_filename = argv[1]
dest_filename = argv[2]

from PIL import Image

im = Image.open(image_filename)

import numpy as np

im_array = np.array(im)

from PixelArtOfBabel.seed_from_image import seed_from_image

seed1 = seed_from_image(im_array)
seed2 = seed_from_image(im_array)

with open(f'00_{dest_filename}', 'w') as f:
    print(seed1, file=f, end='')
with open(f'01_{dest_filename}', 'w') as f:
    print(seed2, file=f, end='')

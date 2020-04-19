from sys import argv

from PixelArtOfBabel.seed_from_image import seed_from_image

if len(argv) < 3:
    print(f'USAGE: {argv[0]} <path_to_image> <destination_file>')
    exit(1)

image_filename = argv[1]
dest_filename = argv[2]

from PIL import Image

im = Image.open(image_filename)

seed1 = seed_from_image(im)
seed2 = seed_from_image(im)

with open(f'00_{dest_filename}', 'w') as f:
    print(seed1, file=f, end='')
with open(f'01_{dest_filename}', 'w') as f:
    print(seed2, file=f, end='')

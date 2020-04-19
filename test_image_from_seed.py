from sys import argv

if len(argv) < 3:
    print(f'USAGE: {argv[0]} <path_to_seed> <destination_filename>')
    exit(1)

seed_filename = argv[1]
dest_filename = argv[2]
with open(seed_filename, 'r') as f:
    seed = f.read()

from PixelArtOfBabel.image_from_seed import image_from_seed

array1 = image_from_seed(seed)
array2 = image_from_seed(seed)

from PIL import Image

new_image = Image.fromarray(array1)
new_image.save(f'{dest_filename}')

# new_image = Image.fromarray(array2)
# new_image.save(f'01_{dest_filename}')

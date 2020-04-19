from PixelArtOfBabel.dictionaries import rgb_to_index, indices_to_seed_char
import numpy as np

IMAGE_WIDTH = 64
IMAGE_HEIGHT = 64

def seed_from_image(image):

    image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    image_array = np.array(image)

    row = 0
    col = 0
    seed = ''
    while row < len(image_array):
        v1 = tuple(image_array[row][col])
        v2 = tuple(image_array[row][col + 1])
        i1 = rgb_to_index[v1]
        i2 = rgb_to_index[v2]
        seed_char = indices_to_seed_char[(i1, i2)]
        seed += seed_char
        col += 2
        if col > len(image_array[0]) - 2:
            col = 0
            row += 1
    return seed

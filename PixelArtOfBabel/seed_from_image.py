from PixelArtOfBabel.dictionaries import rgb_to_index, indices_to_seed_char
import numpy as np
from scipy.spatial import distance

IMAGE_WIDTH = 64
IMAGE_HEIGHT = 64

def seed_from_image(image):

    image_small = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    image_array = np.array(image_small)

    row = 0
    col = 0
    seed = ''
    while row < len(image_array):
        v1 = tuple(image_array[row][col])
        v2 = tuple(image_array[row][col + 1])

        # approximate closest of given colors
        best_match1 = (None, float('inf'))
        for rgb in rgb_to_index.keys():
            dist = distance.euclidean(v1, rgb)
            if dist < best_match1[1]:
                best_match1 = (rgb, dist)
        best_match2 = (None, float('inf'))
        for rgb in rgb_to_index.keys():
            dist = distance.euclidean(v2, rgb)
            if dist < best_match2[1]:
                best_match2 = (rgb, dist)

        i1 = rgb_to_index[best_match1[0]]
        i2 = rgb_to_index[best_match2[0]]
        seed_char = indices_to_seed_char[(i1, i2)]
        seed += seed_char
        col += 2
        if col > len(image_array[0]) - 2:
            col = 0
            row += 1
    return seed

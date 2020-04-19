import numpy as np

seed_char_to_indices = {
    '0': (0, 0),
    '1': (0, 1),
    '2': (0, 2),
    '3': (0, 3),
    '4': (0, 4),
    '5': (0, 5),
    '6': (0, 6),
    '7': (0, 7),
    '8': (1, 0),
    '9': (1, 1),
    'a': (1, 2),
    'b': (1, 3),
    'c': (1, 4),
    'd': (1, 5),
    'e': (1, 6),
    'f': (1, 7),
    'g': (2, 0),
    'h': (2, 1),
    'i': (2, 2),
    'j': (2, 3),
    'k': (2, 4),
    'l': (2, 5),
    'm': (2, 6),
    'n': (2, 7),
    'o': (3, 0),
    'p': (3, 1),
    'q': (3, 2),
    'r': (3, 3),
    's': (3, 4),
    't': (3, 5),
    'u': (3, 6),
    'v': (3, 7),
    'w': (4, 0),
    'x': (4, 1),
    'y': (4, 2),
    'z': (4, 3),
    'A': (4, 4),
    'B': (4, 5),
    'C': (4, 6),
    'D': (4, 7),
    'E': (5, 0),
    'F': (5, 1),
    'G': (5, 2),
    'H': (5, 3),
    'I': (5, 4),
    'J': (5, 5),
    'K': (5, 6),
    'L': (5, 7),
    'M': (6, 0),
    'N': (6, 1),
    'O': (6, 2),
    'P': (6, 3),
    'Q': (6, 4),
    'R': (6, 5),
    'S': (6, 6),
    'T': (6, 7),
    'U': (7, 0),
    'V': (7, 1),
    'W': (7, 2),
    'X': (7, 3),
    'Y': (7, 4),
    'Z': (7, 5),
    '-': (7, 6),
    '_': (7, 7),
}

indices_to_seed_char = {
    (0, 0): '0',
    (0, 1): '1',
    (0, 2): '2',
    (0, 3): '3',
    (0, 4): '4',
    (0, 5): '5',
    (0, 6): '6',
    (0, 7): '7',
    (1, 0): '8',
    (1, 1): '9',
    (1, 2): 'a',
    (1, 3): 'b',
    (1, 4): 'c',
    (1, 5): 'd',
    (1, 6): 'e',
    (1, 7): 'f',
    (2, 0): 'g',
    (2, 1): 'h',
    (2, 2): 'i',
    (2, 3): 'j',
    (2, 4): 'k',
    (2, 5): 'l',
    (2, 6): 'm',
    (2, 7): 'n',
    (3, 0): 'o',
    (3, 1): 'p',
    (3, 2): 'q',
    (3, 3): 'r',
    (3, 4): 's',
    (3, 5): 't',
    (3, 6): 'u',
    (3, 7): 'v',
    (4, 0): 'w',
    (4, 1): 'x',
    (4, 2): 'y',
    (4, 3): 'z',
    (4, 4): 'A',
    (4, 5): 'B',
    (4, 6): 'C',
    (4, 7): 'D',
    (5, 0): 'E',
    (5, 1): 'F',
    (5, 2): 'G',
    (5, 3): 'H',
    (5, 4): 'I',
    (5, 5): 'J',
    (5, 6): 'K',
    (5, 7): 'L',
    (6, 0): 'M',
    (6, 1): 'N',
    (6, 2): 'O',
    (6, 3): 'P',
    (6, 4): 'Q',
    (6, 5): 'R',
    (6, 6): 'S',
    (6, 7): 'T',
    (7, 0): 'U',
    (7, 1): 'V',
    (7, 2): 'W',
    (7, 3): 'X',
    (7, 4): 'Y',
    (7, 5): 'Z',
    (7, 6): '-',
    (7, 7): '_',
}


index_to_rgb = {
    0: (np.uint8(0),np.uint8(0),np.uint8(0)),
    1: (np.uint8(255),np.uint8(255),np.uint8(255)),
    2: (np.uint8(255),np.uint8(0),np.uint8(0)),
    3: (np.uint8(255),np.uint8(160),np.uint8(16)),
    4: (np.uint8(255),np.uint8(224),np.uint8(32)),
    5: (np.uint8(0),np.uint8(192),np.uint8(0)),
    6: (np.uint8(0),np.uint8(32),np.uint8(255)),
    7: (np.uint8(160),np.uint8(32),np.uint8(255)),
    }

rgb_to_index = {
    (np.uint8(0),np.uint8(0),np.uint8(0)): 0,
    (np.uint8(255),np.uint8(255),np.uint8(255)): 1,
    (np.uint8(255),np.uint8(0),np.uint8(0)): 2,
    (np.uint8(255),np.uint8(160),np.uint8(16)): 3,
    (np.uint8(255),np.uint8(224),np.uint8(32)): 4,
    (np.uint8(0),np.uint8(192),np.uint8(0)): 5,
    (np.uint8(0),np.uint8(32),np.uint8(255)): 6,
    (np.uint8(160),np.uint8(32),np.uint8(255)): 7,
}

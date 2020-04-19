import numpy as np

from PixelArtOfBabel.dictionaries import seed_char_to_indices, index_to_rgb

IMAGE_WIDTH = 64  # must be even number
IMAGE_HEIGHT = 64

def image_from_seed(seed):
    if len(seed) < (IMAGE_WIDTH * IMAGE_HEIGHT) // 2:
        # Seed is too short, front fill with 0s
        nseed = ''.join(['0' for i in range((IMAGE_WIDTH * IMAGE_HEIGHT) // 2 - len(seed))]) + seed
    else:
        nseed = seed
    image_array = [[(np.uint8(0),np.uint8(0),np.uint8(0)) for i in range(IMAGE_WIDTH)] for j in range(IMAGE_HEIGHT)]
    row = 0
    col = 0
    for c in nseed:
        cell_pair = seed_char_to_indices[c]
        image_array[row][col] = index_to_rgb[cell_pair[0]]
        image_array[row][col + 1] = index_to_rgb[cell_pair[1]]
        col += 2
        if col > IMAGE_WIDTH - 2:
            col = 0
            row += 1
    return np.array(image_array, dtype=np.uint8)

if __name__ == '__main__':
    array1 = image_from_seed('9WlWKlySlRd26MsX1xkfst4ZhvCGC-XB_3kB3KmIhcv97q9mMISkN11u24C8izKbaVUTGQRF3_n3kKtfrRfXjBFLKUDWaiYLyEFymSOxlUXzZK20OJlvJ_3eBQdnEPHqOXh1q70R2JHXtCW2SoeUMAYfLIgRnM3puYVX5OeAScFwAri53Qew9HXDJUXFQwtdKJE8Hvi9pdsoYVG142Ipv8HM9x1xyRM2sxWeJGiLRQLw8mjprYZZt1Y2gl_VN40YgiypFLyAIfS4NAcPgQhDOdIO5lh6yYFDTK54rOD49BFHFRcQ7SUaeJ-cFIWEswFsycs4vrBao8_5ZjFlwS1e0trLn4sAXUmW_kY2glSthE-gydOKFxPFk_vNriFfkdZVHkeFG4yO_qjQCr7EjQbrs9EoAMb4KlSjH-rqSf6Xd4nRv7Cmbf2osVrKj2iNdWNCmJQ0BbqDF2TMOLdhaZh0jPqEaoQIl5KaX_95azE1WraqbeasMWAG7-D8ZOvdANJTUjW6FGVMWUweW9lUslYyvWElSpRXFt5cppOrnWt89pPIufO_jQI9hVZt4BTjSqE72kcYyOx4VQuD7cui6FmM6t49mJAWh0lDS3Aytly_W3oggH45W1QZn-qrvoqwXvKssPswR7BoitEdjTetQvJXGmIa4xTcr3AhgEpvfJykEj6yQJRuaGe3lLuhjY189t2qgZPYFVGfOrGdSEB8MGpV2uzU34iC8bIvaNhyK4FfCoyANHl7lQf9jFnnntwaAUQ9wmx4rRi6G77zjmi5bb9SUiI1MaUCRjG8BbtnC_zd2kbMXoteNW-H_IxcGC4d44Qpv07UtKuEG94N_ANPiRxJupZ_0ee0PCN8K7UstOCjoOkW7IwRATP55D0QCMd3TmpXlBnnLE1QdHdL2TLUdEPw5sxOjNsarNnXohYFb3xU9iDpSQnlH7RMChtAHDvuWbiXXFyKNiPQpobI-rSrywE1i5xKgDqLbc8ED61zRbbqGkA5L4Bz2aZ8uCsY6olyTNPNnxKAyJCfZSgss8K0aAhwhAD18gPqb_XU0On_iHRYXCwnuGfOC0N7MEmRtJed6wEekzkL9wHE3mMFyd61NdoMxUFCuOOA67LVhl-MVsJ-VVMhyLh1G8hnfZvuYL81QihHmxcmMfDefmdBz8BNUnJ86n0Mb3ccgts5qBeIuZLMLnxww67tJro1Aka79xsHpCM96hoEUwOninW78iIdm2rQoZBC10v1EuShHqo8J6d2dGYZO99uitx-b1QQqu1gjSnWXEnFTrWvMocZUwzZxucV3FbUW3DTlq-j2rBVdMbT4RbrW2EXsDRCQrWsQNgYmXYX0TN_T9yATBLMxX6yihr3002UUxmxdOO4GRaXlXfmt34AYoH1qr64ZTRSX13qnEWVgOGGuffrtJY6N30U3PbWoAjvECnJGhwKuOACiDYKrYskxEMil2O5hCBcoSHnz3Njhp8JJyV-feSOBlt0uiR83sVL--87MflT_OgNdZ-YMhjok2yZvoGrTBDumw9pD2b9ocVk0AMf2ULlVOfUHUwAf5nAx7bv_VbjX_pbXXXi0HEnGknqryz1affVCb8KWe_lIbJCx9e1hG90aG5LirsDOrBHCyAWx6Nh33HYXe_YLn6RhjxCTI2EdW4BI96FUyD_so63A8abS9Kh_Mfji75757hsBnTs3FgMBO-HDFddbAO90JB3n8rtcaeHxtf7L5uGf3Wk1WfLHp3Xafn5BwSFG8M9q45pR538a1jQPsNGEnHnHUOHHbDp5nUpkPIUU0M62nu1b5jShnYYq0hq2AJHgudbqgC6QVUThLDXlfneIiG8DZhvpM2eUBQtDfI6xd13DRtYdbOQnC4QpqDdk7mY_q-le7bSelpjne5ulkBbZoP6dTN0Ezbp3A6E1KUO4q_bL15z5zSxJbvETLitruBwTxvnCZ1-KCS9ijB-7dM9NwsmOcJAgE0TTevaoKjGpfrWj--a8L4npuk3TPZAe7nbs8PlcS_7EffmQ9SD66dG1H9yBGLIYzZFmCGEKpShxRrw')
    x = 0
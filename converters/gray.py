import math
from time import perf_counter

import cv2
import numpy as np
import pyperclip

import data
from trim import trim_text

COLOR_NAMES = data.COLOR_NAMES_GRAY
COLOR_KEYS = list(COLOR_NAMES.keys())
COLOR_VALUES = np.array(list(COLOR_NAMES.values()))


def closest_color(pixel: int) -> str:
    return COLOR_KEYS[np.argmin(np.abs(COLOR_VALUES - pixel))]


def resize_image(img: np.ndarray, pixels) -> np.ndarray:
    height, width = img.shape
    total_pixels = height * width
    scale_factor = math.sqrt(pixels / total_pixels)
    print(f"Original image pixels: {total_pixels}", end="\t")
    print(f"Pixels: {pixels:04d}", end="\t")
    print(f"Scale factor: {scale_factor:.5f}", end="\t")

    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

    height, width = resized_img.shape
    total_pixels = height * width

    print(f"Resized image pixels: {total_pixels}", end="\t")

    return resized_img

def img_to_ascii(img: np.ndarray, pixels: int) -> str:
    resized_img = resize_image(img, pixels)

    ascii_lines = []
    prev_color = None
    for row in resized_img:
        line_chars = []
        for pixel in row:
            current_color = closest_color(pixel)

            if current_color != prev_color:
                line_chars.append(current_color + current_color[-1])
                prev_color = current_color
            else:
                line_chars.append(current_color[-1] + current_color[-1])
        ascii_lines.append("".join(line_chars))

    ascii_art = "\n".join(ascii_lines)
    ascii_art = trim_text(ascii_art)
    ascii_art = f"```\n{ascii_art.rstrip()}```"

    print(f"Length of ascii art: {len(ascii_art)}", end="\t")
    return ascii_art


def process_image(path: str, length: int) -> None:
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    pixels = int((length - 10) / 7)
    interation = 0
    res = None

    while True:
        interation += 1
        print(f"\rIteration: {interation}", end="\t")
        new_ascii = img_to_ascii(img, pixels)
        pixels += 10

        if len(new_ascii) > 2000:
            break

        res = new_ascii

    pyperclip.copy(res)
    print("\nFinal ASCII Art:")
    print(res + "[0m")
    print(f"Final length: {len(res)}")


if __name__ == "__main__":
    start_time = perf_counter()

    process_image("../images/a50821d98a87b2b7e5b6862829c5d544.jpg", 2000)

    print(f"Total processing time: {perf_counter() - start_time:.3f} сек")

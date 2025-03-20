import math
from time import perf_counter

import cv2
import numpy as np
import pyperclip

import data
from trim import trim_text

COLOR_NAMES = None
COLOR_KEYS = None
COLOR_VALUES = None


def closest_color(pixel: np.ndarray) -> str:
    rgb_pixel = pixel[::-1]

    distances = np.sum((COLOR_VALUES - rgb_pixel) ** 2, axis=1)
    idx = np.argmin(distances)
    return COLOR_KEYS[idx]


def resize_image(img: np.ndarray, pixels) -> np.ndarray:
    height, width, _ = img.shape
    total_pixels = height * width
    scale_factor = math.sqrt(pixels / total_pixels)
    print(f"Original image pixels: {total_pixels}", end="\t")
    print(f"Pixels: {pixels:04d}", end="\t")
    print(f"Scale factor: {scale_factor:.5f}", end="\t")

    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

    height, width, _ = resized_img.shape
    total_pixels = height * width

    print(f"Resized image pixels: {total_pixels}", end="\t")

    return resized_img


def img_to_ascii(img: np.ndarray, pixels: float) -> str:
    resized_img = resize_image(img, pixels)

    ascii_lines = []
    prev_color = None
    for row in resized_img:
        line_chars = []
        for pixel in row:
            current_color = closest_color(pixel)

            if current_color == prev_color:
                line_chars.append(current_color[-1] + current_color[-1])
            else:
                line_chars.append(current_color + current_color[-1])
                prev_color = current_color

        ascii_lines.append("".join(line_chars))

    ascii_art = "\n".join(ascii_lines)
    if ascii_art.startswith("[0m"):
        ascii_art = ascii_art[4:]

    ascii_art = trim_text(ascii_art)
    ascii_art = f"```ansi\n{ascii_art.rstrip()}```"

    print(f"Length of ascii art: {len(ascii_art)}", end="\t")
    return ascii_art


def process_image(path: str, length: int, color: str) -> None:
    global COLOR_NAMES
    global COLOR_KEYS
    global COLOR_VALUES

    if color == "9-bit":
        COLOR_NAMES = data.COLOR_NAMES_261
    elif color == "6-bit":
        COLOR_NAMES = data.COLOR_NAMES_33
    else:
        raise ValueError("Unknown color mode.")

    COLOR_KEYS = list(COLOR_NAMES.keys())
    COLOR_VALUES = np.array(list(COLOR_NAMES.values()))

    img = cv2.imread(path)
    pixels = int((length - 10) / 7)
    interation = 0
    res = None

    while True:
        interation += 1
        print(f"\rIteration: {interation}", end="\t")
        pixels += 10
        new_ascii = img_to_ascii(img, pixels)

        if len(new_ascii) > length:
            break

        res = new_ascii

    pyperclip.copy(res)
    print("\nFinal ASCII Art:")
    print(res + "[0m")
    print(f"Final length: {len(res)}")


if __name__ == "__main__":
    start_time = perf_counter()

    process_image("../images/a50821d98a87b2b7e5b6862829c5d544.jpg", 2000, "9-bit")

    print(f"Total processing time: {perf_counter() - start_time:.3f} сек")

import pyperclip
import time

colors = []

def loop():
    color = None

    while True:
        time.sleep(0.1)
        buffer = pyperclip.paste()

        if buffer == color:
            continue
        else:
            color = buffer

        if len(color) == 6:
            r = int(color[0:2], 16)
            g = int(color[2:4], 16)
            b = int(color[4:6], 16)

            rgb = f"({r}, {g}, {b})"

            print(rgb)

            colors.append(rgb)


try:
    loop()
except KeyboardInterrupt:
    print(colors)
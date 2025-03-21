<p align="center">
    <img style="width: 100px; height: auto;" src="https://github.com/user-attachments/assets/76031be2-f446-4a19-a61c-b1fe8de98ea8">
</p>
<h3 align="center" id="discord-ansi-art-generator">
    Discord ANSI Art Generator
</h3>
<p align="center">
    Make beautiful arts in Discord using ANSI and Python
</p>

## `🔱` Table of Contents

- [🥽┃Requirements](#-requirements-)
- [🔮┃Installation](#-installation-)
- [🎮┃Usage](#-usage-)
- [🚧┃Warnings & Tips](#-warnings--tips-)
- [🌠┃Plans](#-plans-)
- [📝┃License](#-license-)
- [💽┃Examples](#-examples-)
- [🎨┃Colors](#-colors-)

## `🥽` Requirements [🔼](#discord-ansi-art-generator)

- [Python](https://www.python.org/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Inquirer](https://pypi.org/project/inquirer/)
- [Numpy](https://pypi.org/project/numpy/)
- [Pyperclip](https://pypi.org/project/pyperclip/)

## `🔮` Installation [🔼](#discord-ansi-art-generator)

### `📦┃Linux/macOS`
```bash
git clone https://github.com/satrak33/Art_Generator
cd Art_Generator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### `📦┃Windows`
```bash
git clone https://github.com/satrak33/Art_Generator
cd Art_Generator
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## `🎮` Usage [🔼](#discord-ansi-art-generator)
```bash
python main.py
```
#### Or using without SLI
- [Gray converter](./converters/gray.py)
- [Color converter](./converters/color.py)

## `🚧` Warnings & Tips [🔼](#discord-ansi-art-generator)
### `🎈` Tips:
- You can right-click in cmd or powershell to paste the path
- The optimizing algorithm works better with pictures that have one dominating color
- The 6-bit color mode is more suitable for black and white images

### `🔥` Warnings:
- Don't use huge custom lengths, it will take a lot of time, and time will increase in geometry progression
- ANSI doesn’t support purple
- IDE's terminals don't support SLI

## `🌠` Plans [🔼](#discord-ansi-art-generator)
- Try to add more color modes by making automatic algorithm
- Create Discord application 
- Create site using GitHub Pages

## `📝` License [🔼](#discord-ansi-art-generator)
You can read license [here](./LICENSE) 

## `💽` Examples [🔼](#discord-ansi-art-generator)

#### `Disnake logo (mod: 9-bit)`
<img style="width: auto; height: 200px;" src="https://github.com/user-attachments/assets/a89ab64d-fca4-4c9f-9c3e-e111a3bf694a">
<img style="width: auto; height: 200px;" src="https://github.com/user-attachments/assets/7936102a-8671-4cea-84de-b96d9debca8f">

#### `Isagi eye (mod: gray)`
<img style="width: auto; height: 200px;" src="https://github.com/user-attachments/assets/5b3d9850-9311-4e5c-af51-879651e4dc7d">
<img style="width: auto; height: 200px;" src="https://github.com/user-attachments/assets/29630c3e-0cae-4f24-8c16-3e873581c07d">


#### `Meteor (mod: 6-bit)`
<img style="width: auto; height: 200px;" src="https://github.com/user-attachments/assets/c1667b31-3861-41e2-8141-74f922cb6c46">
<img style="width: auto; height: 200px;" src="https://github.com/user-attachments/assets/5c8f8243-8518-4f5b-aee3-d6045eb0d4fd">

### `🎨` Colors [🔼](#discord-ansi-art-generator)
#### `9-bit`
<img style="width: auto; height: 300px;" src="https://github.com/user-attachments/assets/57fe53f8-353f-43ef-8c6c-8076913434eb">

#### `6-bit`
<img style="width: auto; height: auto;" src="https://github.com/user-attachments/assets/7aa8c87a-5b47-476b-ac25-f64968af3042">

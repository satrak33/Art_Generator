<p align="center">
    <img style="width: 100px; height: auto;" src="https://github.com/user-attachments/assets/76031be2-f446-4a19-a61c-b1fe8de98ea8">
</p>
<h4 align="center">
    Discord ANSI Art Generator
</h4>
<p align="center">
    Make beautiful arts in Discord using ANSI and Python
</p>

## `🔱` Table of Contents

- [🥽┃Requirements](#requirements)
- [🔮┃Installation](#installation)
- [🎮┃Usage](#usage)
- [🚧┃Warnings & Tips](#warnings-&-tips)
- [🌠┃Plans](#plans)
- [📝┃License](#license)

## `🥽` Requirements [[🔱]](#table-of-contents)

- [Python](https://www.python.org/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Inquirer](https://pypi.org/project/inquirer/)
- [Numpy](https://pypi.org/project/numpy/)
- [Pyperclip](https://pypi.org/project/pyperclip/)

## `🔮` Installation [[🔱]](#table-of-contents)

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

## `🎮` Usage [[🔱]](#table-of-contents)
```bash
python main.py
```
#### Or using without SLI
- [Gray convertor](./converters/gray.py)
- [Color convertor](./converters/color.py)

## `🚧` Warnings & Tips [[🔱]](#table-of-contents)
### `🎈` Tips:
- You can right-click in cmd or powershell to paste path
- Optimazing algorithm works better with pictures wich have one dominating color like photos of space

### `🔥` Warnings:
- Don`t use huge custom length, it will take a lot of time, and it will increase in geometry progression
- ANSI don`t support purple

## `🌠` Plans [[🔱]](#table-of-contents)
- Try to add more color modes by making automatic algorithm
- Create Discord application 
- Create site using GitHub Pages

## `📝` License [[🔱]](#table-of-contents)
You can read license [here](./LICENSE) 
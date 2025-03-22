import argparse
import inquirer
from inquirer import Path, List, Text
import cv2
import converters


def parse_cli_args():
    parser = argparse.ArgumentParser(description='Image processing tool')
    parser.add_argument('image', nargs='?', help='Path to image file')
    parser.add_argument('--size', type=int, help='Custom size value')
    parser.add_argument('--mode', choices=['9-bit', '6-bit', 'grayscale'], help='Color mode')
    return parser.parse_args()

def is_valid_number(_, current):
    return current.isdigit()


def is_valid_image(_, current):
    original_log_level = cv2.getLogLevel()
    cv2.setLogLevel(0)
    image = cv2.imread(current)
    cv2.setLogLevel(original_log_level)
    return image is not None


def get_answers():
    questions = [
        Path(
            "image",
            message="Enter the path to the image",
            exists=True,
            path_type="file",
            validate=is_valid_image
        ),
        List(
            "size",
            message="Choose the length",
            choices=["Basic", "Nitro", "Custom"]
        )
    ]

    answers = inquirer.prompt(questions)

    if answers["size"] == "Custom":
        custom_question = [
            Text(
                "custom_size",
                message="Enter a custom length",
                validate=is_valid_number
            )
        ]
        custom_answer = inquirer.prompt(custom_question)
        answers.update(custom_answer)

    questions2 = [
        List(
            "mode",
            message="Choose the mode mode",
            choices=["9-bit", "6-bit", "Grayscale"]
        )
    ]

    answers2 = inquirer.prompt(questions2)
    answers.update(answers2)

    return answers


def process_answers(answers):
    size = answers["size"]

    if size == "Basic":
        size = 2000
    elif size == "Nitro":
        size = 4000
    else:
        size = int(answers["custom_size"])

    if answers["mode"] == "Grayscale":
        converters.gray_process_image(answers["image"], size)
    else:
        converters.color_process_image(answers["image"], size, answers["mode"])


def main():
    args = parse_cli_args()

    if any([args.size, args.mode]):
        answers = {
            "image": args.image,
            "size": "Custom",
            "custom_size": args.size,
            "mode": "Grayscale" if args.mode == "grayscale" else args.mode
        }
        process_answers(answers)
    else:
        answers = get_answers()
        process_answers(answers)


if __name__ == "__main__":
    main()
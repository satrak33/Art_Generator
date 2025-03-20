import inquirer
from inquirer import Path, List, Text
import cv2
import converters


def is_valid_number(_, current):
    return current.isdigit()


def is_valid_image(_, current):
    image = cv2.imread(current)
    if image is None:
        return False
    return True


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
            "color",
            message="Choose the color mode",
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

    if answers["color"] == "Grayscale":
        converters.gray_process_image(answers["image"], size)
    else:
        converters.color_process_image(answers["image"], size, answers["color"])


if __name__ == "__main__":
    answers = get_answers()
    process_answers(answers)
from PIL import Image, ImageFont, ImageDraw

questions = [
    ["What is the capital of Alabama?", "Montgomery", "Huntsville", "Birmingham", "Mobile"],
    ["What is the capital of Alaska?", "Juneau", "Anchorage", "Fairbanks", "Wasilla"],
    ["What is the capital of Arizona?", "Phoenix", "Tucson", "Mesa", "Tempe"],
    ["What is the capital of Arkansas?", "Little Rock", "Fayetteville", "Jonesboro", "Fort Smith"],
    ["What is the capital of California?", "Sacramento", "Fresno", "Stockton", "Bakersfield"],
    ["What is the capital of Colorado?", "Denver", "Colorado Springs", "Fort Collins", "Boulder"],
    ["What is the capital of Connecticut?", "Hartford", "New Haven", "Stamford", "Greenwich"],
    ["What is the capital of Delaware?", "Dover", "Wilmington", "Newark", "Middletown"],
    ["What is the capital of Florida?", "Tallahassee", "Jacksonville", "Gainesville", "Tampa"],
    ["What is the capital of Georgia?", "Atlanta", "Augusta", "Macon", "Savannah"]
]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def question_only(frame_number, question):

    # get a font
    fnt = ImageFont.truetype("arial.ttf", 40)

    filename = f"./output/frame_{frame_number}.jpg"

    img = Image.new('RGB', (1920, 1080), WHITE)

    # get a drawing context
    d = ImageDraw.Draw(img)

    # draw question
    d.text((100, 100), question, font=fnt, fill=BLACK)
    img.save(filename, "JPEG")


def question_and_four_choices(frame_number, question, answer_choices):

    filename = f"./output/frame_{frame_number}.jpg"

    img = Image.new('RGB', (1920, 1080), WHITE)

    # get a drawing context
    d = ImageDraw.Draw(img)

    fnt = ImageFont.truetype("arial.ttf", 40)
    d.text((100, 100), question, font=fnt, fill=BLACK)

    d.rounded_rectangle((80, 260, 1800, 340), radius=20, fill=WHITE, outline=BLACK, width=1)
    d.rounded_rectangle((80, 360, 1800, 440), radius=20, fill=WHITE, outline=BLACK, width=1)
    d.rounded_rectangle((80, 460, 1800, 540), radius=20, fill=WHITE, outline=BLACK, width=1)
    d.rounded_rectangle((80, 560, 1800, 640), radius=20, fill=WHITE, outline=BLACK, width=1)

    d.text((100, 300), answer_choices[0], font=fnt, fill=BLACK)
    d.text((100, 400), answer_choices[1], font=fnt, fill=BLACK)
    d.text((100, 500), answer_choices[2], font=fnt, fill=BLACK)
    d.text((100, 600), answer_choices[3], font=fnt, fill=BLACK)

    img.save(filename, "JPEG")


def question_and_highlighted_answer(frame_number, question, answer_choices, correct_answer):

    filename = f"./output/frame_{frame_number}.jpg"

    img = Image.new('RGB', (1920, 1080), WHITE)

    # get a drawing context
    d = ImageDraw.Draw(img)

    fnt = ImageFont.truetype("arial.ttf", 40)
    d.rounded_rectangle((80, 260, 1800, 340), radius=20, fill=GREEN, outline=BLACK, width=1)
    d.rounded_rectangle((80, 360, 1800, 440), radius=20, fill=GREEN, outline=BLACK, width=1)
    d.rounded_rectangle((80, 460, 1800, 540), radius=20, fill=GREEN, outline=BLACK, width=1)
    d.rounded_rectangle((80, 560, 1800, 640), radius=20, fill=GREEN, outline=BLACK, width=1)

    d.text((100, 300), answer_choices[0], font=fnt, fill=BLACK)
    d.text((100, 400), answer_choices[1], font=fnt, fill=BLACK)
    d.text((100, 500), answer_choices[2], font=fnt, fill=BLACK)
    d.text((100, 600), answer_choices[3], font=fnt, fill=BLACK)

    img.save(filename, "JPEG")

    """
    Answer file
    """
    frame_number += 1
    filename = f"./output/frame_{frame_number}.jpg"

    img = Image.new('RGB', (1920, 1080), WHITE)

    # get a drawing context
    d = ImageDraw.Draw(img)

    # draw text
    d.text((100, 100), question, font=fnt, fill=BLACK)
    d.text((100, 300), correct_answer, font=fnt, fill=BLACK)

    img.save(filename, "JPEG")


def create_frames():

    frame_number = 0

    for q in questions:
        question = q[0]
        correct_answer = q[1]
        answer_choices = sorted(q[1:5])

        # print(f"{question} | {correct} | {answers}")

        frame_number += 1
        question_only(frame_number, question)
        frame_number += 1
        question_and_four_choices(frame_number, question, answer_choices)
        frame_number += 1
        question_and_highlighted_answer(frame_number, question, answer_choices, correct_answer)


if __name__ == '__main__':

    create_frames()

from PIL import Image


def make_sprite_sheet(name, number, k, side, output_name):
    if number % 2 == 0 and number // 2 <= 10:
        width = number // 2
        height = 2
    elif number == 32:
        width = 8
        height = 4
    elif number == 64:
        width = 8
        height = 8
    elif number == 128:
        width = 16
        height = 8
    else:
        width = number
        height = 1
    sheet = Image.new('RGBA', (width * side, height * side), color=(255, 255, 255, 0))
    opened = Image.open(name)
    opened_width, opened_height = opened.size

    image1 = Image.new('RGBA', (1200, 1200), color=(255, 255, 255, 0))

    image1.paste(opened, ((1200 - opened_width) // 2, (1200 - opened_height) // 2))
    for y in range(height):
        for x in range(width):
            a = 360 * (width * y + x) / number
            image1 = Image.new('RGBA', (1200, 1200), color=(255, 255, 255, 0))

            image1.paste(opened, ((1200 - opened_width) // 2, (1200 - opened_height) // 2))

            image1 = image1.copy().rotate(a).crop(
                (600 - side * k, 600 - side * k, 600 + side * k, 600 + side * k)).resize(
                (side, side))
            sheet.paste(image1, (x * side, y * side))
    sheet.save(f'data/{output_name}')
    return height, width


make_sprite_sheet('data/images/mono_images/AP.png', 180, 2.5, 40, 'images/bullet_sheet.png')

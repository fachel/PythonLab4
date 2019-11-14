from PIL import ImageDraw, Image

# # создание изображения  
# new_im = Image.new('RGB', (512, 200), (255,205,255))
# # на изображении создаем рисунок для рисования
# draw = ImageDraw.Draw(new_im)
# draw.line((0, 0, 100, 200), fill=(255, 0, 0), width=1)
# new_im.save('line1.png')

def gradient(color):
    x = 512
    y = 200
    count = 0
    new_image = Image.new('RGB', (x, y), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    pixels = new_image.load()
    color = color.upper()
    flagR = flagG = flagB = False
    rr = gg = bb = 0
    if color == 'R':
        flagR = True
    elif color == 'G':
        flagG = True
    elif color == 'B':
        flagB = True

    for i in range(x):
        if flagR == 1 and count == 2:
            rr += 1
            count = 0
        elif flagG == 1 and count == 2:
            gg += 1
            count = 0
        elif flagB == 1 and count == 2:
            bb += 1
            count = 0
        for j in range(y):
            r, g, b = pixels[i, j]
            r += rr
            g += gg
            b += bb
            pixels[i, j] = r, g, b
        count += 1
    new_image.save('gradient.png')

gradient('g')

from PIL import Image


# меняет контрастность

def image_filter(pixels, i, j):
    k = 1.0 + correction / 100.0
    deltaR = pixels[i, j][0] - brightness
    deltaG = pixels[i, j][1] - brightness
    deltaB = pixels[i, j][2] - brightness
    r = brightness + int(k * deltaR)
    g = brightness + int(k * deltaG)
    b = brightness + int(k * deltaB)
    return r, g, b


def get_brightness(pixels, x, y):  # получение средней яркости
    br = 0
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            br += (r + g + b)
    br = int(br / (x * y))
    return br


def main():
    global brightness
    global correction
    correction = 50
    im = Image.open("Риана.jpg")
    pixels = im.load()  # список с пикселями
    x, y = im.size
    brightness = get_brightness(pixels, x, y)
    for i in range(x):
        for j in range(y):
            pixels[i, j] = image_filter(pixels, i, j)
    im.save('Риана2.jpg')


main()

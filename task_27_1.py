from PIL import ImageDraw, Image

def make_preview(size, n_colors):
    img = Image.open('image.jpg')
    resize_img = img.resize(size, Image.ANTIALIAS) #Image.ANTIALIAS метод сглаживания
    recolors_img = resize_img.quantize(n_colors) # уменьшение колва цветов
    recolors_img.save('image2.bmp')
make_preview((400, 200), 64)
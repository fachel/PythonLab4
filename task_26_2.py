from PIL import ImageDraw, Image

def board(num, size): #8 50
    new_color = (0, 0, 0)
    new_image = Image.new('RGB', (num * size, num * size), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    x1 = y1 = 0
    x2 = y2 = size
    switchChet = -1 #для столбиков с четной линией
    switchNechet = 1
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i % 2 != 0: #если строчка нечетная
                if j % 2 != 0: # если столбик нечетный
                    if switchNechet == 1:
                        draw.rectangle((x1, y1, x2 - 1, y2 - 1), fill=new_color, outline=new_color)
                switchNechet *= -1
            elif i % 2 == 0:
                if j % 2 == 0:
                    if switchChet == 1:
                        draw.rectangle((x1, y1, x2 - 1, y2 - 1), fill=new_color, outline=new_color)
                switchChet *= -1
            x1 += size
            x2 += size
        switchChet = -1
        switchNechet = 1
        x1 = 0
        x2 = size
        y1 += size
        y2 += size

    new_image.save('rec.png')
board(8, 50)

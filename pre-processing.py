from PIL import Image
from pathlib import Path

def is_grey_scale(img_path):
    img = Image.open(img_path).convert('RGB')
    w, h = img.size
    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i,j))
            if r != g != b: 
                return False
    return True


def convert_binary_img(fn):
    img = Image.open(fn)
    img2 = img.convert('1')
    threshold = 100
    img = img2.point(lambda p: p > threshold and 255)
    return img    

if __name__ == "__main__":
    for i in range (5):
        fn = Path(f"./images/{i}.png")
        bol = is_grey_scale(fn) 
        if bol == False:
            img = convert_binary_img(fn)
            print(img)
            print("not grey scale")
        else:
            img = Image.open(fn)
            img.tobytes()
            print("grey scale")
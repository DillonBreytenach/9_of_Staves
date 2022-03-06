from readline import read_init_file
from gui import assests
from PIL import Image
from io import BytesIO


class main(object):
    def __init__(self):
        self.data = []

    def read_image(image_encoded):
        pil_image = Image.open(BytesIO(image_encoded))
        return pil_image

    def greet():
        #image must be in return
        img = main.read_image('assests/Rune_All_giz.png')
        return img

import os
import string
import math
from email.utils import parseaddr

from PIL import Image


def watermark(img_path: string, output_path: string, watermark_path: string = './watermark/sample.png', rel_size: float = 0.021, padding: tuple[int, int] = (200, 200), pos: string = 'BL', opacity: float = 0.6):
    assert os.path.splitext(os.path.basename(watermark_path))[
        1] == '.png', "Watermark file must be of type PNG."
    assert pos in ['TL', 'TR', 'BL', 'BR'], "Specified watermark position is invalid. Valid position values are TL, TR, BL and BR"
    base_image = Image.open(img_path)
    img_w, img_h = base_image.size

    wm_img = Image.open(watermark_path)
    wm_img.convert("RGBA")
    wm_w, wm_h = wm_img.size
    img_area = img_w * img_h
    wm_ratio = wm_w / wm_h
    # Calculate new watermark size based on relative size
    new_wm_h = math.sqrt(rel_size * img_area / wm_ratio)
    new_wm_w = wm_ratio * new_wm_h
    # Resize watermark
    wm_img = wm_img.resize((int(new_wm_w), int(new_wm_h)))
    # Adjust opacity
    wm_color_data = wm_img.getdata()
    new_color_data = []
    alpha = int(255*opacity)
    for pixel in wm_color_data:
        if pixel[3] != 0:
            new_color_data.append((255, 255, 255, alpha))
        else:
            new_color_data.append(pixel)

    wm_img.putdata(new_color_data)
    # Find positional data for watermark based on given position value
    wm_w, wm_h = wm_img.size
    wm_pos = ()
    if pos == 'TL':
        wm_pos = (padding[0], padding[1])
    elif pos == 'TR':
        wm_pos = (img_w - padding[0] - wm_w, padding[1])
    elif pos == 'BR':
        wm_pos = (img_w - padding[0] - wm_w, img_h - padding[1] - wm_h)
    elif pos == 'BL':
        wm_pos = (padding[0], img_h - padding[1] - wm_h)

    output_img = Image.new('RGBA', (img_w, img_h), (0, 0, 0, 0))
    output_img.paste(base_image, (0, 0))
    output_img.paste(wm_img, wm_pos, mask=wm_img)
    output_img = output_img.convert('RGB')
    output_img.save(output_path)

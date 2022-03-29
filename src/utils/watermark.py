import os
import string

import numpy as np
from PIL import Image


def watermark(img_path: string, output_path: string, watermark_path: string = '../../resource/watermark/sample.png', rel_size: float = 0.05, padding: tuple[int, int] or float = 0.5, pos: string = 'BL', opacity: float = 0.6):
    assert os.path.splitext(os.path.basename(watermark_path))[
        1] == '.png', "Watermark file must be of type PNG."
    assert pos in ['TL', 'TR', 'BL',
                   'BR'], "Specified watermark position is invalid. Valid position values are TL, TR, BL and BR"
    # Get base image
    base_image = Image.open(img_path)
    img_w, img_h = base_image.size

    # Get watermark
    wm_img = Image.open(watermark_path)
    wm_img = wm_img.convert("RGBA")
    wm_w, wm_h = wm_img.size
    img_area = img_w * img_h
    wm_ratio = wm_w / wm_h

    # Resize watermark based on relative size
    new_wm_h = np.sqrt(rel_size * img_area / wm_ratio)
    new_wm_w = wm_ratio * new_wm_h
    wm_img = wm_img.resize((int(new_wm_w), int(new_wm_h)))
    wm_w, wm_h = wm_img.size

    # Find positional data for watermark based on given pos value
    if type(padding) == float:
        padding = (int(wm_h*padding), int(wm_h*padding))
    wm_pos = ()
    if pos == 'TL':
        wm_pos = (padding[0], padding[1])
    elif pos == 'TR':
        wm_pos = (img_w - padding[0] - wm_w, padding[1])
    elif pos == 'BR':
        wm_pos = (img_w - padding[0] - wm_w, img_h - padding[1] - wm_h)
    elif pos == 'BL':
        wm_pos = (padding[0], img_h - padding[1] - wm_h)

    # Decide if watermark needs to be inverted based on watermark background area
    base_is_dark = True
    # The crop method from the Image module takes four coordinates as input.
    # The right can also be represented as (left+width)
    # and lower can be represented as (upper+height).
    wm_gs_area = base_image.copy().convert('L').crop(
        (wm_pos[0], wm_pos[1], wm_pos[0] + wm_w, wm_pos[1]+wm_h))
    img_data = np.asarray(wm_gs_area.getdata())
    if np.mean(img_data) > 150:
        base_is_dark = False

    # Adjust opacity (and invert)
    wm_color_data = wm_img.getdata()
    new_color_data = []
    alpha = int(255*opacity)
    for pixel in wm_color_data:
        if pixel[-1] != 0:
            if base_is_dark:
                new_color_data.append((255, 255, 255, alpha))
            else:
                new_color_data.append((0, 0, 0, alpha))
        else:
            new_color_data.append(pixel)
    wm_img.putdata(new_color_data)

    output_img = Image.new('RGBA', (img_w, img_h), (0, 0, 0, 0))
    output_img.paste(base_image, (0, 0))
    output_img.paste(wm_img, wm_pos, mask=wm_img)
    output_img = output_img.convert('RGB')
    output_img.save(output_path)

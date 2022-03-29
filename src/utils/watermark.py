"""
Inhibits the core function of the WaterMarker which applies watermarks to a respective image.
"""
import os
import string

import numpy as np
from PIL import Image


def watermark(img_path: string, output_path: string, watermark_path: string = '../../resource/watermark/sample.png', rel_size: float = 0.03, padding: tuple[int, int] or float = 0.6, pos: string = 'BL', opacity: float = 0.7, threshold: int = 150):
    """Applies a watermark to a given image in accordance to the specified parameters.

    Args:
        img_path (string): Path to the base image
        output_path (string): Path to the output directory
        watermark_path (string, optional): Path to the watermark image. Defaults to '../../resource/watermark/sample.png'.
        rel_size (float, optional): Percentage value between 1 and 0 of the total area of the base image used to scale the watermark. Defaults to 0.03.
        padding (tuple[int, int]orfloat, optional): Either an integer tupel of pixel margins, where [0] is the horizontal and [1] the vertical margin, or a percentage value between 1 and 0 of the watermark's pixelheight to be used as a margin on both sides. Defaults to 0.6.
        pos (string, optional): Watermark position value. Accepted values are 'TL', 'TR', 'BL' or 'BR'. Defaults to 'BL'.
        opacity (float, optional): Watermark opacity in as a percentage value between 1 and 0. Defaults to 0.7.
        threshold (int, optional): Threshold value which determines if an image is bright or dark. It is recommended to not touch this value. Defaults to 150.
    """
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
    if np.mean(img_data) > threshold:
        base_is_dark = False

    # Adjust opacity (and invert)
    wm_color_data = wm_img.getdata()
    new_color_data = []
    for pixel in wm_color_data:
        if pixel[-1] != 0:
            if (base_is_dark and pixel[0] < 128) or (not base_is_dark and pixel[0] > 128):
                new_color_data.append(
                    (256 - pixel[0], 256 - pixel[1], 256 - pixel[2], int(pixel[3] * opacity)))
            else:
                new_color_data.append(
                    (pixel[0], pixel[1], pixel[2], int(pixel[3] * opacity)))
        else:
            new_color_data.append(pixel)
    wm_img.putdata(new_color_data)

    output_img = Image.new('RGBA', (img_w, img_h), (0, 0, 0, 0))
    output_img.paste(base_image, (0, 0))
    output_img.paste(wm_img, wm_pos, mask=wm_img)
    output_img = output_img.convert('RGB')
    output_img.save(output_path)

# [WaterMarker](https://nico.ismaili.de/) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ismailinico/watermarker/blob/main/LICENSE)

![Logo](resource/watermark/sample.png)

A [Python 3.10](https://www.python.org/downloads/) program which autonomizes the application of watermarks to a specified set of images.

Apart from **automatic watermarking**, it also supports **auto watermark color inversion** and **auto watermark scaling**.

This software was developed by [Nico Ismaili](https://nico.ismaili.de/) with the primary goal of facilitating the selling of his [photographies](https://nico.ismaili.de/).

## Prerequisites

To be able to run the program and install required dependencies you will need to have [Python 3.10](https://www.python.org/downloads/) and [pipenv](https://pipenv.pypa.io/en/latest/) installed.

## Getting Started

Clone the repository, navigate to the project folder and run `pipenv install` to let [pipenv](https://pipenv.pypa.io/en/latest/) install all required dependencies.

Then Run the python script [watermarker.py](./src/watermarker.py) by using the following command.

```cmd
python watermarker.py
```

Afterwards, two folders should open name [unmarked](resource/unmarked/), in which images to be watermarked can be placed, and [marked](resource/marked/), the output folder of the watermarker.

To change the path of both in- or output folder as well as the watermark image, please refer to the next [chapter](#Configuration).

## Configuration

## Examples

In this section two different images, one [bright](./resource/unmarked/bright_og.jpg) and one [dark](./resource/unmarked/dark_og.jpg), are to be watermarked. In addition to this cropped versions of each image are provided to showcase the automatic relative sizing capabilities.

### Originale Images

These were the image inputted into the program.

#### No Crop (Unmarked)

[<img src="resource/unmarked/bright_og.jpg" alt="A white bicycle infront of a yellow container on a sandy road" width="40%"/>](resource/unmarked/bright_og.jpg)
[<img src="resource/unmarked/dark_og.jpg" alt="A long exposure of a street at night" width="45%"/>](resource/unmarked/dark_og.jpg)

#### Instagram square crop (Unmarked)

[<img src="resource/unmarked/bright_1x1.jpg" alt="A white bicycle infront of a yellow container on a sandy road" width="32%"/>](resource/unmarked/bright_1x1.jpg)
[<img src="resource/unmarked/dark_1x1.jpg" alt="A long exposure of a street at night" width="32%"/>](unmarked/dark_1x1.jpg)

#### Instagram landscape crop (Unmarked)

[<img src="resource/unmarked/bright_2x1.jpg" alt="A white bicycle infront of a yellow container on a sandy road" width="32%"/>](resource/unmarked/bright_2x1.jpg)
[<img src="resource/unmarked/dark_2x1.jpg" alt="A long exposure of a street at night" width="32%"/>](unmarked/dark_2x1.jpg)

#### Instagram portrait crop (Unmarked)

[<img src="resource/unmarked/bright_4x5.jpg" alt="A white bicycle infront of a yellow container on a sandy road" width="32%"/>](unmarked/bright_4x5.jpg)
[<img src="resource/unmarked/dark_4x5.jpg" alt="A long exposure of a street at night" width="32%"/>](unmarked/dark_4x5.jpg)

### Watermarked images

This is what was outputted by the program.

#### No Crop (Marked)

[<img src="resource/marked/bright_og_marked.jpg" alt="A white bicycle infront of a yellow container on a sandy road" width="40%"/>](resource/marked/bright_og_marked.jpg)
[<img src="resource/marked/dark_og_marked.jpg" alt="A long exposure of a street at night" width="45%"/>](resource/marked/dark_og_marked.jpg)

#### Instagram square crop (Marked)

[<img src="resource/marked/bright_1x1_marked.jpg" alt="A white bicycle infront of a yellow container on a sandy road" width="32%"/>](resource/marked/bright_1x1_marked.jpg)
[<img src="resource/marked/dark_1x1_marked.jpg" alt="A long exposure of a street at night" width="32%"/>](marked/dark_1x1_marked.jpg)

#### Instagram landscape crop (Marked)

[<img src="resource/marked/bright_2x1_marked.jpg" alt="A white bicycle infront of a yellow container on a sandy road" width="32%"/>](resource/marked/bright_2x1_marked.jpg)
[<img src="resource/marked/dark_2x1_marked.jpg" alt="A long exposure of a street at night" width="32%"/>](marked/dark_2x1_marked.jpg)

#### Instagram portrait crop (Marked)

[<img src="resource/marked/bright_4x5_marked.jpg" alt="A white bicycle infront of a yellow container on a sandy road" width="32%"/>](marked/bright_4x5_marked.jpg)
[<img src="resource/marked/dark_4x5_marked.jpg" alt="A long exposure of a street at night" width="32%"/>](marked/dark_4x5_marked.jpg)

## Credits

[Bright sample photo](resource/unmarked/bright_og.jpg) was created by [Alexey Lin](https://unsplash.com/@alex_lin?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

[Dark sample photo](resource/unmarked/dark_og.jpg) was created by [Osman Rana](https://unsplash.com/@osmanrana?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).
  
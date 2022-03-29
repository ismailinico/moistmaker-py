"""
Inhibits the ImageEventHandler class which is responsible for handling events fired by the DirWatcher class.
"""
import os
import string
import time

from watchdog.events import RegexMatchingEventHandler

from utils.watermark import watermark


class ImageEventHandler(RegexMatchingEventHandler):
    """
    Directory watcher implementation based on the watchdog.observers' Observer module.

    Attributes:
        __output_path (string): Path to the to-be-observed directory.
        __watermark_path (string): Path to the output directory.
        __rel_size (float, optional): Percentage value between 1 and 0 of the total area of the base image used to scale the watermark. Defaults to 0.03.
        __padding (tuple[int, int]orfloat, optional): Either an integer tupel of pixel margins, where [0] is the horizontal and [1] the vertical margin, or a percentage value between 1 and 0 of the watermark's pixelheight to be used as a margin on both sides. Defaults to 0.6.
        __pos (string, optional): Watermark position value. Accepted values are 'TL', 'TR', 'BL' or 'BR'. Defaults to 'BL'.
        __opacity (float, optional): Watermark opacity in as a percentage value between 1 and 0. Defaults to 0.7.
        __threshold (int, optional): Threshold value which determines if an image is bright or dark. It is recommended to not touch this value. Defaults to 150.

    Constants:
        IMAGES_REGEX (regex): Regular expression defining which file extensions to react to.

    Methods:
        on_created : Defines what to do when a file is created.
        process : Processes an event.
    """

    IMAGES_REGEX = [r"(.*)\.jpg$"]

    def __init__(self, output_path: string, watermark_path: string, rel_size: float = 0.03, padding: tuple[int, int] or float = 0.6, pos: string = 'BL', opacity: float = 0.7, threshold: int = 150):
        """_summary_

        Args:
        output_path (string): Path to the to-be-observed directory.
        watermark_path (string): Path to the output directory.
        rel_size (float, optional): Percentage value between 1 and 0 of the total area of the base image used to scale the watermark. Defaults to 0.03.
        padding (tuple[int, int]orfloat, optional): Either an integer tupel of pixel margins, where [0] is the horizontal and [1] the vertical margin, or a percentage value between 1 and 0 of the watermark's pixelheight to be used as a margin on both sides. Defaults to 0.6.
        pos (string, optional): Watermark position value. Accepted values are 'TL', 'TR', 'BL' or 'BR'. Defaults to 'BL'.
        opacity (float, optional): Watermark opacity in as a percentage value between 1 and 0. Defaults to 0.7.
        threshold (int, optional): Threshold value which determines if an image is bright or dark. It is recommended to not touch this value. Defaults to 150.
        """
        self.__output_path = output_path
        self.__watermark_path = watermark_path
        self.__opacity = opacity
        self.__padding = padding
        self.__rel_size = rel_size
        self.__pos = pos
        self.__threshold = threshold
        super().__init__(self.IMAGES_REGEX)

    def on_created(self, event):
        # Wait until file size has stopped increasing before processing file
        # Important when uploading larger filed
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path.getsize(event.src_path)
            time.sleep(1)
        self.process(event)

    def process(self, event):
        og_filename, file_ext = os.path.splitext(
            os.path.basename(event.src_path))
        output_dir = os.path.abspath(self.__output_path)
        output_path = f"{output_dir}/{og_filename}_marked.jpg"
        watermark(event.src_path, output_path, self.__watermark_path, self.__rel_size,
                  self.__padding, self.__pos, self.__opacity, self.__threshold)

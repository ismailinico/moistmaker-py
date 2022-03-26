import os
import string
import time

from watchdog.events import RegexMatchingEventHandler

from WaterMarker import watermark


class ImageEventHandler(RegexMatchingEventHandler):
    IMAGES_REGEX = [r"(.*)\.jpg$"]

    def __init__(self, output_path: string, watermark_path: string, rel_size: float, padding: tuple[int, int] or float, pos: string, opacity: float):
        self.__output_path = output_path
        self.__rel_size = rel_size
        self.__watermark_path = watermark_path
        self.__padding = padding
        self.__pos = pos
        self.__opacity = opacity
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
                  self.__padding, self.__pos, self.__opacity)

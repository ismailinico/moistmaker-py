import os
import time
from PIL import Image
from watchdog.events import RegexMatchingEventHandler

class WaterMarker(RegexMatchingEventHandler):
    IMAGES_REGEX = [r"(.*)\.jpg$"]

    def __init__(self, output_path):
        self.__output_path = output_path
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
        og_filename, file_ext = os.path.splitext(os.path.basename(event.src_path))
        output_dir = os.path.abspath(self.__output_path)
        output_path = f"{output_dir}/{og_filename}_marked.jpg"
        # image = Image.open(event.src_path)
        # image.save(output_path)
        print("New image was created in watched dir!")
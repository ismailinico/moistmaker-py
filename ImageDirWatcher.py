import os
import string
import sys
import time

from watchdog.observers import Observer

from ImageEventHandler import ImageEventHandler


class ImageDirWatcher:
    def __init__(self, input_path: string, output_path: string, watermark_path: string, padding: tuple[int, int], pos: string, opacity: float):
        self.__input_path = input_path
        self.__event_handler = ImageEventHandler(
            output_path, watermark_path, padding, pos, opacity)
        self.__event_observer = Observer()

    def run(self):
        self.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__input_path,
            recursive=True
        )


if __name__ == "__main__":
    input_path = './unmarked'
    output_path = './marked'
    watermark_path = './watermark/sample.png'
    pos = 'BL'
    padding = (200, 200)
    opacity = 0.6

    if not os.path.exists(watermark_path):
        os.makedirs(watermark_path)

    if not os.path.exists(input_path):
        os.makedirs(input_path)
    elif len(sys.argv) > 1:
        input_path = sys.argv[1]

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    elif len(sys.argv) > 2:
        output_path = sys.argv[2]

    ImageDirWatcher(input_path, output_path, watermark_path,
                    padding, pos, opacity).run()

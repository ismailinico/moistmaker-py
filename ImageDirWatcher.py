import os
import string
import sys
import time

from watchdog.observers import Observer

from ImageEventHandler import ImageEventHandler


class ImageDirWatcher:
    def __init__(self, input_path: string, output_path: string, watermark_path: string, rel_size: float, padding: tuple[int, int] or float, pos: string, opacity: float):
        self.__input_path = input_path
        self.__event_handler = ImageEventHandler(
            output_path, watermark_path, rel_size, padding, pos, opacity)
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

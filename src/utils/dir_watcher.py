"""
Inhibits the DirWatcher class which is responsible for watching over the input directory.
"""
import string
import time

from watchdog.observers import Observer

from utils.image_event_handler import ImageEventHandler


class DirWatcher:
    """
    Directory watcher implementation based on the watchdog.observers' Observer module.

    Attributes:
    __input_path (str): path to the to-be-observed directory
    __event_handler (utils.image_event_handler): object which is called upon when events are fired
    __event_observer (Observer): watchdog object which handles directory supervision

    Methods:
    run: Starts infinite watch loop.
    start: Runs __schedule and starts the Observer.
    stop: Terminates the Observer.
    __schedule: initializes Observer.
    """

    def __init__(self, input_path: string, output_path: string, watermark_path: string, rec_watch: bool = False, rel_size: float = 0.03, padding: tuple[int, int] or float = 0.6, pos: string = 'BL', opacity: float = 0.7, threshold: int = 150):
        """Initializes class attributes and forwards various parameters to ImageEventHandler.

        Args:
            input_path (string): Path to the to-be-observed directory.
            output_path (string): Path to the output directory.
            watermark_path (string): Path to the watermark image.
            rec_watch (bool, optional): Define if input folder should be watched recursively.
            rel_size (float, optional): Percentage value between 1 and 0 of the total area of the base image used to scale the watermark. Defaults to 0.03.
            padding (tuple[int, int]orfloat, optional): Either an integer tupel of pixel margins, where [0] is the horizontal and [1] the vertical margin, or a percentage value between 1 and 0 of the watermark's pixelheight to be used as a margin on both sides. Defaults to 0.6.
            pos (string, optional): Watermark position value. Accepted values are 'TL', 'TR', 'BL' or 'BR'. Defaults to 'BL'.
            opacity (float, optional): Watermark opacity in as a percentage value between 1 and 0. Defaults to 0.6.
            threshold (int, optional): Threshold value which determines if an image is bright or dark. It is recommended to not touch this value. Defaults to 150.
        """
        self.__input_path = input_path
        self.__rec_watch = rec_watch
        self.__event_handler = ImageEventHandler(
            output_path, watermark_path, rel_size, padding, pos, opacity, threshold)
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
            recursive=self.__rec_watch
        )

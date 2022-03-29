import string
import time


from watchdog.observers import Observer

from utils.image_event_handler import ImageEventHandler


class DirWatcher:
    """
    Directory watcher implementation based on the watchdog.observers' Observer module.

    ...

    Attributes
    ----------
    input_path : str
        path to the to-be-observed directory
    event_handler : utils.image_event_handler
        object which is called upon when events are fired
    event_observer : Observer
        watchdog object which handles directory supervision

    Methods
    -------
    run:
        starts infinite watch loop
    start:
        euns __schedule and starts the Observer
    stop:
        terminates the Observer
    __schedule:
        initializes Observer
    """

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

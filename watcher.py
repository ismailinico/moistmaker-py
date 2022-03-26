import time

from watchdog.observers import Observer

from watermarker import WaterMarker

class Watcher:
    def __init__(self, input_path, output_path):
        self.__input_path = input_path
        self.__event_handler = WaterMarker(output_path)
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

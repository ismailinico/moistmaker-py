import os
import sys
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


if __name__ == "__main__":
    input_path = './unmarked'
    output_path = './marked'

    if not os.path.exists(input_path):
        os.makedirs(input_path)
    elif len(sys.argv) > 1:
        input_path = sys.argv[1]

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    elif len(sys.argv) > 2:
        output_path = sys.argv[2]

Watcher(input_path, output_path).run()

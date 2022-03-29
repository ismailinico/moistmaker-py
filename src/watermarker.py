"""
Main module responsible for initial configuration and path finding. 
"""
import os
import sys

from utils.dir_watcher import DirWatcher

if __name__ == '__main__':
    resource_base_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir, 'resource'))
    input_path = os.path.join(resource_base_path, 'unmarked')
    output_path = os.path.join(input_path, 'marked')
    watermark_path = os.path.join(resource_base_path, 'watermark/sample.png')

    if not os.path.exists(input_path):
        os.makedirs(input_path)
    elif len(sys.argv) > 1:
        input_path = sys.argv[1]
    os.startfile(input_path)

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    elif len(sys.argv) > 2:
        output_path = sys.argv[2]

    if not os.path.exists(watermark_path):
        os.makedirs(watermark_path)
        os.startfile(watermark_path)

    DirWatcher(input_path, output_path, watermark_path).run()

"""
Main module responsible for initial configuration and path finding. 
"""
import os
import sys
import json

from utils.dir_watcher import DirWatcher

if __name__ == '__main__':
    # Load config from JSON
    config_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir, 'config.json'))
    with open(config_path, 'r') as cfg:
        config = json.load(cfg)
    # Get path resource folder
    resource_base_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir, 'resource'))

    default_vals = {'input_path': os.path.join(resource_base_path, 'unmarked'), 'output_path': os.path.join(resource_base_path, 'unmarked', 'marked'),
                    'watermark_path': os.path.join(resource_base_path, 'watermark/sample.png'), 'rel_size': 0.03, 'padding': 0.6, 'pos': 'BL', 'opacity': 0.7, 'threshold': 150, 'rec_watch': False}
    # Get parameter values from config or use default values if not defined or out of bounds
    input_path = config.get(
        'unmarkedDirPath', default_vals['input_path'])
    if not input_path:
        input_path = default_vals['input_path']

    output_path = config.get(
        'markedDirPath', default_vals['output_path'])
    if not output_path:
        output_path = default_vals['output_path']

    watermark_path = config.get(
        'watermarkPath', default_vals['watermark_path'])
    if not watermark_path:
        watermark_path = default_vals['watermark_path']

    pos = config.get('pos', default_vals['pos'])
    if not pos:
        pos = default_vals['pos']

    rec_watch = config.get('rec_watch', False)
    rel_size = config.get('rel_size', 0.03)
    opacity = config.get('opacity', 0.7)
    threshold = config.get('threshold', 150)
    print(input_path, output_path, watermark_path)
    # Get padding and convert to tuple if necessary
    padding = config.get('padding', 0.6)
    if type(padding) == list and len(padding) == 2:
        padding = tuple(padding)
    # Check if given paths exist and raise error if not
    if (not os.path.exists(input_path)) or (not os.path.exists(output_path)) or (not os.path.exists(watermark_path)):
        raise FileNotFoundError
    # Open unmarked folder
    os.startfile(input_path)
    # Start watching folder
    DirWatcher(input_path, output_path, watermark_path).run()

"""
Main module responsible for initial configuration and path finding. 
"""
from concurrent.futures import thread
import os
import json

from utils.dir_watcher import DirWatcher
from utils.error_handling import check_bool, check_color, check_padding, check_path, check_percentage, check_pos, check_rec_watch
from utils.watermark import watermark

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
    if check_path(input_path, 'unmarked directory'):
        input_path = default_vals['input_path']
    output_path = config.get(
        'markedDirPath', default_vals['output_path'])
    if check_path(output_path, 'marked directory'):
        output_path = default_vals['output_path']
    watermark_path = config.get(
        'watermarkPath', default_vals['watermark_path'])
    if check_path(watermark_path, 'watermark file'):
        watermark_path = default_vals['watermark_path']
    pos = config.get('pos', default_vals['pos'])
    if check_pos(pos, ['TL', 'TR', 'BL', 'BR']):
        pos = default_vals['pos']
    rec_watch = config.get('rec_watch', False)
    if check_bool(rec_watch, 'rec_watch'):
        rec_watch = default_vals['rec_watch']
    rel_size = config.get('rel_size', 0.03)
    if check_percentage(rel_size, 'rel_size'):
        rel_size = default_vals['rel_size']
    opacity = config.get('opacity', 0.7)
    if check_percentage(opacity, 'opacity'):
        opacity = default_vals['opacity']
    threshold = config.get('threshold', 150)
    if check_color(threshold, 'threshold'):
        threshold = default_vals['threshold']
    # Get padding and convert to tuple if necessary
    padding = config.get('padding', 0.6)
    if check_padding(padding):
        padding = default_vals['padding']
    else:
        if check_percentage(padding, 'padding'):
            padding = default_vals['padding']
    # Open unmarked folder
    os.startfile(input_path)
    # Start watching folder
    DirWatcher(input_path, output_path, watermark_path, rec_watch,
               rel_size, padding, pos, opacity, threshold).run()

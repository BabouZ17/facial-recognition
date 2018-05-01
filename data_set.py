#! /user/bin/env python
# -*- coding: utf-8 -*-
# A class that represents the data set

"""
DataSet class represents the set of data
"""

import os

class DataSet:
    """
    Object containing the images's urls, labels and images.
    """

    def __init__(self, path, winking=False):
        """
        Main constructor
            - path (string) path to the images
            - winking (bool) if the data set includes winking labeled images or not
        """

        self.path = path
        if winking:
            try:
                self.images_urls = [os.path.join(self.path, url) for url in os.listdir(self.path) \
                if 'subject' in url]
                self.labels = [label.split('.')[1] for label in os.listdir(self.path) \
                if 'subject' in label]
                self.images = [image.split('.')[0] for image in os.listdir(self.path) \
                if 'subject' in image]
                self.numbers = [number.split('.')[0][7:] for number in os.listdir(self.path) \
                if 'subject' in number]
            except FileNotFoundError:
                pass
        else:try:
                self.images_urls = [os.path.join(self.path, f) for f in os.listdir(self.path)
                if 'subject' in f]
                self.labels = [label.split('.')[1] for label in os.listdir(self.path) if 'subject' in label]
                self.images = [image.split('.')[0] for image in os.listdir(self.path) if 'subject' in image]
                self.numbers = [number.split('.')[0][7:] for number in os.listdir(self.path) if 'subject' in number]
            except FileNotFoundError:
                pass
            try:
                self.images_urls = [os.path.join(self.path, url) for url in os.listdir(self.path) \
                if 'subject' in url and not url.endswith('.wink')]
                self.labels = [label.split('.')[1] for label in os.listdir(self.path) \
                if 'subject' in label and not label.endswith('.wink')]
                self.images = [image.split('.')[0] for image in os.listdir(self.path) \
                if 'subject' in image and not image.endswith('.wink')]
                self.numbers = [number.split('.')[0][7:] for number in os.listdir(self.path) \
                if 'subject' in number and not number.endswith('.wink')]
            except FileNotFoundError:
                pass

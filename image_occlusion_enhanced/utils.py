# -*- coding: utf-8 -*-
####################################################
##                                                ##
##           Image Occlusion Enhanced             ##
##                                                ##
##        Copyright (c) Glutanimate 2016          ##
##       (https://github.com/Glutanimate)         ##
##                                                ##
####################################################

"""
Common reusable utilities
"""

import os, re

from aqt import mw

import urllib.parse, urllib.request, urllib.parse, urllib.error
from .Imaging import PIL

def path2url(path):
    """URL-encode local path"""
    return urllib.parse.urljoin(
      'file:', urllib.request.pathname2url(path.encode('utf-8')))

def fname2img(path):
    """Return HTML img element for given path"""
    return '<img src="%s" />' % os.path.split(path)[1]

def img2path(img, nameonly=False):
    """Extract path or file name out of HTML img element"""
    imgpatt = r"""<img.*?src=(["'])(.*?)\1"""
    imgregex = re.compile(imgpatt, flags=re.I|re.M|re.S)
    fname = imgregex.search(img)
    if not fname:
        return None
    if nameonly:
        return fname.group(2)
    fpath = os.path.join(mw.col.media.dir(),fname.group(2))
    if not os.path.isfile(fpath):
        return None
    return fpath

def imageProp(image_path):
    """Get image width and height"""
    image = PIL.Image.open(image_path)
    width, height = image.size
    return width, height

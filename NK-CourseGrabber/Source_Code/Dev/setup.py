"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['vcodeData', 'vcodeData2', 'ValidateCode.jpg', 'ValidateCode2']
OPTIONS = {'argv_emulation': True,
 'iconfile': '/Users/Accelerator/Documents/Code/Python/NK/NKU-SSS/NK-CourseGrabber/Source_Code/Dev/NKU.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

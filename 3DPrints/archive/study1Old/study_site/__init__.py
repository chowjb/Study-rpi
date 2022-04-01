"""
The flask application package.
"""

from flask import Flask
from utilities import constants
from in_out import grbl
from . import globals

app = Flask(__name__)

from utilities import constants, basic
import study_site.views

if constants.IS_RASPBERRY_PI:
    port = '/dev/ttyUSB0'
else:
    port = 'COM6'
globals.g_transport = grbl.Grbl(port)
globals.g_transport.open()

if not constants.IS_RASPBERRY_PI:
    globals.g_gcode_file = 'C:\\Users\\Jeff\\OneDrive\\Dev\\Bots\\Src\\jandi\\in_out\\gcode_reverse.txt'

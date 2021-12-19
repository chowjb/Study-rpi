"""
This script runs the Study_Site application using a development server.
"""

from os import environ
from study_site import app
from utilities import constants
from in_out import grbl

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
        
    if constants.IS_RASPBERRY_PI:
        app.run(host='0.0.0.0', port=5000)      # iPhone: http://study-rpi.local:5000
    else:
        app.run(HOST, PORT, debug=False)        # Test it in Chrome.
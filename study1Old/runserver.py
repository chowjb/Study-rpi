"""
This script runs the website application using a development server.
"""

from os import environ
from study_site import app
from utilities import basic


IS_RASPBERRY_PI = basic.Util.isRaspberryPi()
print('IS_RASPBERRY_PI = %s' % (IS_RASPBERRY_PI))

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    if IS_RASPBERRY_PI:
        app.run(host='0.0.0.0', port=5000)     # iPhone: http://wb1-rpi.local:5000
    else:
        app.run(HOST, 5555, debug=True)        # Test it in Chrome.
        #app.run(host='0.0.0.0', port=5000)

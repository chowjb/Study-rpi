"""
Prototyping website using Flask.
Put this in the text file /etc/rc.local to automatically start up
the website: python /home/pi/bots/code/flask/run.py &
"""

from flask import Flask, render_template
import os
from urllib.parse import unquote
import ScorePlayer

app = Flask(__name__)

@app.route("/")
def index():
    currentStatus = "Select a motion composition from the dropdown list."
    print("Resting: Dir = {}".format(os.getcwd()))
    return render_template("home.html", currentStatus=currentStatus)

# @app.route("/play/<string:scoreName>/<string:numTimes>")
# def play(scoreName, numTimes):
#     scoreName = unquote(scoreName)
#     #playScore(scoreName, int(numTimes))
#     currentStatus = 'Playing score "{}" for {} cycles.'.format(scoreName, numTimes)
#     return render_template("home.html", currentStatus=currentStatus)

def playScore(scoreName : str, numTimes: int):
    print('[Playing] scoreName "{}" for {} cycles. Dir={}'.format(scoreName, numTimes, os.getcwd()))
    # statusDisplayer = StatusDisplayer(1)
    # player = ScorePlayer(scoreName, numTimes, statusDisplayer)
    # try:
    #     player.play()
    # except:
    #     print('Exception running player')


if __name__ == "__main__":
    app.directory='./'
    app.run(host='0.0.0.0', port=5000)     # for testing on iPhone
    #app.run(host='localhost', port=5001)    # for testing in PC browser

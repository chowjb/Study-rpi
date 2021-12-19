""" 
Current Kinetic Mockup: To study how to achieve graceful moves and provide 
some useful information. The ambient fixture will gesture wind condition at a 
specific location.
"""
from gcode import Streamer, Conductor, ScoreStore
import StatusDisplayer

""" Plays a gcode score """
class ScorePlayer():
    def __init__(self, scoreName : str, numTimes : int, statusDisplayer : StatusDisplayer) -> None:
        self.scoreName = scoreName
        self.numTimes = numTimes
        self.statusDisplayer = statusDisplayer

    # Play a score
    def play(self):
        # Retrieve the score
        scoreStore = ScoreStore.ScoreStore()
        filename = scoreStore.getFilename(self.scoreName)

        with open(filename) as f:
            gcodeScore = f.readlines()

            # Show the current score
            displayer = self.statusDisplayer(1)
            displayer.show(self.scoreName)
    
            # Play the score
            #Conductor.play(gocdeScore)

class ScoreStore:
    """ Handles all scores in the dictionary """
    def __init__(self):
        self.scoreDict = {'Dual Infinity': 'DualInfinity.txt',
                         'Graceful Duet': 'GracefulDuet.txt'}
        
    def getFilename(self, scoreTitle):
        return self.scoreDict.get(scoreTitle, None)
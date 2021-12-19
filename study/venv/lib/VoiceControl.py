class VoiceControl:
    """ 
    *** Handles all voice input/output ***
    Interim: Create a website that you can input from
    your iPhone browser.
    Mockup: input from a Python input prompt.
    """
    def __init__(self):
        self.voiceCmd = None
    
    def waitForVoiceCmd(self):
        scoreRequestPrompt = 'Enter the score number to play: 1) Dual Infinity, 2) Graceful Duet: '
        scoreRequest = int(input(scoreRequestPrompt))
        while scoreRequest not in (1,2):
            print('Number needs to be between 1-2. Try again. ')
            scoreRequest = int(input(scoreRequestPrompt))

        if scoreRequest == 1:
            self.voiceCmd = ('score', 'play', 'Dual Infinity')
        elif scoreRequest == 2:
            self.voiceCmd = ('score', 'play', 'Graceful Duet')
        else:
            raise Exception(f'Invalid scoreRequest={scoreRequest}')
            
        return self.voiceCmd
    
    def getScoreTitle(self, voiceCmd):
       return voiceCmd[2]
   
    
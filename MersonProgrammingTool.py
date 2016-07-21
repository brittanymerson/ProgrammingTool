#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), July 20, 2016, at 15:24
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'MersonProgrammingTool'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1097, 731), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Start_Screen"
Start_ScreenClock = core.Clock()
WelcomeText = visual.TextStim(win=win, ori=0, name='WelcomeText',
    text='Welcome to the Food Choice Game!\n\nIn this game healthy foods are your target items and unhealthy foods are your penalty items.\n\nPress the space bar to move forward.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instruction1 = visual.TextStim(win=win, ori=0, name='Instruction1',
    text='The goal of this game is to get points while going as quickly as possible.\n\nHow to Get Points:\n+1 point for pressing the j key when you see a target item \n+1 point for ignoring a penalty item.\n\nHow to Lose Points:\n-2 points for pressing the j key when you see a penalty item\n\n-2 points for missing a target item.\n\n\nPress the space key to move forward.',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
TargetExample = visual.ImageStim(win=win, name='TargetExample',
    image='C:\\Users\\twinnymerson\\Desktop\\ProgrammingTool\\Project Images\\HealthyFoods.png', mask=None,
    ori=0, pos=[-.75, 0], size=[0.45, 0.45],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
PenaltyExample = visual.ImageStim(win=win, name='PenaltyExample',
    image='C:\\Users\\twinnymerson\\Desktop\\ProgrammingTool\\Project Images\\UnhealthyFoods.png', mask=None,
    ori=0, pos=[0.75, 0], size=[0.45, 0.45],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "Instructions_Page_2"
Instructions_Page_2Clock = core.Clock()
InstructionsPart2 = visual.TextStim(win=win, ori=0, name='InstructionsPart2',
    text='Try to go as quickly as possible while gaining points!\nGet a high score!\n\nReady to play?\n\n',    font='Arial',
    pos=[0, 0.25], height=None, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
rating = visual.RatingScale(win=win, name='rating', marker='hover', size=1.5, pos=[0.0, -0.25], choices=[u'Not yet...', u'Yes!'], tickHeight=0.0, markerStart='0,0')

# Initialize components for Routine "RoundStart"
RoundStartClock = core.Clock()
StartRound = visual.TextStim(win=win, ori=0, name='StartRound',
    text='Press the space bar to start the round!',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=2,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
ITEM = visual.ImageStim(win=win, name='ITEM',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
msg=''

ImmediateFeedbackText = visual.TextStim(win=win, ori=0, name='ImmediateFeedbackText',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)


# Initialize components for Routine "Final_Score"
Final_ScoreClock = core.Clock()
FeedbackMSG = ''
HoldCorrectAnswer = 0
FinalScoreScreen = visual.TextStim(win=win, ori=0, name='FinalScoreScreen',
    text='default text',    font='Arial',
    pos=[0, 0.25], height=0.2, wrapWidth=2,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
EndFinalScoreScreen = visual.TextStim(win=win, ori=0, name='EndFinalScoreScreen',
    text='Press the space bar to end the game.',    font='Arial',
    pos=[0, -.75], height=0.1, wrapWidth=2,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Goodbye_Screen"
Goodbye_ScreenClock = core.Clock()
Goodbye = visual.TextStim(win=win, ori=0, name='Goodbye',
    text='Thanks for playing!',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=2,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Start_Screen"-------
t = 0
Start_ScreenClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
StartScreenMoveForward = event.BuilderKeyResponse()  # create an object of type KeyResponse
StartScreenMoveForward.status = NOT_STARTED
# keep track of which components have finished
Start_ScreenComponents = []
Start_ScreenComponents.append(WelcomeText)
Start_ScreenComponents.append(StartScreenMoveForward)
for thisComponent in Start_ScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Start_Screen"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Start_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeText* updates
    if t >= 0.0 and WelcomeText.status == NOT_STARTED:
        # keep track of start time/frame for later
        WelcomeText.tStart = t  # underestimates by a little under one frame
        WelcomeText.frameNStart = frameN  # exact frame index
        WelcomeText.setAutoDraw(True)
    
    # *StartScreenMoveForward* updates
    if t >= 0.0 and StartScreenMoveForward.status == NOT_STARTED:
        # keep track of start time/frame for later
        StartScreenMoveForward.tStart = t  # underestimates by a little under one frame
        StartScreenMoveForward.frameNStart = frameN  # exact frame index
        StartScreenMoveForward.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(StartScreenMoveForward.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if StartScreenMoveForward.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            StartScreenMoveForward.keys = theseKeys[-1]  # just the last key pressed
            StartScreenMoveForward.rt = StartScreenMoveForward.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Start_Screen"-------
for thisComponent in Start_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if StartScreenMoveForward.keys in ['', [], None]:  # No response was made
   StartScreenMoveForward.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('StartScreenMoveForward.keys',StartScreenMoveForward.keys)
if StartScreenMoveForward.keys != None:  # we had a response
    thisExp.addData('StartScreenMoveForward.rt', StartScreenMoveForward.rt)
thisExp.nextEntry()
# the Routine "Start_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
MoveForward = event.BuilderKeyResponse()  # create an object of type KeyResponse
MoveForward.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(Instruction1)
InstructionsComponents.append(TargetExample)
InstructionsComponents.append(PenaltyExample)
InstructionsComponents.append(MoveForward)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruction1* updates
    if t >= 0.0 and Instruction1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instruction1.tStart = t  # underestimates by a little under one frame
        Instruction1.frameNStart = frameN  # exact frame index
        Instruction1.setAutoDraw(True)
    
    # *TargetExample* updates
    if t >= 0.0 and TargetExample.status == NOT_STARTED:
        # keep track of start time/frame for later
        TargetExample.tStart = t  # underestimates by a little under one frame
        TargetExample.frameNStart = frameN  # exact frame index
        TargetExample.setAutoDraw(True)
    
    # *PenaltyExample* updates
    if t >= 0.0 and PenaltyExample.status == NOT_STARTED:
        # keep track of start time/frame for later
        PenaltyExample.tStart = t  # underestimates by a little under one frame
        PenaltyExample.frameNStart = frameN  # exact frame index
        PenaltyExample.setAutoDraw(True)
    
    # *MoveForward* updates
    if t >= 0.0 and MoveForward.status == NOT_STARTED:
        # keep track of start time/frame for later
        MoveForward.tStart = t  # underestimates by a little under one frame
        MoveForward.frameNStart = frameN  # exact frame index
        MoveForward.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(MoveForward.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if MoveForward.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            MoveForward.keys = theseKeys[-1]  # just the last key pressed
            MoveForward.rt = MoveForward.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if MoveForward.keys in ['', [], None]:  # No response was made
   MoveForward.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('MoveForward.keys',MoveForward.keys)
if MoveForward.keys != None:  # we had a response
    thisExp.addData('MoveForward.rt', MoveForward.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Instructions_Page_2"-------
t = 0
Instructions_Page_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
rating.reset()
# keep track of which components have finished
Instructions_Page_2Components = []
Instructions_Page_2Components.append(InstructionsPart2)
Instructions_Page_2Components.append(rating)
for thisComponent in Instructions_Page_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions_Page_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instructions_Page_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionsPart2* updates
    if t >= 0.0 and InstructionsPart2.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstructionsPart2.tStart = t  # underestimates by a little under one frame
        InstructionsPart2.frameNStart = frameN  # exact frame index
        InstructionsPart2.setAutoDraw(True)
    # *rating* updates
    if t >= 0.0 and rating.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating.tStart = t  # underestimates by a little under one frame
        rating.frameNStart = frameN  # exact frame index
        rating.setAutoDraw(True)
    continueRoutine &= rating.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_Page_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions_Page_2"-------
for thisComponent in Instructions_Page_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating.response', rating.getRating())
thisExp.addData('rating.rt', rating.getRT())
thisExp.nextEntry()
# the Routine "Instructions_Page_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
GameplayPlusScoreFeedback = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='GameplayPlusScoreFeedback')
thisExp.addLoop(GameplayPlusScoreFeedback)  # add the loop to the experiment
thisGameplayPlusScoreFeedback = GameplayPlusScoreFeedback.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisGameplayPlusScoreFeedback.rgb)
if thisGameplayPlusScoreFeedback != None:
    for paramName in thisGameplayPlusScoreFeedback.keys():
        exec(paramName + '= thisGameplayPlusScoreFeedback.' + paramName)

for thisGameplayPlusScoreFeedback in GameplayPlusScoreFeedback:
    currentLoop = GameplayPlusScoreFeedback
    # abbreviate parameter names if possible (e.g. rgb = thisGameplayPlusScoreFeedback.rgb)
    if thisGameplayPlusScoreFeedback != None:
        for paramName in thisGameplayPlusScoreFeedback.keys():
            exec(paramName + '= thisGameplayPlusScoreFeedback.' + paramName)
    
    #------Prepare to start Routine "RoundStart"-------
    t = 0
    RoundStartClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    StartRoundMove = event.BuilderKeyResponse()  # create an object of type KeyResponse
    StartRoundMove.status = NOT_STARTED
    # keep track of which components have finished
    RoundStartComponents = []
    RoundStartComponents.append(StartRound)
    RoundStartComponents.append(StartRoundMove)
    for thisComponent in RoundStartComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "RoundStart"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = RoundStartClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StartRound* updates
        if t >= 0.0 and StartRound.status == NOT_STARTED:
            # keep track of start time/frame for later
            StartRound.tStart = t  # underestimates by a little under one frame
            StartRound.frameNStart = frameN  # exact frame index
            StartRound.setAutoDraw(True)
        
        # *StartRoundMove* updates
        if t >= 0.0 and StartRoundMove.status == NOT_STARTED:
            # keep track of start time/frame for later
            StartRoundMove.tStart = t  # underestimates by a little under one frame
            StartRoundMove.frameNStart = frameN  # exact frame index
            StartRoundMove.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(StartRoundMove.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if StartRoundMove.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                StartRoundMove.keys = theseKeys[-1]  # just the last key pressed
                StartRoundMove.rt = StartRoundMove.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RoundStartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "RoundStart"-------
    for thisComponent in RoundStartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if StartRoundMove.keys in ['', [], None]:  # No response was made
       StartRoundMove.keys=None
    # store data for GameplayPlusScoreFeedback (TrialHandler)
    GameplayPlusScoreFeedback.addData('StartRoundMove.keys',StartRoundMove.keys)
    if StartRoundMove.keys != None:  # we had a response
        GameplayPlusScoreFeedback.addData('StartRoundMove.rt', StartRoundMove.rt)
    # the Routine "RoundStart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('ProgrammingTool\\TrialConditions.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        ITEM.setImage(ShortItemName)
        key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_2.status = NOT_STARTED
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(ISI)
        trialComponents.append(ITEM)
        trialComponents.append(key_resp_2)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITEM* updates
            if t >= 0.0 and ITEM.status == NOT_STARTED:
                # keep track of start time/frame for later
                ITEM.tStart = t  # underestimates by a little under one frame
                ITEM.frameNStart = frameN  # exact frame index
                ITEM.setAutoDraw(True)
            
            
            # *key_resp_2* updates
            if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t  # underestimates by a little under one frame
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['none', 'j'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_2.keys == str(thisTrial.CorrectAns)) or (key_resp_2.keys == thisTrial.CorrectAns):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
                    
                                # check for quit:
                elif t >= 5.0: 
                    key_resp_2.keys = theseKeys 
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_2.keys == str(thisTrial.CorrectAns)) or (key_resp_2.keys == thisTrial.CorrectAns):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
                    
                    
            # *ISI* period
            if t >= 0.0 and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t  # underestimates by a little under one frame
                ISI.frameNStart = frameN  # exact frame index
                ISI.start(0.5)
            elif ISI.status == STARTED: #one frame should pass before updating params and completing
                # updating other components during *ISI*
                ITEM.setPos([x,y])
                # component updates done
                ISI.complete() #finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
           key_resp_2.keys=None
           # was no response the correct answer?!
           if str(thisTrial.CorrectAns).lower() == 'none': key_resp_2.corr = 1  # correct non-response
           else: key_resp_2.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        trials.addData('key_resp_2.corr', key_resp_2.corr)
        HoldCorrectAnswer = HoldCorrectAnswer + key_resp_2.corr
        if key_resp_2.keys != None:  # we had a response
            trials.addData('key_resp_2.rt', key_resp_2.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        #------Prepare to start Routine "Feedback"-------
        t = 0
        FeedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        if key_resp_2.corr:
            msg = '+1 :D  '+ str(HoldCorrectAnswer)
        else: 
            msg = '-2 :('
        ImmediateFeedbackText.setText(msg)
        # keep track of which components have finished
        FeedbackComponents = []
        FeedbackComponents.append(ImmediateFeedbackText)
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Feedback"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *ImmediateFeedbackText* updates
            if t >= 0.0 and ImmediateFeedbackText.status == NOT_STARTED:
                # keep track of start time/frame for later
                ImmediateFeedbackText.tStart = t  # underestimates by a little under one frame
                ImmediateFeedbackText.frameNStart = frameN  # exact frame index
                ImmediateFeedbackText.setAutoDraw(True)
            if ImmediateFeedbackText.status == STARTED and t >= (0.0 + (0.25-win.monitorFramePeriod*0.75)): #most of one frame period left
                ImmediateFeedbackText.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 2 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'GameplayPlusScoreFeedback'


#------Prepare to start Routine "Final_Score"-------
t = 0
Final_ScoreClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
FeedbackMSG = "OVERALL CORRECT = "+ str(HoldCorrectAnswer)
FinalScoreScreen.setText(FeedbackMSG)
MoveToGoodbyeScreen = event.BuilderKeyResponse()  # create an object of type KeyResponse
MoveToGoodbyeScreen.status = NOT_STARTED
# keep track of which components have finished
Final_ScoreComponents = []
Final_ScoreComponents.append(FinalScoreScreen)
Final_ScoreComponents.append(EndFinalScoreScreen)
Final_ScoreComponents.append(MoveToGoodbyeScreen)
for thisComponent in Final_ScoreComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Final_Score"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Final_ScoreClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *FinalScoreScreen* updates
    if t >= 0.0 and FinalScoreScreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        FinalScoreScreen.tStart = t  # underestimates by a little under one frame
        FinalScoreScreen.frameNStart = frameN  # exact frame index
        FinalScoreScreen.setAutoDraw(True)
    
    # *EndFinalScoreScreen* updates
    if t >= 0.0 and EndFinalScoreScreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndFinalScoreScreen.tStart = t  # underestimates by a little under one frame
        EndFinalScoreScreen.frameNStart = frameN  # exact frame index
        EndFinalScoreScreen.setAutoDraw(True)
    
    # *MoveToGoodbyeScreen* updates
    if t >= 0.0 and MoveToGoodbyeScreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        MoveToGoodbyeScreen.tStart = t  # underestimates by a little under one frame
        MoveToGoodbyeScreen.frameNStart = frameN  # exact frame index
        MoveToGoodbyeScreen.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(MoveToGoodbyeScreen.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if MoveToGoodbyeScreen.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            MoveToGoodbyeScreen.keys = theseKeys[-1]  # just the last key pressed
            MoveToGoodbyeScreen.rt = MoveToGoodbyeScreen.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Final_ScoreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Final_Score"-------
for thisComponent in Final_ScoreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if MoveToGoodbyeScreen.keys in ['', [], None]:  # No response was made
   MoveToGoodbyeScreen.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('MoveToGoodbyeScreen.keys',MoveToGoodbyeScreen.keys)
if MoveToGoodbyeScreen.keys != None:  # we had a response
    thisExp.addData('MoveToGoodbyeScreen.rt', MoveToGoodbyeScreen.rt)
thisExp.nextEntry()
# the Routine "Final_Score" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Goodbye_Screen"-------
t = 0
Goodbye_ScreenClock.reset()  # clock 
frameN = -1
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
Goodbye_ScreenComponents = []
Goodbye_ScreenComponents.append(Goodbye)
for thisComponent in Goodbye_ScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Goodbye_Screen"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Goodbye_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Goodbye* updates
    if t >= 0.0 and Goodbye.status == NOT_STARTED:
        # keep track of start time/frame for later
        Goodbye.tStart = t  # underestimates by a little under one frame
        Goodbye.frameNStart = frameN  # exact frame index
        Goodbye.setAutoDraw(True)
    if Goodbye.status == STARTED and t >= (0.0 + (10.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        Goodbye.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Goodbye_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Goodbye_Screen"-------
for thisComponent in Goodbye_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()

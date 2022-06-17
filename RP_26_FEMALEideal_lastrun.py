#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on Mai 21, 2022, at 12:30
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'Name of Experiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\bitcu\\Desktop\\RP-26\\RP_26_FEMALEideal_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=1, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Rate_Practice"
Rate_PracticeClock = core.Clock()
RatePractice = visual.Slider(win=win, name='RatePractice',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.3), units=None,
    labels=["Not at all", "Very Much"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor=[0.2078, 0.5922, -0.5843], lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=0, readOnly=False)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
button = visual.ImageStim(
    win=win,
    name='button', 
    image='continuebutton.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.45, -0.45), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
RatePracticeText = visual.TextStim(win=win, name='RatePracticeText',
    text="Welcome to rate practice!\n\nIn the experiment, you will see a slider like this one. After you've clicked on the slider, the continue button appears. Click on it when your choice is final, in order to carry on with the experiment.",
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "LSL"
LSLClock = core.Clock()
from pylsl import StreamInfo, StreamOutlet

info = StreamInfo(name='Triggerstream',type = 'Markers',channel_count=1, channel_format='int32', source_id='Example')

outlet = StreamOutlet(info)


# Initialize components for Routine "Prompt_Prime"
Prompt_PrimeClock = core.Clock()
Prompt1 = keyboard.Keyboard()
Prompt1text = visual.TextStim(win=win, name='Prompt1text',
    text="Dear Participant,\n\nWelcome to our study: Your Brain on Food.\n\nDuring the task, you will see a series of food related images, followed by a rating slider.\n\nWe are now preparing your task and calibrating the fNIRS equipment. While we do so, you will see some motivational images.\n\nYou will press to start the calibration but after that, you don't need to click any buttons. A fixation cross will sometimes appear at the center of the screen. Both this text, the images and the cross will automatically disappear. You don't have to click on the screen unless told to.\n\nPlease keep your head still and keep your gaze on the cross. The fNIRS device might de-calibrate if you don't do so. ",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "StartPrime"
StartPrimeClock = core.Clock()
StartPrimeRun = visual.TextStim(win=win, name='StartPrimeRun',
    text='Press ‘space’ to start the calibration',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
StartPrimeKey = keyboard.Keyboard()
outlet.push_sample(x=[1])

# Initialize components for Routine "PrimeImage"
PrimeImageClock = core.Clock()
Prime = visual.ImageStim(
    win=win,
    name='Prime', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
plus = visual.TextStim(win=win, name='plus',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Prompt_Condition"
Prompt_ConditionClock = core.Clock()
Prompt_Cond = visual.TextStim(win=win, name='Prompt_Cond',
    text="Great job! We are now ready to start.\n\nYou will be asked to press start. You will then see another fixation cross followed by the first image. \n\nA slider will appear to rate desirability of the image you just saw. This will procede until the end of the experiment. \n\nDon't forget to keep your head still and keep your gaze on the cross. The fNIRS device might de-calibrate if you don't do so. \n\nReady to start?",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "StartCondition"
StartConditionClock = core.Clock()
key_resp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='Press ‘space’ to start the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
plus = visual.TextStim(win=win, name='plus',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ConditionImage"
ConditionImageClock = core.Clock()
outlet.push_sample(x=[1])
FoodImage = visual.ImageStim(
    win=win,
    name='FoodImage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.6, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Rate"
RateClock = core.Clock()
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=["Not at all", "Very much"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor=[0.2078, 0.5922, -0.5843], lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=0, readOnly=False)
SliderText = visual.TextStim(win=win, name='SliderText',
    text='How much would you like to have this item, right now? \n',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
outlet.push_sample(x=[1])
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
continuebutton = visual.ImageStim(
    win=win,
    name='continuebutton', 
    image='continuebutton.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.45, -0.45), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
plus = visual.TextStim(win=win, name='plus',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "EndPrompt"
EndPromptClock = core.Clock()
EndText = visual.TextStim(win=win, name='EndText',
    text='Uff! That was long.\n\nGreat job! You are now done!\n\nThank you so much for helping our experiment.\n\nHave a great rest of your day!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
outlet.push_sample(x=[1])

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Rate_Practice"-------
continueRoutine = True
# update component parameters for each repeat
RatePractice.reset()
# setup some python lists for storing info about the mouse_2
mouse_2.x = []
mouse_2.y = []
mouse_2.leftButton = []
mouse_2.midButton = []
mouse_2.rightButton = []
mouse_2.time = []
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Rate_PracticeComponents = [RatePractice, mouse_2, button, RatePracticeText]
for thisComponent in Rate_PracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Rate_PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Rate_Practice"-------
while continueRoutine:
    # get current time
    t = Rate_PracticeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Rate_PracticeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RatePractice* updates
    if RatePractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RatePractice.frameNStart = frameN  # exact frame index
        RatePractice.tStart = t  # local t and not account for scr refresh
        RatePractice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RatePractice, 'tStartRefresh')  # time at next scr refresh
        RatePractice.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and RatePractice.rating:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(button)
                    clickableList = button
                except:
                    clickableList = [button]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                x, y = mouse_2.getPos()
                mouse_2.x.append(x)
                mouse_2.y.append(y)
                buttons = mouse_2.getPressed()
                mouse_2.leftButton.append(buttons[0])
                mouse_2.midButton.append(buttons[1])
                mouse_2.rightButton.append(buttons[2])
                mouse_2.time.append(mouse_2.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # *button* updates
    if button.status == NOT_STARTED and RatePractice.rating:
        # keep track of start time/frame for later
        button.frameNStart = frameN  # exact frame index
        button.tStart = t  # local t and not account for scr refresh
        button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
        button.setAutoDraw(True)
    
    # *RatePracticeText* updates
    if RatePracticeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RatePracticeText.frameNStart = frameN  # exact frame index
        RatePracticeText.tStart = t  # local t and not account for scr refresh
        RatePracticeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RatePracticeText, 'tStartRefresh')  # time at next scr refresh
        RatePracticeText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Rate_PracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Rate_Practice"-------
for thisComponent in Rate_PracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('RatePractice.response', RatePractice.getRating())
thisExp.addData('RatePractice.rt', RatePractice.getRT())
thisExp.addData('RatePractice.started', RatePractice.tStartRefresh)
thisExp.addData('RatePractice.stopped', RatePractice.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_2.x', mouse_2.x)
thisExp.addData('mouse_2.y', mouse_2.y)
thisExp.addData('mouse_2.leftButton', mouse_2.leftButton)
thisExp.addData('mouse_2.midButton', mouse_2.midButton)
thisExp.addData('mouse_2.rightButton', mouse_2.rightButton)
thisExp.addData('mouse_2.time', mouse_2.time)
thisExp.addData('mouse_2.clicked_name', mouse_2.clicked_name)
thisExp.addData('mouse_2.started', mouse_2.tStart)
thisExp.addData('mouse_2.stopped', mouse_2.tStop)
thisExp.nextEntry()
thisExp.addData('button.started', button.tStartRefresh)
thisExp.addData('button.stopped', button.tStopRefresh)
thisExp.addData('RatePracticeText.started', RatePracticeText.tStartRefresh)
thisExp.addData('RatePracticeText.stopped', RatePracticeText.tStopRefresh)
# the Routine "Rate_Practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "LSL"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
LSLComponents = []
for thisComponent in LSLComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LSLClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LSL"-------
while continueRoutine:
    # get current time
    t = LSLClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LSLClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LSLComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LSL"-------
for thisComponent in LSLComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "LSL" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Prompt_Prime"-------
continueRoutine = True
routineTimer.add(30.000000)
# update component parameters for each repeat
Prompt1.keys = []
Prompt1.rt = []
_Prompt1_allKeys = []
# keep track of which components have finished
Prompt_PrimeComponents = [Prompt1, Prompt1text]
for thisComponent in Prompt_PrimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Prompt_PrimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Prompt_Prime"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Prompt_PrimeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Prompt_PrimeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Prompt1* updates
    waitOnFlip = False
    if Prompt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Prompt1.frameNStart = frameN  # exact frame index
        Prompt1.tStart = t  # local t and not account for scr refresh
        Prompt1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Prompt1, 'tStartRefresh')  # time at next scr refresh
        Prompt1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Prompt1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Prompt1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Prompt1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Prompt1.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            Prompt1.tStop = t  # not accounting for scr refresh
            Prompt1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Prompt1, 'tStopRefresh')  # time at next scr refresh
            Prompt1.status = FINISHED
    if Prompt1.status == STARTED and not waitOnFlip:
        theseKeys = Prompt1.getKeys(keyList=['space'], waitRelease=False)
        _Prompt1_allKeys.extend(theseKeys)
        if len(_Prompt1_allKeys):
            Prompt1.keys = _Prompt1_allKeys[-1].name  # just the last key pressed
            Prompt1.rt = _Prompt1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Prompt1text* updates
    if Prompt1text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Prompt1text.frameNStart = frameN  # exact frame index
        Prompt1text.tStart = t  # local t and not account for scr refresh
        Prompt1text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Prompt1text, 'tStartRefresh')  # time at next scr refresh
        Prompt1text.setAutoDraw(True)
    if Prompt1text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Prompt1text.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            Prompt1text.tStop = t  # not accounting for scr refresh
            Prompt1text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Prompt1text, 'tStopRefresh')  # time at next scr refresh
            Prompt1text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Prompt_PrimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Prompt_Prime"-------
for thisComponent in Prompt_PrimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Prompt1.keys in ['', [], None]:  # No response was made
    Prompt1.keys = None
thisExp.addData('Prompt1.keys',Prompt1.keys)
if Prompt1.keys != None:  # we had a response
    thisExp.addData('Prompt1.rt', Prompt1.rt)
thisExp.addData('Prompt1.started', Prompt1.tStartRefresh)
thisExp.addData('Prompt1.stopped', Prompt1.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Prompt1text.started', Prompt1text.tStartRefresh)
thisExp.addData('Prompt1text.stopped', Prompt1text.tStopRefresh)

# ------Prepare to start Routine "StartPrime"-------
continueRoutine = True
# update component parameters for each repeat
StartPrimeKey.keys = []
StartPrimeKey.rt = []
_StartPrimeKey_allKeys = []
# keep track of which components have finished
StartPrimeComponents = [StartPrimeRun, StartPrimeKey]
for thisComponent in StartPrimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartPrimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartPrime"-------
while continueRoutine:
    # get current time
    t = StartPrimeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartPrimeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *StartPrimeRun* updates
    if StartPrimeRun.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        StartPrimeRun.frameNStart = frameN  # exact frame index
        StartPrimeRun.tStart = t  # local t and not account for scr refresh
        StartPrimeRun.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(StartPrimeRun, 'tStartRefresh')  # time at next scr refresh
        StartPrimeRun.setAutoDraw(True)
    
    # *StartPrimeKey* updates
    waitOnFlip = False
    if StartPrimeKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        StartPrimeKey.frameNStart = frameN  # exact frame index
        StartPrimeKey.tStart = t  # local t and not account for scr refresh
        StartPrimeKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(StartPrimeKey, 'tStartRefresh')  # time at next scr refresh
        StartPrimeKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(StartPrimeKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(StartPrimeKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if StartPrimeKey.status == STARTED and not waitOnFlip:
        theseKeys = StartPrimeKey.getKeys(keyList=['space'], waitRelease=False)
        _StartPrimeKey_allKeys.extend(theseKeys)
        if len(_StartPrimeKey_allKeys):
            StartPrimeKey.keys = _StartPrimeKey_allKeys[-1].name  # just the last key pressed
            StartPrimeKey.rt = _StartPrimeKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartPrimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartPrime"-------
for thisComponent in StartPrimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('StartPrimeRun.started', StartPrimeRun.tStartRefresh)
thisExp.addData('StartPrimeRun.stopped', StartPrimeRun.tStopRefresh)
# check responses
if StartPrimeKey.keys in ['', [], None]:  # No response was made
    StartPrimeKey.keys = None
thisExp.addData('StartPrimeKey.keys',StartPrimeKey.keys)
if StartPrimeKey.keys != None:  # we had a response
    thisExp.addData('StartPrimeKey.rt', StartPrimeKey.rt)
thisExp.addData('StartPrimeKey.started', StartPrimeKey.tStartRefresh)
thisExp.addData('StartPrimeKey.stopped', StartPrimeKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "StartPrime" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PrimeLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('imagelist.xlsx'),
    seed=None, name='PrimeLoop')
thisExp.addLoop(PrimeLoop)  # add the loop to the experiment
thisPrimeLoop = PrimeLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrimeLoop.rgb)
if thisPrimeLoop != None:
    for paramName in thisPrimeLoop:
        exec('{} = thisPrimeLoop[paramName]'.format(paramName))

for thisPrimeLoop in PrimeLoop:
    currentLoop = PrimeLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPrimeLoop.rgb)
    if thisPrimeLoop != None:
        for paramName in thisPrimeLoop:
            exec('{} = thisPrimeLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "PrimeImage"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    Prime.setImage(idealfemale)
    outlet.push_sample(x=[2])
    # keep track of which components have finished
    PrimeImageComponents = [Prime]
    for thisComponent in PrimeImageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PrimeImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PrimeImage"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PrimeImageClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PrimeImageClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Prime* updates
        if Prime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prime.frameNStart = frameN  # exact frame index
            Prime.tStart = t  # local t and not account for scr refresh
            Prime.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prime, 'tStartRefresh')  # time at next scr refresh
            Prime.setAutoDraw(True)
        if Prime.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Prime.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                Prime.tStop = t  # not accounting for scr refresh
                Prime.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Prime, 'tStopRefresh')  # time at next scr refresh
                Prime.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PrimeImageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PrimeImage"-------
    for thisComponent in PrimeImageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PrimeLoop.addData('Prime.started', Prime.tStartRefresh)
    PrimeLoop.addData('Prime.stopped', Prime.tStopRefresh)
    
    # ------Prepare to start Routine "FixCross"-------
    continueRoutine = True
    routineTimer.add(12.000000)
    # update component parameters for each repeat
    outlet.push_sample(x=[1])
    # keep track of which components have finished
    FixCrossComponents = [plus]
    for thisComponent in FixCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *plus* updates
        if plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            plus.frameNStart = frameN  # exact frame index
            plus.tStart = t  # local t and not account for scr refresh
            plus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(plus, 'tStartRefresh')  # time at next scr refresh
            plus.setAutoDraw(True)
        if plus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > plus.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                plus.tStop = t  # not accounting for scr refresh
                plus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(plus, 'tStopRefresh')  # time at next scr refresh
                plus.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixCross"-------
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PrimeLoop.addData('plus.started', plus.tStartRefresh)
    PrimeLoop.addData('plus.stopped', plus.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'PrimeLoop'


# ------Prepare to start Routine "Prompt_Condition"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
Prompt_ConditionComponents = [Prompt_Cond]
for thisComponent in Prompt_ConditionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Prompt_ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Prompt_Condition"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Prompt_ConditionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Prompt_ConditionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Prompt_Cond* updates
    if Prompt_Cond.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Prompt_Cond.frameNStart = frameN  # exact frame index
        Prompt_Cond.tStart = t  # local t and not account for scr refresh
        Prompt_Cond.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Prompt_Cond, 'tStartRefresh')  # time at next scr refresh
        Prompt_Cond.setAutoDraw(True)
    if Prompt_Cond.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Prompt_Cond.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            Prompt_Cond.tStop = t  # not accounting for scr refresh
            Prompt_Cond.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Prompt_Cond, 'tStopRefresh')  # time at next scr refresh
            Prompt_Cond.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Prompt_ConditionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Prompt_Condition"-------
for thisComponent in Prompt_ConditionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Prompt_Cond.started', Prompt_Cond.tStartRefresh)
thisExp.addData('Prompt_Cond.stopped', Prompt_Cond.tStopRefresh)

# ------Prepare to start Routine "StartCondition"-------
continueRoutine = True
# update component parameters for each repeat
outlet.push_sample(x=[1])
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
StartConditionComponents = [key_resp, text]
for thisComponent in StartConditionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartCondition"-------
while continueRoutine:
    # get current time
    t = StartConditionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartConditionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartConditionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartCondition"-------
for thisComponent in StartConditionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "StartCondition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
routineTimer.add(12.000000)
# update component parameters for each repeat
outlet.push_sample(x=[1])
# keep track of which components have finished
FixCrossComponents = [plus]
for thisComponent in FixCrossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FixCross"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FixCrossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *plus* updates
    if plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        plus.frameNStart = frameN  # exact frame index
        plus.tStart = t  # local t and not account for scr refresh
        plus.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(plus, 'tStartRefresh')  # time at next scr refresh
        plus.setAutoDraw(True)
    if plus.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > plus.tStartRefresh + 12-frameTolerance:
            # keep track of stop time/frame for later
            plus.tStop = t  # not accounting for scr refresh
            plus.frameNStop = frameN  # exact frame index
            win.timeOnFlip(plus, 'tStopRefresh')  # time at next scr refresh
            plus.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FixCross"-------
for thisComponent in FixCrossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('plus.started', plus.tStartRefresh)
thisExp.addData('plus.stopped', plus.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Food = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('imagelist.xlsx'),
    seed=None, name='Food')
thisExp.addLoop(Food)  # add the loop to the experiment
thisFood = Food.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFood.rgb)
if thisFood != None:
    for paramName in thisFood:
        exec('{} = thisFood[paramName]'.format(paramName))

for thisFood in Food:
    currentLoop = Food
    # abbreviate parameter names if possible (e.g. rgb = thisFood.rgb)
    if thisFood != None:
        for paramName in thisFood:
            exec('{} = thisFood[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ConditionImage"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    FoodImage.setImage(foodpics)
    # keep track of which components have finished
    ConditionImageComponents = [FoodImage]
    for thisComponent in ConditionImageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ConditionImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ConditionImage"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ConditionImageClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ConditionImageClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FoodImage* updates
        if FoodImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FoodImage.frameNStart = frameN  # exact frame index
            FoodImage.tStart = t  # local t and not account for scr refresh
            FoodImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FoodImage, 'tStartRefresh')  # time at next scr refresh
            FoodImage.setAutoDraw(True)
        if FoodImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FoodImage.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                FoodImage.tStop = t  # not accounting for scr refresh
                FoodImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FoodImage, 'tStopRefresh')  # time at next scr refresh
                FoodImage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConditionImageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ConditionImage"-------
    for thisComponent in ConditionImageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Food.addData('FoodImage.started', FoodImage.tStartRefresh)
    Food.addData('FoodImage.stopped', FoodImage.tStopRefresh)
    
    # ------Prepare to start Routine "Rate"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider.reset()
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RateComponents = [slider, SliderText, mouse, continuebutton]
    for thisComponent in RateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Rate"-------
    while continueRoutine:
        # get current time
        t = RateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # *SliderText* updates
        if SliderText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SliderText.frameNStart = frameN  # exact frame index
            SliderText.tStart = t  # local t and not account for scr refresh
            SliderText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SliderText, 'tStartRefresh')  # time at next scr refresh
            SliderText.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and slider.rating:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(continuebutton)
                        clickableList = continuebutton
                    except:
                        clickableList = [continuebutton]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *continuebutton* updates
        if continuebutton.status == NOT_STARTED and slider.rating:
            # keep track of start time/frame for later
            continuebutton.frameNStart = frameN  # exact frame index
            continuebutton.tStart = t  # local t and not account for scr refresh
            continuebutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continuebutton, 'tStartRefresh')  # time at next scr refresh
            continuebutton.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Rate"-------
    for thisComponent in RateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Food.addData('slider.response', slider.getRating())
    Food.addData('slider.rt', slider.getRT())
    Food.addData('slider.started', slider.tStartRefresh)
    Food.addData('slider.stopped', slider.tStopRefresh)
    Food.addData('SliderText.started', SliderText.tStartRefresh)
    Food.addData('SliderText.stopped', SliderText.tStopRefresh)
    # store data for Food (TrialHandler)
    Food.addData('mouse.x', mouse.x)
    Food.addData('mouse.y', mouse.y)
    Food.addData('mouse.leftButton', mouse.leftButton)
    Food.addData('mouse.midButton', mouse.midButton)
    Food.addData('mouse.rightButton', mouse.rightButton)
    Food.addData('mouse.time', mouse.time)
    Food.addData('mouse.clicked_name', mouse.clicked_name)
    Food.addData('mouse.started', mouse.tStart)
    Food.addData('mouse.stopped', mouse.tStop)
    Food.addData('continuebutton.started', continuebutton.tStartRefresh)
    Food.addData('continuebutton.stopped', continuebutton.tStopRefresh)
    # the Routine "Rate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "FixCross"-------
    continueRoutine = True
    routineTimer.add(12.000000)
    # update component parameters for each repeat
    outlet.push_sample(x=[1])
    # keep track of which components have finished
    FixCrossComponents = [plus]
    for thisComponent in FixCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *plus* updates
        if plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            plus.frameNStart = frameN  # exact frame index
            plus.tStart = t  # local t and not account for scr refresh
            plus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(plus, 'tStartRefresh')  # time at next scr refresh
            plus.setAutoDraw(True)
        if plus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > plus.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                plus.tStop = t  # not accounting for scr refresh
                plus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(plus, 'tStopRefresh')  # time at next scr refresh
                plus.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixCross"-------
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Food.addData('plus.started', plus.tStartRefresh)
    Food.addData('plus.stopped', plus.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Food'


# ------Prepare to start Routine "EndPrompt"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndPromptComponents = [EndText]
for thisComponent in EndPromptComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndPromptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndPrompt"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndPromptClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndPromptClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndText* updates
    if EndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndText.frameNStart = frameN  # exact frame index
        EndText.tStart = t  # local t and not account for scr refresh
        EndText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndText, 'tStartRefresh')  # time at next scr refresh
        EndText.setAutoDraw(True)
    if EndText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EndText.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            EndText.tStop = t  # not accounting for scr refresh
            EndText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(EndText, 'tStopRefresh')  # time at next scr refresh
            EndText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndPromptComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndPrompt"-------
for thisComponent in EndPromptComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndText.started', EndText.tStartRefresh)
thisExp.addData('EndText.stopped', EndText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

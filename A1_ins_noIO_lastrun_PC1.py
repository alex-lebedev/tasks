#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v1.90.3),
    on januari 04, 2019, at 19:10
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '1.90.3'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'', u'eye-tracking':1}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

#save ET status
ET = expInfo['eye-tracking']

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\Users\Emotionlab\Desktop\RALT_pupillometry\A1_ins_noIO_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Inserted ET Code to run Calibration
if ET:

    # run calibration
    # ---------------------------------------------
    #---- connect to iViewX 
    # ---------------------------------------------
    from iViewXAPI import  *            #iViewX library
    from iViewXAPIReturnCodes import *
    res = iViewXAPI.iV_SetLogger(c_int(1), c_char_p("shock_task"))
    res = iViewXAPI.iV_Connect(c_char_p('169.254.2.2'), c_int(4444), c_char_p('169.254.2.1'), c_int(5555))
    if res != 1:
        HandleError(res)
        exit(0)
        
    res = iViewXAPI.iV_GetSystemInfo(byref(systemData))
    print "iV_GetSystemInfo: " + str(res)
    print "Samplerate: " + str(systemData.samplerate)
    print "iViewX Version: " + str(systemData.iV_MajorVersion) + "." + str(systemData.iV_MinorVersion) + "." + str(systemData.iV_Buildnumber)
    print "iViewX API Version: " + str(systemData.API_MajorVersion) + "." + str(systemData.API_MinorVersion) + "." + str(systemData.API_Buildnumber)

    # ---------------------------------------------
    #---- configure and start calibration
    # ---------------------------------------------

    calibrationData = CCalibration(9, 1, 0, 0, 1, 250, 220, 2, 20, b"")

    res = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
    print "iV_SetupCalibration " + str(res)

    while 1:
        res = iViewXAPI.iV_Calibrate()
        print "iV_Calibrate " + str(res)

        res = iViewXAPI.iV_Validate()
        print "iV_Validate " + str(res)

        res = iViewXAPI.iV_GetAccuracy(byref(accuracyData), 1)
        print "iV_GetAccuracy " + str(res)
        print "deviationXLeft " + str(accuracyData.deviationLX) + " deviationYLeft " + str(accuracyData.deviationLY)
        print "deviationXRight " + str(accuracyData.deviationRX) + " deviationYRight " + str(accuracyData.deviationRY)

        res = iViewXAPI.iV_ShowTrackingMonitor()
        print "iV_ShowTrackingMonitor " + str(res)
        
        ET_dlg = gui.Dlg(title = "Calibration confirmation")
        ET_dlg.addText("Calibration OK?")
        ET_dlg.show()
        if ET_dlg.OK:
            break
        else:
            continue

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "like"
likeClock = core.Clock()
rate_img = visual.ImageStim(
    win=win, name='rate_img',
    image='stim/Instructions/rate.JPG', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# leftKeys='1',rightKeys='2', acceptKeys='4'

rating_scale = visual.RatingScale(win=win, name='rating_scale', marker='triangle', size=0.8, pos=[0.0, -0.5], low=1, high=21, labels=['', ''], scale='', markerStart='11', showAccept=False)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "transition"
transitionClock = core.Clock()
transition_fix = visual.TextStim(win=win, name='transition_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='>>',
    font='Arial',
    pos=(0.8, 0.8), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "WHO"
WHOClock = core.Clock()
who_img = visual.ImageStim(
    win=win, name='who_img',
    image='stim/Instructions/WHOA.JPG', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "intro"
introClock = core.Clock()
instructions_img = visual.ImageStim(
    win=win, name='instructions_img',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text="Press 's' if you understand the instructions and are ready to start the experiment.",
    font='Arial',
    pos=(0, -0.8), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Task"
TaskClock = core.Clock()
bkgdFix = visual.TextStim(win=win, name='bkgdFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fixStim = visual.TextStim(win=win, name='fixStim',
    text='default text',
    font='Arial',
    pos=(0, -0.25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
face_stim = visual.ImageStim(
    win=win, name='face_stim',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
polygon = visual.Rect(
    win=win, name='polygon',
    width=(10, 10)[0], height=(10, 10)[1],
    ori=0, pos=(0, 0),
    lineWidth=2, lineColor=[255,0,0], lineColorSpace='rgb',
    fillColor=[255,0,0], fillColorSpace='rgb',
    opacity=0.5, depth=-4.0, interpolate=True)


# Initialize components for Routine "transition"
transitionClock = core.Clock()
transition_fix = visual.TextStim(win=win, name='transition_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='>>',
    font='Arial',
    pos=(0.8, 0.8), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "like"
likeClock = core.Clock()
rate_img = visual.ImageStim(
    win=win, name='rate_img',
    image='stim/Instructions/rate.JPG', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# leftKeys='1',rightKeys='2', acceptKeys='4'

rating_scale = visual.RatingScale(win=win, name='rating_scale', marker='triangle', size=0.8, pos=[0.0, -0.5], low=1, high=21, labels=['', ''], scale='', markerStart='11', showAccept=False)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
rating_pre = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ratings.xlsx'),
    seed=123, name='rating_pre')
thisExp.addLoop(rating_pre)  # add the loop to the experiment
thisRating_pre = rating_pre.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRating_pre.rgb)
if thisRating_pre != None:
    for paramName in thisRating_pre:
        exec('{} = thisRating_pre[paramName]'.format(paramName))

for thisRating_pre in rating_pre:
    currentLoop = rating_pre
    # abbreviate parameter names if possible (e.g. rgb = thisRating_pre.rgb)
    if thisRating_pre != None:
        for paramName in thisRating_pre:
            exec('{} = thisRating_pre[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "like"-------
    t = 0
    likeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    rating_scale.reset()
    image.setImage(faceStim)
    # keep track of which components have finished
    likeComponents = [rate_img, rating_scale, image]
    for thisComponent in likeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "like"-------
    while continueRoutine:
        # get current time
        t = likeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rate_img* updates
        if t >= 0.0 and rate_img.status == NOT_STARTED:
            # keep track of start time/frame for later
            rate_img.tStart = t
            rate_img.frameNStart = frameN  # exact frame index
            rate_img.setAutoDraw(True)
        
        # *rating_scale* updates
        if t >= 0.0 and rating_scale.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_scale.tStart = t
            rating_scale.frameNStart = frameN  # exact frame index
            rating_scale.setAutoDraw(True)
        continueRoutine &= rating_scale.noResponse  # a response ends the trial
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in likeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "like"-------
    for thisComponent in likeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # store data for rating_pre (TrialHandler)
    rating_pre.addData('rating_scale.response', rating_scale.getRating())
    rating_pre.addData('rating_scale.rt', rating_scale.getRT())
    # the Routine "like" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'rating_pre'


# ------Prepare to start Routine "transition"-------
t = 0
transitionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
transition_key = event.BuilderKeyResponse()
# keep track of which components have finished
transitionComponents = [transition_fix, transition_key, text_2]
for thisComponent in transitionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "transition"-------
while continueRoutine:
    # get current time
    t = transitionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *transition_fix* updates
    if t >= 0.0 and transition_fix.status == NOT_STARTED:
        # keep track of start time/frame for later
        transition_fix.tStart = t
        transition_fix.frameNStart = frameN  # exact frame index
        transition_fix.setAutoDraw(True)
    
    # *transition_key* updates
    if t >= 0.0 and transition_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        transition_key.tStart = t
        transition_key.frameNStart = frameN  # exact frame index
        transition_key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(transition_key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if transition_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            transition_key.keys = theseKeys[-1]  # just the last key pressed
            transition_key.rt = transition_key.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in transitionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "transition"-------
for thisComponent in transitionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if transition_key.keys in ['', [], None]:  # No response was made
    transition_key.keys=None
thisExp.addData('transition_key.keys',transition_key.keys)
if transition_key.keys != None:  # we had a response
    thisExp.addData('transition_key.rt', transition_key.rt)
thisExp.nextEntry()
# the Routine "transition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WHO"-------
t = 0
WHOClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
who_response = event.BuilderKeyResponse()
# keep track of which components have finished
WHOComponents = [who_img, who_response]
for thisComponent in WHOComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WHO"-------
while continueRoutine:
    # get current time
    t = WHOClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *who_img* updates
    if t >= 0.0 and who_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        who_img.tStart = t
        who_img.frameNStart = frameN  # exact frame index
        who_img.setAutoDraw(True)
    
    # *who_response* updates
    if t >= 0.0 and who_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        who_response.tStart = t
        who_response.frameNStart = frameN  # exact frame index
        who_response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(who_response.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if who_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['left', 'right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            who_response.keys = theseKeys[-1]  # just the last key pressed
            who_response.rt = who_response.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WHOComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WHO"-------
for thisComponent in WHOComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if who_response.keys in ['', [], None]:  # No response was made
    who_response.keys=None
thisExp.addData('who_response.keys',who_response.keys)
if who_response.keys != None:  # we had a response
    thisExp.addData('who_response.rt', who_response.rt)
thisExp.nextEntry()
# the Routine "WHO" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instructions_img.setImage('stim/Instructions/InstructionsA_ins.JPG')
trTrigger = event.BuilderKeyResponse()
# keep track of which components have finished
introComponents = [instructions_img, text, trTrigger]
for thisComponent in introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_img* updates
    if t >= 0.0 and instructions_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_img.tStart = t
        instructions_img.frameNStart = frameN  # exact frame index
        instructions_img.setAutoDraw(True)
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *trTrigger* updates
    if t >= 0.0 and trTrigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        trTrigger.tStart = t
        trTrigger.frameNStart = frameN  # exact frame index
        trTrigger.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(trTrigger.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if trTrigger.status == STARTED:
        theseKeys = event.getKeys(keyList=['s'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            trTrigger.keys = theseKeys[-1]  # just the last key pressed
            trTrigger.rt = trTrigger.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trTrigger.keys in ['', [], None]:  # No response was made
    trTrigger.keys=None
thisExp.addData('trTrigger.keys',trTrigger.keys)
if trTrigger.keys != None:  # we had a response
    thisExp.addData('trTrigger.rt', trTrigger.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('faces1A_ins.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Task"-------
    t = 0
    TaskClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    face_stim.setImage(face)
    RevConfirm = event.BuilderKeyResponse()
    # start ET
    if ET:
        iViewXAPI.iV_StartRecording()
        iViewXAPI.iV_SendImageMessage(c_char_p("Start of trial " + str(thisTrial['trial'])))
    # keep track of which components have finished
    TaskComponents = [bkgdFix, fixStim, face_stim, RevConfirm, polygon]
    for thisComponent in TaskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Task"-------
    while continueRoutine:
        # get current time
        t = TaskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *bkgdFix* updates
        if t >= 0.0 and bkgdFix.status == NOT_STARTED:
            # keep track of start time/frame for later
            bkgdFix.tStart = t
            bkgdFix.frameNStart = frameN  # exact frame index
            bkgdFix.setAutoDraw(True)
        frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
        if bkgdFix.status == STARTED and t >= frameRemains:
            bkgdFix.setAutoDraw(False)
        
        # *fixStim* updates
        if t >= 8 and fixStim.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixStim.tStart = t
            fixStim.frameNStart = frameN  # exact frame index
            fixStim.setAutoDraw(True)
        frameRemains = 8 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixStim.status == STARTED and t >= frameRemains:
            fixStim.setAutoDraw(False)
        if fixStim.status == STARTED:  # only update if drawing
            fixStim.setText(revInst, log=False)
        
        # *face_stim* updates
        if t >= 0.0 and face_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            face_stim.tStart = t
            face_stim.frameNStart = frameN  # exact frame index
            face_stim.setAutoDraw(True)
        frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if face_stim.status == STARTED and t >= frameRemains:
            face_stim.setAutoDraw(False)
        
        # *RevConfirm* updates
        if t >= 8 and RevConfirm.status == NOT_STARTED:
            # keep track of start time/frame for later
            RevConfirm.tStart = t
            RevConfirm.frameNStart = frameN  # exact frame index
            RevConfirm.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(RevConfirm.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 8 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if RevConfirm.status == STARTED and t >= frameRemains:
            RevConfirm.status = FINISHED
        if RevConfirm.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if RevConfirm.keys == []:  # then this was the first keypress
                    RevConfirm.keys = theseKeys[0]  # just the first key pressed
                    RevConfirm.rt = RevConfirm.clock.getTime()
        
        # *polygon* updates
        if t >= shockstart and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        frameRemains = shockstart + shock- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon.status == STARTED and t >= frameRemains:
            polygon.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Task"-------
    for thisComponent in TaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if RevConfirm.keys in ['', [], None]:  # No response was made
        RevConfirm.keys=None
    trials.addData('RevConfirm.keys',RevConfirm.keys)
    if RevConfirm.keys != None:  # we had a response
        trials.addData('RevConfirm.rt', RevConfirm.rt)
    
    # the Routine "Task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'trials'

# finish and clean up ET
if ET:
    iViewXAPI.iV_StopRecording()
    
    #save
    # CLOSE ET CONNECTION AND SAVE DATA!
    path = "d:/Recorded Data/"
    filename='%s_%s' %('Alex_L_shock_task', expInfo['participant'])
    outputfile = path + filename + ".idf"
    res = iViewXAPI.iV_SaveData(str(outputfile), str("Shock task"), str("pp"), 1)
    print "iV_SaveData " + str(res)
    print "data saved to: " + outputfile

    iViewXAPI.iV_Disconnect()


# ------Prepare to start Routine "transition"-------
t = 0
transitionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
transition_key = event.BuilderKeyResponse()
# keep track of which components have finished
transitionComponents = [transition_fix, transition_key, text_2]
for thisComponent in transitionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "transition"-------
while continueRoutine:
    # get current time
    t = transitionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *transition_fix* updates
    if t >= 0.0 and transition_fix.status == NOT_STARTED:
        # keep track of start time/frame for later
        transition_fix.tStart = t
        transition_fix.frameNStart = frameN  # exact frame index
        transition_fix.setAutoDraw(True)
    
    # *transition_key* updates
    if t >= 0.0 and transition_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        transition_key.tStart = t
        transition_key.frameNStart = frameN  # exact frame index
        transition_key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(transition_key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if transition_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            transition_key.keys = theseKeys[-1]  # just the last key pressed
            transition_key.rt = transition_key.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in transitionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "transition"-------
for thisComponent in transitionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if transition_key.keys in ['', [], None]:  # No response was made
    transition_key.keys=None
thisExp.addData('transition_key.keys',transition_key.keys)
if transition_key.keys != None:  # we had a response
    thisExp.addData('transition_key.rt', transition_key.rt)
thisExp.nextEntry()
# the Routine "transition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
rating_post = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ratings.xlsx'),
    seed=5654, name='rating_post')
thisExp.addLoop(rating_post)  # add the loop to the experiment
thisRating_post = rating_post.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRating_post.rgb)
if thisRating_post != None:
    for paramName in thisRating_post:
        exec('{} = thisRating_post[paramName]'.format(paramName))

for thisRating_post in rating_post:
    currentLoop = rating_post
    # abbreviate parameter names if possible (e.g. rgb = thisRating_post.rgb)
    if thisRating_post != None:
        for paramName in thisRating_post:
            exec('{} = thisRating_post[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "like"-------
    t = 0
    likeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    rating_scale.reset()
    image.setImage(faceStim)
    # keep track of which components have finished
    likeComponents = [rate_img, rating_scale, image]
    for thisComponent in likeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "like"-------
    while continueRoutine:
        # get current time
        t = likeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rate_img* updates
        if t >= 0.0 and rate_img.status == NOT_STARTED:
            # keep track of start time/frame for later
            rate_img.tStart = t
            rate_img.frameNStart = frameN  # exact frame index
            rate_img.setAutoDraw(True)
        
        # *rating_scale* updates
        if t >= 0.0 and rating_scale.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_scale.tStart = t
            rating_scale.frameNStart = frameN  # exact frame index
            rating_scale.setAutoDraw(True)
        continueRoutine &= rating_scale.noResponse  # a response ends the trial
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in likeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "like"-------
    for thisComponent in likeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # store data for rating_post (TrialHandler)
    rating_post.addData('rating_scale.response', rating_scale.getRating())
    rating_post.addData('rating_scale.rt', rating_scale.getRT())
    # the Routine "like" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'rating_post'


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = []
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

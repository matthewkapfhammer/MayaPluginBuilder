import os

import sublime
import sublime_plugin

"""
Idea: Allow the user to generate some sublime settings automatically generated
from the cookie cutter.
If Jedi will stop being a dick:
These settings would go into the folder that they're setting up and they could
just have the separate executables for the Maya version they need and comment
it out.
"""

PYPLUGINNAMESTR = 'pyPluginName'
PYPLUGINLABEL = 'Python Plugin Name:'
CPPPLUGINNAMESTR = 'cppPluginName'
CPPPLUGINLABEL = 'C++ Plugin Name:'
COMMANDNAMESTR = 'commandName'
COMMANDNAMELABEL = 'Command Name:'
USER_DIR = os.path.expanduser('~')
IS_WIN = (os.name == 'nt')

ILLEGALCHARS = ' !@#$%^&*()-_=+[{]}\\|:;"\'<,>.?/`~'
ILLEGALCHARSMSG = 'You have an illegal character in your name.'
FOLDEREXISTSMSG = 'This folder already exists. Try a new name.'

if IS_WIN:
    SCRIPTSPATH = os.path.join(USER_DIR, 'Documents', 'maya', 'scripts')
else:
    SCRIPTSPATH = os.path.join(USER_DIR, 'Library', 'Preferences', 'Autodesk',
                               'maya', 'scripts')


def checkName(pluginName):
    if [c for c in pluginName if c in ILLEGALCHARS]:
        return False
    return True


def makePluginFolder():
    # Cookie Cutter stuff
    pass


def makeTempScript(scriptType):
    from datetime import datetime
    currentTime = str(datetime.now()).split('.')[0]
    currentTime = currentTime.replace(':', '_').replace(' ', '_')
    if scriptType == 'python':
        tempScript = os.path.join(SCRIPTSPATH, 'tempPy_' + currentTime + '.py')
    elif scriptType == 'mel':
        tempScript = os.path.join(SCRIPTSPATH, 'tempMEL_' + currentTime + '.py')

    if not os.path.isfile(tempScript):
        if scriptType == 'python':
            # Cookie Cutter
            pass
        elif scriptType == 'mel':
            # Cookie Cutter
            pass


class MayaMakeComm(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel(COMMANDNAMELABEL, COMMANDNAMESTR,
                                            self.commandCheck, None, None)

    def commandCheck(self, commandName):
        if checkName(commandName):
            # This SHOULD exist because of Maya.
            if not os.path.isdir(SCRIPTSPATH):
                os.mkdir(SCRIPTSPATH)
            # continue here
        else:
            sublime.error_message(ILLEGALCHARSMSG)
            self.view.window().show_input_panel(COMMANDNAMELABEL, commandName,
                                                self.commandCheck, None, None)


class MayaMakePythonPlugin(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel(PYPLUGINLABEL, PYPLUGINNAMESTR,
                                            self.pluginCheck, None, None)

    def pluginCheck(self, pluginName):
        if checkName(pluginName):
            pluginFolder = os.path.join(SCRIPTSPATH, pluginName)
            if not os.path.isdir(pluginFolder):
                os.mkdir(pluginFolder)
            # continue here
        else:
            sublime.error_message(ILLEGALCHARSMSG)
            self.view.window().show_input_panel(PYPLUGINLABEL, pluginName,
                                                self.pluginCheck, None, None)


class MayaMakeMelScript(sublime_plugin.TextCommand):
    def run(self, edit):
        makeTempScript(scriptType='mel')


class MayaMakePythonScript(sublime_plugin.TextCommand):
    def run(self, edit):
        makeTempScript(scriptType='python')


class MayaMakeCppPlugin(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel(CPPPLUGINLABEL, CPPPLUGINNAMESTR,
                                            self.pluginCheck, None, None)

    def pluginCheck(self, pluginName):
        if checkName(pluginName):
            makePluginFolder(pluginName)
        else:
            sublime.error_message(ILLEGALCHARSMSG)
            self.view.window().show_input_panel(CPPPLUGINLABEL, pluginName,
                                                self.pluginCheck, None, None)

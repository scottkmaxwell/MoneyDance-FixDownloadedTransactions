#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Python script to be run in Moneydance to perform amazing feats of
# financial scripting

from __future__ import print_function

import json
import os.path
import traceback
import datetime
import subprocess

from com.infinitekind.moneydance.model import Account, ParentTxn, AccountIterator
from com.moneydance.util import Platform
from com.moneydance.apps.md.view.gui import MDImages
from com.moneydance.awt import JTextPanel

from java.lang import System, Runnable, IllegalArgumentException
from java.awt import (
    Color,
    Dimension,
    Toolkit,
    Font,
    FileDialog,
    FlowLayout,
)
from java.awt.datatransfer import StringSelection

# noinspection PyUnresolvedReferences
from java.awt.event import KeyEvent, WindowAdapter
from java.awt import Point
from java.text import MessageFormat
from java.io import FilenameFilter, File

from javax.swing import SwingUtilities, JFrame, JOptionPane, JFileChooser
from javax.swing import (
    JButton,
    JScrollPane,
    WindowConstants,
    JComponent,
    KeyStroke,
    JLabel,
)
from javax.swing import JTextArea, JMenuBar, AbstractAction
from javax.swing import Box, JCheckBox, JTextField, JPanel
from javax.swing.text import DefaultHighlighter
from javax.swing.event import AncestorListener
from javax.swing.border import EmptyBorder
from javax.swing.filechooser import FileFilter

# noinspection PyUnresolvedReferences
from javax.print import attribute
from javax.print.attribute import standard
from java.awt.print import PrinterJob

try:
    from moneydance import *

    # noinspection PyUnresolvedReferences
    from typing import Callable, Dict, Generator, Iterator, List, Optional, Set, Tuple, Union

    unicode = str
    basestring = str
except ImportError:
    pass

MD_REF = moneydance
debug = False

myModuleID = "fix_downloaded_transactions"
version_build = "1000"
MIN_BUILD_REQD = 1904  # Check for builds less than 1904 / version < 2019.4
_I_CAN_RUN_AS_MONEYBOT_SCRIPT = True


class MyJFrame(JFrame):
    def __init__(self, frameTitle=None):  # type: (str) -> None
        super(self.__class__, self).__init__(frameTitle)
        self.disposing = False

    def dispose(self):
        # This removes all content as VAqua retains the JFrame reference in memory...
        if self.disposing:
            return
        # noinspection PyBroadException
        try:
            self.disposing = True
            self.removeAll()
            if self.getJMenuBar() is not None:
                self.setJMenuBar(None)
            super(self.__class__, self).dispose()
        except Exception:
            _msg = "%s: ERROR DISPOSING OF FRAME: %s\n" % (myModuleID, self)
            print(_msg)
            System.err.write(_msg)
        finally:
            self.disposing = False


# SET THESE VARIABLES FOR ALL SCRIPTS ##################################################################################
if "GlobalVars" in globals():  # Prevent wiping if 'buddy' extension - like Toolbox - is running too...
    global GlobalVars
else:

    class GlobalVars:  # Started using this method for storing global variables from August 2021
        CONTEXT = MD_REF
        defaultPrintService = None
        defaultPrinterAttributes = None  # type: Optional[attribute.HashPrintRequestAttributeSet]
        defaultPrintFontSize = None
        defaultPrintLandscape = None
        defaultDPI = 72  # NOTE: 72dpi is Java2D default for everything; just go with it. No easy way to change
        STATUS_LABEL = None
        DARK_GREEN = Color(0, 192, 0)
        resetPickleParameters = False
        decimalCharSep = "."
        lGlobalErrorDetected = False
        MYPYTHON_DOWNLOAD_URL = "https://yogi1967.github.io/MoneydancePythonScripts/"
        i_am_an_extension_so_run_headless = None
        parametersLoadedFromFile = {}
        thisScriptName = None
        MD_MDPLUS_BUILD = 4040
        MD_ALERTCONTROLLER_BUILD = 4077

        def __init__(self):
            pass  # Leave empty

        class Strings:
            def __init__(self):
                pass  # Leave empty


GlobalVars.thisScriptName = "%s.py(Extension)" % myModuleID


def setDisplayStatus(_theStatus, _theColor=None):
    """Sets the Display / Status label on the main diagnostic display: G=Green, B=Blue, R=Red, DG=Dark Green"""

    if GlobalVars.STATUS_LABEL is None or not isinstance(GlobalVars.STATUS_LABEL, JLabel):
        return

    class SetDisplayStatusRunnable(Runnable):
        def __init__(self, _status, _color):
            super(self.__class__, self).__init__()
            self.status = _status
            self.color = _color

        def run(self):
            GlobalVars.STATUS_LABEL.setText(_theStatus)
            if self.color is None or self.color == "":
                self.color = "X"
            self.color = self.color.upper()
            if self.color == "R":
                GlobalVars.STATUS_LABEL.setForeground(getColorRed())
            elif self.color == "B":
                GlobalVars.STATUS_LABEL.setForeground(getColorBlue())
            elif self.color == "DG":
                GlobalVars.STATUS_LABEL.setForeground(getColorDarkGreen())
            else:
                GlobalVars.STATUS_LABEL.setForeground(MD_REF.getUI().getColors().defaultTextForeground)

    if not SwingUtilities.isEventDispatchThread():
        SwingUtilities.invokeLater(SetDisplayStatusRunnable(_theStatus, _theColor))
    else:
        SetDisplayStatusRunnable(_theStatus, _theColor).run()


# P=Display on Python Console, J=Display on MD (Java) Console Error Log, B=Both, D=If Debug Only print, DB=print both

# noinspection PyBroadException
def myPrint(where, *args):
    if where[0] == "D" and not debug:
        return

    try:
        print_string = ""
        for what in args:
            print_string += "%s " % what
        print_string = print_string.strip()

        if where == "P" or where == "B" or where[0] == "D":
            if not GlobalVars.i_am_an_extension_so_run_headless:
                try:
                    print(print_string)
                except:
                    print("Error writing to screen...")
                    dump_sys_error_to_md_console_and_errorlog()

        if where == "J" or where == "B" or where == "DB":
            dt = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
            try:
                System.err.write(GlobalVars.thisScriptName + ":" + dt + ": ")
                System.err.write(print_string)
                System.err.write("\n")
            except:
                System.err.write(GlobalVars.thisScriptName + ":" + dt + ": " + "Error writing to console")
                dump_sys_error_to_md_console_and_errorlog()

    except IllegalArgumentException:
        myPrint(
            "B",
            "ERROR - Probably on a multi-byte character..... Will ignore as code should just continue (PLEASE REPORT TO DEVELOPER).....",
        )
        dump_sys_error_to_md_console_and_errorlog()

    return


# Copies MD_REF.getUI().showInfoMessage (but a newer version now exists in MD internal code)
def myPopupInformationBox(
    theParent=None,
    theMessage="What no message?!",
    theTitle="Info",
    theMessageType=JOptionPane.INFORMATION_MESSAGE,
):

    if theParent is None and (
        theMessageType == JOptionPane.PLAIN_MESSAGE or theMessageType == JOptionPane.INFORMATION_MESSAGE
    ):
        icon = getMDIcon(lAlwaysGetIcon=True)
    else:
        icon = getMDIcon(None)
    JOptionPane.showMessageDialog(theParent, JTextPanel(theMessage), theTitle, theMessageType, icon)


def dump_sys_error_to_md_console_and_errorlog(lReturnText=False):

    tb = traceback.format_exc()
    trace = traceback.format_stack()
    text = ".\n" "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n" "@@@@@ Unexpected error caught!\n".upper()
    text += tb
    for trace_line in trace:
        text += trace_line
    text += "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
    myPrint("B", text)
    if lReturnText:
        return text
    return


def safeStr(text):
    return "%s" % text


def pad(text, length, pad_char=" "):
    if not isinstance(text, (unicode, str)):
        text = safeStr(text)
    text = text[:length].ljust(length, pad_char)
    return text


def rpad(text, length, pad_char=" "):
    if not isinstance(text, (unicode, str)):
        text = safeStr(text)
    text = text[:length].rjust(length, pad_char)
    return text


def cpad(text, length, pad_char=" "):
    if not isinstance(text, (unicode, str)):
        text = safeStr(text)
    if len(text) >= length:
        return text[:length]
    pad_length = int((length - len(text)) / 2)
    text = text[:length]
    text = ((pad_char * pad_length) + text + (pad_char * pad_length))[:length]
    return text


# noinspection PyBroadException
def getMonoFont():
    try:
        return MD_REF.getUI().getFonts().code
    except:
        return Font("monospaced", Font.PLAIN, 15)


class GenericDisposeRunnable(Runnable):
    def __init__(self, theFrame):
        super(self.__class__, self).__init__()
        self.theFrame = theFrame

    def run(self):
        self.theFrame.setVisible(False)
        self.theFrame.dispose()


class GenericVisibleRunnable(Runnable):
    def __init__(self, theFrame, lVisible=True, lToFront=False):
        super(self.__class__, self).__init__()
        self.theFrame = theFrame
        self.lVisible = lVisible
        self.lToFront = lToFront

    def run(self):
        self.theFrame.setVisible(self.lVisible)
        if self.lVisible and self.lToFront:
            if self.theFrame.getExtendedState() == JFrame.ICONIFIED:
                self.theFrame.setExtendedState(JFrame.NORMAL)
            self.theFrame.toFront()


def check_file_writable(fnm):
    if os.path.exists(fnm):
        # path exists
        if os.path.isfile(fnm):  # is it a file or a dir?
            # also works when file is a link and the target is writable
            return os.access(fnm, os.W_OK)
        else:
            return False  # path is a dir, so cannot write as a file
    # target does not exist, check perms on parent dir
    pdir = os.path.dirname(fnm)
    if not pdir:
        pdir = "."
    # target is creatable if parent dir is writable
    return os.access(pdir, os.W_OK)


class ExtFilenameFilter(FilenameFilter):
    """File extension filter for FileDialog"""

    def __init__(self, ext):
        super(self.__class__, self).__init__()
        self.ext = "." + ext.upper()  # noqa

    def accept(self, thedir, filename):  # noqa
        if filename is not None and filename.upper().endswith(self.ext):
            return True
        return False


class ExtFileFilterJFC(FileFilter):
    """File extension filter for JFileChooser"""

    def __init__(self, ext):
        super(self.__class__, self).__init__()
        self.ext = "." + ext.upper()

    def getDescription(self):
        return "*" + self.ext  # noqa

    def accept(self, _theFile):  # noqa
        if _theFile is None:
            return False
        return _theFile.getName().upper().endswith(self.ext)


def setJFileChooserParameters(
    _jf,
    lPackagesT=None,
    lApplicationsT=None,
    lOptionsButton=None,
    lNewFolderButton=None,
):
    """sets up Client Properties for JFileChooser() to behave as required >> Mac only"""
    if not Platform.isOSX():
        return
    if not isinstance(_jf, JFileChooser):
        return

    _PKG = "JFileChooser.packageIsTraversable"
    _APP = "JFileChooser.appBundleIsTraversable"
    _OPTIONS = "JFileChooser.optionsPanelEnabled"
    _NEWFOLDER = "JFileChooser.canCreateDirectories"

    if lPackagesT is not None:
        _jf.putClientProperty(_PKG, lPackagesT)
    if lApplicationsT is not None:
        _jf.putClientProperty(_APP, lApplicationsT)
    if lOptionsButton is not None:
        _jf.putClientProperty(_OPTIONS, lOptionsButton)
    if lNewFolderButton is not None:
        _jf.putClientProperty(_NEWFOLDER, lNewFolderButton)


def setFileDialogParameters(lDefaults=False, lSelectDirectories=None, lPackagesT=None):
    """sets up System Properties for FileDialog() to behave as required >> Mac only"""
    if not Platform.isOSX():
        return

    _TRUE = "true"
    _FALSE = "false"

    _DIRS_FD = "apple.awt.fileDialogForDirectories"  # When True you can select a Folder (rather than a file)
    _PKGS_FD = "apple.awt.use-file-dialog-packages"  # When True allows you to select a 'bundle' as a file; False means navigate inside the bundle

    if lDefaults:
        System.setProperty(_DIRS_FD, _FALSE)
        System.setProperty(_PKGS_FD, _TRUE)
    else:
        if lSelectDirectories is not None:
            System.setProperty(_DIRS_FD, (_TRUE if lSelectDirectories else _FALSE))
        if lPackagesT is not None:
            System.setProperty(_PKGS_FD, (_TRUE if lPackagesT else _FALSE))


def get_file_from_file_chooser(
    parent,  # The Parent Frame, or None
    starting_dir,  # The Starting Dir
    filename,  # Default filename (or None)
    title,  # The Title (with FileDialog, only works on SAVE)
    multi_mode,  # Normally False (True has not been coded!)
    for_open,  # True for Open/Load, False for Save
    select_files,  # True for files, False for Directories
    ok_text=None,  # Normally None, unless set - use text
    file_filter_text=None,  # E.g. "txt" or "qif"
    force_jfc=False,
    force_fd=False,
    allow_traverse_packages=None,
    allow_traverse_applications=None,  # JFileChooser only..
    allow_new_folder_button=True,  # JFileChooser only..
    allow_options_button=None,
):  # JFileChooser only..
    """Launches FileDialog on Mac, or JFileChooser on other platforms... NOTE: Do not use Filter on Macs!"""
    if not starting_dir or not os.path.exists(starting_dir):
        starting_dir = MD_REF.getPreferences().getSetting("gen.data_dir", None)
        if starting_dir and not os.path.exists(starting_dir):
            starting_dir = None

    if (Platform.isOSX() and not force_jfc) or force_fd:
        setFileDialogParameters(
            lPackagesT=allow_traverse_packages,
            lSelectDirectories=(not select_files),
        )

        file_dialog = FileDialog(parent, title)
        file_dialog.setTitle(title)

        if starting_dir:
            file_dialog.setDirectory(starting_dir)
        if filename:
            file_dialog.setFile(filename)

        file_dialog.setMultipleMode(multi_mode)

        file_dialog.setMode(FileDialog.LOAD if for_open else FileDialog.SAVE)

        if file_filter_text and (not Platform.isOSX() or isOSXVersionMontereyOrLater()):
            file_dialog.setFilenameFilter(ExtFilenameFilter(file_filter_text))

        file_dialog.setVisible(True)

        setFileDialogParameters(lDefaults=True)

        if not multi_mode:
            filename = file_dialog.getFile()
            return os.path.join(file_dialog.getDirectory(), filename) if filename else None
        return [f.getAbsolutePath() for f in file_dialog.getFiles()]

    jfc = JFileChooser(starting_dir) if starting_dir else JFileChooser()

    if filename:
        jfc.setSelectedFile(File(filename))
    setJFileChooserParameters(
        jfc,
        lPackagesT=allow_traverse_packages,
        lApplicationsT=allow_traverse_applications,
        lNewFolderButton=allow_new_folder_button,
        lOptionsButton=allow_options_button,
    )

    jfc.setDialogTitle(title)
    jfc.setMultiSelectionEnabled(multi_mode)

    if select_files:
        jfc.setFileSelectionMode(JFileChooser.FILES_ONLY)  # FILES_ONLY, DIRECTORIES_ONLY, FILES_AND_DIRECTORIES
    else:
        jfc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)  # FILES_ONLY, DIRECTORIES_ONLY, FILES_AND_DIRECTORIES

    if file_filter_text and (not Platform.isOSX() or isOSXVersionMontereyOrLater()):
        jfc.setFileFilter(ExtFileFilterJFC(file_filter_text))

    if ok_text:
        return_value = jfc.showDialog(parent, ok_text)
    else:
        if for_open:
            return_value = jfc.showOpenDialog(parent)
        else:
            return_value = jfc.showSaveDialog(parent)

    if return_value == JFileChooser.CANCEL_OPTION:
        return None
    if not multi_mode:
        selected_file = jfc.getSelectedFile()
        if not selected_file or not selected_file.getName():
            return None

        return selected_file.getAbsolutePath()
    return [f.getAbsolutePath() for f in jfc.getSelectedFiles()]


# noinspection PyBroadException
def isOSXVersionAtLeast(compareVersion):
    # type: (str) -> bool
    """Pass a string in the format 'x.x.x'. Will check that this MacOSX version is at least that version. The 3rd micro number is optional"""

    if not Platform.isOSX():
        return False

    def to_tuple(convertString):
        convertString += ".0.0"
        return tuple([int(i) for i in convertString.split(".")][:3])

    return to_tuple(System.getProperty("os.version", "0.0.0")) >= to_tuple(compareVersion)


def isOSXVersionMontereyOrLater():
    return isOSXVersionAtLeast("12.0")


def get_home_dir():
    # noinspection PyBroadException
    try:
        if Platform.isOSX():
            home_dir = System.getProperty("UserHome")  # On a Mac in a Java VM, the homedir is hidden
        else:
            home_dir = os.path.expanduser("~") or System.getProperty("user.home") or os.environ.get("HOMEPATH")
    except:
        home_dir = ""

    return home_dir or MD_REF.getCurrentAccountBook().getRootFolder().getParent() or ""


def action(action_function):
    def inner(*args, **kwargs):
        class Action(AbstractAction):
            def __init__(self):
                super(self.__class__, self).__init__()
                self.args = args
                self.kwargs = kwargs

            def actionPerformed(self, _event):
                action_function(*self.args, **self.kwargs)

        return Action()

    return inner


# noinspection PyBroadException
def play_the_money_sound():
    # Seems to cause a crash on Virtual Machine with no Audio - so just in case....
    try:
        if MD_REF.getPreferences().getSetting("beep_on_transaction_change", "y") == "y":
            MD_REF.getUI().getSounds().playSound("cash_register.wav")
    except:
        pass


# noinspection PyBroadException
class SearchAction(AbstractAction):
    def __init__(self, theFrame, searchJText):
        super(self.__class__, self).__init__()
        self.theFrame = theFrame
        self.searchJText = searchJText
        self.lastSearch = ""
        self.lastPosn = -1
        self.previousEndPosn = -1
        self.lastDirection = 0

    def actionPerformed(self, _event):
        p = JPanel(FlowLayout())
        lbl = JLabel("Enter the search text:")
        tf = JTextField(self.lastSearch, 20)
        p.add(lbl)
        p.add(tf)

        tf.addAncestorListener(RequestFocusListener())

        _search_options = ["Next", "Previous", "Cancel"]

        default_direction = _search_options[self.lastDirection]

        response = JOptionPane.showOptionDialog(
            self.theFrame,
            p,
            "Search for text",
            JOptionPane.OK_CANCEL_OPTION,
            JOptionPane.QUESTION_MESSAGE,
            getMDIcon(None),
            _search_options,
            default_direction,
        )

        l_switch = False
        if response in (0, 1):
            if response != self.lastDirection:
                l_switch = True
            self.lastDirection = response
            search_what = tf.getText()
        else:
            search_what = None

        del p, lbl, tf, _search_options

        if not search_what:
            return

        text = self.searchJText.getText().lower()
        highlighter = self.searchJText.getHighlighter()
        highlighter.removeAllHighlights()

        start_pos = 0

        if response == 0:
            direction = "[forwards]"
            if search_what == self.lastSearch:
                start_pos = self.lastPosn
                if l_switch:
                    start_pos = start_pos + len(search_what) + 1
            self.lastSearch = search_what

            pos = text.find(search_what.lower(), start_pos)  # noqa
        else:
            direction = "[backwards]"
            end_pos = len(text) - 1

            if search_what == self.lastSearch:
                if self.previousEndPosn < 0:
                    self.previousEndPosn = len(text) - 1
                end_pos = max(0, self.previousEndPosn)
                if l_switch:
                    end_pos = max(0, self.lastPosn - 1)

            self.lastSearch = search_what

            pos = text.rfind(search_what.lower(), start_pos, end_pos)  # noqa

        if pos >= 0:
            self.searchJText.setCaretPosition(pos)
            try:
                highlighter.addHighlight(
                    pos,
                    min(pos + len(search_what), len(text)),
                    DefaultHighlighter.DefaultPainter,
                )
            except:
                pass
            if response == 0:
                self.lastPosn = pos + len(search_what)
                self.previousEndPosn = len(text) - 1
            else:
                self.lastPosn = pos - len(search_what)
                self.previousEndPosn = pos - 1
        else:
            self.lastPosn = 0
            self.previousEndPosn = len(text) - 1
            myPopupInformationBox(self.theFrame, "Searching %s text not found" % direction)


class RequestFocusListener(AncestorListener):
    """Add this Listener to a JTextField by using .addAncestorListener(RequestFocusListener()) before calling JOptionPane.showOptionDialog()"""

    def __init__(self, removeListener=True):
        super(self.__class__, self).__init__()
        self.removeListener = removeListener

    def ancestorAdded(self, e):
        component = e.getComponent()
        component.requestFocusInWindow()
        component.selectAll()
        if self.removeListener:
            component.removeAncestorListener(self)


# noinspection PyBroadException
def saveOutputFile(frame, title, default_filename, text):
    chooser_title = "Select location to save the current displayed output... (CANCEL=ABORT)"
    path = get_file_from_file_chooser(
        frame,  # Parent frame or None
        get_home_dir(),  # Starting path
        default_filename,  # Default Filename
        chooser_title,  # Title
        False,  # Multi-file selection mode
        False,  # True for Open/Load, False for Save
        True,  # True = Files, else Dirs
        None,  # Load/Save button text, None for defaults
        "txt",  # File filter (non Mac only). Example: "txt" or "qif"
        allow_traverse_packages=False,
        force_fd=True,
        allow_new_folder_button=True,
        allow_options_button=True,
    )

    if not path:
        return
    elif not safeStr(path).endswith(".txt"):
        myPopupInformationBox(frame, "Sorry - please use a .txt file extension when saving output txt")
        return
    elif ".moneydance" in os.path.dirname(path):
        myPopupInformationBox(
            frame,
            "Sorry, please choose a location outside of the Moneydance location",
        )
        return

    if not check_file_writable(path):
        myPopupInformationBox(
            frame,
            "Sorry, that file/location does not appear allowed by the operating system!?",
        )

    try:
        with open(path, "w") as f:
            f.write(text)
        myPrint("B", "%s: text output copied to: %s" % (title, path))

        play_the_money_sound()
        txt = "%s: Output text saved as requested to: %s" % (title, path)
        setDisplayStatus(txt, "B")
        myPopupInformationBox(frame, txt)
    except:
        txt = "ERROR - failed to write output text to file: %s" % path
        dump_sys_error_to_md_console_and_errorlog()
        myPopupInformationBox(frame, txt)


GlobalVars.defaultPrintFontSize = 12

####################################################################################################################
# PRINTING UTILITIES...: Points to MM, to Inches, to Resolution: Conversion routines etc
_IN2MM = 25.4
_IN2CM = 2.54
_IN2PT = 72


def pt2dpi(_pt, _resolution):
    return _pt * _resolution / _IN2PT


def mm2pt(_mm):
    return _mm * _IN2PT / _IN2MM


def mm2mpt(_mm):
    return _mm * 1000 * _IN2PT / _IN2MM


def pt2mm(_pt):
    return round(_pt * _IN2MM / _IN2PT, 1)


def mm2in(_mm):
    return _mm / _IN2MM


def in2mm(_in):
    return _in * _IN2MM


def in2mpt(_in):
    return _in * _IN2PT * 1000


def in2pt(_in):
    return _in * _IN2PT


def mpt2in(_mpt):
    return _mpt / _IN2PT / 1000


def mm2px(_mm, _resolution):
    return mm2in(_mm) * _resolution


def mpt2px(_mpt, _resolution):
    return mpt2in(_mpt) * _resolution


def printDeducePrintableWidth(page_format, printer_attributes):

    _BUFFER_PCT = 0.95

    if printer_attributes.get(standard.MediaSizeName):
        myPrint(
            "DB",
            "Requested Media: %s" % (printer_attributes.get(standard.MediaSizeName)),
        )

    if not printer_attributes.get(standard.MediaPrintableArea):
        raise Exception("ERROR: MediaPrintableArea not present in printer attributes!?")

    printable_area = printer_attributes.get(standard.MediaPrintableArea)

    if page_format.getOrientation() == page_format.PORTRAIT:
        deduced_width_mm = printable_area.getWidth(standard.MediaPrintableArea.MM)
    elif page_format.getOrientation() == page_format.LANDSCAPE:
        deduced_width_mm = printable_area.getHeight(standard.MediaPrintableArea.MM)
    else:
        raise Exception("ERROR: page_format.getOrientation() was not PORTRAIT or LANDSCAPE!?")

    _maxPaperWidthPTS = mm2px(deduced_width_mm, GlobalVars.defaultDPI)
    _maxPaperWidthPTS_buff = _maxPaperWidthPTS * _BUFFER_PCT

    return deduced_width_mm, _maxPaperWidthPTS, _maxPaperWidthPTS_buff


def loadDefaultPrinterAttributes(printer_attributes=None):

    if printer_attributes is None:
        printer_attributes = attribute.HashPrintRequestAttributeSet()
    else:
        printer_attributes.clear()

    # Refer: https://docs.oracle.com/javase/7/docs/api/javax/print/attribute/standard/package-summary.html
    printer_attributes.add(standard.DialogTypeSelection.NATIVE)
    if GlobalVars.defaultPrintLandscape:
        printer_attributes.add(standard.OrientationRequested.LANDSCAPE)
    else:
        printer_attributes.add(standard.OrientationRequested.PORTRAIT)
    printer_attributes.add(standard.Chromaticity.MONOCHROME)
    printer_attributes.add(standard.JobSheets.NONE)
    printer_attributes.add(standard.Copies(1))
    printer_attributes.add(standard.PrintQuality.NORMAL)

    return printer_attributes


# noinspection PyBroadException
def printOutputFile(_callingClass=None, _theTitle=None, _theJText=None, _theString=None):

    # Possible future modification, leverage MDPrinter, and it's classes / methods to save/load preferences and create printers
    try:
        if _theJText is None and _theString is None:
            return
        if _theJText is not None and len(_theJText.getText()) < 1:
            return
        if _theString is not None and len(_theString) < 1:
            return

        # Make a new one for printing
        if _theJText is not None:
            print_text_area = JTextArea(_theJText.getText())
        else:
            print_text_area = JTextArea(_theString)

        print_text_area.setEditable(False)
        print_text_area.setLineWrap(
            True
        )  # As we are reducing the font size so that the width fits the page width, this forces any remainder to wrap
        # if _callingClass is not None: print_text_area.setLineWrap(_callingClass.lWrapText)  # Mirror the word wrap set by user
        print_text_area.setWrapStyleWord(False)
        print_text_area.setOpaque(False)
        print_text_area.setBackground(Color(0, 0, 0, 0))
        print_text_area.setForeground(Color.BLACK)
        print_text_area.setBorder(EmptyBorder(0, 0, 0, 0))

        try:
            if "MD_REF" in globals():
                use_print_font_size = MD_REF.getUI().getFonts().print.getSize()
            elif "moneydance" in globals():
                use_print_font_size = moneydance.getUI().getFonts().print.getSize()
            else:
                use_print_font_size = (
                    GlobalVars.defaultPrintFontSize
                )  # Just in case cleanup_references() has tidied up once script ended
        except:
            use_print_font_size = 12  # Font print did not exist before build 3036

        font_to_use = getMonoFont()  # Need Monospaced font, but with the font set in MD preferences for print
        font_to_use = font_to_use.deriveFont(float(use_print_font_size))
        print_text_area.setFont(font_to_use)

        # noinspection PyBroadException
        def computeFontSize(_theComponent, _maxPaperWidth, _dpi):

            # Auto shrink font so that text fits on one line when printing
            # Note: Java seems to operate its maths at 72DPI (so must factor that into the maths)
            try:
                _DEFAULT_MIN_WIDTH = mm2px(100, _dpi)  # 100MM
                _minFontSize = 5  # Below 5 too small
                text = _theComponent.getText()
                _startingComponentFont = _theComponent.getFont()

                if not text or len(text) < 1:
                    return -1

                fm = _theComponent.getFontMetrics(_startingComponentFont)
                _maxFontSize = (
                    current_font_size
                ) = (
                    _startingComponentFont.getSize()
                )  # Max out at the MD default for print font size saved in preferences

                max_line_width_in_file = _DEFAULT_MIN_WIDTH
                longest_line = ""
                for line in text.split("\n"):  # Look for the widest line adjusted for font style
                    _w = pt2dpi(fm.stringWidth(line), _dpi)
                    if _w > max_line_width_in_file:
                        longest_line = line
                        max_line_width_in_file = _w

                # Now shrink the font size to fit.....
                while pt2dpi(fm.stringWidth(longest_line) + 5, _dpi) > _maxPaperWidth:
                    current_font_size -= 1
                    fm = _theComponent.getFontMetrics(
                        Font(
                            _startingComponentFont.getName(),
                            _startingComponentFont.getStyle(),
                            current_font_size,
                        )
                    )
                    if current_font_size < _minFontSize:
                        myPrint(
                            "DB",
                            "... calculating... Next font size is too small... exiting the reduction loop...",
                        )
                        break

                if not Platform.isMac():
                    current_font_size -= 1  # For some reason, sometimes on Linux/Windows still too big....
                    myPrint(
                        "DB",
                        "..knocking 1 off font size for good luck...! Now: %s" % current_font_size,
                    )

                current_font_size = max(_minFontSize, current_font_size)
                current_font_size = min(_maxFontSize, current_font_size)

            except:
                myPrint("B", "ERROR: computeFontSize() crashed?")
                dump_sys_error_to_md_console_and_errorlog()
                return -1
            return current_font_size

        printer_job = PrinterJob.getPrinterJob()

        if GlobalVars.defaultPrintService is not None:
            printer_job.setPrintService(GlobalVars.defaultPrintService)

        if GlobalVars.defaultPrinterAttributes is not None:
            printer_attributes = attribute.HashPrintRequestAttributeSet(GlobalVars.defaultPrinterAttributes)
        else:
            printer_attributes = loadDefaultPrinterAttributes(None)

        printer_attributes.remove(standard.JobName)
        printer_attributes.add(standard.JobName("%s: %s" % (myModuleID.capitalize(), _theTitle), None))

        if GlobalVars.defaultDPI != 72:
            printer_attributes.remove(standard.PrinterResolution)
            printer_attributes.add(
                standard.PrinterResolution(
                    GlobalVars.defaultDPI,
                    GlobalVars.defaultDPI,
                    standard.PrinterResolution.DPI,
                )
            )

        if not printer_job.printDialog(printer_attributes):
            return

        page_format = printer_job.getPageFormat(printer_attributes)

        # .setPrintable() seems to modify printer_attributes & adds MediaPrintableArea. Do this before printDeducePrintableWidth()
        header = MessageFormat(_theTitle)
        footer = MessageFormat("- page {0} -")
        printer_job.setPrintable(print_text_area.getPrintable(header, footer), page_format)  # Yes - we do this twice

        (
            deduced_width_mm,
            maxPaperWidthPTS,
            maxPaperWidthPTS_buff,
        ) = printDeducePrintableWidth(page_format, printer_attributes)

        if _callingClass is None or not _callingClass.lWrapText:

            new_font_size = computeFontSize(print_text_area, int(maxPaperWidthPTS), GlobalVars.defaultDPI)

            if new_font_size > 0:
                font_to_use = font_to_use.deriveFont(float(new_font_size))
                print_text_area.setFont(font_to_use)

        # Yup - calling .setPrintable() twice - before and after .computeFontSize()
        printer_job.setPrintable(print_text_area.getPrintable(header, footer), page_format)
        eval("printer_job.print(printer_attributes)")

        del print_text_area

        GlobalVars.defaultPrinterAttributes = attribute.HashPrintRequestAttributeSet(printer_attributes)
        GlobalVars.defaultPrintService = printer_job.getPrintService()

    except:
        myPrint("B", "ERROR in printing routines.....:")
        dump_sys_error_to_md_console_and_errorlog()
    return


def pageSetup():
    pj = PrinterJob.getPrinterJob()

    if GlobalVars.defaultPrinterAttributes is not None:
        printer_attributes = attribute.HashPrintRequestAttributeSet(GlobalVars.defaultPrinterAttributes)
    else:
        printer_attributes = loadDefaultPrinterAttributes(None)

    if not pj.pageDialog(printer_attributes):
        return
    GlobalVars.defaultPrinterAttributes = attribute.HashPrintRequestAttributeSet(printer_attributes)


# noinspection PyBroadException
def isMacDarkModeDetected():
    dark_response = "LIGHT"
    if Platform.isOSX():
        try:
            dark_response = subprocess.check_output("defaults read -g AppleInterfaceStyle", shell=True)
            dark_response = dark_response.strip().lower()
        except:
            pass
    return "dark" in dark_response


def getColorBlue():
    if not isMDThemeDark() and not isMacDarkModeDetected():
        return Color.BLUE
    return MD_REF.getUI().getColors().defaultTextForeground


def getColorRed():
    return MD_REF.getUI().getColors().errorMessageForeground


def getColorDarkGreen():
    return MD_REF.getUI().getColors().budgetHealthyColor


# noinspection PyBroadException
def isMDThemeDark():
    try:
        current_theme = MD_REF.getUI().getCurrentTheme()
        try:
            if current_theme.isSystemDark():
                return True  # NOTE: Only VAQua has isSystemDark()
        except:
            pass
        if "dark" in current_theme.getThemeID().lower():
            return True
        if isMDThemeFlatDark():
            return True
        if isMDThemeDarcula():
            return True
    except:
        pass
    return False


# noinspection PyBroadException
def is_moneydance_theme(name):
    # type: (str) -> bool
    try:
        return name in MD_REF.getUI().getCurrentTheme().getThemeID()
    except:
        return False


# noinspection PyBroadException
def isMDThemeDarcula():
    return not isMDThemeFlatDark() and is_moneydance_theme("darcula")


# noinspection PyBroadException
def isMDThemeCustomizable():
    try:
        return MD_REF.getUI().getCurrentTheme().isCustomizable()
    except:
        return False


# noinspection PyBroadException
def isMDThemeHighContrast():
    return is_moneydance_theme("high_contrast")


# noinspection PyBroadException
def isMDThemeDefault():
    return is_moneydance_theme("default")


# noinspection PyBroadException
def isMDThemeClassic():
    return is_moneydance_theme("classic")


# noinspection PyBroadException
def isMDThemeSolarizedLight():
    return is_moneydance_theme("solarized_light")


# noinspection PyBroadException
def isMDThemeSolarizedDark():
    return is_moneydance_theme("solarized_dark")


# noinspection PyBroadException
def isMDThemeFlatDark():
    try:
        current_theme = MD_REF.getUI().getCurrentTheme()
        return "flat dark" in current_theme.toString().lower()
    except:
        return False


# noinspection PyBroadException
def isMDThemeVAQua():
    if Platform.isOSX():
        try:
            current_theme = MD_REF.getUI().getCurrentTheme()
            return ".vaqua" in safeStr(current_theme.getClass()).lower()
        except:
            pass
    return False


def isIntelX86_32bit():
    """Detect Intel x86 32bit system"""
    return System.getProperty("os.arch", "null").strip().lower() == "x86"


def getMDIcon(startingIcon=None, lAlwaysGetIcon=False):
    if lAlwaysGetIcon or isIntelX86_32bit():
        return MD_REF.getUI().getIcon("/com/moneydance/apps/md/view/gui/glyphs/appicon_64.png")
    return startingIcon


class SetupMDColors:
    OPAQUE = None
    FOREGROUND = None
    FOREGROUND_REVERSED = None
    BACKGROUND = None
    BACKGROUND_REVERSED = None

    @classmethod
    def updateUI(cls):
        cls.OPAQUE = False

        cls.FOREGROUND = GlobalVars.CONTEXT.getUI().getColors().defaultTextForeground
        cls.FOREGROUND_REVERSED = SetupMDColors.FOREGROUND

        cls.BACKGROUND = GlobalVars.CONTEXT.getUI().getColors().defaultBackground
        cls.BACKGROUND_REVERSED = cls.BACKGROUND

        if (not isMDThemeVAQua() and not isMDThemeDark() and isMacDarkModeDetected()) or (
            not isMacDarkModeDetected() and isMDThemeDarcula()
        ):
            cls.FOREGROUND_REVERSED = GlobalVars.CONTEXT.getUI().colors.defaultBackground
            cls.BACKGROUND_REVERSED = GlobalVars.CONTEXT.getUI().colors.defaultTextForeground


# noinspection PyBroadException
class GetFirstMainFrame:
    DEFAULT_MAX_WIDTH = 1024
    DEFAULT_MAX_HEIGHT = 768

    @classmethod
    def getSize(cls, default_width=None, default_height=None):
        if default_width is None:
            default_width = cls.DEFAULT_MAX_WIDTH
        if default_height is None:
            default_height = cls.DEFAULT_MAX_HEIGHT
        try:
            first_main_frame = MD_REF.getUI().firstMainFrame
            return first_main_frame.getSize()
        except:
            pass
        return Dimension(default_width, default_height)

    @staticmethod
    def getSelectedAccount():
        try:
            return MD_REF.getUI().firstMainFrame.getSelectedAccount()
        except:
            return None


class ActionButton(JButton):
    def __init__(self, text, action_listener, tooltip=""):
        # type: (str, Union[AbstractAction, Callable], str) -> None
        super(self.__class__, self).__init__(text)
        self.setOpaque(SetupMDColors.OPAQUE)
        self.setBackground(SetupMDColors.BACKGROUND)
        self.setForeground(SetupMDColors.FOREGROUND)
        if isinstance(action_listener, AbstractAction):
            self.addActionListener(action_listener)
        else:

            @action
            def _action():
                action_listener()

            self.addActionListener(_action())
        if tooltip:
            self.setToolTipText(tooltip)


class FrameController(Runnable):
    def __init__(
        self,
        title,
        output,
        problems="",
        lAlertLevel=0,
        copyToClipboard=False,
        lJumpToEnd=False,
        lWrapText=True,
        screenLocation=None,
        lAutoSize=False,
    ):
        super(self.__class__, self).__init__()
        self.title = title
        self.output = output
        self.problems = problems
        self.lAlertLevel = lAlertLevel
        self.copyToClipboard = copyToClipboard
        self.lJumpToEnd = lJumpToEnd
        self.lWrapText = lWrapText
        self.screenLocation = screenLocation
        self.lAutoSize = lAutoSize
        self.returnFrame = None

    def show(self):
        if not SwingUtilities.isEventDispatchThread():
            SwingUtilities.invokeAndWait(self)
        else:
            self.run()
        return self.returnFrame

    def run(self):  # noqa
        screen_size = Toolkit.getDefaultToolkit().getScreenSize()
        frame_width = min(
            screen_size.width - 20,
            max(
                GetFirstMainFrame.DEFAULT_MAX_WIDTH,
                int(round(GetFirstMainFrame.getSize().width * 0.9, 0)),
            ),
        )
        frame_height = min(
            screen_size.height - 20,
            max(
                GetFirstMainFrame.DEFAULT_MAX_HEIGHT,
                int(round(GetFirstMainFrame.getSize().height * 0.9, 0)),
            ),
        )

        # JFrame.setDefaultLookAndFeelDecorated(True)   # Note: Darcula Theme doesn't like this and seems to be OK without this statement...
        extra_text = ""

        internal_jframe = MyJFrame(
            self.title + " (%s+F to find/search for text)%s" % (MD_REF.getUI().ACCELERATOR_MASK_STR, extra_text)
        )
        internal_jframe.setName("%s_quickjframe" % myModuleID)

        if not Platform.isOSX():
            internal_jframe.setIconImage(MDImages.getImage(MD_REF.getSourceInformation().getIconResource()))

        internal_jframe.setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE)
        internal_jframe.setResizable(True)

        shortcut = Toolkit.getDefaultToolkit().getMenuShortcutKeyMaskEx()

        # noinspection PyArgumentList
        internal_jframe.getRootPane().getInputMap(JComponent.WHEN_ANCESTOR_OF_FOCUSED_COMPONENT).put(
            KeyStroke.getKeyStroke(KeyEvent.VK_W, shortcut), "close-window"
        )
        # noinspection PyArgumentList
        internal_jframe.getRootPane().getInputMap(JComponent.WHEN_ANCESTOR_OF_FOCUSED_COMPONENT).put(
            KeyStroke.getKeyStroke(KeyEvent.VK_F4, shortcut), "close-window"
        )
        # noinspection PyArgumentList
        internal_jframe.getRootPane().getInputMap(JComponent.WHEN_ANCESTOR_OF_FOCUSED_COMPONENT).put(
            KeyStroke.getKeyStroke(KeyEvent.VK_F, shortcut), "search-window"
        )
        # noinspection PyArgumentList
        internal_jframe.getRootPane().getInputMap(JComponent.WHEN_ANCESTOR_OF_FOCUSED_COMPONENT).put(
            KeyStroke.getKeyStroke(KeyEvent.VK_P, shortcut), "print-me"
        )
        # noinspection PyArgumentList
        internal_jframe.getRootPane().getInputMap(JComponent.WHEN_IN_FOCUSED_WINDOW).put(
            KeyStroke.getKeyStroke(KeyEvent.VK_ESCAPE, 0), "close-window"
        )

        text_area = JTextArea(self.output)
        text_area.setEditable(False)
        text_area.setLineWrap(self.lWrapText)
        text_area.setWrapStyleWord(False)
        text_area.setFont(getMonoFont())

        @action
        def close_action(theFrame):
            # noinspection PyBroadException
            try:
                if not SwingUtilities.isEventDispatchThread():
                    SwingUtilities.invokeLater(GenericDisposeRunnable(theFrame))
                else:
                    theFrame.dispose()
            except:
                dump_sys_error_to_md_console_and_errorlog()

        @action
        def printAction(theCallingClass, theJText, theTitle=""):
            printOutputFile(
                _callingClass=theCallingClass,
                _theTitle=theTitle,
                _theJText=theJText,
            )

        print_action = printAction(self, text_area, self.title)
        internal_jframe.getRootPane().getActionMap().put("close-window", close_action(internal_jframe))
        internal_jframe.getRootPane().getActionMap().put("search-window", SearchAction(internal_jframe, text_area))
        internal_jframe.getRootPane().getActionMap().put(
            "print-me",
            print_action,
        )

        class WindowListener(WindowAdapter):
            def __init__(self, theFrame):
                self.theFrame = theFrame
                self.saveMD_REF = MD_REF

            def windowClosing(self, _event):
                self.theFrame.dispose()

        internal_jframe.addWindowListener(WindowListener(internal_jframe))

        internal_scroll_pane = JScrollPane(
            text_area,
            JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,
            JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED,
        )

        if self.lAlertLevel >= 2:
            text_area.setBackground(Color.RED)
            text_area.setForeground(Color.BLACK)
            text_area.setOpaque(True)
        elif self.lAlertLevel >= 1:
            text_area.setBackground(Color.GREEN)
            text_area.setForeground(Color.BLACK)
            text_area.setOpaque(True)

        if not self.lAutoSize:
            internal_jframe.setPreferredSize(Dimension(frame_width, frame_height))

        SetupMDColors.updateUI()

        print_button = ActionButton(
            "Print",
            print_action,
            tooltip="Prints the output displayed in this window to your printer",
        )

        if GlobalVars.defaultPrinterAttributes is None:
            print_page_setup = ActionButton(
                "Page Setup",
                lambda: pageSetup(),
                tooltip="Printer Page Setup",
            )

        save_button = ActionButton(
            "Save to file",
            lambda: saveOutputFile(
                internal_jframe,
                "QUICKJFRAME",
                "%s_output.txt" % myModuleID,
                self.output,
            ),
            tooltip="Saves the output displayed in this window to a file",
        )

        @action
        def toggle_wrap(calling_class, _text_area):
            calling_class.lWrapText = not calling_class.lWrapText
            _text_area.setLineWrap(calling_class.lWrapText)

        wrap_option = JCheckBox("Wrap Contents (Screen & Print)", self.lWrapText)
        wrap_option.addActionListener(toggle_wrap(self, text_area))
        wrap_option.setForeground(SetupMDColors.FOREGROUND_REVERSED)
        wrap_option.setBackground(SetupMDColors.BACKGROUND_REVERSED)

        top_button = ActionButton("Top", lambda: text_area.setCaretPosition(0))
        bottom_button = ActionButton("Bottom", lambda: text_area.setCaretPosition(text_area.getDocument().getLength()))

        if self.problems:
            show_problems_button = ActionButton("Show Problems", lambda: show_problems(self.problems))
        else:
            show_problems_button = None

        close_button = ActionButton("Close", close_action(internal_jframe))

        if Platform.isOSX():
            save_use_screen_menu_bar = System.getProperty("apple.laf.useScreenMenuBar")
            if save_use_screen_menu_bar is None or save_use_screen_menu_bar == "":
                save_use_screen_menu_bar = System.getProperty("com.apple.macos.useScreenMenuBar")
            System.setProperty("apple.laf.useScreenMenuBar", "false")
            System.setProperty("com.apple.macos.useScreenMenuBar", "false")
        else:
            save_use_screen_menu_bar = "true"

        mb = JMenuBar()
        mb.setBorder(EmptyBorder(0, 0, 0, 0))
        mb.add(Box.createRigidArea(Dimension(10, 0)))
        mb.add(top_button)
        mb.add(Box.createRigidArea(Dimension(10, 0)))
        mb.add(bottom_button)
        mb.add(Box.createHorizontalGlue())
        mb.add(wrap_option)

        if GlobalVars.defaultPrinterAttributes is None:
            mb.add(Box.createRigidArea(Dimension(10, 0)))
            mb.add(print_page_setup)  # noqa

        mb.add(Box.createHorizontalGlue())
        mb.add(print_button)
        mb.add(Box.createRigidArea(Dimension(10, 0)))
        mb.add(save_button)
        if show_problems_button is not None:
            mb.add(Box.createRigidArea(Dimension(10, 0)))
            mb.add(show_problems_button)
        mb.add(Box.createRigidArea(Dimension(10, 0)))
        mb.add(close_button)
        mb.add(Box.createRigidArea(Dimension(30, 0)))

        internal_jframe.setJMenuBar(mb)

        internal_jframe.add(internal_scroll_pane)

        internal_jframe.pack()
        if self.screenLocation and isinstance(self.screenLocation, Point):
            internal_jframe.setLocation(self.screenLocation)
        else:
            internal_jframe.setLocationRelativeTo(None)

        internal_jframe.setVisible(True)

        if Platform.isOSX():
            System.setProperty("apple.laf.useScreenMenuBar", save_use_screen_menu_bar)
            System.setProperty("com.apple.macos.useScreenMenuBar", save_use_screen_menu_bar)

        if "errlog.txt" in self.title or self.lJumpToEnd:
            text_area.setCaretPosition(text_area.getDocument().getLength())

        # noinspection PyBroadException
        try:
            if self.copyToClipboard:
                Toolkit.getDefaultToolkit().getSystemClipboard().setContents(StringSelection(self.output), None)
        except:
            myPrint("J", "Error copying contents to Clipboard")
            dump_sys_error_to_md_console_and_errorlog()

        self.returnFrame = internal_jframe


def show_problems(document):
    document = (
        "Problems are grouped and sorted by the frequency of the first word.\n"
        "Then we show the online description to match against, followed by the list of transactions with that description.\n\n"
        + document
    )
    FrameController(
        "Unknown Transactions",
        document,
        lAlertLevel=2,
        lWrapText=False,
        lAutoSize=True,
    ).show()


# ############# END OF ADDITIONS ########################################################################################
# ############# END OF ADDITIONS ########################################################################################
# ############# END OF ADDITIONS ########################################################################################


# Change this to True to install as an extension. Then you will need to choose
# Extensions -> Fix Downloaded Transactions from the menu.
# Since this extension is not signed, it must be installed whenever you restart
# MoneyDance, so you may not find this very useful.
INSTALL_EXTENSION = False

# Location of CSV files with replacements.
# Note: At the time of this writing, all CSVs must be in your Downloads folder
#       due to security issues.
# If you leave this empty, you will be prompted for a single CSV file.
CSV_FILE_NAMES = []

# Common unicode patterns used by spreadsheets with ASCII replacements
UNICODE_REPLACEMENTS = {
    "\xe2\x80\x99": "'",
}

# Many credit card descriptions begin with a prefix and a "*", such as "SQ *"
# for Square. List all such prefixes that you would like to automatically
# remove before any further processing. Do not include spaces or "*".
PREFIXES_TO_STRIP = {"CKE", "EV", "PY", "SP", "SQ", "TST"}

# The following fields are required in each CSV file, and must be in the first
# row of the CSV. They can be in any order.
REQUIRED_FIELDS = {
    "account_type",
    "account_name",
    "category",
    "replacement",
    "exact_match",
    "starts_with",
    "memo_contains",
    "amount",
    "amount_below",
    "amount_above",
    "skip_confirm",
}


# ClearedStatus = AbstractTxn.ClearedStatus
class ClearedStatus(object):
    CLEARED = "CLEARED"
    RECONCILING = "RECONCILING"
    UNRECONCILED = "UNRECONCILED"
    ALL = (CLEARED, RECONCILING, UNRECONCILED)


# AccountType = Account.AccountType
class AccountType(object):
    ASSET = "ASSET"
    BANK = "BANK"
    CREDIT_CARD = "CREDIT_CARD"
    EXPENSE = "EXPENSE"
    INCOME = "INCOME"
    INVESTMENT = "INVESTMENT"
    LIABILITY = "LIABILITY"
    LOAN = "LOAN"
    ROOT = "ROOT"
    SECURITY = "SECURITY"
    ALL = (
        ASSET,
        BANK,
        CREDIT_CARD,
        EXPENSE,
        INCOME,
        INVESTMENT,
        LIABILITY,
        LOAN,
        ROOT,
        SECURITY,
    )


# BalanceType = Account.BalanceType
class BalanceType(object):
    CLEARED = "CLEARED"
    CONFIRMED = "CONFIRMED"
    CURRENT = "CURRENT"
    NORMAL = "NORMAL"
    UNCONFIRMED = "UNCONFIRMED"
    ALL = (CLEARED, CONFIRMED, CURRENT, NORMAL, UNCONFIRMED)


def strip_prefixes(s):
    # type: (str) -> str
    """Remove common description prefixes."""
    prefix, _, message = s.partition("*")
    if message and prefix.strip() in PREFIXES_TO_STRIP:
        return message.strip()
    return s


def first_word(s):
    # type: (str) -> str
    """Get the first word to use as a key."""
    for separator in (" ", "*", ".", "-", "/"):
        s = s.partition(separator)[0]
    return s.upper()


def remove_extra_spaces(s):
    # type: (str) -> str
    """Replace series of spaces with single spaces."""
    return " ".join(s.split())


def fix_unicode(s):
    # type: (str) -> str
    """Replace unicode patterns commonly used by spreadsheets with ASCII."""
    for uni, replacement in UNICODE_REPLACEMENTS.items():
        s = s.replace(uni, replacement)
    return s


_found_accounts = {}  # type: Dict[str, Account]


def find_account(account):
    # type: (str) -> Optional[Account]
    if not account:
        return None
    result = _found_accounts.get(account)
    if result:
        return result
    result = moneydance.getCurrentAccountBook().getRootAccount().getAccountByName(account)
    _found_accounts[account] = result
    return result


class Transaction(object):
    """Wrapper for the Java transaction object that makes it more Pythonic."""

    _category = None
    _original_category = None
    _description = None
    _original_description = None
    _is_new = None
    _original_is_new = None

    def __init__(self, txn):
        # type: (ParentTxn) -> None
        self._txn = txn
        self._dollars = None
        self._memo = None

    @property
    def account(self):
        # type: () -> Account
        return self._txn.getAccount()

    @property
    def amount(self):
        # type: () -> float
        return float(self._txn.getValue()) / 100.0

    @property
    def category(self):
        # type: () -> Account
        if self._original_category is None:
            self._original_category = self._txn.getSplit(0).getAccount() if self._txn.getSplitCount() == 1 else None
            self._category = self._original_category
        return self._category

    @category.setter
    def category(self, value):
        # type: (Union[str, Account]) -> None
        if isinstance(value, str):
            value = find_account(value)
        if str(self.category) != str(value):
            self._category = value

    @property
    def dateint(self):
        # type: () -> int
        return self._txn.getDateInt()

    @property
    def description(self):
        # type: () -> str
        if self._original_description is None:
            self._original_description = remove_extra_spaces(strip_prefixes(self._txn.getDescription()))
            self._description = self._original_description
        return self._description

    @description.setter
    def description(self, value):
        # type: (str) -> None
        if self.description != value:
            self._description = value

    @property
    def online_description(self):
        # type: () -> str
        return remove_extra_spaces(strip_prefixes(self._txn.getOriginalOnlineTxn().getName()))

    @property
    def first_word(self):
        # type: () -> str
        return first_word(self.online_description)

    @property
    def dollars(self):
        # type: () -> str
        if self._dollars is None:
            # noinspection PyTypeChecker
            currency_type = self.account.getCurrencyType()
            # noinspection PyTypeChecker
            self._dollars = currency_type.formatFancy(self._txn.getValue(), ".")
        return self._dollars

    @property
    def is_new(self):
        # type: () -> bool
        if self._original_is_new is None:
            self._original_is_new = self._txn.isNew()
            self._is_new = self._original_is_new
        return self._is_new

    @is_new.setter
    def is_new(self, value):
        # type: (bool) -> None
        if self.is_new != value:
            self._is_new = value

    @property
    def memo(self):
        # type: () -> str
        if self._memo is None:
            self._memo = self._txn.getMemo()
        return self._memo

    def sync(self):
        # type: () -> None
        needs_sync = False
        self._txn.setEditingMode()  # SCB
        if self._description != self._original_description:
            self._txn.setEditingMode()  # SCB
            self._txn.setDescription(self._description)
            needs_sync = True
        if self._is_new != self._original_is_new:
            self._txn.setEditingMode()  # SCB
            self._txn.setIsNew(self._is_new)
            needs_sync = True
        if self._original_category != self._category:
            self._txn.setEditingMode()  # SCB
            self._txn.getSplit(0).setAccount(self._category)
            needs_sync = True
        if needs_sync:
            self._txn.getParentTxn().syncItem()

    def __str__(self):
        # type: () -> str
        return self.summary()

    @property
    def is_modified(self):
        # type: () -> bool
        return (
            self.description != self._original_description
            or self.is_new != self._original_is_new
            or self.category != self._original_category
        )

    def changes(self):
        # type: () -> List[str]
        changes = []  # type: List[str]
        if self.description != self._original_description:
            changes.append("description: {} -> {}".format(self._original_description, self.description))
        if self.category != self._original_category:
            changes.append("category: {} -> {}".format(self._original_category, self.category))
        if self.is_new != self._original_is_new:
            changes.append("confirmed: {}".format("True" if self._original_is_new else "False"))
        return changes

    def summary(self, original=False):
        # type: (bool) -> str
        is_new = self.is_new
        desc = self.description
        cat = self.category
        if original:
            is_new = self._original_is_new
            desc = self._original_description
            cat = self._original_category
        return '%s%u: %s - %s (%s, %s) online: "%s" memo: "%s"' % (
            "*" if is_new else "",
            self.dateint,
            desc,
            self.dollars,
            self.account,
            cat,
            self.online_description,
            self.memo,
        )

    def change_summary(self):  # type: () -> str
        dateint_str = "%u" % self.dateint
        date_str = "{}-{}-{}".format(dateint_str[:4], dateint_str[4:6], dateint_str[6:8])
        lines = ["{} {} - {} ({})".format(date_str, self.description, self.dollars, self.category)]
        for change in self.changes():
            lines.append("- {}".format(change))
        return "\n".join(lines)


class FixerError(RuntimeError):
    def __init__(self, message):
        super(FixerError, self).__init__()
        self.message = message


class Fixer(object):
    def __init__(
        self,
        replacement,
        exact_match="",
        starts_with="",
        memo_contains="",
        amount=0.0,
        amount_below=0.0,
        amount_above=0.0,
        category="",
        skip_confirm=False,
    ):
        # type: (str, str, str, str, float, float, float, str, bool) -> None
        self.replacement = replacement
        if not exact_match and not starts_with:
            starts_with = replacement
        self.exact_match = remove_extra_spaces(strip_prefixes(exact_match.upper()))
        self.starts_with = strip_prefixes(starts_with.upper())
        self.memo_contains = memo_contains.upper()
        self.amount = float(amount) if amount else 0.0
        self.amount_below = float(amount_below) if amount_below else 0.0
        self.amount_above = float(amount_above) if amount_above else 0.0
        self.category = find_account(category) if category else None
        self.confirm = not skip_confirm
        if category and not self.category:
            raise FixerError('Could not find category "{}"'.format(category))

    def check_replacement(self, txn, check_starts_with=True):
        # type: (Transaction, bool) -> bool
        if check_starts_with and self.starts_with:
            matched = txn.online_description.upper().startswith(self.starts_with) or (
                self.exact_match and txn.online_description.upper() == self.exact_match
            )
            if not matched:
                return False
        if self.memo_contains and self.memo_contains not in txn.memo.upper():
            return False
        if self.amount and txn.amount != self.amount:
            return False
        if self.amount_above and txn.amount < self.amount_above:
            return False
        if self.amount_below and txn.amount > self.amount_below:
            return False
        return True

    def fix(self, txn, save_changes=False, check_starts_with=True):
        # type: (Transaction, bool, bool) -> bool
        if not self.check_replacement(txn, check_starts_with):
            return False
        txn.description = self.replacement
        if self.confirm:
            txn.is_new = False
        if self.category:
            txn.category = self.category
        if save_changes:
            txn.sync()
        return True

    @property
    def first_word(self):
        # type: () -> str
        return first_word(self.starts_with)


class FixerGroup(object):
    def __init__(self):
        # type: () -> None
        self.exact_matches = {}  # type: Dict[str, List[Fixer]]
        self.starts_with = {}  # type: Dict[str, List[Fixer]]

    def add(self, fixer):
        # type: (Fixer) -> None
        if fixer.starts_with:
            self.starts_with.setdefault(fixer.first_word, []).append(fixer)
        elif fixer.exact_match:
            self.exact_matches.setdefault(fixer.exact_match, []).append(fixer)
            if fixer.exact_match == fixer.replacement.upper():
                # Don't add it twice
                return
        self.exact_matches.setdefault(fixer.replacement.upper(), []).append(fixer)

    def fix(self, txn, save_changes=False):
        # type: (Transaction, bool) -> bool
        for possible in self.exact_matches.get(txn.online_description.upper(), []):
            if possible.fix(txn, save_changes=save_changes, check_starts_with=False):
                return True
        for possible in self.starts_with.get(txn.first_word, []):
            if possible.fix(txn, save_changes=save_changes):
                return True
        return False


class FixerCollection(object):
    _fixer_groups_by_account_type = {}  # type: Dict[str, FixerGroup]
    _fixer_groups_by_account_name = {}  # type: Dict[str, FixerGroup]
    _global_fixers = FixerGroup()

    @classmethod
    def load(cls, *paths):
        # type: (str) -> None

        # Start fresh
        cls._fixer_groups_by_account_type = {}
        cls._fixer_groups_by_account_name = {}
        cls._global_fixers = FixerGroup()

        for path in paths:
            path = os.path.join(os.getcwd(), path)
            if not os.path.exists(path):
                myPrint("B", "No data file found at {}".format(os.path.realpath(path)))
                continue
            with open(path, "r") as f:
                lines = [line.strip().replace("\xe2\x80\x99", "'") for line in f]
            field_names = lines[0].split(",")
            missing_fields = REQUIRED_FIELDS - set(field_names)
            if missing_fields:
                myPopupInformationBox(
                    None,
                    "CSV is missing the following required fields: {}".format(", ".join(missing_fields)),
                    "Error",
                )
                continue
            for line in lines[1:]:
                kwargs = dict(zip(field_names, line.split(",")))
                try:
                    cls.create_fixer(**kwargs)
                except FixerError as e:
                    myPopupInformationBox(
                        None,
                        "Error: '{}' ({})".format(line, e.message),
                        "Error",
                    )

    @classmethod
    def add(cls, fixer, account_type="", account_name=""):
        # type: (Fixer, str, str) -> None
        if account_name:
            if not find_account(account_name):
                raise FixerError("Unknown account: {}".format(account_name))
            group = cls._fixer_groups_by_account_name.setdefault(account_name.upper(), FixerGroup())
        elif account_type:
            if account_type not in AccountType.ALL:
                raise FixerError("Unknown account type: {}".format(account_type))
            group = cls._fixer_groups_by_account_type.setdefault(account_type, FixerGroup())
        else:
            group = cls._global_fixers
        group.add(fixer)

    @classmethod
    def create_fixer(
        cls,
        replacement,
        exact_match="",
        starts_with="",
        memo_contains="",
        amount=0.0,
        amount_above=0.0,
        amount_below=0.0,
        category="",
        skip_confirm=False,
        account_type="",
        account_name="",
    ):
        # type: (str, str, str, str, float, float, float, str, bool, str, str) -> None
        cls.add(
            Fixer(
                replacement,
                exact_match=exact_match,
                starts_with=starts_with,
                memo_contains=memo_contains,
                amount=amount,
                amount_above=amount_above,
                amount_below=amount_below,
                category=category,
                skip_confirm=skip_confirm,
            ),
            account_type,
            account_name,
        )

    @classmethod
    def fix(cls, txn, save_changes=False):
        # type: (Transaction, bool) -> bool
        group = cls._fixer_groups_by_account_name.get(str(txn.account).upper())
        if group and group.fix(txn, save_changes):
            return True
        account_type = str(txn.account.getAccountType())
        group = cls._fixer_groups_by_account_type.get(account_type)
        if group and group.fix(txn, save_changes):
            return True
        if cls._global_fixers.fix(txn, save_changes):
            return True
        return False


class DescriptionCounter(object):
    def __init__(self, description):
        # type: (str) -> None
        self.count = 0
        self.description = description
        self.outputs = set()

    def add(self, s):
        # type: (str) -> None
        self.count += 1
        self.outputs.add(s)

    def __cmp__(self, other):
        if self.count < other.count:
            return -1
        if self.count > other.count:
            return 1
        if self.description < other.description:
            return -1
        if self.description > other.description:
            return 1
        return 0


class DescriptionFirstWordCounter(object):
    def __init__(self, fw):
        # type: (str) -> None
        self.count = 0
        self.first_word = fw
        self.descriptions = {}  # type: Dict[str, DescriptionCounter]

    def add(self, description, output):
        # type: (str, str) -> None
        self.count += 1
        self.descriptions.setdefault(description, DescriptionCounter(description)).add(output)

    def __cmp__(self, other):
        if self.count < other.count:
            return 1
        if self.count > other.count:
            return -1
        if self.first_word < other.first_word:
            return 1
        if self.first_word > other.first_word:
            return -1
        return 0

    def sorted(self):
        # noinspection PyTypeChecker
        return sorted(self.descriptions.values())


class DescriptionContainer(object):
    def __init__(self):
        # type: () -> None
        self.first_words = {}  # type: Dict[str, DescriptionFirstWordCounter]
        self.count = 0

    def add(self, description, output):
        # type: (str, str) -> None
        self.count += 1
        fw = first_word(description)
        if fw == "THE":
            fw = first_word(description[4:])
        self.first_words.setdefault(fw, DescriptionFirstWordCounter(fw)).add(description, output)

    def sorted(self):  # type: () -> List[DescriptionFirstWordCounter]
        # noinspection PyTypeChecker
        return sorted(self.first_words.values())


class FixDownloadedTransactionsExtension(object):
    myContext = None
    myExtensionObject = None
    name = "Fix Downloaded Transactions"
    _accounts_by_type = {}  # type: Dict[str, List[Account]]
    _account_names_by_type = {}  # type: Dict[str, Set[str]]
    _fixer_groups_by_account_type = {}  # type: Dict[str, FixerGroup]
    _fixer_groups_by_account_name = {}  # type: Dict[str, FixerGroup]
    _global_fixers = FixerGroup()
    _instance = None

    # The initialize method is called when the extension is loaded and
    # provides the extension's context.  The context implements the methods
    # defined in the FeatureModuleContext:
    # http://infinitekind.com/dev/apidoc/com/moneydance/apps/md/controller
    # /FeatureModuleContext.html

    @classmethod
    def get_instance(cls):  # type: () -> FixDownloadedTransactionsExtension
        if cls._instance is None:
            cls._instance = FixDownloadedTransactionsExtension()
        return cls._instance

    @property
    def account_names_by_type(self):  # type: () -> Dict[str, Set[str]]
        if not self._account_names_by_type:
            self._init_data()
        return self._account_names_by_type

    @property
    def accounts_by_type(self):  # type: () -> Dict[str, List[Account]]
        if not self._accounts_by_type:
            self._init_data()
        return self._accounts_by_type

    def _init_data(self):  # type: () -> None
        self._account_names_by_type = {}
        for account in AccountIterator(moneydance.getCurrentAccountBook()):
            if account.getAccountOrParentIsInactive():
                continue

            # account_type = str(account.getAccountType())
            # if account_type in (
            #         AccountType.EXPENSE, AccountType.INCOME, AccountType.ROOT):
            #     continue

            at = account.getAccountType()  # SCB
            # noinspection PyUnresolvedReferences
            if at in [
                Account.AccountType.EXPENSE,
                Account.AccountType.INCOME,
                Account.AccountType.ROOT,
            ]:
                continue  # SCB
            self._accounts_by_type.setdefault(str(account.getAccountType()), []).append(account)
            self._account_names_by_type.setdefault(str(account.getAccountType()), set()).add(str(account))

    def initialize(self, extension_context, extension_object):
        self.myContext = extension_context
        self.myExtensionObject = extension_object
        self._init_data()

        # here we register ourselves with a menu item to invoke a feature
        # (ignore the button and icon mentions in the docs)
        self.myContext.registerFeature(
            extension_object,
            "fixDownloadedTransactions",
            None,
            "Fix Downloaded Transactions",
        )

    @staticmethod
    def create_modified_summary(modified):
        # type: (List[Transaction]) -> str
        lines = []  # type: List[str]
        by_account = {}  # type: Dict[str, List[Transaction]]
        for txn in modified:
            by_account.setdefault(str(txn.account), []).append(txn)
        for account in sorted(by_account):
            heading = "{} - {} modified".format(account, len(by_account[account]))
            lines.append(heading)
            lines.append("-" * len(heading))
            for txn in sorted(by_account[account], key=lambda x: x.dateint):
                lines.append(txn.change_summary())
            lines.append("")
        return "\n".join(lines)

    # invoke(eventstring) is called when we receive a callback for the
    # feature that we registered in the initialize method
    def invoke(self, _eventString=""):
        # type: (str) -> None
        csv_paths = CSV_FILE_NAMES
        if not csv_paths:
            default_load_path = get_home_dir()
            default_load_filename = "MoneyDance.csv"
            config = "fdt-config.json"
            if os.path.exists(config):
                with open(config, "r") as f:
                    data = json.load(f)
                    csv_path = data.get("csv_path")
                    if csv_path and os.path.exists(csv_path):
                        default_load_path = os.path.dirname(csv_path)
                        default_load_filename = os.path.basename(csv_path)
            chooser_title = "Select location of your csv file... (CANCEL=ABORT)"
            csv_paths = get_file_from_file_chooser(
                None,  # Parent frame or None
                default_load_path,  # Starting path
                default_load_filename,  # Default Filename
                title=chooser_title,  # Title
                multi_mode=True,  # Multi-file selection mode
                for_open=True,  # True for Open/Load, False for Save
                select_files=True,  # True = Files, else Dirs
                ok_text="LOAD",  # Load/Save button text, None for defaults
                file_filter_text="csv",  # File filter (non Mac only). Example: "txt" or "qif"
                allow_options_button=True,
            )

            if not csv_paths:
                return
            with open(config, "w") as f:
                json.dump({"csv_path": csv_paths[0]}, f)

        FixerCollection.load(*csv_paths)
        # self.fix_transactions(AccountType.BANK, AccountType.CREDIT_CARD)
        modified, unmodified = self.fix_transactions(AccountType.BANK, AccountType.CREDIT_CARD)

        # ConsoleWindow.showConsoleWindow(MD_REF.getUI())
        unmodified_message = ""
        fix_count = len(modified)
        total = fix_count + unmodified.count
        if unmodified:
            lines = []  # type: List[str]
            for entry in unmodified.sorted():
                lines.append("{} ({}):".format(entry.first_word, entry.count))
                for desc in entry.sorted():
                    lines.append("- {}".format(desc.description))
                    for o in sorted(desc.outputs):
                        o = str(o)[1:]
                        o = "".join([o[:4], "-", o[4:6], "-", o[6:]])
                        lines.append("  {}".format(o))
                    lines.append("")
            unmodified_message = "\n".join(lines)
        if modified:
            output = self.create_modified_summary(modified)
            FrameController(
                "Fixed Transactions",
                "Fixed {} of {} ({}%)\n\n".format(fix_count, total, (fix_count * 100 / total)) + output,
                unmodified_message,
                lAlertLevel=1,
                lWrapText=False,
                lAutoSize=True,
            ).show()
        elif unmodified:
            show_problems(
                "Fixed {} of {} ({}%)\n\n".format(fix_count, total, (fix_count * 100 / total)) + unmodified_message
            )

    def set_status(self, message):
        # type: (str) -> None
        if self.myContext:
            self.myContext.setStatus(message)

    def show_accounts(self):  # type: () -> None
        for account_type in sorted(self.account_names_by_type):
            myPrint("B", "Type: {}".format(account_type))
            for account in sorted(self.account_names_by_type.get(account_type, [])):
                myPrint("B", "- Account: {}".format(account))

    def _process_transactions(self, account_types, commit_changes=False):
        # type: (Tuple[str, ...], bool) -> Tuple[List[Transaction], DescriptionContainer]
        all_parented_transactions = list(self.get_unreconciled_for_account_types(*account_types))
        all_parented_transactions.sort(key=lambda x: -x.dateint)

        modified_transactions = []  # type: List[Transaction]
        counter = 0
        fix_count = 0
        no_change_required = 0
        unmodified = DescriptionContainer()

        if not all_parented_transactions:
            self.set_status("No new transactions")
            return modified_transactions, unmodified

        self.set_status("Analyzing {} transactions".format(len(all_parented_transactions)))

        for txn in all_parented_transactions:
            fixed = FixerCollection.fix(txn, save_changes=commit_changes)
            if fixed:
                if txn.is_modified:
                    modified_transactions.append(txn)
                    fix_count += 1
                else:
                    no_change_required += 1
            else:
                unmodified.add(txn.online_description, str(txn))
            counter += 1
        self.set_status("Fixed {} of {} ({}%)".format(fix_count, counter, (fix_count * 100 / counter)))
        return modified_transactions, unmodified

    def test_fix_transactions(self, *account_types):
        # type: (*str) -> Tuple[List[Transaction], DescriptionContainer]
        return self._process_transactions(account_types, commit_changes=False)

    def fix_transactions(self, *account_types):
        # type: (*str) -> Tuple[List[Transaction], DescriptionContainer]
        return self._process_transactions(account_types, commit_changes=True)

    @property
    def transactions(self):
        # type: () -> Generator[Transaction, None, None]
        i = moneydance.getCurrentAccountBook().getTransactionSet().iterator()
        for txn in i:
            if txn != txn.getParentTxn():
                continue
            yield Transaction(txn)

    def get_unreconciled_for_account_types(self, *account_types):
        # type: (*str) -> Generator[Transaction, None, None]
        for txn in self.transactions:
            if not txn.is_new:
                continue
            account_name = str(txn.account)
            for account_type in account_types:
                if account_name in self.account_names_by_type.get(account_type, set()):
                    yield txn
                    break

    def get_unreconciled_for_account_names(self, *accounts):
        # type: (*str) -> Generator[Transaction, None, None]
        accounts_to_match = set(accounts)
        for txn in self.transactions:
            if not txn.is_new:
                continue
            if str(txn.account) not in accounts_to_match:
                continue
            yield txn

    # invoke(eventstring) is called when we receive a callback for the
    # feature that we registered in the initialize method
    def __str__(self):
        return "FixDownloadedTransactions"


def immediate_mode():
    o = FixDownloadedTransactionsExtension.get_instance()
    o.invoke()


if INSTALL_EXTENSION:
    moneydance_extension = FixDownloadedTransactionsExtension.get_instance()
else:
    immediate_mode()

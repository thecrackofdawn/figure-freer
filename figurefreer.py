#-*- coding:utf-8-*-
#author:cd
import wx
import pyHook
import pythoncom
import time
import win32api
import win32con
import threading
import pickle
from wx.lib.embeddedimage import PyEmbeddedImage
from wx.lib.wordwrap import wordwrap

figurefree = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAAA3NCSVQICAjb4U/gAAAC0UlE"
    "QVRIib2WPSxrYRjHf62qhJS2yiA+alBJDQY2kZgMEpsIiTAhjdEmBlPHLtI2JhIJNotVIjr6"
    "FpNIK0iapsRXqGpxh8f73oN7ucnN6Tuc9Jw8p8/ze5/n/f+P5fn5GbBYLMDLywtQUlICrKys"
    "AEtLS0BxcTHQ1tYGTE1NAa+vr4DVauWn9XPEfy5bOp0GioqKUARVVVVALBYDZmdngYaGBmBs"
    "bAw4ODgAWltb+TcO8wlqamr0jRAIjXAkEgkUQUtLC3B6eooieHt7++ZaKALJJlNkzOz1ejVB"
    "V1cXcHd3B5SVlekY47ty/brMJ/hb5tvbW6C2tlY/SSaTQHNzs34i3ZI5PD4+BuLxOJBKpYD7"
    "+3sKQfDhxmZDTff29jYwMjKC6sTT05OubnFxETVR0onq6mqgrq4O8Pl8gMvlKiCBKJLdbgci"
    "kQjQ1NQEOJ1OIBwOA4eHh8D6+jrQ3t4OjI+PA5WVld8kMJ9Adlxql3nY3NwE5ufndZDf70fR"
    "TExMABcXF8DDwwOqB7Lj+XweeHx8BK6urgpBYJH8R0dHKO3s7OwEhoaGdNDZ2RmqNx6PR9PI"
    "qZZ6d3Z2UOdfOHK5XCEIbJI5GAyinKunp+dTkFQkJ7m3txfo6OjQNcpbu7u7wMDAAFBfX4/q"
    "jfkEk5OTKLcSlS8tLf0UtL+/D/T39wOrq6t8VKq9vT3U+TfW/u53phNMT0+jJlo8S3ZWlihi"
    "d3c3sLa2BgQCARRlNpvVV6PKijOKsplPIFUvLy/r2jOZDGo2pFKjS4sWjY6OolxM4t1ut/5T"
    "o8eYTzAzMwOcnJwAjY2NqB3s6+vjo0vLb4fDASwsLOhKhSkUCv2u2vClZD7B3NwcyptEiy4v"
    "L1HzMzw8rEOlHxUVFcDg4CBwfX0NbGxsAOXl5X9MYL6aynl71w3D3kWjUWBrawul9Tc3N8D5"
    "+TnKgeU8i29Lz75+rZpO8AsCJE578O/FcgAAAABJRU5ErkJggg==")

TheCrackOfDawn = PyEmbeddedImage(
    "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")

try:
    GLOBAL_SETTINGS = pickle.load(open('config', 'r'))
except Exception, err:
    GLOBAL_SETTINGS = {'leftclick':59, 'rightclick':60, 'hold':True}
ENTRIES = []
DOWNKEYS = set()
#LOCK = threading.Lock()

def OnHook(event):
    scan_code =  event.ScanCode
    if scan_code == GLOBAL_SETTINGS['leftclick']:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        return False
    elif scan_code == GLOBAL_SETTINGS['rightclick']:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        return False
    elif scan_code == 55:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        return False
    return True

def OnKeyUp(event):
    code = event.ScanCode
    if code in DOWNKEYS:
        if code == GLOBAL_SETTINGS['leftclick']:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        elif code ==  GLOBAL_SETTINGS['rightclick']:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        DOWNKEYS.remove(code)
        return False
    
    return True

def OnKeyDown(event):
    code = event.ScanCode
    if code == GLOBAL_SETTINGS['leftclick'] :
        #LOCK.acquire()
        if not code in DOWNKEYS:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            DOWNKEYS.add(code)
        #LOCK.release()
        return False
    elif code == GLOBAL_SETTINGS['rightclick'] :
        #LOCK.acquire()
        if not code in DOWNKEYS:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
            DOWNKEYS.add(code)
        #LOCK.release()
        return False
    return True


def OnSet(event):
    scan_code =  event.ScanCode
    entry = ENTRIES.pop()
    entry.SetValue(str(scan_code))
    entry.SetBackgroundColour('#f0f0f0')
    entry.Refresh()
    ENTRIES.insert(0, entry)
    ENTRIES[-1].SetBackgroundColour('green')
    ENTRIES[-1].Refresh()
    return False

def hook(callback):
    hm = pyHook.HookManager()
    if isinstance(callback, list):
        hm.KeyDown = callback[0]
        hm.KeyUp = callback[1]
    else:
        hm.KeyDown = callback
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    hm.UnhookKeyboard()

class TaskBarIcon(wx.TaskBarIcon):
    ID_About = wx.NewId()
    ID_Exit = wx.NewId()
    ID_Stop = wx.NewId()
    ID_Start = wx.NewId()
    ID_Setting = wx.NewId()
    def __init__(self):
        wx.TaskBarIcon.__init__(self)  
        self.SetIcon(figurefree.getIcon(), 'figuerfreer')  
        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.ID_About)
        self.Bind(wx.EVT_MENU, self.OnExit, id=self.ID_Exit)
        self.Bind(wx.EVT_MENU, self.OnStop, id=self.ID_Stop)
        self.Bind(wx.EVT_MENU, self.OnStart, id=self.ID_Start)
        self.Bind(wx.EVT_MENU, self.OnSetting, id=self.ID_Setting)
        self.OnStart(None)
        

    def OnStop(self, event):
        win32api.PostThreadMessage(self.hook.ident, 0x12)
        
    def OnStart(self, event):
        if GLOBAL_SETTINGS['hold']:
            self.hook = threading.Thread(target=hook, args=([OnKeyDown, OnKeyUp],))
        else:
            self.hook = threading.Thread(target=hook, args=(OnHook,))
        self.hook.daemon = True
        self.hook.start()
    
    def OnAbout(self, event):
        # First we create and fill the info object
        painter = wx.Frame(None)
        info = wx.AboutDialogInfo()
        info.SetIcon(TheCrackOfDawn.getIcon())
        info.Name = "figure freer"
        info.Version = "1.0"
        info.Copyright = "(c) cd"
        info.Description = wordwrap(
            "you can perform the mouse clicking action by any key you want."
            "For now, it meets my need perfectly. So no more time will be paid."
            "If you have any need, you are free to change or ever rewrite it.",
            350, wx.ClientDC(painter))
        info.WebSite = ("https://github.com/thecrackofdawn/figure-freer", "figure freer's source code")
        info.Developers = ["weibo : TheCrackOfDawn",
                           "hoping more and more attention ^_^"]
        licenseText = "MIT. You are free to do whatever you want."
        info.License = wordwrap(licenseText, 500, wx.ClientDC(painter))

        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)

    def OnSetting(self, event):
        alive = False
        if self.hook.is_alive():
            alive = True
            self.OnStop(None)
        dialog = SettingDialog()
        result = dialog.ShowModal()
        if result == wx.ID_OK:
            GLOBAL_SETTINGS['leftclick'] = int(dialog.leftClick.GetValue())
            GLOBAL_SETTINGS['rightclick'] = int(dialog.rightClick.GetValue())
            pickle.dump(GLOBAL_SETTINGS, open('config', 'w'))
        dialog.Stop()
        dialog.Destroy()
        if alive:
            self.OnStart(None)

    def OnExit(self, event):
        self.RemoveIcon()
        self.Destroy()
        
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_About, 'about')
        if self.hook.is_alive():
            menu.Append(self.ID_Stop, 'stop')
        else:
            menu.Append(self.ID_Start, 'start')
        menu.Append(self.ID_Setting, 'settings')
        menu.Append(self.ID_Exit, 'exit')
        return menu

class SettingDialog(wx.Dialog):
    def __init__(self):    
        global  ENTRIES
        wx.Dialog.__init__(self, None, -1, 'settings', size=(250, 200))
        panel = wx.Panel(self)
        wx.StaticText(panel, -1, 'left click:', pos=(20, 30))
        self.leftClick = wx.TextCtrl(panel, -1, pos=(100, 27), value=str(GLOBAL_SETTINGS['leftclick']), style=wx.TE_READONLY)
        wx.StaticText(panel, -1, 'right click:', pos=(20, 70))
        self.rightClick = wx.TextCtrl(panel, -1, pos=(100, 67), value=str(GLOBAL_SETTINGS['rightclick']), style=wx.TE_READONLY)
        self.hold = wx.CheckBox(panel, -1, 'simulate holding',  pos=(60, 110))
        self.hold.SetValue(GLOBAL_SETTINGS['hold'])        
        self.hold.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        
        okButton = wx.Button(panel, wx.ID_OK, 'OK', pos=(20, 140))
        okButton.SetDefault()
        cancelButton = wx.Button(panel, wx.ID_CANCEL, 'cancel', pos=(140, 140))
        ENTRIES = [self.rightClick, self.leftClick]
        ENTRIES[-1].SetBackgroundColour('green')
        self.Start()
    
    def OnCheckBox(self, event):
        GLOBAL_SETTINGS['hold'] = self.hold.GetValue()    
    def Stop(self):
        win32api.PostThreadMessage(self.hook.ident, 0x12)
        
    def Start(self):
        self.hook = threading.Thread(target=hook, args=(OnSet,))
        self.hook.daemon = True
        self.hook.start()
    
def run():  
    app = wx.App() 
    taskBar = TaskBarIcon()
    app.MainLoop()  
if __name__ == '__main__':  
    run()  

#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import string
try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"

class fromMenu(wx.Menu):
    
    def __init__(self, parent):
        super(fromMenu, self).__init__()
        self.units = ["psi","bar","atm","Pa","mmHg"]
        self.parent = parent

        for unit in self.units:
            item = wx.MenuItem(self, wx.NewId(), unit)
            self.AppendItem(item)
            self.Bind(wx.EVT_MENU, self.OnFromUnitSelected, item)

    def OnFromUnitSelected(self,event):
        fromUnit = self.FindItemById(event.GetId())
        text = fromUnit.GetText()

        ## set "From ___" label
        fromText.SetLabel("From %s"% text)

        toUnitText = toText.GetLabel().split(" ")[1]
        fromTo = text + "_" + toUnitText

        ## if text is only digits, then convert and display result
        try:
            fromFloat = float(fromEnter.GetValue())
            toString = str(fromFloat * conversionFactors[fromTo])
            toEnter.SetValue(toString)
        except ValueError:
            toEnter.SetValue("Only Enter Digits")



class toMenu(wx.Menu):
    
    def __init__(self, parent):
        super(toMenu, self).__init__()
        self.units = ["psi","bar","atm","Pa","mmHg"]
        self.parent = parent

        for unit in self.units:
            item = wx.MenuItem(self, wx.NewId(), unit)
            self.AppendItem(item)
            self.Bind(wx.EVT_MENU, self.OnToUnitSelected, item)

    def OnToUnitSelected(self,event):
        toUnit = self.FindItemById(event.GetId())
        text = toUnit.GetText()

        ## set "To ___" label to correct unit
        toText.SetLabel("To %s"% text)

        fromUnitText = fromText.GetLabel().split(" ")[1]
        fromTo=fromUnitText + "_" + text


        ## if text is only digits, then convert and display result
        try:
            fromFloat = float(fromEnter.GetValue())
            toString = str(fromFloat * conversionFactors[fromTo])
            toEnter.SetValue(toString)
        except ValueError:
            toEnter.SetValue("Error")


class pressureConvert(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title, style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.parent = parent
        self.initialize()

    def initialize(self):
        ## Conversion Factors using "From_To" as key to multiply by
        global conversionFactors
        conversionFactors = {"psi_psi":1,"bar_psi":14.504,"atm_psi":14.7,"Pa_psi":.000145,"mmHg_psi":.01934,
                                "psi_bar":.0689,"bar_bar":1,"atm_bar":1.01325,"Pa_bar":.00001,"mmHg_bar":.001333,
                                "psi_atm":.0681,"bar_atm":.987,"atm_atm":1,"Pa_atm":.00001,"mmHg_atm":.001316,
                                "psi_Pa":6895,"bar_Pa":100000,"atm_Pa":101325,"Pa_Pa":1,"mmHg_Pa":133.3,
                                "psi_mmHg":51.715,"bar_mmHg":750.1,"atm_mmHg":760,"Pa_mmHg":.0075,"mmHg_mmHg":1}
        self.units = ["psi","bar","atm","Pa","mmHg"]
        global fromTo
        fromTo="psi_psi"


        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(3, 3, 9, 25)


        global fromText
        fromText = wx.Button(panel, id=0, label="From psi")

        global toText
        toText = wx.Button(panel, id=-1, label="To psi")
        self.Bind(wx.EVT_BUTTON, self.OnToFromTextSelected)

        global fromEnter
        fromEnter = wx.TextCtrl(panel, -1, style=wx.TE_PROCESS_ENTER)
        ## Bind typing enter from text box to updating the returned conversion
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnterKeyPress)

        global toEnter
        toEnter = wx.TextCtrl(panel,-1,style=wx.TE_READONLY)

        fgs.AddMany([(fromText), (wx.StaticText(panel),1,wx.EXPAND), (toText), 
            (fromEnter, 1, wx.EXPAND), (wx.StaticText(panel, label="=")), (toEnter, 1, wx.EXPAND),
            (wx.StaticText(panel),1,wx.EXPAND),(wx.StaticText(panel),1,wx.EXPAND),(wx.StaticText(panel),1,wx.EXPAND)])

        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)
        self.SetSize((275,100))
        self.Show(True)

    def OnEnterKeyPress(self, event):
        fromTo = (fromText.GetLabel().split(" ")[1]) + "_" + toText.GetLabel().split(" ")[1]
        try:
            fromFloat = float(fromEnter.GetValue())
            toString = str(fromFloat * conversionFactors[fromTo])
            toEnter.SetValue(toString)
        except ValueError:
            toEnter.SetValue("Error")

    def OnToFromTextSelected(self,event):
        buttonID = event.GetId()
        buttonByID = self.FindWindowById(buttonID)
        buttonStartText = buttonByID.GetLabel().split(" ")[0]

        ## Check if Button Label is "To" or "From" and handle menu appropriately
        if buttonStartText == "From":
            self.PopupMenu(fromMenu(self), (25,10))
        elif buttonStartText == "To":
            self.PopupMenu(toMenu(self), (195,10))

if __name__ == "__main__":
    app = wx.App()
    frame = pressureConvert(None,-1,'Pressure Convert')
    app.MainLoop()